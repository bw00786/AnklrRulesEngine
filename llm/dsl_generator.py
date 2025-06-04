# llm/dsl_generator.py
import os
import re
import logging
from typing import List, Dict, Any
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, HTTPException, Depends, Form
from fastapi.responses import JSONResponse
from openai import OpenAI
from functools import lru_cache
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.schema import TextNode

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class DSLGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.example_index = self._build_example_index()
        
    def _build_example_index(self):
        """Build a vector index of example DSL rules using LlamaIndex"""
        examples_dir = os.path.join(os.path.dirname(__file__), "examples")
        
        if not os.path.exists(examples_dir):
            raise FileNotFoundError(f"Examples directory not found: {examples_dir}")

        try:
            # Load and index examples using LlamaIndex
            documents = SimpleDirectoryReader(examples_dir).load_data()
            
            # Create nodes with metadata
            nodes = []
            for doc in documents:
                content = doc.text
                if "NL:" not in content or "DSL:" not in content:
                    continue
                
                nl_part, dsl_part = content.split("DSL:", 1)
                node = TextNode(
                    text=content,
                    metadata={
                        "natural_language": nl_part.replace("NL:", "").strip(),
                        "dsl": dsl_part.strip()
                    }
                )
                nodes.append(node)
            
            return VectorStoreIndex(nodes)
            
        except Exception as e:
            logger.info(f"Failed to build example index: {str(e)}")
            raise RuntimeError(f"Failed to build example index: {str(e)}")
    @lru_cache(maxsize=100)
    def generate_dsl(self, natural_language: str) -> str:
        """Generate DSL using few-shot learning with GPT-4 and LlamaIndex"""
        try:
            # Retrieve relevant examples using semantic search
            query_engine = self.example_index.as_query_engine(similarity_top_k=3)
            response = query_engine.query(natural_language)
            examples_str = "\n\n".join(
                f"NL: {node.metadata['natural_language']}\nDSL: {node.metadata['dsl']}"
                for node in response.source_nodes
            )

            if not examples_str:
                raise ValueError("No relevant examples found for few-shot learning")

            # Generate DSL with GPT-4 using few-shot examples
            llm_response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a financial rules engine expert. Use these examples to convert the natural language rule to DSL:"
                        f"\n{examples_str}\n\nGenerate ONLY the DSL code without any markdown."
                    },
                    {
                        "role": "user",
                        "content": f"Convert this rule: {natural_language}"
                    }
                ],
                temperature=0.1,
                max_tokens=3000
            )
            
            raw_dsl = llm_response.choices[0].message.content.strip()
            logger.info(f"raw dsl: {raw_dsl}")
            if "invalid" in raw_dsl.lower():
               return "invalid"
        
            #return self._validate_dsl(raw_dsl)
            return {
                "full_dsl": raw_dsl,
                "conditions": self._extract_conditions(raw_dsl),
                "actions": self._extract_actions(raw_dsl)
            } 

        except Exception as e:
            raise ValueError(f"DSL generation failed: {str(e)}")

    def _extract_conditions(self, dsl: str) -> str:
        """Extract conditions from DSL text"""
        lines = dsl.split('\n')
    
        # Skip header row and empty lines
        header_passed = False
        for line in lines:
            line = line.strip()
            if not line:
               continue
            
            # Check for header row
            if all(section in line.lower() for section in ["context", "name", "priority"]):
               header_passed = True
               continue
            
            if header_passed:
               # Split columns using at least 4 spaces
               parts = re.split(r'\s{4,}', line)
               if len(parts) >= 5:
                return parts[4].strip()
            
        raise ValueError("No valid conditions found in DSL")

    def _extract_actions(self, dsl: str) -> list:
        """Extract actions from DSL text"""
        actions = []
        in_actions = False
        
        for line in dsl.split('\n'):
            if 'actions' in line.lower():
                in_actions = True
                continue
                
            if in_actions and line.strip().startswith('set'):
                actions.append(line.strip())
                
        return actions

    def _validate_dsl(self, dsl: str) -> str:
        """Clean and validate generated DSL"""
        # Remove markdown artifacts
        dsl = re.sub(r'```(plaintext)?', '', dsl).strip()
        
        # Validate required sections
        required_sections = {
            'context', 'name', 'priority',
            'description', 'conditions', 'actions'
        }
        if not all(section in dsl.lower() for section in required_sections):
            raise ValueError("Generated DSL missing required sections")
            
        return dsl
    
    def validate_llm_dsl_response(self, dsl_text: str) -> Any:
        # Add LLM-based validation using the correct OpenAI client method
        validation_prompt = f"Validate this DSL for logical consistency: {dsl_text}"
    
        # Use the correct client method for chat completions
        validation_response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
               {"role": "system", "content": "You are a financial rules validator. Check for logical errors."},
               {"role": "user", "content": validation_prompt}
            ]
        )
        validation_result = validation_response.choices[0].message.content
        logger.info(f"validation result: {validation_result}")
        return validation_result
       