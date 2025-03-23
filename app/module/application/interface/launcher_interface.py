from abc import ABC, abstractmethod

class LauncherRepositoryInterface(ABC):
    @abstractmethod
    def get_all_launcher_data(self, *, launcher_path: str) -> list[dict]:
        pass
    
    @abstractmethod
    def save_launcher_data(self, *, launcher_path: str, key: str, launch_app_path: str) -> None:
        pass

    @abstractmethod
    def delete_launcher_data(self, *, launcher_path: str, key: str) -> str:
        pass