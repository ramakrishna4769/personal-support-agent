from src.retriever import retrieve_documents

query = "How do I reset my password?"

results = retrieve_documents(query)

print(results)