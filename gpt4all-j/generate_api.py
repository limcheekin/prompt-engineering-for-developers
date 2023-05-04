import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

"""
default_params: dict = {
    "seed": -1,
    "n_threads": -1,
    "n_predict": 200,
    "top_k": 40,
    "top_p": 0.9,
    "temp": 0.9,
    "repeat_penalty": 1,
    "repeat_last_n": 64,
    "n_batch":  8
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
    return completion['message']


if __name__ == '__main__':
    print(get_completion('AI is going to', params={"temp": 0.5}))
