from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.services.numbers_api import get_number_fact
from app.services.numbers_utils import classify_number
import httpx

app = FastAPI(title="Number API")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/api/classify-number")
async def classify_number_endpoint(
    number: str = Query(..., description="Number to classify")
):
    try:
        # Validate input is a valid integer
        parsed_number = int(number)
    except ValueError:
        raise HTTPException(
            status_code=400, 
            detail={
                "number": number,
                "error": True
            }
        )
    
    try:
        # Get number properties
        number_details = classify_number(parsed_number)
        
        # Get fun fact from Numbers API
        async with httpx.AsyncClient() as client:
            fact_response = await get_number_fact(client, parsed_number)
        
        # Combine results
        response = {
            "number": parsed_number,
            "is_prime": number_details["is_prime"],
            "is_perfect": number_details["is_perfect"],
            "properties": number_details["properties"],
            "digit_sum": number_details["digit_sum"],
            "fun_fact": fact_response
        }
        
        return response
    
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail={
                "error": str(e)
            }
        )
