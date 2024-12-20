import sqlite3
from typing import Dict, Any


class DatabaseManager:
    def __init__(self):
        """Инициализация менеджера базы данных."""
        self.db_name = "bank.db"
        self.init_database()

    def init_database(self):
        """Инициализация базы данных и создание таблиц."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    num_of_deposits INTEGER NOT NULL,
                    deposit_size REAL NOT NULL,
                    deposit_type TEXT NOT NULL
                )
            """)
            conn.commit()

    def add_client(self, client_data: Dict[str, Any]) -> None:
        """Добавление нового клиента в базу данных."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO clients (name, num_of_deposits, deposit_size, deposit_type)
                VALUES (?, ?, ?, ?)
            """, (
                client_data["name"],
                client_data["num_of_deposits"],
                client_data["deposit_size"],
                client_data["deposit_type"].__class__.__name__
            ))
            conn.commit()

    def get_all_clients(self) -> list:
        """Получение всех клиентов из базы данных."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clients")
            return cursor.fetchall()

    def get_client_by_name(self, name: str) -> tuple:
        """Получение клиента по имени."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clients WHERE name = ?", (name,))
            return cursor.fetchone()

    def update_client(self, client_data: Dict[str, Any]) -> None:
        """Обновление данных клиента."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE clients 
                SET num_of_deposits = ?, deposit_size = ?, deposit_type = ?
                WHERE name = ?
            """, (
                client_data["num_of_deposits"],
                client_data["deposit_size"],
                client_data["deposit_type"].__class__.__name__,
                client_data["name"]
            ))
            conn.commit()

    def delete_client(self, name: str) -> None:
        """Удаление клиента из базы данных."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM clients WHERE name = ?", (name,))
            conn.commit()
