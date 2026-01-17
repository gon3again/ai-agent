import os
from dotenv import load_dotenv
import argparse
from google import genai
from google.genai import types


parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()
# Now we can access `args.user_prompt`
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("api_key is not found")


client = genai.Client(api_key=api_key)

content_response = client.models.generate_content(model="gemini-2.5-flash",contents=args.user_prompt)
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
