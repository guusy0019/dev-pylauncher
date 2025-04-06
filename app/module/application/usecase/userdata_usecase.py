import logging
import os
from app.config.settings import LOCALE_DIR
from app.module.application.usecase.launcher_usecase import LauncherUsecase
from app.module.infrastructure.repository.userdata_repository import UserDataRepository
from app.module.application.interface.userdata_interface import UserDataRepositoryInterface

logger = logging.getLogger("userdataLogger")

class UserDataUsecase:
    
    def __init__(self, userdata_repository: UserDataRepositoryInterface = None):
        self.userdata_repository = userdata_repository or UserDataRepository()

    def save_user_data(self, *, key: str, value: str, user_data_path: str) -> None:
        return self.userdata_repository.save_user_data(key=key, value=value, user_data_path=user_data_path)
    
    def get_all_user_data(self, *, user_data_path: str) -> dict:
        return self.userdata_repository.get_all_user_data(user_data_path=user_data_path)
        
    @staticmethod
    def get_all_available_language_json_list() -> list[str]:
        """LOCALE_DIRのjsonファイルを全て取得
        Return:
            list: list[{language_code}.json]
        """
        return [file_name for file_name in os.listdir(LOCALE_DIR) if file_name.endswith(".json")]
    
    @staticmethod
    def get_all_available_language_code_list() -> list[str]:
        """LOCALE_DIRのjsonファイルのファイル名を取得
        Return:
            list: list[language_code]
        """
        return [file_name.replace(".json", "") for file_name in os.listdir(LOCALE_DIR) if file_name.endswith(".json")]
    
    @staticmethod
    def get_all_available_language() -> list[str]:
        """LOCALE_DIR/langのvalueを取得する
        Return:
            list: list[language]
        """
        lang_code_data_path = os.path.join(LOCALE_DIR, "lang.json")
        lang_code_data = LauncherUsecase().get_all_launcher_data(launcher_path=lang_code_data_path)
        return list(lang_code_data.values())
    
    @staticmethod
    def get_all_lang_data() -> dict[str, str]:
        """lang.jsonのデータを全て取得します。"""
        lang_code_data_path = os.path.join(LOCALE_DIR, "lang.json")
        return LauncherUsecase().get_all_launcher_data(launcher_path=lang_code_data_path)

