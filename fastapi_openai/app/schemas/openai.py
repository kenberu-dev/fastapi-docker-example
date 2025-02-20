from pydantic import BaseModel, Field

class PromptSchema(BaseModel):
    prompt: str
