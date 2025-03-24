import os
import customtkinter
from PIL import Image

from app.config.settings import IMAGE_DIR, ICON_PATH, USER_DATA_PATH
from app.ui.layout.menu_layout import MenuLayout
from app.ui.widget.appearance_mode_widget import AppearanceModeWidget
from app.ui.widget.scaling_option_widget import ScalingOptionWidget
from app.ui.widget.themes_color_widget import ThemesColorWidget
from app.module.application.usecase.userdata_usecase import UserDataUsecase
from app.module.infrastructure.repository.userdata_repository import UserDataRepository


class BaseCtkLayout(customtkinter.CTk):
    def __init__(self, **kwargs):
        
        # テーマカラーを設定していた場合それを一番最初に読み込みアプリ全体に反映させる
        userdata_usecase = UserDataUsecase(userdata_repository=UserDataRepository())
        theme_color = userdata_usecase.get_all_user_data(user_data_path=USER_DATA_PATH).get("theme_color")
        if theme_color:
            ThemesColorWidget.set_color_theme(theme_color)

        super().__init__(**kwargs)

        self.title("pylauncher")
        self.geometry("1200x800")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # iconの設定
        self.iconbitmap(ICON_PATH)

        # メニューバーを配置
        self.menu_layout = MenuLayout(self)
        self.menu_layout.grid(row=0, column=0, sticky="ew")

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        # テーマカラーのウィジェットの配置
        self.themes_color_menu = ThemesColorWidget(self.navigation_frame)
        # テーマカラーがすでに選択されていた場合はそれをoptionの初期値にする
        if theme_color:
            self.themes_color_menu.set(theme_color)
        self.themes_color_menu.grid(row=9, column=0, padx=20, pady=(10, 20))

        # 外観モードのウィジェットの配置
        self.appearance_mode_menu = AppearanceModeWidget(self.navigation_frame)
        appearance_mode = userdata_usecase.get_all_user_data(user_data_path=USER_DATA_PATH).get("appearance_mode")
        if appearance_mode:
            self.appearance_mode_menu.set(appearance_mode)
            AppearanceModeWidget.set_appearance_mode(appearance_mode)
        self.appearance_mode_menu.grid(row=7, column=0, padx=20, pady=(10, 20))

        # スケーリングのウィジェットの配置
        self.scaling_optionemenu = ScalingOptionWidget(self.navigation_frame)
        scaling_option = userdata_usecase.get_all_user_data(user_data_path=USER_DATA_PATH).get("scaling_option")
        if scaling_option:
            self.scaling_optionemenu.set(scaling_option)
            ScalingOptionWidget.set_scaling(scaling_option)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # 各ページのアイコン画像を取得
        self.home_icon = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(IMAGE_DIR, "home_dark.png")),
            dark_image=Image.open(os.path.join(IMAGE_DIR, "home_light.png")),
            size=(20, 20),
        )
        self.launcher_icon = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(IMAGE_DIR, "launcher", "launch_light.png")),
            dark_image=Image.open(os.path.join(IMAGE_DIR, "launcher", "launch_dark.png")),
            size=(20, 20),
        )

        self.config_icon = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(IMAGE_DIR, "config", "config_light.png")),
            dark_image=Image.open(os.path.join(IMAGE_DIR, "config", "config_dark.png")),
            size=(20, 20),
        )
        

