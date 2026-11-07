from generator import generate_data
from storage import load_data, save_data, is_unique
from config import SPONSOR_CODE

def generate_batch(amount=100):
    accounts = load_data()
    generated = []

    while len(generated) < amount:
        account = generate_data()

        if is_unique(account, accounts):
            account["sponsor"] = SPONSOR_CODE

            accounts.append(account)
            generated.append(account)

    save_data(accounts)

    print(f"\nGenerated: {len(generated)}")

    for i, account in enumerate(generated, 1):
        print(f"{i}. {account['username']} - {account['email']}")

    print("\nAll data saved successfully!")

if __name__ == "__main__":
    generate_batch(100)
