from abc import ABC, abstractmethod

class LauncherRepositoryInterface(ABC):
    @abstractmethod
    def get_all_launcher_data(self, *, launcher_path: str | None) -> list[dict]:
        pass
    
    @abstractmethod
    def save_launcher_data(self, *, launcher_path: str | None, key: str, launch_app_path: str) -> None:
        pass

    @abstractmethod
    def delete_launcher_data(self, *, launcher_path: str | None, key: str) -> str:
        pass

    @abstractmethod
    def save_launcher_workspace(self, *, file_name: str, launcher_data: dict) -> dict | None:
        pass

    @abstractmethod
    def rename_workspace_file(self, *, old_path: str, new_path: str) -> str | None:
        pass

    @abstractmethod
    def delete_workspace_file(self, *, file_path: str) -> str | None:
        pass

