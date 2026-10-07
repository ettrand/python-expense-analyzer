from collections import defaultdict
from datetime import datetime


transactions = [
    {"date": "2026-10-01", "category": "Food", "description": "Lunch", "amount": 45.0},
    {"date": "2026-10-01", "category": "Transport", "description": "Metro", "amount": 5.0},
    {"date": "2026-10-02", "category": "Entertainment", "description": "Cinema", "amount": 35.0},
    {"date": "2026-10-03", "category": "Food", "description": "Restaurant", "amount": 120.0},
    {"date": "2026-10-04", "category": "Shopping", "description": "Clothes", "amount": 200.0},
    {"date": "2026-10-05", "category": "Food", "description": "Coffee", "amount": 18.0},
    {"date": "2026-10-06", "category": "Transport", "description": "Uber", "amount": 32.0},
]


def calculate_total(transactions):
    return sum(transaction["amount"] for transaction in transactions)


def spending_by_category(transactions):
    categories = defaultdict(float)

    for transaction in transactions:
        categories[transaction["category"]] += transaction["amount"]

    return dict(categories)


def average_daily_spending(transactions):
    dates = set(transaction["date"] for transaction in transactions)

    if not dates:
        return 0

    return calculate_total(transactions) / len(dates)


def largest_expense(transactions):
    if not transactions:
        return None

    return max(transactions, key=lambda transaction: transaction["amount"])


def print_report(transactions):
    total = calculate_total(transactions)
    categories = spending_by_category(transactions)
    average = average_daily_spending(transactions)
    largest = largest_expense(transactions)

    print("=" * 45)
    print("          PERSONAL EXPENSE ANALYZER")
    print("=" * 45)

    print(f"\nTotal spending: {total:.2f} RON")
    print(f"Average daily spending: {average:.2f} RON")

    print("\nSpending by category:")
    print("-" * 30)

    for category, amount in sorted(
        categories.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        percentage = amount / total * 100
        print(f"{category:<15} {amount:>8.2f} RON ({percentage:.1f}%)")

    print("\nLargest expense:")
    print("-" * 30)
    print(f"Description: {largest['description']}")
    print(f"Category:    {largest['category']}")
    print(f"Amount:      {largest['amount']:.2f} RON")
    print(f"Date:        {largest['date']}")

    print("\n" + "=" * 45)


def add_transaction():
    print("\nAdd a new transaction")

    date = input("Date (YYYY-MM-DD): ")
    category = input("Category: ")
    description = input("Description: ")
    amount = float(input("Amount (RON): "))

    return {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }


while True:
    print("\n1. View report")
    print("2. Add transaction")
    print("3. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        print_report(transactions)

    elif choice == "2":
        transaction = add_transaction()
        transactions.append(transaction)
        print("Transaction added!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
