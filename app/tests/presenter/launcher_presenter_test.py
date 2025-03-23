import logging
import pytest
from app.config.settings import LAUNCHER_PATH
from app.module.application.presenter.launcher_presenter import LauncherPresenter
from app.module.infrastructure.repository.launcher_repositpry import LauncherRepository

logger = logging.getLogger("launcherLogger")

@pytest.fixture
def launcher_repository():
    return LauncherRepository()

def test_get_all_launcher_data(launcher_repository):
    presenter = LauncherPresenter(launcher_repository=launcher_repository)
    data = presenter.get_all_launcher_data()
    assert data == {}

def test_save_launcher_data(launcher_repository):
    presenter = LauncherPresenter(launcher_repository=launcher_repository)
    presenter.save_launcher_data(key="test_key", launch_app_path="test_path")
    data = presenter.get_all_launcher_data()
    assert data["test_key"] == "test_path"

def test_delete_launcher_data(launcher_repository):
    presenter = LauncherPresenter(launcher_repository=launcher_repository)
    presenter.save_launcher_data(key="test_key", launch_app_path="test_path")
    presenter.delete_launcher_data(key="test_key")
    data = presenter.get_all_launcher_data()
    assert data == {}
