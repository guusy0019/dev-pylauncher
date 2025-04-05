import json
import pytest

from app.config.settings import USER_DATA_PATH
from app.module.infrastructure.repository.userdata_repository import UserDataRepository
from app.module.utility.file_utility import FileUtility

@pytest.fixture
def user_data_repository():
    return UserDataRepository()

@pytest.fixture
def user_data_path():
    return USER_DATA_PATH

def test_save_user_data(user_data_repository, user_data_path):
    """ユーザーデータ保存機能のテスト"""
    user_data_repository.save_user_data(key="test_key", value="test_value", user_data_path=user_data_path)
    
    with open(user_data_path, "r") as f:
        data = json.load(f)
        assert data["test_key"] == "test_value"

def test_get_all_user_data(user_data_repository, user_data_path):
    """ユーザーデータ取得機能のテスト"""
    user_data_repository.save_user_data(key="test_key", value="test_value", user_data_path=user_data_path)
    
    data = user_data_repository.get_all_user_data(user_data_path=user_data_path)
    assert data["test_key"] == "test_value"