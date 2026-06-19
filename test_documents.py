from src.document_loader import load_documents

docs = load_documents()

print("Documents Loaded:", len(docs))

for doc in docs:
    print(doc["source"])