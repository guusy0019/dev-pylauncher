import os
import customtkinter
from PIL import Image

from app.config.settings import IMAGE_DIR, ICON_PATH


class BaseCtkLayout(customtkinter.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title("pylauncher")
        self.geometry("1200x800")

        # iconの設定
        self.iconbitmap(ICON_PATH)

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
        

