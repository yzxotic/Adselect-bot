import random
import string

def generate_username():
    return "user" + str(random.randint(10000, 99999))

def generate_email():
    number = random.randint(10000, 99999)
    return f"pepe{number}@example.com"

def generate_phone():
    number = random.randint(1000000, 9999999)
    return f"862{number}"

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%"
    return ''.join(
        random.SystemRandom().choices(chars, k=16)
    )

def generate_data():
    return {
        "username": generate_username(),
        "email": generate_email(),
        "phone": generate_phone(),
        "password": generate_password()
    }
