"""Модуль реализует функции для операций с банковским счётом и проверяет
правильность данных с помощью пользовательских исключений, таких как
NegativeDepositError, InsufficientFundsError, и UnauthorizedAccessError.
"""

from exceptions import NegativeDepositError, InsufficientFundsError, UnauthorizedAccessError

def deposit(amount):
    """Шаг 1. Пополнение счёта. Вызывает исключение, если сумма пополнения отрицательна."""
    if amount < 0:
        raise NegativeDepositError("Сумма пополнения не может быть отрицательной.")
    print(f"Счёт пополнен на {amount} единиц.")
    return amount

def withdraw(balance, amount):
    """Шаг 1. Снятие средств. Вызывает исключение, если недостаточно средств на счёте."""
    if amount > balance:
        raise InsufficientFundsError("Недостаточно средств для снятия.")
    balance -= amount
    print(f"Снято {amount} единиц. Остаток: {balance}")
    return balance

def safe_divide(a, b):
    """Шаг 2. Безопасное деление с проверкой деления на ноль."""
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"Ошибка при делении: {e}")
        return None

def access_account_data(user_role):
    """Шаг 3. Доступ к закрытым данным с проверкой роли пользователя."""
    try:
        if user_role != "admin":
            raise UnauthorizedAccessError("Только администраторы могут получить доступ к данным.")
        print("Доступ к данным разрешен")
        return "Данные аккаунта"
    except UnauthorizedAccessError as e:
        print(f"Ошибка доступа: {e}")
        return None
    finally:
        print("Проверка доступа завершена.")

def transfer_funds(balance, amount, account_status="active"):
    """Шаг 4. Перевод средств с проверкой статуса аккаунта и наличия средств."""
    try:
        if account_status != "active":
            raise UnauthorizedAccessError("Аккаунт не активен для перевода средств.")
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма перевода должна быть числом.")
        if amount > balance:
            raise InsufficientFundsError("Недостаточно средств для перевода.")
        balance -= amount
        print(f"Переведено {amount} единиц. Остаток: {balance}")
        return balance
    except UnauthorizedAccessError as e:
        print(f"Ошибка доступа: {e}")
    except TypeError as e:
        print(f"Некорректный тип данных для суммы: {e}")
    except InsufficientFundsError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Завершение операции перевода.")
    return None

def validate_transaction_data(data):
    """Шаг 5. Валидация данных транзакции с генерацией и обработкой исключений."""
    try:
        if not isinstance(data, dict):
            raise TypeError("Ожидается словарь с данными транзакции.")
        if "amount" in data and data["amount"] < 0:
            raise NegativeDepositError("Сумма транзакции не может быть отрицательной.")
        if "user_role" in data and data["user_role"] != "admin":
            raise UnauthorizedAccessError("Только администраторы могут выполнять это действие.")
        print("Данные транзакции валидны.")
        return "Данные валидны"
    except (TypeError, NegativeDepositError, UnauthorizedAccessError) as e:
        print(f"Ошибка валидации данных транзакции: {e}")
    finally:
        print("Завершение проверки данных транзакции.")
    return None

def validate_deposit_amount(amount):
    """Шаг 7. Проверяет сумму пополнения, выдает NegativeDepositError, если сумма некорректна."""
    try:
        if amount < 0:
            raise NegativeDepositError("Сумма пополнения не может быть отрицательной.")
        print("Сумма пополнения корректна.")
        return True
    except NegativeDepositError as e:
        print(f"Ошибка: {e}")
        return False
    finally:
        print("Проверка суммы пополнения завершена.")

def create_transaction(user_role, amount, account_status):
    """Шаг 8. Создаёт транзакцию пополнения с проверкой роли и статуса."""
    try:
        access_account_data(user_role)
        if account_status != "active":
            raise UnauthorizedAccessError("Аккаунт не активен.")
        validate_deposit_amount(amount)
        deposit(amount)
    except UnauthorizedAccessError as e:
        print(f"Ошибка при создании транзакции: {e}")
    except NegativeDepositError as e:
        print(f"Ошибка при создании транзакции: {e}")

def close_account(user_role):
    """Шаг 8. Закрытие аккаунта с проверкой роли пользователя."""
    access_account_data(user_role)

def audit_transactions(transaction_list):
    """Шаг 8. Проверка списка транзакций на корректность данных."""
    for transaction in transaction_list:
        validate_transaction_data(transaction)
