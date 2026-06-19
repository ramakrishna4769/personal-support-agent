from src.retriever import retrieve_documents
from src.generator import generate_response

query = input("Ask a question: ")

results = retrieve_documents(query)

context = ""

for doc in results["documents"][0]:
    context += doc + "\n"

answer = generate_response(query, context)

print("\nAnswer:")
print(answer)