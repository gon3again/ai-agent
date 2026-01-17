import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("api_key is not found")

from google import genai
client = genai.Client(api_key=api_key)

content_response = client.models.generate_content(model="gemini-2.5-flash",contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")
if content_response.usage_metadata != None:
    prompt_tokens = content_response.usage_metadata.prompt_token_count
    response_tokens = content_response.usage_metadata.candidates_token_count
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")
else:
    raise RuntimeError("usage_metadate = None")

print(content_response.text)


def main():
    print("Hello from ai-agent!")


if __name__ == "__main__":
    main()
