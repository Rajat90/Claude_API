

from dotenv import load_dotenv, find_dotenv
import os
import httpx
from anthropic import Anthropic

load_dotenv(find_dotenv(), override=True)

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    http_client=httpx.Client(
        proxy=httpx.Proxy(url=os.getenv("HTTPS_PROXY")),
        verify=False
    )
)

model = "claude-sonnet-4-6"
# add user message to the conversation and get the response

def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})
    return messages

# add claud message to the conversation and get the response

def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})
    return messages

# get the response from the model based on the conversation
def chat(messages, system=None, temperature=1.0,stop_sequences=[]):   
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
    }

    if system is not None:
        params["system"] = system
    
    if stop_sequences:
        params["stop"] = stop_sequences

    response = client.messages.create(**params)
    return response.content[0].text