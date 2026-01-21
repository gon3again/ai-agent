import os
from dotenv import load_dotenv
import argparse
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions


parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
# Now we can access `args.user_prompt`
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("api_key is not found")


client = genai.Client(api_key=api_key)

response = client.models.generate_content(model="gemini-2.5-flash",contents=messages,config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt,temperature=0))
if response.usage_metadata != None:
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
else:
    raise RuntimeError("usage_metadate = None")

function_list = response.function_calls
print(f"function_list:{function_list} len: {len(function_list)} is_None:{function_list == None}")
if function_list != None:
    for func in function_list:
        print(f"Calling function: {func.name}({func.args})")

print(response.text)
print(f"function_calls: {response.function_calls}")
(f"code_execution_result: {response.code_execution_result}")



def main():
    print("Hello from ai-agent!")


if __name__ == "__main__":
    main()
