from generator import generate_data
from storage import load_data, save_data, is_unique
from config import SPONSOR_CODE

def main():
accounts = load_data()
generated = []

while len(generated) < 100:
    account = generate_data()
    if is_unique(account, accounts):
        account["sponsor"] = SPONSOR_CODE
        accounts.append(account)
        generated.append(account)
save_data(accounts)
print(f"\n=== {len(generated)} TEST RECORDS GENERATED ===")
for i, account in enumerate(generated, 1):
    print(f"{i}. {account['username']} - {account['email']}")
print("\nSaved successfully!")

if name == “main”:
main()
