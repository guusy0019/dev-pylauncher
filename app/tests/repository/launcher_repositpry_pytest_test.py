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

# テスト関数
def test_save_launch_path(launcher_repository, launcher_path, app_path):
    launcher_repository.save_launcher_data(
        key="test_key", launcher_app_path=app_path, launcher_path=launcher_path
    )
    
    # ファイルからデータを読み込んで検証
    with open(launcher_path, "r") as f:
        data = json.load(f)
        assert data["test_key"] == "home\\doc\\test_path.lnk"

def test_get_all_launcher_data(launcher_repository, launcher_path, app_path):
    """ランチャーデータ取得機能のテスト"""
    # 最初のパラメータが間違っていたので修正 (元のコードではkeyパラメータを渡していたが、
    # メソッド定義ではlauncher_pathのみ受け取る)
    launcher_repository.save_launcher_data(
        key="test_key", launcher_app_path=app_path, launcher_path=launcher_path
    )
    
    # パラメータを渡して呼び出す
    data = launcher_repository.get_all_launcher_data(launcher_path=launcher_path)
    assert data["test_key"] == "home\\doc\\test_path.lnk"

def test_delete_launcher_data(launcher_repository, launcher_path, app_path):
    """ランチャーデータ削除機能のテスト"""
    # 初期データを作成
    launcher_repository.save_launcher_data(
        key="test_key", launcher_app_path=app_path, launcher_path=launcher_path
    )
    
    # データを削除
    launcher_repository.delete_launcher_data(key="test_key", launcher_path=launcher_path)
    
    # 削除の検証
    data = launcher_repository.get_all_launcher_data(launcher_path=launcher_path)
    assert data == {}