
import logging
from app.module.infrastructure.repository.launcher_repositpry import LauncherRepository
from app.module.application.interface.launcher_interface import LauncherRepositoryInterface

logger = logging.getLogger("launcherLogger")

class LauncherUsecase:

    def __init__(self, launcher_repository: LauncherRepositoryInterface):
        self.launcher_repository = launcher_repository

    def save_launcher_data(self, *, launcher_path: str, key: str, launch_app_path: str) -> None:
        return self.launcher_repository.save_launcher_data(launcher_path=launcher_path, key=key, launch_app_path=launch_app_path)
    
    def get_all_launcher_data(self, *, launcher_path: str) -> list[dict]:
        return self.launcher_repository.get_all_launcher_data(launcher_path=launcher_path)
    
    def delete_launcher_data(self, *, launcher_path: str, key: str) -> str:
        return self.launcher_repository.delete_launcher_data(launcher_path=launcher_path, key=key)
    
    def read_launcher_data(self, *, launcher_path: str) -> dict:
        return self.launcher_repository.read_launcher_data(launcher_path=launcher_path)
    

