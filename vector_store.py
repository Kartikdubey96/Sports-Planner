import chromadb
from chromadb.utils import embedding_functions
import os
import hashlib
from datetime import datetime

# Initialize ChromaDB (persistent local storage)
CHROMA_PATH = os.path.join(os.path.dirname(__file__), "chroma_db")

def get_client():
    return chromadb.PersistentClient(path=CHROMA_PATH)

def get_collection(name: str = "sports_content"):
    client = get_client()
    ef = embedding_functions.DefaultEmbeddingFunction()
    collection = client.get_or_create_collection(
        name=name,
        embedding_function=ef,
        metadata={"hnsw:space": "cosine"}
    )
    return collection

def save_content(content_type: str, topic: str, sport: str, tone: str, body: str) -> str:
    """Save generated content to ChromaDB. Returns the document ID."""
    collection = get_collection()
    doc_id = hashlib.md5(f"{topic}{datetime.now().isoformat()}".encode()).hexdigest()[:12]
    collection.add(
        documents=[body],
        metadatas=[{
            "content_type": content_type,
            "topic": topic,
            "sport": sport,
            "tone": tone,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }],
        ids=[doc_id]
    )
    return doc_id

def search_similar(query: str, n_results: int = 3):
    """Search for similar past content using semantic similarity."""
    collection = get_collection()
    count = collection.count()
    if count == 0:
        return []
    results = collection.query(
        query_texts=[query],
        n_results=min(n_results, count)
    )
    output = []
    for i, doc in enumerate(results["documents"][0]):
        meta = results["metadatas"][0][i]
        output.append({
            "id": results["ids"][0][i],
            "body": doc,
            "meta": meta
        })
    return output

def get_all_saved(limit: int = 20):
    """Retrieve all saved content entries."""
    collection = get_collection()
    count = collection.count()
    if count == 0:
        return []
    results = collection.get(limit=min(limit, count), include=["documents", "metadatas"])
    output = []
    for i, doc in enumerate(results["documents"]):
        output.append({
            "id": results["ids"][i],
            "body": doc,
            "meta": results["metadatas"][i]
        })
    return output

def delete_content(doc_id: str) -> bool:
    """Delete a saved content entry by ID."""
    try:
        collection = get_collection()
        collection.delete(ids=[doc_id])
        return True
    except Exception:
        return False

def get_count() -> int:
    """Return total number of saved items."""
    try:
        return get_collection().count()
    except Exception:
        return 0