import tkinter as tk
from tkinter import ttk, messagebox
from models.bank import Bank
from app.client_window import ClientWindow
from app.rate_window import RateWindow  # Импорт окна для просмотра клиентов


class MainWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Tk()  # Основное окно Tk
        self.window.title("Главное окно банка")
        self.window.geometry("400x400")

        # Создание объекта банка
        self.bank = Bank()

        # Создание кнопок
        self._create_buttons()

        # Подключаем обработчик закрытия окна
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    def _create_buttons(self):
        """Создание кнопок для разных действий."""
        button_frame = tk.Frame(self.window)
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Кнопка для добавления клиента
        ttk.Button(button_frame, text="Добавить вкладчика", command=self.open_client_window).pack(fill=tk.X, padx=5, pady=5)

        # Кнопка для просмотра информации о всех клиентах
        ttk.Button(button_frame, text="Показать информацию о клиентах", command=self.open_rate_window).pack(fill=tk.X, padx=5, pady=5)

        # Кнопка для вычисления суммы всех вкладов
        ttk.Button(button_frame, text="Вычислить сумму всех вкладов", command=self.show_total_deposits).pack(fill=tk.X, padx=5, pady=5)

    def open_client_window(self):
        """Открыть окно для добавления нового клиента."""
        ClientWindow(self.window, self.bank, self.update_clients_list)

    def open_rate_window(self):
        """Открыть окно для просмотра информации о клиентах."""
        RateWindow(self.window, self.bank)

    def show_total_deposits(self):
        """Показать общую сумму вкладов."""
        total_deposits = self.bank.get_total_deposits()
        messagebox.showinfo("Сумма всех вкладов", f"Общая сумма всех вкладов: {total_deposits} рублей")

    def update_clients_list(self):
        """Метод для обновления списка клиентов (если нужно)."""
        pass

    def on_close(self):
        """Сохранение данных при закрытии программы."""
        self.window.destroy()
