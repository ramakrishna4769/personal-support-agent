import os
import chromadb
from google import genai
from dotenv import load_dotenv

from src.document_loader import load_documents

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_or_create_collection(
    name="support_kb"
)


def get_embedding(text):
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return response.embeddings[0].values


def index_documents():
    documents = load_documents()

    for doc in documents:
        embedding = get_embedding(doc["content"])

        collection.add(
            ids=[doc["source"]],
            embeddings=[embedding],
            documents=[doc["content"]],
            metadatas=[
                {
                    "source": doc["source"]
                }
            ]
        )

    print("Documents Indexed Successfully")