from app.module.infrastructure.repository.launcher_repositpry import LauncherRepository
from app.module.application.interface.launcher_interface import LauncherRepositoryInterface


class LauncherUsecase:

    def __init__(self, launcher_repository: LauncherRepository):
        self.launcher_repository = launcher_repository

    def save_launcher_path(self, *, key: str, launch_app_path: str):
        launcer_repository = LauncherRepository()
        launcer_repository.save_launcher_path(key=key, launch_app_path=launch_app_path)

    def get_launcher_path(self, *, key: str) -> str:
        launcer_repository = LauncherRepository()
        return launcer_repository.get_launcher_path(key=key)

    def get_all_launcher_path(self) -> dict[str, str]:
        launcer_repository = LauncherRepository()
        return launcer_repository.get_all_launcher_path()

    def delete_launcher_path(self, *, key: str) -> None:
        launcer_repository = LauncherRepository()
        launcer_repository.delete_launcher_path(key=key)
