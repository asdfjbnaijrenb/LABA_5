class Client:
    def __init__(self, name: str, num_of_deposits: int, deposit_size: float, deposit_type) -> None:
        self.name = name
        self.num_of_deposits = num_of_deposits
        self.deposit_size = deposit_size
        self.deposit_type = deposit_type

    def __str__(self):
        """Отображение информации о клиенте."""
        return f"Имя: {self.name}\n" \
               f"Тип депозита: {self.deposit_type.__class__.__name__}\n" \
               f"Количество вкладов: {self.num_of_deposits}\n" \
               f"Размер вклада: {self.deposit_size} рублей"
