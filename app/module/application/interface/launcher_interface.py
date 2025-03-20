from abc import ABC, abstractmethod

class LauncherRepositoryInterface(ABC):
    @abstractmethod
    def get_all_launcher_data(self, *, launcher_path: str) -> list[dict]:
        pass
    
    @abstractmethod
    def save_launcher_data(self, *, launcher_path: str, launcher_data: dict) -> None:
        pass

    @abstractmethod
    def delete_launcher_data(self, *, launcher_path: str, key: str) -> str:
        pass

    @abstractmethod
    def read_launcher_data(self, *, launcher_path: str) -> dict:
        pass