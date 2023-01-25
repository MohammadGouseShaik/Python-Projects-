import random
import string

def generate_password(length):
    password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))
    return password

print(generate_password(10))