import json
import os
import locale
import logging
from typing import Dict, Any


from app.config.settings import LOCALE_DIR, USER_DATA_PATH
from app.module.utility.file_utility import FileUtility

from app.module.application.usecase.userdata_usecase import UserDataUsecase
from app.module.infrastructure.repository.userdata_repository import UserDataRepository

logger = logging.getLogger("launcherLogger")

class I18n:

    def __init__(self):
        sys_language_code = locale.getdefaultlocale()[0][:2]

        file_utility = FileUtility()
        available_language_list = file_utility.read_json_data(os.path.join(LOCALE_DIR, "lang.json"))

        userdata_usecase = UserDataUsecase(userdata_repository=UserDataRepository())
        user_data = userdata_usecase.get_all_user_data(user_data_path=USER_DATA_PATH)

        user_language_code = user_data.get("language_code", None)
        # user_language_code = "en"
        
        # 初期化時の言語情報保存時にはlang.jsonで翻訳済みの言語コードのみを保存するようにする。
        if user_language_code is None:
            language_code = sys_language_code if sys_language_code in available_language_list else "en"

            userdata_usecase.save_user_data(
                key="language_code", 
                value=language_code, 
                user_data_path=USER_DATA_PATH
                )
        else:
            language_code = user_language_code

        locale_file = os.path.join(LOCALE_DIR, f"{language_code}.json")
        locale_data = file_utility.read_json_data(locale_file)
        self.locale_data = locale_data

        logger.info(f"language_code: {language_code}. locale_file_path: {locale_file}")

    def get_text(self, key: str) -> str:
        """
        ドット表記で階層的にアクセスするメソッド
        例: get_text("menu.settings") は self.locale_data["menu"]["settings"] の値を返す
        """
        keys = key.split('.')
        current_data = self.locale_data
        for k in keys:
            if isinstance(current_data, dict) and k in current_data:
                current_data = current_data[k]
            else:
                # キーが存在しない場合はキー名をそのまま返す
                return key
        
        # 最終的な値が辞書でなければその値を返す
        if isinstance(current_data, str):
            return current_data
        else:
            # 辞書の場合はキー名をそのまま返す
            return key
    
    def get_section(self, section_key: str = None) -> Dict[str, Any]:
        """
        指定されたセクション（階層）全体を取得するメソッド
        例: get_section("menu") は self.locale_data["menu"] 辞書全体を返す
        """
        if section_key is None:
            return self.locale_data
            
        # キーをドットで分割
        keys = section_key.split('.')
        # 階層を辿って値を取得
        current_data = self.locale_data
        for k in keys:
            if isinstance(current_data, dict) and k in current_data:
                current_data = current_data[k]
            else:
                # キーが存在しない場合は空の辞書を返す
                return {}
                
        return current_data if isinstance(current_data, dict) else {}