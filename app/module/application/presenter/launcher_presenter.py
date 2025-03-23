
import logging
from app.config.settings import LAUNCHER_PATH
from app.module.application.interface.launcher_interface import LauncherRepositoryInterface

logger = logging.getLogger("launcherLogger")

class LauncherPresenter:
    launcher_path = LAUNCHER_PATH


    def __init__(self, launcher_repository: LauncherRepositoryInterface):
        self.launcher_repository = launcher_repository

    def get_all_launcher_data(self) -> list[dict]:
        try:
            launch_data =  self.launcher_repository.get_all_launcher_data(launcher_path=self.launcher_path)
            return launch_data
        except Exception as e:
            logger.error(f"error get_all_launcher_data: error: {e}, launcher_path: {self.launcher_path}")
            return 

    def save_launcher_data(self, *, key: str, launch_app_path: str) -> None:
        try:
            self.launcher_repository.save_launcher_data(
                launcher_path=self.launcher_path, key=key, launch_app_path=launch_app_path
                )
        except Exception as e:
            logger.error(f"error save_launcher_data: error: {e}, launcher_path: {self.launcher_path}, key: {key}, launch_app_path: {launch_app_path}")
            return
    
    def delete_launcher_data(self, *, key: str) -> str:
        try:
            return self.launcher_repository.delete_launcher_data(launcher_path=self.launcher_path, key=key)
        except Exception as e:
            logger.error(f"error delete_launcher_data: error: {e}, launcher_path: {self.launcher_path}, key: {key}")
            return
