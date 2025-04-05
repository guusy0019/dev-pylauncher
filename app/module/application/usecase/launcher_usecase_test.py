import pytest
from app.module.application.usecase.launcher_usecase import LauncherUsecase
from app.module.infrastructure.repository.launcher_repositpry import LauncherRepository
from app.config.settings import LAUNCHER_PATH


@pytest.fixture
def launcher_repository():
    return LauncherRepository()

def test_get_all_launcher_data(launcher_repository):
    usecase = LauncherUsecase(launcher_repository=launcher_repository)
    data = usecase.get_all_launcher_data(launcher_path=LAUNCHER_PATH)
    assert data == {}

def test_save_launcher_data(launcher_repository):
    usecase = LauncherUsecase(launcher_repository=launcher_repository)
    usecase.save_launcher_data(launcher_path=LAUNCHER_PATH, key="test_key", launcher_app_path="test_path")
    data = usecase.get_all_launcher_data(launcher_path=LAUNCHER_PATH)
    assert data["test_key"] == "test_path"

def test_delete_launcher_data(launcher_repository):
    usecase = LauncherUsecase(launcher_repository=launcher_repository)
    usecase.save_launcher_data(launcher_path=LAUNCHER_PATH, key="test_key", launcher_app_path="test_path")
    usecase.delete_launcher_data(launcher_path=LAUNCHER_PATH, key="test_key")
    data = usecase.get_all_launcher_data(launcher_path=LAUNCHER_PATH)
    assert data == {}

def test_get_all_workspace_file_names(launcher_repository):
    usecase = LauncherUsecase(launcher_repository=launcher_repository)
    file_names = usecase.get_all_workspace_file_names()
    assert file_names != []

def test_get_app_name_from_shortcut_path(launcher_repository):
    usecase = LauncherUsecase(launcher_repository=launcher_repository)
    app_name = usecase.get_app_name_from_shortcut_path(
        shortcut_path="C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Outlook (classic).lnk"
        )
    assert app_name == "Outlook (classic)"

