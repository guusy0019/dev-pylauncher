import json
import os
import pytest

from app.config.settings import LAUNCHER_PATH, LAUNCHER_WORKSPACE_DIR
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

@pytest.fixture
def workspace_path():
    return LAUNCHER_WORKSPACE_DIR

def test_save_launch_path(launcher_repository, launcher_path, app_path):
    launcher_repository.save_launcher_data(
        key="test_key", launch_app_path=app_path, launcher_path=launcher_path
    )
    
    with open(launcher_path, "r") as f:
        data = json.load(f)
        assert data["test_key"] == "home\\doc\\test_path.lnk"

def test_get_all_launcher_data(launcher_repository, launcher_path, app_path):
    """ランチャーデータ取得機能のテスト"""
    launcher_repository.save_launcher_data(
        key="test_key", launch_app_path=app_path, launcher_path=launcher_path
    )
    
    data = launcher_repository.get_all_launcher_data(launcher_path=launcher_path)
    assert data["test_key"] == "home\\doc\\test_path.lnk"

def test_delete_launcher_data(launcher_repository, launcher_path, app_path):
    """ランチャーデータ削除機能のテスト"""
    launcher_repository.save_launcher_data(
        key="test_key", launch_app_path=app_path, launcher_path=launcher_path
    )
    
    launcher_repository.delete_launcher_data(key="test_key", launcher_path=launcher_path)
    
    data = launcher_repository.get_all_launcher_data(launcher_path=launcher_path)
    assert data == {}

def test_rename_workspace_file(launcher_repository, workspace_path):
    
    old_name = os.path.join(workspace_path, "test.json")
    new_name = os.path.join(workspace_path, "test_new.json")
    
    launcher_repository.rename_workspace_file(old_path=old_name, new_path=new_name)
    assert os.path.exists(new_name)

def test_delete_workspace_file(launcher_repository, workspace_path):
    file_path = os.path.join(workspace_path, "test_new.json")
    launcher_repository.delete_workspace_file(file_path=file_path)
    assert not os.path.exists(file_path)

