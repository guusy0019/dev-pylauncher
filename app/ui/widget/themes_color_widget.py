
import os
import customtkinter

from app.config.settings import THEME_DIR
from app.utility.app_manager import restart_app


class ThemesColorWidget(customtkinter.CTkOptionMenu):
    def __init__(self, master, **kwargs):
        # ctk_default_themes_list=["blue", "green", "dark-blue"],
        themes_color_list = os.listdir(THEME_DIR)
        themes_color_list = [
            theme_color.replace(".json", "") for theme_color in themes_color_list
        ]
        super().__init__(
            master,
            values=themes_color_list,
            command=self.change_themes_color_event,
            **kwargs,
        )

    def change_themes_color_event(self, themes_color):
        try:
            customtkinter.set_default_color_theme(f"{THEME_DIR}/{themes_color}.json")
            restart_app()
            print(f"Themes color changed to {themes_color}")
        except Exception as e:
            print(f"Error: {e}")


# なぜうまくいかん？
# customtkinter.navigation_frameのインスタンスでは変更不可のため、最初にプルダウンからテーマを選ばせる
# その後、テーマの文字列を保存してインスタンスを再起動するのが必要ぽいね
# まあ、後回しかな、ただテーマだけは保存しておく
