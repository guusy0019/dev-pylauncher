import tkinter as tk
import customtkinter

from app.module.application.presenter.launcher_presenter import LauncherPresenter
from app.module.infrastructure.repository.launcher_repositpry import LauncherRepository

class SaveLauncherListWidget(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.launcher_repository = LauncherRepository()
        self.launcher_presenter = LauncherPresenter(self.launcher_repository)
        self.textbox_text = ""
        self.notification_label = customtkinter.CTkLabel(
            master=self,
            text=self.textbox_text,
            text_color="red",
        )

        self.setup()

    def setup(self):
        self.textbox = customtkinter.CTkEntry(
            master=self,
            placeholder_text="ワークスペースとして保存する名前を入力してください",
        )
        self.textbox.grid(row=0, column=0, padx=10, pady=20, sticky="ew")

        self.button = customtkinter.CTkButton(
            master=self,
            text="保存",
            command=self.save_launcher_list_as_workspace,
        )
        self.button.grid(row=0, column=1, padx=10, pady=20)

    def save_launcher_list_as_workspace(self):
        work_space_name = self.textbox.get()
        if work_space_name == "":
            self.textbox_text = "ワークスペース名は必須です。入力してください"
            self.notification_label.configure(text=self.textbox_text, text_color="red")
            self.notification_label.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
            return
        
        all_launcher_dict: dict[str, str] = self.launcher_presenter.get_all_launcher_data()
        val = self.launcher_presenter.save_launcher_workspace(
            file_name=work_space_name, 
            launcher_data=all_launcher_dict
        )

        if val["status"] == "success":
            self.textbox_text = val["message"]
            self.notification_label.configure(text=self.textbox_text, text_color="blue")
            self.notification_label.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
            self.textbox.delete(0, tk.END)
            # こうするしかないのか？
            self.master.master.master.master.workspace_frame.setup()

        else:
            self.textbox_text = val["message"]
            self.notification_label.configure(text=self.textbox_text, text_color="red")
            self.notification_label.grid(row=1, column=0, padx=10, pady=10, sticky="ew")




