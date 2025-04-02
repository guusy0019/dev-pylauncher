import os

from app.ui.page.launcher_page import LauncherPage
from app.config.settings import LAUNCHER_WORKSPACE_DIR
from app.module.application.usecase.launcher_usecase import LauncherUsecase


class WorkspaceLauncherPage(LauncherPage):
    def __init__(self, master):
        launcher_usecase = LauncherUsecase()
        workspace_file_names = launcher_usecase.get_all_workspace_file_names()

        self.workspace_file_paths = [ 
            os.path.join(LAUNCHER_WORKSPACE_DIR, file_name) for file_name in workspace_file_names
            ]

        super().__init__(master)
        self.setup()
        
    def setup(self):
        super().setup(self.workspace_file_paths)
