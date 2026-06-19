import os

def load_documents(data_folder="data"):
    documents = []

    for filename in os.listdir(data_folder):
        if filename.endswith(".txt") or filename.endswith(".md"):
            filepath = os.path.join(data_folder, filename)

            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()

                documents.append({
                    "source": filename,
                    "content": content
                })

    return documents