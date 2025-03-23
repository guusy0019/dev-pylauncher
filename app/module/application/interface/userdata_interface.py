from abc import ABC, abstractmethod

class UserDataRepositoryInterface(ABC):
    @abstractmethod
    def get_all_user_data(self, *, user_data_path: str) -> list[dict]:
        pass

    @abstractmethod
    def save_user_data(self, *, user_data_path: str, key: str, value: str) -> dict | None:
        pass