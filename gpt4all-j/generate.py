from gpt4allj import Model

model = Model('./models/ggml-gpt4all-j', instructions='avx')


def get_completion(prompt):
    return model.generate(prompt)


if __name__ == '__main__':
    print(get_completion('AI is going to'))
