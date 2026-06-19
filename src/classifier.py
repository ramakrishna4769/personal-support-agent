import os
import json
from google import genai

def classify_persona(user_message):
    
    client = genai.Client(
    )

    prompt = f"""
    Classify this customer message into ONE category:

    1. Technical Expert
    2. Frustrated User
    3. Business Executive

    Return JSON only.

    Message:
    {user_message}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text