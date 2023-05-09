import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

"""
default_params: dict = {
    "max_tokens": 128,
    "temperature": 0.8,
    "top_p": 0.95,
    "top_k": 40,
    "repeat_penalty": 1.1,
    "stop": []
}
"""


def get_completion(prompt: str = None,
                   params: dict = None):
    if params:
        payload = {"prompt": prompt, "params": params}
    else:
        payload = {"prompt": prompt}
    api_url = os.environ.get("API_URL")
    headers = {
        "Content-Type": "application/json",
        # "Authorization": f"Bearer {os.environ['HF_API_TOKEN']}"
    }

    data = json.dumps(payload)
    response = requests.request("POST", api_url, headers=headers, data=data)
    completion = json.loads(response.content.decode("utf-8"))
    return completion['message']['choices'][0]['text']


def format(messages=[], system="", user="Human: ", assistant="AI: "):
    """
    Format the messages from the API into human readable strings.
    """
    formatted_message = ""

    for message in messages:
        if message['role'] == 'system':
            formatted_message += f"{system}{message['content']}\n"
        elif message['role'] == 'user':
            formatted_message += f"{user}{message['content']}\n"
        elif message['role'] == 'assistant':
            formatted_message += f"{assistant}{message['content']}\n"

    return formatted_message


def get_completion_from_messages(messages=[],
                                 params: dict = None):
    prompt = format(messages)
    return get_completion(prompt, params)


if __name__ == '__main__':
    print(get_completion('AI is going to', params={"temperature": 0.5}))
