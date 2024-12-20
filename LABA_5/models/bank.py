from models.database import DatabaseManager
from models.client import Client
from models.deposit import StandardDeposit, BonusDeposit


class Bank:
    def __init__(self):
        """Инициализация банка."""
        self.clients = {}
        self.db_manager = DatabaseManager()
        self.load_clients_from_db()

    def load_clients_from_db(self):
        """Загрузка клиентов из базы данных."""
        clients_data = self.db_manager.get_all_clients()
        for client_data in clients_data:
            _, name, num_deposits, deposit_size, deposit_type = client_data
            deposit_type_obj = StandardDeposit() if deposit_type == "StandardDeposit" else BonusDeposit()
            self.clients[name] = Client(name, num_deposits, deposit_size, deposit_type_obj)

    def add_new_client(self, name, num_of_deposits, deposit_size, deposit_type):
        """Добавить нового клиента."""
        if name in self.clients:
            raise ValueError(f"Клиент с именем '{name}' уже существует.")

        client = Client(name, num_of_deposits, deposit_size, deposit_type)
        self.clients[name] = client

        # Сохранение в базу данных
        self.db_manager.add_client({
            "name": name,
            "num_of_deposits": num_of_deposits,
            "deposit_size": deposit_size,
            "deposit_type": deposit_type
        })

    def remove_client(self, name: str) -> None:
        """Удаление клиента из банка и базы данных."""
        if name in self.clients:
            del self.clients[name]
            self.db_manager.delete_client(name)
        else:
            raise ValueError(f"Клиент с именем '{name}' не найден.")

    def get_total_deposits(self):
        """Получить сумму всех вкладов."""
        total = 0
        for client in self.clients.values():
            deposit_amount = client.num_of_deposits * client.deposit_size
            total += client.deposit_type.calculate_deposit(deposit_amount)
        return total
