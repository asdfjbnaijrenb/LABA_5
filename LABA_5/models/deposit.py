from abc import ABC, abstractmethod

class DepositType(ABC):
    @abstractmethod
    def calculate_deposit(self, deposit_size: float) -> float:
        pass

class StandardDeposit(DepositType):
    def calculate_deposit(self, deposit_size: float) -> float:
        return deposit_size  # Стандартный вклад без бонуса

class BonusDeposit(DepositType):
    def calculate_deposit(self, deposit_size: float) -> float:
        bonus = 1000  # Бонус
        return deposit_size + bonus
