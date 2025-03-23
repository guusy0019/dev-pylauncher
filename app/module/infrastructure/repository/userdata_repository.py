import json
import logging

from app.config.settings import USER_DATA_PATH
from app.module.utility.file_utility import FileUtility

logger = logging.getLogger("launcherLogger")

class UserDataRepository:
    
        def get_all_user_data(self, user_data_path: str = USER_DATA_PATH) -> list[dict]:
            """ユーザーデータのすべてのデータを取得します。
    
            Args:
                user_data_path (str): ユーザーデータが格納されているファイルパス
    
            Returns:
                list[dict]: ユーザーデータのリスト
            """
            user_data = FileUtility().read_json_data(user_data_path)
            return user_data
        
        def save_user_data(self, *, user_data_path: str = USER_DATA_PATH, key: str, value: str) -> dict | None:
            """ユーザーデータを保存します。
    
            Args:
                user_data_path (str): ユーザーのデータを保存しているパス
                key (str): テーマー名や言語名などのキー
                value (str): テーマーや言語の値
                
            Returns:
                dict or None: 保存されたユーザーデータ。失敗した場合はNone
            """
            user_data = FileUtility().read_json_data(user_data_path)
            user_data[key] = value
            with open(user_data_path, "w") as f:
                json.dump(user_data, f, indent=2)
            return user_data