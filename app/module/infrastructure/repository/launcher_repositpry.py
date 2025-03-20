import json
import logging

from app.config.settings import LAUNCHER_PATH
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
        launcher_data = self._read_launcher_data(launcher_path)
        return launcher_data
    
    def save_launcher_data(self, *, launcher_path: str = LAUNCHER_PATH, key: str, launcher_app_path: str) -> dict | None:
        """ランチャーデータを保存します。
        
        Args:
            launcher_path (str): ランチャーのデータを保存しているパス
            key (str): アプリケーション名
            launcher_app_path (str): ランチャーに保存するアプリ単体のパス
            
        Returns:
            dict or None: 保存されたランチャーデータ。失敗した場合はNone
        """
        launcher_data = self._read_launcher_data(launcher_path)
        launcher_data[key] = launcher_app_path
        with open(launcher_path, "w") as f:
            json.dump(launcher_data, f)
        return launcher_data
        
    def delete_launcher_data(self, *, launcher_path : str = LAUNCHER_PATH, key : str) -> dict | None:
        launcher_data = self._read_launcher_data(launcher_path)
        launcher_data.pop(key)
        with open(launcher_path, "w") as f:
            json.dump(launcher_data, f)
        return launcher_data
    
    def _read_launcher_data(self, launcher_path : str) -> dict:
        """pathを読み込む、読み込めなければ空のdictを返す"""
        try:
            with open(launcher_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"FileNotFoundError read_launcher_data: {launcher_path}")
            return {}
        except json.JSONDecodeError:
            logger.error(f"JSONDecodeError read_launcher_data: {launcher_path}")
            return {}
        except Exception as e:
            logger.error(f"Exception read_launcher_data: error:{e} launcher_path:{launcher_path}")
            return {}
