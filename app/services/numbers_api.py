import httpx

async def get_number_fact(client, number):
    """
    Fetch a fun fact about the number from Numbers API.
    """
    try:
        # Make GET request to Numbers API
        response = await client.get(f"http://numbersapi.com/{number}/math")
        return response.text if response.status_code == 200 else "No fact available"
    except Exception:
        return "Unable to fetch number fact"