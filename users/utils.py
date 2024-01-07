import random


def token_generate(email):
    key = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    token = f'{email}:{key}'
    return key, token

def email_token(token):
    email = token.split(':')[0]
    key = token.split(':')[1]
    return key, email
