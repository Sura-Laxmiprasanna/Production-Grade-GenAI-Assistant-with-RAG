A chat assistant using Retrieval-Augmented Generation (RAG) to answer queries from a private knowledge base.
Backend is built with FastAPI; frontend uses HTML, Tailwind CSS, and JS.
Documents are stored in docs.json and converted to embeddings in vector_store.json.
The assistant retrieves top 3 relevant chunks using cosine similarity.
User queries are converted to embeddings and matched with the vector store.
Responses are generated using the retrieved context to prevent AI hallucinations.
Run uvicorn server:app --reload to start the backend API.
Frontend index.html connects to the API for live chat interactions.
API endpoint: POST /api/chat with sessionId and message in JSON.
Do not push .env with API keys to GitHub.
Use ingest_docs.py to generate embeddings from your documents.
Screenshots or video demo should show the chat working with relevant responses.
