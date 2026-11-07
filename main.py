from generator import generate_data
from storage import load_data, save_data, is_unique
from config import SPONSOR_CODE

def main():
    accounts = load_data()

    account = generate_data()

    while not is_unique(account, accounts):
        account = generate_data()

    account["sponsor"] = SPONSOR_CODE

    accounts.append(account)

    save_data(accounts)

    print("\n=== TEST DATA GENERATED ===")

    for key, value in account.items():
        print(f"{key}: {value}")

    print("\nSaved successfully!")

if __name__ == "__main__":
    main()
