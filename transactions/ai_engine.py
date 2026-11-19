
import os 

from google import genai

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

#authenticate

client = genai.Client(api_key=GOOGLE_API_KEY)

prompt = "explain django in few words"

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[prompt]
)

print(response.text)