import pytest

from app.config.settings import USER_DATA_PATH
from app.module.application.usecase.userdata_usecase import UserDataUsecase
from app.module.infrastructure.repository.userdata_repository import UserDataRepository


@pytest.fixture
def userdata_repository():
    return UserDataRepository()

def test_save_user_data(userdata_repository):
    """ユーザーデータ保存機能のテスト"""
    userdata_usecase = UserDataUsecase(userdata_repository=userdata_repository)
    userdata_usecase.save_user_data(key="test_key", value="test_value", user_data_path=USER_DATA_PATH)
    data = userdata_usecase.get_all_user_data(user_data_path=USER_DATA_PATH)
    assert data["test_key"] == "test_value"


