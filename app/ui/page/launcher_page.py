import os
import tkinter as tk
import customtkinter
import logging
from PIL import Image

from app.config.settings import IMAGE_DIR

from app.ui.widget.file_dialog_widget import FileDialogWidget
from app.ui.widget.save_launcher_list_widget import SaveLauncherListWidget
from app.module.application.usecase.launcher_usecase import LauncherUsecase
from app.module.utility.shortcut_excuter import ShortcutExecutor
from app.module.utility.get_shortcut_icon_utility import IconExtractor
from app.module.application.presenter.launcher_presenter import LauncherPresenter
from app.module.infrastructure.repository.launcher_repositpry import LauncherRepository

logger = logging.getLogger("launcherLogger")

class LauncherPage(customtkinter.CTkScrollableFrame):
    def __init__(self, master, workspace_file_path: str | None = None):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.launcher_repository = LauncherRepository()
        self.launcher_presenter = LauncherPresenter(self.launcher_repository)

        self.workspace_file_path = workspace_file_path
        self.setup()

    def setup(self):
        # ランチャーでファイルダイアログを表示する場合の初期ディレクトリを設定
        if os.name == "nt":
            candidate_dir = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
            if not os.path.exists(candidate_dir):
                candidate_dir = os.path.expanduser("~/Desktop")
            initial_dir = candidate_dir
        else:
            logger.error(f"Unsupported OS: {os.name}")
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
        
        # ワークスペースの場合は、ワークスペースのファイル名を表示
        if self.workspace_file_path is not None:
            app_name = LauncherUsecase.get_app_name_from_shortcut_path(self.workspace_file_path)
            self.workspace_label = customtkinter.CTkLabel(
                self,
                text=f"ワークスペース名: {app_name}",
                font=customtkinter.CTkFont(size=18, weight="bold"),
            )
            self.workspace_label.grid(row=1, column=0, padx=20, sticky="ew")

        # self.utility_frame = customtkinter.CTkFrame(
        #     self, corner_radius=0, fg_color="transparent"
        # )
        # self.utility_frame.grid(
        #     row=1, column=0, columnspan=4, padx=10, pady=10, sticky="ew"
        # )

        # ランチャーapp表示用のフレーム
        self.launcher_list = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.launcher_list.grid(
            row=2, column=0, columnspan=4, padx=10, pady=20, sticky="ew"
        )

        # checkboxを使用して、アプリケーションの一括操作を実装したいが、ムズイのでいったん保留
        # self.add_utility_buttons()

        if self.workspace_file_path is None:
        # work space保存用のフレーム
            self.save_launcher_list_as_workspace = SaveLauncherListWidget(master=self)
            self.save_launcher_list_as_workspace.grid(
                row=3, column=0, columnspan=4, padx=10, pady=20, sticky="ew"
            )

        self.update_launcher_list()

    def update_launcher_list(self):
        """ランチャーリストを更新"""
        # 既存のウィジェットをクリア
        for widget in self.launcher_list.winfo_children():
            widget.destroy()

        all_launcher_dict: dict[str, str] = self.launcher_presenter.get_all_launcher_data(self.workspace_file_path)

        icon_extractor = IconExtractor()
        shortcut_executor = ShortcutExecutor()

        for i, (shortcut_name, shortcut_path) in enumerate(all_launcher_dict.items()):
            # 行と列を計算
            row = i // 2  # 2つのセットで1行
            col = (i % 2) * 2  # 1セットごとに2列を占有

            # ショートカットのアイコンを取得
            pillow_image = icon_extractor.get_pillow_image(shortcut_path)

            if pillow_image is None:
                ctk_image = customtkinter.CTkImage(
                    light_image=Image.open(os.path.join(IMAGE_DIR, "common", "not_image_light.png")),
                    dark_image=Image.open(os.path.join(IMAGE_DIR, "common", "not_image_dark.png")),
                    size=(32, 32),
                )
            else:
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
                command=lambda p=shortcut_path: shortcut_executor.exec_shortcut_by_shortcut_path(
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

        if os.path.exists(file_path):
            self.launcher_presenter.save_launcher_data(key=app_name, launch_app_path=file_path, launcher_path=self.workspace_file_path)
            # textをクリア
            self.file_dialog.textbox.delete(0, tk.END)
            self.update_launcher_list()
        else:
            raise FileNotFoundError(f"{file_path} not found")

    def delete_launcher(self, key: str):
        """指定したランチャーを削除してリストを更新"""
        self.launcher_presenter.delete_launcher_data(key=key, launcher_path=self.workspace_file_path)
        self.update_launcher_list()
