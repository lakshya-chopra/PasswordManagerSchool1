import secrets
import string

def generate_password(number_of_chars,include_numbers=True):

    choices = string.ascii_letters + string.digits + string.punctuation
    password = [secrets.choice(choices) for i in range(number_of_chars)]
    return ''.join(password)
