import tkinter as tk
from tkinter import ttk, messagebox

class RateWindow:
    def __init__(self, parent, bank):
        self.parent = parent
        self.bank = bank

        # Создание окна
        self.window = tk.Toplevel(parent)
        self.window.title("Информация о клиентах")
        self.window.geometry("400x400")

        # Создание Listbox для отображения клиентов
        self.clients_listbox = tk.Listbox(self.window)
        self.clients_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Заполнение списка клиентов
        self.update_clients_list()

        # Кнопка для отображения информации о клиенте
        ttk.Button(self.window, text="Показать информацию о клиенте", command=self.show_client_info).pack(pady=10)

        # Кнопка для сохранения списка
        ttk.Button(self.window, text="Сохранить список", command=self.save_clients_list).pack(pady=10)

        # Клавиша для удаления клиента
        self.window.bind("<BackSpace>", lambda event: self.delete_client())

    def update_clients_list(self):
        """Обновление списка клиентов в Listbox."""
        self.clients_listbox.delete(0, tk.END)  # Очистить текущий список
        for name in self.bank.clients:
            self.clients_listbox.insert(tk.END, name)  # Добавить клиентов в список

    def delete_client(self, event=None):
        """Удаление выбранного клиента."""
        try:
            selection = self.clients_listbox.curselection()
            if not selection:
                messagebox.showwarning("Предупреждение", "Выберите клиента для удаления")
                return

            client_name = self.clients_listbox.get(selection[0])
            if messagebox.askyesno("Подтверждение",
                                 f"Вы уверены, что хотите удалить клиента '{client_name}'?"):
                self.bank.remove_client(client_name)
                self.update_clients_list()
                messagebox.showinfo("Успех", f"Клиент '{client_name}' успешно удален")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при удалении: {str(e)}")

    def show_client_info(self):
        """Показать информацию о выбранном клиенте."""
        try:
            selected_name = self.clients_listbox.get(tk.ACTIVE)
            client = self.bank.clients.get(selected_name)
            if client:
                client_info = (
                    f"Имя: {client.name}\n"
                    f"Тип депозита: {client.deposit_type.__class__.__name__}\n"
                    f"Количество вкладов: {client.num_of_deposits}\n"
                    f"Размер вклада: {client.deposit_size}"
                )
                messagebox.showinfo("Информация о клиенте", client_info)
            else:
                messagebox.showerror("Ошибка", "Клиент не найден.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

    def save_clients_list(self):
        """Сохранить список клиентов в базу данных и файл."""
        try:
            # Сохранение в файл
            with open("clients_list.txt", "w") as file:
                for name, client in self.bank.clients.items():
                    file.write(f"Имя: {client.name}, "
                               f"Тип депозита: {client.deposit_type.__class__.__name__}, "
                               f"Количество вкладов: {client.num_of_deposits}, "
                               f"Размер вклада: {client.deposit_size}\n")

            # Обновление данных в базе данных
            for name, client in self.bank.clients.items():
                self.bank.db_manager.update_client({
                    "name": name,
                    "num_of_deposits": client.num_of_deposits,
                    "deposit_size": client.deposit_size,
                    "deposit_type": client.deposit_type
                })

            messagebox.showinfo("Успех", "Список клиентов сохранен.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить данные. Ошибка: {str(e)}")
