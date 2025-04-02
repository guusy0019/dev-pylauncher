
import logging
import customtkinter
from app.module.application.usecase.launcher_usecase import LauncherUsecase

logger = logging.getLogger("launcherLogger")

class WorkspaceFrameWidget(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

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
        pass
