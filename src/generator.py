import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_response(user_query, retrieved_text):

    prompt = f"""
    Answer ONLY using the information below.

    Context:
    {retrieved_text}

    User Question:
    {user_query}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text