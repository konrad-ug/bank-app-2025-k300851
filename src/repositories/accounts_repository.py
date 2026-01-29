from abc import ABC, abstractmethod


class AccountsRepository(ABC):
    @abstractmethod
    def save_all(self): #pragma: no cover
        pass

    @abstractmethod
    def load_all(self): #pragma: no cover
        pass
