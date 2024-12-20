import tkinter as tk
from tkinter import ttk, messagebox
from models.bank import Bank
from models.deposit import StandardDeposit, BonusDeposit

class ClientWindow:
    """Окно добавления вкладчика."""

    def __init__(self, parent: tk.Tk, bank: Bank, callback=None) -> None:
        self.window = tk.Toplevel(parent)
        self.window.title("Добавление вкладчика")
        self.window.geometry("400x400")
        self.bank = bank
        self.callback = callback

        # Создание интерфейса
        self.create_widgets()

    def create_widgets(self) -> None:
        """Создание виджетов для добавления вкладчика."""
        frame = ttk.LabelFrame(self.window, text="Данные вкладчика")
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Ввод имени вкладчика
        ttk.Label(frame, text="Имя:").pack(anchor=tk.W, padx=5, pady=2)
        self.name_entry = ttk.Entry(frame)
        self.name_entry.pack(fill=tk.X, padx=5, pady=2)

        # Ввод количества вкладов
        ttk.Label(frame, text="Количество вкладов:").pack(anchor=tk.W, padx=5, pady=2)
        self.num_of_deposits_entry = ttk.Entry(frame)
        self.num_of_deposits_entry.pack(fill=tk.X, padx=5, pady=2)

        # Ввод размера одного вклада
        ttk.Label(frame, text="Размер одного вклада:").pack(anchor=tk.W, padx=5, pady=2)
        self.deposit_size_entry = ttk.Entry(frame)
        self.deposit_size_entry.pack(fill=tk.X, padx=5, pady=2)

        # Выбор типа вклада
        ttk.Label(frame, text="Тип вклада:").pack(anchor=tk.W, padx=5, pady=2)
        self.deposit_type_var = tk.StringVar()
        self.deposit_type_combo = ttk.Combobox(
            frame,
            textvariable=self.deposit_type_var,
            values=["Обычный вклад", "Вклад с бонусом"]
        )
        self.deposit_type_combo.pack(fill=tk.X, padx=5, pady=2)

        # Кнопки для добавления или отмены
        button_frame = ttk.Frame(self.window)
        button_frame.pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(button_frame, text="Добавить", command=self.save_client).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Отмена", command=self.window.destroy).pack(side=tk.LEFT, padx=5)

    def save_client(self) -> None:
        """Сохранить вкладчика в банк."""
        try:
            # Получаем значения из полей
            name = self.name_entry.get().strip()
            num_of_deposits = self.num_of_deposits_entry.get().strip()
            deposit_size = self.deposit_size_entry.get().strip()
            deposit_type_choice = self.deposit_type_combo.get().strip()

            # Проверка, что все поля заполнены корректно
            if not name:
                raise ValueError("Имя вкладчика не может быть пустым.")
            if not num_of_deposits or not deposit_size:
                raise ValueError("Количество вкладов и размер вклада должны быть указаны.")
            if not deposit_type_choice:
                raise ValueError("Выберите тип вклада.")

            # Проверка, что количество вкладов и размер вклада — это числа
            try:
                num_of_deposits = int(num_of_deposits)
                if not (1 <= num_of_deposits <= 100):
                    raise ValueError("Количество вкладов должно быть от 1 до 100.")
            except ValueError:
                raise ValueError("Введите корректное количество вкладов (целое число от 1 до 100).")

            try:
                deposit_size = float(deposit_size)
                if not (1000 <= deposit_size <= 1_000_000):
                    raise ValueError("Размер вклада должен быть от 1000 до 1,000,000.")
            except ValueError:
                raise ValueError("Введите корректный размер вклада (число от 1000 до 1,000,000).")

            # Выбор типа вклада
            if deposit_type_choice == "Обычный вклад":
                deposit_type = StandardDeposit()
            elif deposit_type_choice == "Вклад с бонусом":
                deposit_type = BonusDeposit()
            else:
                raise ValueError("Неверно выбран тип вклада.")

            # Добавляем вкладчика в банк
            self.bank.add_new_client(name, num_of_deposits, deposit_size, deposit_type)

            # Если есть callback, вызываем его
            if self.callback:
                self.callback()

            messagebox.showinfo("Успех", f"Вкладчик '{name}' успешно добавлен.")
            self.window.destroy()

        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка: {str(e)}")
