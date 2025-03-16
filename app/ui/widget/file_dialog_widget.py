"""ファイルダイアログを作成する
ファイルのパスを取得してくれるウィジェット
ボタンを押すとファイル選択ダイアログが表示され、選択されたファイルのパスをテキストボックスに表示する
コマンドの有無によって、実行ボタンを表示するかどうかを切り替えることができる。またコマンド自体は呼び出し元で設定する
"""

import os
from tkinter import filedialog
import customtkinter

from app.config.color_settings import (
    FONTS,
    FG_COLOR,
)


class FileDialogWidget(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, fg_color=FG_COLOR)
        self.grid_columnconfigure(0, weight=1)

        self.kwargs = kwargs
        self.setup_form()

    def setup_form(self):

        self.textbox = customtkinter.CTkEntry(
            master=self,
            placeholder_text=self.kwargs.get("placeholder_text", "ファイルパスを入力"),
            width=120,
            font=FONTS,
        )
        self.textbox.grid(row=0, column=0, padx=10, pady=20, sticky="ew")

        self.button = customtkinter.CTkButton(
            master=self,
            text=self.kwargs.get("button_text", "ファイルを選択"),
            command=self.button_select_callback,
            font=FONTS,
        )
        self.button.grid(row=0, column=1, padx=10, pady=20)

        self.command_button = customtkinter.CTkButton(
            master=self,
            text=self.kwargs.get("command_button_text", "実行"),
            command=self.kwargs.get("custom_command", None),
            font=FONTS,
        )

        # カスタムコマンドが設定されている場合はボタンを表示
        if self.kwargs.get("custom_command") is not None:
            self.command_button.grid(
                row=0, column=2, columnspan=2, pady=20, sticky="ew"
            )

    def button_select_callback(self):
        """
        選択ボタンが押されたときのコールバック。ファイル選択ダイアログを表示する
        """
        file_name = self.file_read()

        if file_name is not None:
            # ファイルパスをテキストボックスに記入or削除
            self.textbox.delete(first_index=0, last_index="end")
            self.textbox.insert(0, file_name)

    def file_read(self):
        """
        ファイル選択ダイアログを表示する
        """
        current_dir = os.path.abspath(os.path.dirname(__file__))

        file_name = self.kwargs.get("file_name", "csvファイル")
        readable_file_types = self.kwargs.get(
            "readable_file_types", "*.csv;*.xlsx;*.xls"
        )
        initial_dir = self.kwargs.get("initial_dir", current_dir)

        file_path = filedialog.askopenfilename(
            filetypes=[(file_name, readable_file_types)], initialdir=initial_dir
        )

        if len(file_path) != 0:
            return file_path
        else:
            # ファイル選択がキャンセルされた場合
            return None

    def command_button_callback(self):
        """
        コマンドボタンが押されたときのコールバック
        """
        self.kwargs.get("custom_command")()
