
import logging
from app.config.settings import LAUNCHER_PATH
from app.module.application.interface.launcher_interface import LauncherRepositoryInterface
from app.module.application.usecase.launcher_usecase import LauncherUsecase

logger = logging.getLogger("launcherLogger")

class LauncherPresenter:

    def __init__(self, launcher_repository: LauncherRepositoryInterface):
        self.launcher_usecase = LauncherUsecase(launcher_repository=launcher_repository)

    def get_all_launcher_data(self, launcher_path: str | None = None) -> list[dict]:
        try:
            if launcher_path is None:
                launch_data =  self.launcher_usecase.get_all_launcher_data(launcher_path=LAUNCHER_PATH)
            else:
                launch_data =  self.launcher_usecase.get_all_launcher_data(launcher_path=launcher_path)
            return launch_data
        except Exception as e:
            logger.error(f"error get_all_launcher_data: error: {e}, launcher_path: {launcher_path}")
            return 

    def save_launcher_data(self, *, key: str, launch_app_path: str, launcher_path: str | None = None) -> None:
        try:
            if launcher_path is None:
                self.launcher_usecase.save_launcher_data(
                    launcher_path=LAUNCHER_PATH, key=key, launch_app_path=launch_app_path
                    )
            else:
                self.launcher_usecase.save_launcher_data(
                    launcher_path=launcher_path, key=key, launch_app_path=launch_app_path
                    )
        except Exception as e:
            logger.error(f"error save_launcher_data: error: {e}, launcher_path: {LAUNCHER_PATH}, key: {key}, launch_app_path: {launch_app_path}")
            return
    
    def delete_launcher_data(self, *, key: str, launcher_path: str | None = None) -> str:
        try:
            if launcher_path is None:
                return self.launcher_usecase.delete_launcher_data(launcher_path=LAUNCHER_PATH, key=key)
            else:
                return self.launcher_usecase.delete_launcher_data(launcher_path=launcher_path, key=key)
        except Exception as e:
            logger.error(f"error delete_launcher_data: error: {e}, launcher_path: {LAUNCHER_PATH}, key: {key}")
            return
        
    def save_launcher_workspace(self, *, file_name: str, launcher_data: dict) -> dict | None:
        """launcherのワークスペースを保存する
        workspaceの各アプリのショートカットのパスはLAUNCHER_WORKSPACE_DIR/file_name.jsonに保存される
        """
        if file_name == "":
            return {
                "status": "error",
                "message": "ワークスペース名は必須です。入力してください"
            }
        
        launcher_usecase = LauncherUsecase()
        workspace_file_names = launcher_usecase.get_all_workspace_file_names()
        if file_name in workspace_file_names:
            return {
                "status": "warning",
                "message": "ワークスペース名は既に存在します。別の名前を入力してください"
            }

        file_name_length = len(file_name)
        if file_name_length > 15:
            return {
                "status": "warning",
                "message": "ワークスペース名は15文字以内で入力してください"
            }

        try:
            self.launcher_usecase.save_launcher_workspace(file_name=file_name, launcher_data=launcher_data)
            return {
                "status": "success",
                "message": f"ワークスペースを保存しました。ワークスペース名: {file_name}"
            }
        except Exception as e:
            logger.error(f"error save_launcher_workspace: error: {e}, file_name: {file_name}, launcher_data: {launcher_data}")
            return {
                "status": "error",
                "message": "ワークスペースを保存できませんでした"
            }
        
    def rename_workspace_file(self, *, old_path: str, new_path: str) -> dict:
        try:
            renamed_workspace_file_path =self.launcher_usecase.rename_workspace_file(old_path=old_path, new_path=new_path)
            workspace_name = self.launcher_usecase.get_app_name_from_shortcut_path(renamed_workspace_file_path)

            logger.info(f"rename file. renamed_file_path: {renamed_workspace_file_path}")
            return {
                "status": "success",
                "message": f"ワークスペース名を{workspace_name}に変更しました"
            }
        except Exception as e:
            logger.error(f"error rename_workspace_file: error: {e}, old_path: {old_path}, new_path: {new_path}")
            return {
                "status": "error",
                "message": "ワークスペースを変更できませんでした"
            }
        
    def delete_workspace_file(self, *, file_path: str) -> dict:
        try:
            deleted_file_path = self.launcher_usecase.delete_workspace_file(file_path=file_path)
            logger.info(f"deleted_file_path: {deleted_file_path}")
            return {
                "status": "success",
                "message": "ワークスペースを削除しました。"
            }
        except Exception as e:
            logger.error(f"error delete_workspace_file: error: {e}, file_path: {file_path}")
            return {
                "status": "error",
                "message": "ワークスペースを削除できませんでした"
            }
        
