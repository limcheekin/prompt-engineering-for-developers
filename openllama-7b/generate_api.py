import os
import requests
import json
import copy
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

completion_prompt_template = "Q: {}? A: "
default_completion_params = {"stop": ["Q:", "A:", "\n"]} 
user="Human: "
assistant="AI: "
default_chat_params = {"stop": [user, assistant, "\n"]} 
def get_completion(prompt: str = None,
                   params: dict = None,
                   is_completion: bool = True):
    if is_completion:
        prompt = completion_prompt_template.format(prompt)
        completion_params = copy.deepcopy(default_completion_params)
        if params:
            completion_params.update(params)
        params = completion_params
    print("params", params)    
    payload = {"prompt": prompt, "params": params}
    api_url = os.environ.get("API_URL")
    headers = {
        "Content-Type": "application/json",
        # "Authorization": f"Bearer {os.environ['HF_API_TOKEN']}"
    }

    data = json.dumps(payload)
    response = requests.request("POST", api_url, headers=headers, data=data)
    completion = json.loads(response.content.decode("utf-8"))
    return completion['message']['choices'][0]['text']


def format(messages=[], system="", user=user, assistant=assistant):
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
    chat_params = copy.deepcopy(default_chat_params)
    if params:
        chat_params.update(params)
    return get_completion(prompt, chat_params, is_completion = False)


if __name__ == '__main__':
    print(get_completion('AI is going to', params={"temperature": 0.5}))
