import json
import os
import random
from datetime import datetime

from generator import generate_data
from storage import load_data, save_data, is_unique
from config import SPONSOR_CODE

def generate_account():
    accounts = load_data()

    for _ in range(1000):
        account = generate_data()

        if is_unique(account, accounts):
            account["sponsor"] = SPONSOR_CODE
            account["created_at"] = datetime.now().isoformat()

            accounts.append(account)
            save_data(accounts)

            return account

    raise Exception("No se pudo generar un registro único")

def menu():
    while True:
        print("\n====== ADSELECT QA BOT ======")
        print("1. Generate test data")
        print("2. Show total generated")
        print("3. Exit")

        option = input("\nChoose: ")

        if option == "1":
            account = generate_account()

            print("\n--- GENERATED TEST DATA ---")

            for key, value in account.items():
                print(f"{key}: {value}")

            print("\nSaved successfully!")

        elif option == "2":
            accounts = load_data()
            print(f"\nTotal generated: {len(accounts)}")

        elif option == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    menu()
