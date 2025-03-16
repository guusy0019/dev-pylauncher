import os
import customtkinter
from PIL import Image
from app.config.settings import IMAGE_DIR
from app.config.color_settings import (
    TEXT_COLOR,
    HOVER_COLOR,
    FG_COLOR,
)
from app.ui.layout._base_ctk_layout import BaseCtkLayout
from app.ui.page.home_page import HomePage
from app.ui.page.launcher_page import LauncherPage
from app.ui.page.config_page import ConfigPage
from app.config.settings import MODE

class AppLayout(BaseCtkLayout):
    def __init__(self):
        super().__init__()

        self.large_test_image = customtkinter.CTkImage(
            Image.open(os.path.join(IMAGE_DIR, "large_test_image.png")),
            size=(500, 150),
        )
        self.image_icon_image = customtkinter.CTkImage(
            Image.open(os.path.join(IMAGE_DIR, "image_icon_light.png")),
            size=(20, 20)
        )

        self.home_frame = HomePage(self, self.large_test_image, self.image_icon_image)
        self.launcher_frame = LauncherPage(self)

        self.config_frame = ConfigPage(self)

        # 将来的にここでworkspaceを管理できればいいかなと
        self.frames = {
            "home": self.home_frame,
            "launcher": self.launcher_frame,
            "config": self.config_frame,
        }

        # configつけてみたが微妙なので、メニューバーでやる
        button_info_list = [
            {"name": "home", "text": "ホーム", "icon": self.home_icon},
            {"name": "launcher", "text": "ランチャー", "icon": self.launcher_icon},
            # {"name": "config", "text": "設定", "icon": self.config_icon},
        ]
        self.button_info_list = []
        # 揮発中はhomeにcustomtkinterのサンプルコード置いておく
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