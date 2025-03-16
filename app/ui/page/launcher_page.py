import os
import tkinter as tk
from PIL import Image
import customtkinter

from app.config.settings import IMAGE_DIR, IMAGE_DIR

from app.ui.widget.file_dialog_widget import FileDialogWidget
from app.module.utility.exec_shortcut_utility import ShortcutExecutor
from app.module.utility.get_shortcut_icon_utility import IconExtractor
from app.module.application.usecase.launcher_usecase import LauncherUsecase
from app.module.infrastructure.repository.launcher_repositpry import LauncherRepository


class LauncherPage(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.launcher_repository = LauncherRepository()
        self.setup()

    def setup(self):
        if os.name == "nt":
            init_dir = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
            if os.path.exists(init_dir):
                initial_dir = init_dir
            else:
                initial_dir = os.path.expanduser("~/Desktop")
        elif os.name == "posix":
            initial_dir = os.path.expanduser("~/Applications")
        else:
            raise ValueError(f"Unsupported OS: {os.name}")

        kwargs = {
            "placeholder_text": "ランチャーに保存するショートカットを選択してください",
            "button_text": "ショートカットを選択",
            "custom_command": self.button_select_callback,
            "command_button_text": "ショートカットを保存",
            "file_name": "ショートカット",
            "readable_file_types": "*.lnk",
            "initial_dir": initial_dir,
        }

        self.file_dialog = FileDialogWidget(master=self, **kwargs)
        self.file_dialog.grid(
            row=0, column=0, columnspan=4, padx=10, pady=20, sticky="ew"
        )

        self.utility_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.utility_frame.grid(
            row=1, column=0, columnspan=4, padx=10, pady=10, sticky="ew"
        )

        self.launcher_list = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.launcher_list.grid(
            row=2, column=0, columnspan=4, padx=10, pady=20, sticky="ew"
        )
        # checkboxを使用して、アプリケーションの一括操作を実装したいが、ムズイのでいったん保留
        self.add_utility_buttons()

        self.update_launcher_list()

    def update_launcher_list(self):
        """ランチャーリストを更新"""
        # 既存のウィジェットをクリア
        for widget in self.launcher_list.winfo_children():
            widget.destroy()

        launcher_usecase = LauncherUsecase(self.launcher_repository)
        all_launcher_dict: dict[str, str] = launcher_usecase.get_all_launcher_path()

        icon_extractor = IconExtractor()
        shortcut_executor = ShortcutExecutor()

        for i, (shortcut_name, shortcut_path) in enumerate(all_launcher_dict.items()):
            # 行と列を計算
            row = i // 2  # 2つのセットで1行
            col = (i % 2) * 2  # 1セットごとに2列を占有

            # ショートカットのアイコンを取得
            pillow_image = icon_extractor.get_pillow_image(shortcut_path)
            ctk_image = customtkinter.CTkImage(
                light_image=pillow_image, dark_image=pillow_image, size=(32, 32)
            )
            delete_image = customtkinter.CTkImage(
                light_image=Image.open(os.path.join(IMAGE_DIR, "launcher", "delete_light.png")),
                dark_image=Image.open(os.path.join(IMAGE_DIR, "launcher", "delete_dark.png")),
                size=(32, 32),
            )

            # ショートカットの実行ボタン
            launch_button = customtkinter.CTkButton(
                self.launcher_list,
                text=shortcut_name,
                image=ctk_image,
                compound="left",
                width=250,
                command=lambda p=shortcut_path: shortcut_executor.execute_shortcut(
                    shortcut_path=p
                ),
                anchor="center",
            )
            launch_button.grid(row=row, column=col, padx=20, pady=10, sticky="ew")

            # ショートカットの削除ボタン
            delete_button = customtkinter.CTkButton(
                self.launcher_list,
                text="削除",
                image=delete_image,
                compound="left",
                command=lambda k=shortcut_name: self.delete_launcher(k),
                anchor="center",
            )
            delete_button.grid(row=row, column=col + 1, padx=5, pady=10)

    def add_utility_buttons(self):
        """ランチャーリストの上部にスタート、停止、一括削除ボタンを追加"""
        start_button_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(IMAGE_DIR, "launcher", "start_light.png")),
            dark_image=Image.open(os.path.join(IMAGE_DIR, "launcher", "start_dark.png")),
            size=(32, 32),
        )
        start_button = customtkinter.CTkButton(
            self.utility_frame, image=start_button_image, text="Start"
        )
        start_button.grid(row=0, column=0, padx=5, pady=5)

        stop_button_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(IMAGE_DIR, "launcher", "stop_light.png")),
            dark_image=Image.open(os.path.join(IMAGE_DIR, "launcher", "stop_dark.png")),
            size=(32, 32),
        )
        stop_button = customtkinter.CTkButton(
            self.utility_frame, image=stop_button_image, text="Stop"
        )
        stop_button.grid(row=0, column=1, padx=5, pady=5)

        delete_sweep_button_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(IMAGE_DIR, "launcher", "delete_sweep_light.png")),
            dark_image=Image.open(os.path.join(IMAGE_DIR, "launcher", "delete_sweep_dark.png")),
            size=(32, 32),
        )
        delete_sweep_button = customtkinter.CTkButton(
            self.utility_frame, image=delete_sweep_button_image, text="Delete All"
        )
        delete_sweep_button.grid(row=0, column=2, padx=5, pady=5)

    def button_select_callback(self):
        file_path = self.file_dialog.textbox.get()
        # ファイルパスからファイル名を取得
        app_name = os.path.splitext(os.path.basename(file_path))[0]

        launcher_usecase = LauncherUsecase(self.launcher_repository)

        if os.path.exists(file_path):
            launcher_usecase.save_launcher_path(key=app_name, launch_app_path=file_path)
            # textをクリア
            self.file_dialog.textbox.delete(0, tk.END)
            self.update_launcher_list()
        else:
            raise FileNotFoundError(f"{file_path} not found")

    def delete_launcher(self, key: str):
        """指定したランチャーを削除してリストを更新"""
        launcher_usecase = LauncherUsecase(self.launcher_repository)
        launcher_usecase.delete_launcher_path(key=key)
        self.update_launcher_list()
