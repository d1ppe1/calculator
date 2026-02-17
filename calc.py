# Простой калькулятор

def add(a, b):
    """Сложение"""
    return a + b

def subtract(a, b):
    """Вычитание"""
    return a - b

def multiply(a, b):
    """Умножение"""
    return a * b

def divide(a, b):
    """Деление"""
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

if name == "__main__":
    print("=" * 30)
    print("     ПРОСТОЙ КАЛЬКУЛЯТОР")
    print("=" * 30)
    
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
    print("4 * 3 =", multiply(4, 3))
    print("10 / 2 =", divide(10, 2))