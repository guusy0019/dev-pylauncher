import os
import customtkinter
from PIL import Image
from app.config.settings import IMAGE_DIR, USER_DATA_PATH
from app.config.color_settings import (
    TEXT_COLOR,
    HOVER_COLOR,
    FG_COLOR,
)
from app.config.settings import MODE
from app.utility.i18n import I18n
from app.ui.layout._base_ctk_layout import BaseCtkLayout
from app.ui.page.home_page import HomePage
from app.ui.page.launcher_page import LauncherPage
from app.ui.page.config_page import ConfigPage
from app.ui.layout.menu_layout import MenuLayout
from app.ui.widget.workspace_frame_widget import WorkspaceFrameWidget
from app.ui.widget.appearance_mode_widget import AppearanceModeWidget
from app.ui.widget.scaling_option_widget import ScalingOptionWidget
from app.ui.widget.themes_color_widget import ThemesColorWidget
from app.module.application.usecase.userdata_usecase import UserDataUsecase
from app.module.infrastructure.repository.userdata_repository import UserDataRepository

class AppLayout(BaseCtkLayout):
    def __init__(self):
        # テーマカラーを設定していた場合それを一番最初に読み込みアプリ全体に反映させる
        userdata_usecase = UserDataUsecase(userdata_repository=UserDataRepository())
        user_data = userdata_usecase.get_all_user_data(user_data_path=USER_DATA_PATH)
        
        theme_color = user_data.get("theme_color")
        if theme_color:
            ThemesColorWidget.set_color_theme(theme_color)

        appearance_mode = user_data.get("appearance_mode")
        if appearance_mode:
            AppearanceModeWidget.set_appearance_mode(appearance_mode)

        scaling_option = user_data.get("scaling_option")
        if scaling_option:
            ScalingOptionWidget.set_scaling(scaling_option)
        super().__init__()

        self.grid_columnconfigure(1, weight=1)
        self.i18n = I18n()  # 多言語対応のインスタンスを作成

        self.home_frame = HomePage(self)
        self.launcher_frame = LauncherPage(self)
        self.config_frame = ConfigPage(self)

        # メニューバーを配置
        self.menu_layout = MenuLayout(self)
        self.menu_layout.grid(row=0, column=0, sticky="ew")

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        # ワークスペースのフレームを配置
        self.workspace_frame = WorkspaceFrameWidget(self.navigation_frame)
        self.workspace_frame.grid(row=5, column=0, sticky="nsew")

        # テーマカラーのウィジェットの配置
        self.themes_color_menu = ThemesColorWidget(self.navigation_frame)
        # テーマカラーがすでに選択されていた場合はそれをoptionの初期値にする
        if theme_color:
            self.themes_color_menu.set(theme_color)
        self.themes_color_menu.grid(row=9, column=0, padx=20, pady=(10, 20))

        # 外観モードのウィジェットの配置
        self.appearance_mode_menu = AppearanceModeWidget(self.navigation_frame)
        if appearance_mode:
            self.appearance_mode_menu.set(appearance_mode)
        self.appearance_mode_menu.grid(row=7, column=0, padx=20, pady=(10, 20))

        # スケーリングのウィジェットの配置
        self.scaling_optionemenu = ScalingOptionWidget(self.navigation_frame)
        if scaling_option:
            self.scaling_optionemenu.set(scaling_option)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # 将来的にここでworkspaceを管理できればいいかなと
        self.frames = {
            "home": self.home_frame,
            "launcher": self.launcher_frame,
            "config": self.config_frame,
        }

        # configつけてみたが微妙なので、メニューバーでやる
        button_info_list = [
            {"name": "home", "text": self.i18n.get_text("side_menu.home"), "icon": self.home_icon},
            {"name": "launcher", "text": self.i18n.get_text("side_menu.launcher"), "icon": self.launcher_icon},
            # {"name": "config", "text": "設定", "icon": self.config_icon},
        ]
        self.button_info_list = []
        # 開発モードの場合のみhomeを表示
        for info in button_info_list:
            if info["name"] == "home" and MODE != "DEBUG":
                continue
            self.button_info_list.append(info)

        self.buttons = {}

        for i, info in enumerate(self.button_info_list, start=1):
            button = customtkinter.CTkButton(
                self.navigation_frame,
                corner_radius=0,
                height=40,
                border_spacing=10,
                text=info["text"],
                fg_color=FG_COLOR,
                text_color=TEXT_COLOR,
                hover_color=HOVER_COLOR,
                image=info["icon"],
                anchor="w",
                command=lambda name=info["name"]: self.select_frame_by_name(name),
            )
            button.grid(
                row=i if info["name"] != "config" else i + 3, 
                column=0, 
                sticky="ew"
                )
            self.buttons[info["name"]] = button

        self.select_frame_by_name("launcher")

    def select_frame_by_name(self, name):
        self.select_button(name)

        for frame_name, frame in self.frames.items():
            if frame_name == name:
                frame.grid(row=0, column=1, sticky="nsew")
            else:
                frame.grid_forget()

    def select_button(self, name):
        for button_name, button in self.buttons.items():
            # 選択したボタン以外は透明に
            button.configure(
                fg_color=FG_COLOR if button_name == name else "transparent"
            )