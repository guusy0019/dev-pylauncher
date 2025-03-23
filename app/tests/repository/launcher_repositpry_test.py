import json
import pytest

from app.config.settings import LAUNCHER_PATH
from app.module.infrastructure.repository.launcher_repositpry import LauncherRepository

@pytest.fixture
def launcher_repository():
    return LauncherRepository()

@pytest.fixture
def app_path():
    return "home\\doc\\test_path.lnk"

@pytest.fixture
def launcher_path():
    return LAUNCHER_PATH

def test_save_launch_path(launcher_repository, launcher_path, app_path):
    launcher_repository.save_launcher_data(
        key="test_key", launcher_app_path=app_path, launcher_path=launcher_path
    )
    
    with open(launcher_path, "r") as f:
        data = json.load(f)
        assert data["test_key"] == "home\\doc\\test_path.lnk"

def test_get_all_launcher_data(launcher_repository, launcher_path, app_path):
    """ランチャーデータ取得機能のテスト"""
    launcher_repository.save_launcher_data(
        key="test_key", launcher_app_path=app_path, launcher_path=launcher_path
    )
    
    data = launcher_repository.get_all_launcher_data(launcher_path=launcher_path)
    assert data["test_key"] == "home\\doc\\test_path.lnk"

def test_delete_launcher_data(launcher_repository, launcher_path, app_path):
    """ランチャーデータ削除機能のテスト"""
    launcher_repository.save_launcher_data(
        key="test_key", launcher_app_path=app_path, launcher_path=launcher_path
    )
    
    launcher_repository.delete_launcher_data(key="test_key", launcher_path=launcher_path)
    
    data = launcher_repository.get_all_launcher_data(launcher_path=launcher_path)
    assert data == {}