import pytest
import tkinter as tk
from calc import Calculator
import time

class TestCalculator:
    """Тесты для графического калькулятора"""
    
    def setup_method(self):
        """Создаем экземпляр калькулятора перед каждым тестом"""
        self.root = tk.Tk()
        self.root.withdraw()  # Скрываем окно
        self.calc = Calculator(self.root)
    
    def teardown_method(self):
        """Уничтожаем окно после каждого теста"""
        try:
            self.root.update()
            time.sleep(0.1)  # Небольшая задержка
            self.root.destroy()
        except:
            pass
    
    def test_initial_state(self):
        """Тест начального состояния"""
        assert self.calc.result_var.get() == "0"
        assert self.calc.current_input == ""
    
    def test_number_input(self):
        """Тест ввода цифр"""
        self.calc.button_click('1')
        assert self.calc.current_input == "1"
        assert self.calc.result_var.get() == "1"
        
        self.calc.button_click('2')
        assert self.calc.current_input == "12"
        assert self.calc.result_var.get() == "12"
    
    def test_clear(self):
        """Тест очистки (C)"""
        self.calc.button_click('1')
        self.calc.button_click('2')
        self.calc.button_click('C')
        assert self.calc.current_input == ""
        assert self.calc.result_var.get() == "0"
    
    def test_backspace(self):
        """Тест удаления последнего символа (⌫)"""
        self.calc.button_click('1')
        self.calc.button_click('2')
        self.calc.button_click('3')
        self.calc.button_click('⌫')
        assert self.calc.current_input == "12"
        assert self.calc.result_var.get() == "12"
    
    def test_addition(self):
        """Тест сложения"""
        self.calc.button_click('2')
        self.calc.button_click('+')
        self.calc.button_click('3')
        self.calc.calculate_result()
        assert self.calc.result_var.get() == "5"
    
    def test_subtraction(self):
        """Тест вычитания"""
        self.calc.button_click('5')
        self.calc.button_click('-')
        self.calc.button_click('2')
        self.calc.calculate_result()
        assert self.calc.result_var.get() == "3"
    
    def test_multiplication(self):
        """Тест умножения"""
        self.calc.button_click('4')
        self.calc.button_click('*')
        self.calc.button_click('3')
        self.calc.calculate_result()
        assert self.calc.result_var.get() == "12"
    
    def test_division(self):
        """Тест деления"""
        self.calc.button_click('1')
        self.calc.button_click('0')
        self.calc.button_click('/')
        self.calc.button_click('2')
        self.calc.calculate_result()
        assert self.calc.result_var.get() == "5.0"
    
    def test_square_root(self):
        """Тест квадратного корня"""
        self.calc.button_click('9')
        self.calc.calculate_square_root()
        assert float(self.calc.result_var.get()) == 3.0
    
    def test_square_root_error(self):
        """Тест корня из отрицательного числа"""
        self.calc.button_click('-')
        self.calc.button_click('9')
        self.calc.calculate_square_root()
        assert "Ошибка" in self.calc.result_var.get()
    
    def test_power(self):
        """Тест возведения в степень (через ^)"""
        self.calc.button_click('2')
        self.calc.button_click('^')
        self.calc.button_click('3')
        self.calc.calculate_result()
        assert self.calc.result_var.get() == "8"
    
    def test_complex_expression(self):
        """Тест сложного выражения"""
        self.calc.button_click('2')
        self.calc.button_click('+')
        self.calc.button_click('3')
        self.calc.button_click('*')
        self.calc.button_click('4')
        self.calc.button_click('-')
        self.calc.button_click('5')
        self.calc.button_click('/')
        self.calc.button_click('2')
        self.calc.calculate_result()
        assert float(self.calc.result_var.get()) == 11.5