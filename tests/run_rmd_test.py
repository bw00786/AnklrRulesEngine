# Add this test script to help debug your rule engine
import requests
import json
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# API endpoint
API_URL = "http://localhost:8000/evaluate_rules/"

# Test cases to identify the issue
test_cases = [
    {
        "name": "Basic RMD Case",
        "facts": {
            "participant_age": 85,
            "plan_type": "401K",
            "prior_year_end_balance": 200000.0,
            "uniform_life_table_factor": 16.5,
            "participant_status": "Active",
            "dob": "1940-01-01"  # Person born in 1940 would be 85 in 2025
        }
    },
    {
        "name": "Expanded RMD Case",
        "facts": {
            "participant_age": 85,
            "plan_type": "401K",
            "prior_year_end_balance": 200000.0,
            "uniform_life_table_factor": 16.5,
            "participant_status": "Active",
            "dob": "1940-01-01",
            "account_type": "Traditional",
            "marital_status": "Single",
            "beneficiary": "None",
            "beneficiary_allocation": 0,
            "rmd_amount": 12121.21,
            "tax_withholding_eligible": True
        }
    },
    {
        "name": "Plan Type Case Sensitivity Test",
        "facts": {
            "participant_age": 85,
            "plan_type": "401k",  # lowercase to test case sensitivity
            "prior_year_end_balance": 200000.0,
            "uniform_life_table_factor": 16.5,
            "participant_status": "Active",
            "dob": "1940-01-01"
        }
    },
    {
        "name": "Specific Rules Test - RMD Due 1231",
        "facts": {
            "participant_age": 75,
            "plan_type": "401K",
            "prior_year_end_balance": 200000.0,
            "uniform_life_table_factor": 16.5,
            "participant_status": "Active",
            "dob": "1950-01-01"  # Exactly matches dob >= '1950-01-01'
        }
    },
    {
        "name": "Specific Rules Test - 73 Initial RMD",
        "facts": {
            "participant_age": 73,
            "plan_type": "401K",
            "prior_year_end_balance": 200000.0,
            "uniform_life_table_factor": 16.5,
            "participant_status": "Active",
            "dob": "1952-01-01"  # Exactly matches dob >= '1952-01-01'
        }
    }
]

def run_tests():
    """Run all test cases and log results"""
    results = []
    
    for test_case in test_cases:
        logger.info(f"Running test: {test_case['name']}")
        
        # Prepare request payload
        payload = {
            "context": "RMD_Distribution",
            "facts": test_case["facts"]
        }
        
        try:
            # Make request
            response = requests.post(API_URL, json=payload)
            response_data = response.json()
            
            # Log result
            logger.info(f"Status Code: {response.status_code}")
            logger.info(f"Response: {json.dumps(response_data, indent=2)}")
            
            # Add to results
            results.append({
                "test_name": test_case["name"],
                "status_code": response.status_code,
                "matched_rules": response_data.get("matched_rules", 0),
                "actions_triggered": response_data.get("actions_triggered", [])
            })
            
        except Exception as e:
            logger.error(f"Error running test {test_case['name']}: {str(e)}")
            results.append({
                "test_name": test_case["name"],
                "error": str(e)
            })
    
    # Summary
    logger.info("\n----- TEST SUMMARY -----")
    for result in results:
        status = "ERROR" if "error" in result else (
            "PASSED" if result.get("matched_rules", 0) > 0 else "FAILED"
        )
        logger.info(f"{result['test_name']}: {status}")
    
    return results

if __name__ == "__main__":
    run_tests()