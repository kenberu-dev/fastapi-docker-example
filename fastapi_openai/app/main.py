from fastapi import FastAPI
from fastapi.responses import JSONResponse
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import ValidationError
from schemas.openai import PromptSchema

load_dotenv()
client = OpenAI()

app = FastAPI()

@app.post("/openai")
async def openai(prompt: PromptSchema):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful tourism assistant. only the conclusion. answer in Japanese."},
            {"role": "user", "content": prompt.prompt},
        ]
    )
    
    return JSONResponse(content=completion.choices[0].message.content)
