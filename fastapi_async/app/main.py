from fastapi import FastAPI, HTTPException
import asyncio
import httpx

app = FastAPI()

async def fecth_address(zip_code: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zip_code}"
        )
        return response.json()
    
@app.get("/addresses")
async def get_addresses():
    zip_codes = [
        '0600000',
        '1000001',
        '9000000',
    ]
    return await asyncio.gather(*(fecth_address(zip_code) for zip_code in zip_codes))