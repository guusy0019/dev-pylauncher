
import os
import logging
import customtkinter

from app.config.settings import THEME_DIR, USER_DATA_PATH
from app.utility.app_manager import restart_app
from app.module.application.usecase.userdata_usecase import UserDataUsecase
from app.module.application.interface.userdata_interface import UserDataRepositoryInterface
from app.module.infrastructure.repository.userdata_repository import UserDataRepository

logger = logging.getLogger("launcherLogger")


class ThemesColorWidget(customtkinter.CTkOptionMenu):
    ctk_default_themes_list = ["blue", "green", "dark-blue"]
    
    def __init__(self, master, **kwargs):

        ex_themes_color_list = os.listdir(THEME_DIR)
        ex_themes_color_list = [
            theme_color.replace(".json", "") for theme_color in ex_themes_color_list
        ]
        default_themes_color_list = self.ctk_default_themes_list
        themes_color_list = default_themes_color_list + ex_themes_color_list
        super().__init__(
            master,
            values=themes_color_list,
            command=self.change_themes_color_event,
            **kwargs,
        )

    def change_themes_color_event(self, theme_color):
        try:
            self.set_color_theme(theme_color)
            # themes_colorをユーザーデータに保存
            user_data_usecase = UserDataUsecase(userdata_repository=UserDataRepository())
            user_data_usecase.save_user_data(key="theme_color", value=theme_color, user_data_path=USER_DATA_PATH)
            restart_app()
        except Exception as e:
            logger.error(f"Error change_themes_color_event: {e}")
            return
        
    @classmethod
    def set_color_theme(cls, theme_color):
        if theme_color in cls.ctk_default_themes_list:
            customtkinter.set_default_color_theme(theme_color)
            logger.info(f"Change themes color: {theme_color}")
        else:
            customtkinter.set_default_color_theme(f"{THEME_DIR}/{theme_color}.json")
            logger.info(f"Change themes color: {theme_color}")
