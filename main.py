from fastapi import FastAPI
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = FastAPI()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class Question(BaseModel):
    # Adding an example helps Swagger UI show you the right format!
    query: str = Field(..., example="What is FastAPI?")

@app.post("/ask")
async def ask_question(request_body: Question):
    try:
        # Note: We updated the model to llama-3.1-8b-instant
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": request_body.query}
            ]
        )
        return {"answer": completion.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}