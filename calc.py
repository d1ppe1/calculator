import tkinter as tk
from tkinter import font
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("400x600")
        self.root.configure(bg='#f0f0f0')
        
        # Переменные
        self.current_input = ""
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        # История вычислений
        self.history = []
        self.max_history = 10
        
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
            ('7', '8', '9', '*', 'H'),  # H - история
            ('4', '5', '6', '-', ''),
            ('1', '2', '3', '+', ''),
            ('0', '.', '=', '', '')
        ]
        
        button_font = font.Font(family='Arial', size=14, weight='bold')
        
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                if text:
                    # Определяем цвет кнопок
                    if text in ['C', '⌫']:
                        bg_color = '#ff6b6b'
                        fg_color = 'white'
                    elif text == '=':
                        bg_color = '#4CAF50'
                        fg_color = 'white'
                    elif text in ['√', '^', 'H']:
                        bg_color = '#2196F3'
                        fg_color = 'white'
                    elif text in ['/', '*', '-', '+']:
                        bg_color = '#f0f0f0'
                        fg_color = 'black'
                    else:
                        bg_color = '#ffffff'
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
        
        # Поле для истории
        history_frame = tk.Frame(self.root, bg='#f0f0f0')
        history_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        history_label = tk.Label(
            history_frame,
            text="История:",
            font=font.Font(family='Arial', size=10),
            bg='#f0f0f0'
        )
        history_label.pack(anchor='w')
        
        self.history_text = tk.Text(
            history_frame,
            height=4,
            width=40,
            state='disabled',
            bg='white',
            fg='gray'
        )
        self.history_text.pack(pady=5)
    
    def add_to_history(self, expression, result):
        """Добавить вычисление в историю"""
        self.history.append(f"{expression} = {result}")
        if len(self.history) > self.max_history:
            self.history.pop(0)
        self.update_history_display()
    
    def update_history_display(self):
        """Обновить отображение истории"""
        self.history_text.config(state='normal')
        self.history_text.delete(1.0, tk.END)
        for item in self.history:
            self.history_text.insert(tk.END, item + "\n")
        self.history_text.config(state='disabled')
    
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
        elif text == 'H':
            self.show_history_popup()
        elif text == '=':
            self.calculate_result()
        else:
            self.current_input += text
            self.result_var.set(self.current_input)
    
    def calculate_square_root(self):
        """Вычисление квадратного корня (исправленная версия)"""
        try:
            # Проверяем, есть ли ввод
            if not self.current_input or self.current_input == "":
                # Если поле пустое, используем текущее значение на дисплее
                current_value = self.result_var.get()
                if current_value and current_value != "0" and current_value != "Ошибка":
                    try:
                        value = float(current_value)
                    except:
                        self.result_var.set("Введите число")
                        return
                else:
                    self.result_var.set("Введите число")
                    return
            else:
                # Пытаемся вычислить текущее выражение
                try:
                    value = eval(self.current_input)
                except:
                    self.result_var.set("Ошибка в выражении")
                    return
            
            # Проверяем, что value - число
            if not isinstance(value, (int, float)):
                self.result_var.set("Ошибка: некорректное значение")
                return
                
            # Вычисляем корень
            if value < 0:
                self.result_var.set("Ошибка: √ отр. числа")
                self.current_input = ""
            else:
                result = math.sqrt(value)
                # Форматируем результат
                if result.is_integer():
                    result_str = str(int(result))
                else:
                    result_str = f"{result:.2f}".rstrip('0').rstrip('.')
                
                self.result_var.set(result_str)
                self.current_input = result_str
                self.add_to_history(f"√{value}", result_str)
                
        except Exception as e:
            self.result_var.set(f"Ошибка: {str(e)}")
            self.current_input = ""
    
    def calculate_result(self):
        """Вычисление результата выражения"""
        try:
            if not self.current_input:
                return
                
            expression = self.current_input
            result = eval(expression)
            
            # Форматируем результат
            if isinstance(result, float):
                if result.is_integer():
                    result_str = str(int(result))
                else:
                    result_str = f"{result:.2f}".rstrip('0').rstrip('.')
            else:
                result_str = str(result)
            
            self.result_var.set(result_str)
            self.add_to_history(expression, result_str)
            self.current_input = result_str
            
        except ZeroDivisionError:
            self.result_var.set("Деление на ноль!")
            self.current_input = ""
        except Exception as e:
            self.result_var.set(f"Ошибка: {str(e)}")
            self.current_input = ""
    
    def show_history_popup(self):
        """Показать историю в отдельном окне"""
        if not self.history:
            self.result_var.set("История пуста")
            return
            
        popup = tk.Toplevel(self.root)
        popup.title("История вычислений")
        popup.geometry("300x400")
        popup.configure(bg='#f0f0f0')
        
        text_widget = tk.Text(popup, font=('Arial', 10), bg='white', fg='black')
        text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        for item in self.history:
            text_widget.insert(tk.END, item + "\n")
        
        text_widget.config(state='disabled')
        
        close_btn = tk.Button(
            popup,
            text="Закрыть",
            command=popup.destroy,
            bg='#2196F3',
            fg='white',
            font=('Arial', 10)
        )
        close_btn.pack(pady=10)

# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
# TODO: Здесь будет исправление бага с корнем в будущей версии