from app.ui.page.launcher_page import LauncherPage
from app.module.application.usecase.launcher_usecase import LauncherUsecase


class WorkspaceLauncherPage(LauncherPage):
    def __init__(self, master, workspace_file_path: str):
        super().__init__(master, workspace_file_path)
