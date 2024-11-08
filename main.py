"""Молуль запускает все функции"""

from functions import (
    deposit,
    withdraw,
    safe_divide,
    access_account_data,
    transfer_funds,
    validate_transaction_data,
    validate_deposit_amount,
    create_transaction,
    close_account,
    audit_transactions
)

from exceptions import NegativeDepositError, InsufficientFundsError

def run_all_bank_functions():
    """Шаг 9. Последовательно вызывает все функции"""
    print("Шаг 1:")
    try:
        deposit(-100)
    except NegativeDepositError as e:
        print(e)

    try:
        withdraw(50, 100)
    except InsufficientFundsError as e:
        print(e)

    print("\nШаг 2:")
    safe_divide(10, 0)

    print("\nШаг 3:")
    access_account_data("user")

    print("\nШаг 4:")
    transfer_funds(200, "100", account_status="inactive")

    print("\nШаг 5:")
    validate_transaction_data({"amount": -500})

    print("\nШаг 7:")
    validate_deposit_amount(-200)

    print("\nШаг 8:")
    create_transaction("user", -100, "active")
    create_transaction("admin", 100, "active")

    close_account("user")
    audit_transactions([{"amount": 50, "user_role": "viewer"}, {"amount": -300}])

if __name__ == "__main__":
    run_all_bank_functions()
