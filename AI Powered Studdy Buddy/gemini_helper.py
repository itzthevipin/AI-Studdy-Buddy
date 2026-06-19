import os
from dotenv import load_dotenv
from groq import Groq


dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=dotenv_path)


API_KEY = os.getenv("AQ.Ab8RN6JJP6Kgmi0jWTmhI2qEC9tt8JRVQIhoL3f0HShhFZ1nPg")


if not API_KEY:
    raise Exception("Groq API key not found")


client = Groq(
    api_key=API_KEY
)


def ask_gemini(prompt):

    try:

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI tutor for students."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.2

        )


        return response.choices[0].message.content


    except Exception as e:

        return f"AI Error: {str(e)}"