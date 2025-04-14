import customtkinter
import logging
from PIL import Image

from app.config.settings import IMAGE_DIR
from app.utility.i18n import I18n

logger = logging.getLogger("launcherLogger")

class UsagePage(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.i18n = I18n()
        self.setup()

    def setup(self):
        # メインタイトル
        title_label = customtkinter.CTkLabel(
            self,
            text=self.i18n.get_text("usage_page.title"),
            font=customtkinter.CTkFont(size=28, weight="bold"),
        )
        title_label.grid(row=0, column=0, padx=30, pady=(30, 20), sticky="w")

        # 基本操作セクション
        self.create_section(
            row=1,
            title=self.i18n.get_text("usage_page.basic_operation.title"),
            content=[
                {
                    "title": self.i18n.get_text("usage_page.basic_operation.add_shortcut.title"),
                    "content": self.i18n.get_text("usage_page.basic_operation.add_shortcut.content")
                },
                {
                    "title": self.i18n.get_text("usage_page.basic_operation.create_workspace.title"),
                    "content": self.i18n.get_text("usage_page.basic_operation.create_workspace.content")
                },
                {
                    "title": self.i18n.get_text("usage_page.basic_operation.launch_shortcut.title"),
                    "content": self.i18n.get_text("usage_page.basic_operation.launch_shortcut.content")
                }
            ]
        )

        # 設定セクション
        self.create_section(
            row=2,
            title=self.i18n.get_text("usage_page.settings.title"),
            content=[
                {
                    "title": self.i18n.get_text("usage_page.settings.theme.title"),
                    "content": self.i18n.get_text("usage_page.settings.theme.content")
                },
                {
                    "title": self.i18n.get_text("usage_page.settings.scaling.title"),
                    "content": self.i18n.get_text("usage_page.settings.scaling.content")
                },
                {
                    "title": self.i18n.get_text("usage_page.settings.language.title"),
                    "content": self.i18n.get_text("usage_page.settings.language.content")
                }
            ]
        )

        # ショートカットキーセクション
        shortcut_keys = self.i18n.get_text("usage_page.shortcut_keys.content")
        if isinstance(shortcut_keys, list):
            self.create_section(
                row=3,
                title=self.i18n.get_text("usage_page.shortcut_keys.title"),
                content=[{"title": "", "content": shortcut_keys}]
            )

    def create_section(self, row: int, title: str, content: list[dict]):
        """セクションを作成するヘルパーメソッド"""
        # セクションフレーム
        section_frame = customtkinter.CTkFrame(
            self,
            fg_color="transparent"
        )
        section_frame.grid(row=row, column=0, padx=30, pady=(30, 0), sticky="nsew")
        section_frame.grid_columnconfigure(0, weight=1)

        # セクションタイトル
        title_label = customtkinter.CTkLabel(
            section_frame,
            text=title,
            font=customtkinter.CTkFont(size=22, weight="bold"),
            text_color=("gray20", "gray80")
        )
        title_label.grid(row=0, column=0, padx=0, pady=(0, 15), sticky="w")

        # セクション内容
        current_row = 1
        for item in content:
            if item["title"]:
                # サブセクションタイトル
                subtitle_label = customtkinter.CTkLabel(
                    section_frame,
                    text=item["title"],
                    font=customtkinter.CTkFont(size=16, weight="bold"),
                    text_color=("gray25", "gray75")
                )
                subtitle_label.grid(row=current_row, column=0, padx=20, pady=(10, 5), sticky="w")
                current_row += 1

            # コンテンツ
            for line in item["content"]:
                content_label = customtkinter.CTkLabel(
                    section_frame,
                    text=line,
                    font=customtkinter.CTkFont(size=14),
                    text_color=("gray30", "gray70"),
                    anchor="w",
                    justify="left",
                    wraplength=600
                )
                content_label.grid(row=current_row, column=0, padx=40, pady=2, sticky="w")
                current_row += 1
