from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import numpy as np

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load documents
with open("data/vector_store.json", "r") as f:
    vector_store = json.load(f)

class ChatRequest(BaseModel):
    sessionId: str
    message: str

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b)+1e-10)

def retrieve_chunks(user_vector, top_n=3, threshold=0.5):
    scored = []
    for doc in vector_store:
        score = cosine_similarity(user_vector, doc["vector"])
        if score >= threshold:
            scored.append((score, doc))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [doc for score, doc in scored[:top_n]]

def get_user_embedding_mock(text):
    return np.random.rand(1536).tolist()  # mock embedding

def generate_response(chunks, message):
    if not chunks:
        return "Sorry, I don't have enough information to answer that."
    context = "\n".join([c["content"] for c in chunks])
    return f"Context used:\n{context}\n\nYour question: {message}\n\nAnswer: (mocked)"

@app.post("/api/chat")
def chat(req: ChatRequest):
    if not req.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    user_vec = get_user_embedding_mock(req.message)
    top_chunks = retrieve_chunks(user_vec)
    reply = generate_response(top_chunks, req.message)
    return {"reply": reply, "tokensUsed": 0, "retrievedChunks": len(top_chunks)}