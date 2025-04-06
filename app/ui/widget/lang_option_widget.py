import logging
import customtkinter

from app.config.settings import USER_DATA_PATH
from app.module.utility.file_utility import FileUtility
from app.utility.app_manager import restart_app

from app.utility.i18n import I18n
from app.module.application.usecase.userdata_usecase import UserDataUsecase
from app.module.infrastructure.repository.userdata_repository import UserDataRepository

logger = logging.getLogger("launcherLogger")

class LangOptionWidget(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.i18n = I18n()

        self.file_utility = FileUtility()
        self.userdata_usecase = UserDataUsecase(UserDataRepository())
        user_data = self.userdata_usecase.get_all_user_data(user_data_path=USER_DATA_PATH)

        self.all_lang_data = self.userdata_usecase.get_all_lang_data()

        user_language_code: str | None = user_data.get("language_code", None)

        # ja, enなどのlang_codeから日本語, 英語などに変換
        self.user_lang = self.all_lang_data.get(user_language_code, None)

        self.available_language_code_list = self.userdata_usecase.get_all_available_language()

        self.setup_frame()

    def setup_frame(self):

        self.lang_option_menu = customtkinter.CTkOptionMenu(
            self,
            values=self.available_language_code_list,
            command=self.lang_option_menu_callback,
        )
        self.lang_option_menu.set(self.user_lang)
        self.lang_option_menu.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.lang_option_menu_label = customtkinter.CTkLabel(
            self,
            text=self.i18n.get_text("config_page.language_settings"),
            font=customtkinter.CTkFont(size=18, weight="bold"),
        )
        self.lang_option_menu_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    def lang_option_menu_callback(self, choice):
        try:
            lang_code = next((key for key, value in self.all_lang_data.items() if value == choice), None)
            self.userdata_usecase.save_user_data(key="language_code", value=lang_code, user_data_path=USER_DATA_PATH)
            logging.info(f"Change language: {choice}")
            restart_app()
        except Exception as e:
            logging.error(f"Error lang_option_menu_callback: {e}")
            return
