from abc import ABC, abstractmethod

class LauncherRepositoryInterface(ABC):
    @abstractmethod
    def save_launcher_path(self, *, key: str, launcher_path: str) -> None:
        pass

    @abstractmethod
    def get_launcher_path(self, *, key: str) -> str:
        pass

    @abstractmethod
    def get_all_launcher_path(self) -> str:
        pass

    @abstractmethod
    def delete_launcher_path(self, *, key: str) -> None:
        pass