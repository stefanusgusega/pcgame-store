import random
import string


def generate_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))