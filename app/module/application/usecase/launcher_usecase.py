
import logging
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
    

