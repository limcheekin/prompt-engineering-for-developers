from gpt4allj import Model

model = Model('./models/ggml-gpt4all-j', instructions='avx')

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


def get_completion(prompt: str, params: dict = default_params):
    default_params.update(params)
    return model.generate(prompt=prompt,
                          seed=default_params["seed"],
                          n_threads=default_params["n_threads"],
                          n_predict=default_params["n_predict"],
                          top_k=default_params["top_k"],
                          top_p=default_params["top_p"],
                          temp=default_params["temp"],
                          repeat_penalty=default_params["repeat_penalty"],
                          repeat_last_n=default_params["repeat_last_n"],
                          n_batch=default_params["n_batch"])


if __name__ == '__main__':
    print(get_completion('AI is going to'))
