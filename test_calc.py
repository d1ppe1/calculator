import pytest
from calc import add, subtract, multiply, divide

def test_add():
    """Тест сложения"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Тест вычитания"""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(10, 10) == 0

def test_multiply():
    """Тест умножения"""
    assert multiply(4, 3) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

def test_divide():
    """Тест деления"""
    assert divide(10, 2) == 5.0
    assert divide(5, 2) == 2.5
    
    # Проверка исключения при делении на ноль
    with pytest.raises(ValueError):
        divide(5, 0)