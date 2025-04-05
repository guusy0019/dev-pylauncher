import os
import logging
import customtkinter

from app.utility.toplevel_window import ToplevelWindow
from app.config.settings import LAUNCHER_WORKSPACE_DIR
from app.module.application.usecase.launcher_usecase import LauncherUsecase

logger = logging.getLogger("launcherLogger")

class WorkspaceFrameWidget(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.textbox_text = ""
        self.toplevel_window = ToplevelWindow(master)
        self.setup()    

    def setup(self):
        self.workspace_frame = customtkinter.CTkFrame(self, corner_radius=0)
        launcher_workspace_file_names: list[str] = LauncherUsecase().get_all_workspace_file_names()
        for i, file_name in enumerate(launcher_workspace_file_names):
            button = customtkinter.CTkButton(
                self.workspace_frame, 
                text=file_name, 
                font=customtkinter.CTkFont(weight="bold"),
                command=lambda name=file_name: self.select_frame_by_name(name)
            )
            button.grid(row=i, column=0, padx=10, pady=10)
        self.workspace_frame.grid(row=0, column=0, sticky="nsew")


    def select_frame_by_name(self, name):
        file_name = f"{name}.json"
        workspace_file_path = os.path.join(LAUNCHER_WORKSPACE_DIR, file_name)
        if not os.path.exists(workspace_file_path):
        # if True:
            self.textbox_text = f"{name} のファイルが存在しません: {workspace_file_path}"
            self.toplevel_window.open_toplevel(
                textbox_text=self.textbox_text,
                title="エラーが発生しました。",
                text_color="red",
                wrap="word",
            )
            return
        
        self.master.master.select_launcher_workspace(workspace_file_path)
