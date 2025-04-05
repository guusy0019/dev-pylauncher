import pytest

from app.config.settings import USER_DATA_PATH
from app.module.application.usecase.userdata_usecase import UserDataUsecase
from app.module.infrastructure.repository.userdata_repository import UserDataRepository
from app.module.application.usecase.launcher_usecase import LauncherUsecase


@pytest.fixture
def userdata_repository():
    return UserDataRepository()

@pytest.fixture
def launcher_usecase():
    return LauncherUsecase()

def test_save_user_data(userdata_repository):
    """ユーザーデータ保存機能のテスト"""
    userdata_usecase = UserDataUsecase(userdata_repository=userdata_repository)
    userdata_usecase.save_user_data(key="test_key", value="test_value", user_data_path=USER_DATA_PATH)
    data = userdata_usecase.get_all_user_data(user_data_path=USER_DATA_PATH)
    assert data["test_key"] == "test_value"

def test_get_all_workspace_file_names():
    """ワークスペースファイル名取得機能のテスト"""
    launcher_usecase = LauncherUsecase()
    workspace_file_names = launcher_usecase.get_all_workspace_file_names()
    assert len(workspace_file_names) > 0

def test_get_workspace_file_paths():
    """ワークスペースファイルパス取得機能のテスト"""
    launcher_usecase = LauncherUsecase()
    workspace_file_paths = launcher_usecase.get_workspace_file_paths()
    assert len(workspace_file_paths) > 0

