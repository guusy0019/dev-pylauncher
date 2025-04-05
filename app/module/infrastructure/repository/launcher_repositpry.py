import json
import os
import logging

from app.config.settings import LAUNCHER_PATH, LAUNCHER_WORKSPACE_DIR
from app.module.utility.file_utility import FileUtility
from app.module.application.interface.launcher_interface import LauncherRepositoryInterface

logger = logging.getLogger("launcherLogger")

class LauncherRepository(LauncherRepositoryInterface):
    
    def get_all_launcher_data(self, launcher_path: str = LAUNCHER_PATH) -> list[dict]:
        """ランチャーのすべてのデータを取得します。 
        
        Args:
            launcher_path (str): ランチャーデータが格納されているファイルパス
            
        Returns:
            list[dict]: ランチャーデータのリスト
        """
        launcher_data = FileUtility().read_json_data(launcher_path)
        return launcher_data
    
    def save_launcher_data(self, *, launcher_path: str = LAUNCHER_PATH, key: str, launch_app_path: str) -> dict | None:
        """ランチャーデータを保存します。
        
        Args:
            launcher_path (str): ランチャーのデータを保存しているパス
            key (str): アプリケーション名
            launch_app_path (str): ランチャーに保存するアプリ単体のパス
            
        Returns:
            dict or None: 保存されたランチャーデータ。失敗した場合はNone
        """
        launcher_data = FileUtility().read_json_data(launcher_path)
        launcher_data[key] = launch_app_path
        with open(launcher_path, "w") as f:
            json.dump(launcher_data, f, indent=2)
        return launcher_data
        
    def delete_launcher_data(self, *, launcher_path : str = LAUNCHER_PATH, key : str) -> dict | None:
        launcher_data = FileUtility().read_json_data(launcher_path)
        launcher_data.pop(key)
        with open(launcher_path, "w") as f:
            json.dump(launcher_data, f)
        return launcher_data

    def save_launcher_workspace(self, *, file_name: str, launcher_data: dict) -> dict | None:
        workspace_path = os.path.join(LAUNCHER_WORKSPACE_DIR, f"{file_name}.json")
        with open(workspace_path, "w") as f:
            json.dump(launcher_data, f, indent=2)
        return launcher_data
    
    def rename_workspace_file(self, *, old_path: str, new_path: str) -> str | None:
        """拡張子含むフルパスを指定してファイル名を変更する"""
        FileUtility().rename_file(old_path, new_path)
        return new_path
    
    def delete_workspace_file(self, *, file_path: str) -> str |None:
        """拡張子含むフルパスを指定してファイルを削除する"""
        FileUtility().delete_file(file_path)
        return file_path
