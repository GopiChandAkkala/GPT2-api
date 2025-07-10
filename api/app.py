from fastapi import FastAPI, Request
from transformers import pipeline

app = FastAPI()
generator = pipeline("text-generation", model="gpt2")

@app.post("/generate")

async def generate_text(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    result = generator(prompt, max_length=50, num_return_sequences=1)
    return {"output": result[0]["generated_text"]}
