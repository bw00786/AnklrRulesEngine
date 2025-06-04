# RMD Rule Engine API

This application is a rules engine for financial RMD (Required Minimum Distribution) calculations. It evaluates financial rules using a custom DSL (Domain Specific Language) and provides REST APIs for rule management, evaluation, and bulk uploads.

## Key Features
- Rule management with priority-based evaluation
- Custom DSL for rule conditions
- Excel-based bulk rule uploads
- LLM-powered natural language rule generation (optional)
- Docker containerization
- PostgreSQL database storage

## Prerequisites
- Docker
- Docker Compose
- OpenAI API key (if using LLM feature)

## Getting Started

### 1. Clone the repository
```bash
git clone <repository-url>
cd <project-directory>

POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=rules_db
OPENAI_API_KEY=<your-openai-api-key>  # Optional for LLM feature
LLM_FEATURE_FLAG=true  # Set to false to disable LLM

docker compose up --build

The application will be available at http://localhost:8000

API Endpoints
1. Rule Evaluation
POST /evaluate_rules/

json
{
  "context": "RMD_Distribution",
  "facts": {
    "participant_age": 72,
    "plan_type": "401K",
    "prior_year_end_balance": 500000,
    "uniform_life_table_factor": 27.4
  }
}
2. Bulk Rule Upload
POST /upload_rules/

Upload Excel file with columns:
context, name, priority, description, conditions, actions

3. Get Upload Report
GET /upload_report/{report_id}

4. Create Rules (Single)
POST /rules/

json
{
  "context": "RMD_Distribution",
  "name": "Uniform Lifetime Rule",
  "priority": 5,
  "description": "Standard RMD calculation",
  "conditions": "participant_age >= 72 and plan_type in [\"401K\", \"403B\"]",
  "actions": "[{\"type\": \"calculate_rmd\", \"parameters\": {...}}]"
}
5. Bulk Rule Creation
POST /rules/bulk

json
{
  "rules": [
    { /* Rule 1 */ },
    { /* Rule 2 */ }
  ]
}
6. LLM Rule Submission (Optional)
POST /submit_rule/

Form-data parameters:

description: Rule description

context: Rule context

priority: Priority number

natural_language: Rule in natural language

file: Excel file (if LLM disabled)

7. Feature Flags
GET /feature-flags

json
{
  "llmEnabled": true,
  "excelFallback": false
}
Rule DSL Syntax
Conditions use a custom DSL with:

Comparisons: ==, !=, >, <, >=, <=, in

Boolean logic: and, or, not

Functions: lifeExpectancyFactor(age)

Rule references: refRule("rule_name")

Example:

python
participant_age >= 72 
and plan_type in ["401K", "403B"] 
or refRule("Special_Case_Rule")
Excel Format
Required columns:

context

name

priority

description

conditions (DSL string)

actions (DSL string)

Example actions DSL:

set type to calculate_rmd; 
set balance_field to prior_year_end_balance; 
set divisor_source to uniform_life_table_factor
LLM Integration
When enabled (LLM_FEATURE_FLAG=true):

Submit natural language description to /submit_rule/

System generates valid DSL using GPT-4

Generated rules are validated and stored

Database Schema
rules2056
Column	Type
id	Integer
context	String
name	String
description	String
conditions	Text
actions	JSON
priority	Integer
active	Boolean
full_dsl	Text
upload_reports2056
Column	Type
id	String
filename	String
status	String
context	String
processing_time	Float
success_rate	Float
total_rules	Integer
successful_uploads	Integer
failed_uploads	Integer
created_at	DateTime
Troubleshooting
Database connection issues:

Verify PostgreSQL credentials in .env

Check database container logs

Rule evaluation failures:

Check rule syntax in debug logs

Validate fact formats match rule expectations

LLM generation failures:

Ensure valid OpenAI API key

Check GPT-4 model availability


## Key Components Explained

1. **Docker Setup**:
   - PostgreSQL container for data storage
   - FastAPI container for application logic
   - Environment variables for configuration

2. **Core Functionality**:
   - ANTLR-based DSL parser for rule conditions
   - Priority-based rule evaluation
   - Excel processing for bulk uploads
   - Caching for evaluation results

3. **Advanced Features**:
   - Life expectancy factor calculations
   - Fact normalization/preprocessing
   - Rule reference system (`refRule()`)
   - LLM integration with GPT-4

4. **Security**:
   - Input sanitization
   - Restricted AST evaluation
   - Environment-based configuration
   - CORS middleware for web access

To start the application:
1. Create `.env` file with required variables
2. Run `docker compose up --build`
3. Access API at `http://localhost:8000`
4. Use `/feature-flags` endpoint to verify LLM status
5. Submit rules via Excel upload or natural language endpoint
