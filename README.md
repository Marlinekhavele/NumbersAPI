# NumbersAPI
## Overview
A FastAPI-based microservice that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Features
- Classify numbers as prime ornon-prime
- Identify perfect numbers
- Determine number even or odd
- Detect Armstrong numbers
- Retrieve fun facts about numbers

## Setup & Installation
1. Clone the repository
```bash
git clone https://github.com/Marlinekhavele/NumbersAPI
cd NumbersAPI
```
#### Create and activate a virtual environment:
```bash
pyenv virtualenv env
pyenv activate env
```
#### Alternatively, using Python's built-in venv:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `uvicorn main:app --reload`

## Endpoint
`GET /api/classify-number?number=371`

### Example Response
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number"
}
```
## Deployment


