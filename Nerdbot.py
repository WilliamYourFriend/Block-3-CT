import random

responses = ["Your a nerd", "Nerd", "Lmao nerd", "Ha, nerd",]
response = []

while True:
    you = input("Talk with nerd bot! (type your response)     ")

    random.shuffle(responses)
    response.append(responses.pop(0))

    print('Nerd bot says:')
    print(response)

    you2 = input("Keep talking with nerd bot? y/n    ")
    if you2 == "n":
        break
    responses.append(response.pop(0))
