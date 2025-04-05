
import logging
import os

from app.config.settings import LAUNCHER_WORKSPACE_DIR
from app.module.infrastructure.repository.launcher_repositpry import LauncherRepository
from app.module.application.interface.launcher_interface import LauncherRepositoryInterface

logger = logging.getLogger("launcherLogger")

class LauncherUsecase:

    def __init__(self, launcher_repository: LauncherRepositoryInterface = None):
        self.launcher_repository = launcher_repository or LauncherRepository()

    def get_all_launcher_data(self, *, launcher_path: str) -> list[dict]:
        return self.launcher_repository.get_all_launcher_data(launcher_path=launcher_path)

    def save_launcher_data(self, *, launcher_path: str, key: str, launcher_app_path: str) -> None:
        return self.launcher_repository.save_launcher_data(launcher_path=launcher_path, key=key, launcher_app_path=launcher_app_path)
    
    def delete_launcher_data(self, *, launcher_path: str, key: str) -> str:
        return self.launcher_repository.delete_launcher_data(launcher_path=launcher_path, key=key)
    
    def save_launcher_workspace(self, *, file_name: str, launcher_data: dict) -> dict | None:
        return self.launcher_repository.save_launcher_workspace(file_name=file_name, launcher_data=launcher_data)
    
    @staticmethod
    def get_all_workspace_file_names() -> list[str]:
        workspace_file_names = os.listdir(LAUNCHER_WORKSPACE_DIR)
        return [file_name.replace(".json", "") for file_name in workspace_file_names if file_name.endswith(".json")]
    
    @staticmethod
    def get_all_workspace_file_paths() -> list[str]:
        workspace_file_names = os.listdir(LAUNCHER_WORKSPACE_DIR)
        return [os.path.join(LAUNCHER_WORKSPACE_DIR, file_name) for file_name in workspace_file_names if file_name.endswith(".json")]
    
    @staticmethod
    def get_app_name_from_shortcut_path(shortcut_path: str) -> str:
        return os.path.splitext(os.path.basename(shortcut_path))[0]
