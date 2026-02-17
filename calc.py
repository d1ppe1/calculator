import tkinter as tk
from tkinter import font
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("400x550")  # Немного увеличил высоту
        self.root.configure(bg='#f0f0f0')
        
        # Переменные
        self.current_input = ""
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        # Создание интерфейса
        self.create_widgets()
        
    def create_widgets(self):
        # Поле ввода/вывода
        display_frame = tk.Frame(self.root, bg='#f0f0f0')
        display_frame.pack(pady=20)
        
        display_font = font.Font(family='Arial', size=24, weight='bold')
        display = tk.Entry(
            display_frame,
            textvariable=self.result_var,
            font=display_font,
            bd=0,
            bg='white',
            fg='black',
            justify='right',
            readonlybackground='white',
            state='readonly',
            width=15
        )
        display.pack(ipady=15)
        
        # Кнопки
        buttons_frame = tk.Frame(self.root, bg='#f0f0f0')
        buttons_frame.pack()
        
        # Расположение кнопок
        buttons = [
            ('√', 'C', '⌫', '/', '^'),
            ('7', '8', '9', '*', ''),
            ('4', '5', '6', '-', ''),
            ('1', '2', '3', '+', ''),
            ('0', '.', '=', '', '')
        ]
        
        button_font = font.Font(family='Arial', size=14, weight='bold')
        
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                if text:  # Пропускаем пустые кнопки
                    # Определяем цвет кнопок
                    if text in ['C', '⌫']:
                        bg_color = '#ff6b6b'  # Красный для очистки
                        fg_color = 'white'
                    elif text == '=':
                        bg_color = '#4CAF50'  # Зеленый для равно
                        fg_color = 'white'
                    elif text in ['√', '^']:
                        bg_color = '#2196F3'  # Синий для специальных операций
                        fg_color = 'white'
                    elif text in ['/', '*', '-', '+']:
                        bg_color = '#f0f0f0'  # Светлый для арифметики
                        fg_color = 'black'
                    else:
                        bg_color = '#ffffff'  # Белый для цифр
                        fg_color = 'black'
                    
                    btn = tk.Button(
                        buttons_frame,
                        text=text,
                        font=button_font,
                        width=5,
                        height=2,
                        bd=0,
                        command=lambda t=text: self.button_click(t),
                        bg=bg_color,
                        fg=fg_color,
                        activebackground='#e0e0e0'
                    )
                    btn.grid(row=i, column=j, padx=5, pady=5)
    
    def button_click(self, text):
        if text == 'C':
            self.current_input = ""
            self.result_var.set("0")
        elif text == '⌫':
            self.current_input = self.current_input[:-1]
            self.result_var.set(self.current_input if self.current_input else "0")
        elif text == '√':
            self.calculate_square_root()
        elif text == '^':
            self.current_input += '**'
            self.result_var.set(self.current_input)
        elif text == '=':
            self.calculate_result()
        else:
            self.current_input += text
            self.result_var.set(self.current_input)
    
    def calculate_square_root(self):
        """Вычисление квадратного корня"""
        try:
            if self.current_input:
                # Пытаемся вычислить текущее выражение
                value = eval(self.current_input)
                if value < 0:
                    self.result_var.set("Ошибка: √ отр. числа")
                    self.current_input = ""
                else:
                    result = math.sqrt(value)
                    self.result_var.set(str(result))
                    self.current_input = str(result)
            else:
                # Если поле пустое, используем текущее значение
                current_value = self.result_var.get()
                if current_value and current_value != "0":
                    value = float(current_value)
                    if value < 0:
                        self.result_var.set("Ошибка: √ отр. числа")
                        self.current_input = ""
                    else:
                        result = math.sqrt(value)
                        self.result_var.set(str(result))
                        self.current_input = str(result)
        except:
            self.result_var.set("Ошибка")
            self.current_input = ""
    
    def calculate_result(self):
        """Вычисление результата выражения"""
        try:
            result = eval(self.current_input)
            self.result_var.set(str(result))
            self.current_input = str(result)
        except:
            self.result_var.set("Ошибка")
            self.current_input = ""

# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()