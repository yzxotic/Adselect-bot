import random
import string
import json
import os

FILE = "generated_data.json"

if os.path.exists(FILE):
    with open(FILE, "r") as f:
        used = json.load(f)
else:
    used = []

def generate():
    while True:
        number = "86255501" + str(random.randint(10, 99))
        email = "pepe" + str(random.randint(10000, 99999)) + "@example.com"
        username = "user" + str(random.randint(10000, 99999))
        password = ''.join(
            random.choices(
                string.ascii_letters + string.digits + "!@#$",
                k=14
            )
        )

        if not any(
            x["number"] == number or x["email"] == email
            or x["username"] == username for x in used
        ):
            break

    account = {
        "number": number,
        "email": email,
        "username": username,
        "password": password
    }

    used.append(account)

    with open(FILE, "w") as f:
        json.dump(used, f, indent=4)

    print(account)

generate()
