import pytest
from app.module.application.usecase.launcher_usecase import LauncherUsecase


class TestLauncherUseCase:
    """LauncherUsecaseのテストクラス（pytestスタイル）"""

    def test_save_launch_path(self):
        """launch_pathの保存機能をテスト"""
        launcher_usecase = LauncherUsecase()
        launcher_usecase.save_launch_path(
            key="test_key", launch_app_path="home\\doc\\test_path.lnk"
        )
        data = launcher_usecase.get_launch_path(key="test_key")
        assert data == "home\\doc\\test_path.lnk"

    def test_get_launch_path(self):
        """特定のkeyに対するlaunch_pathの取得機能をテスト"""
        launcher_usecase = LauncherUsecase()
        launcher_usecase.save_launch_path(
            key="test_key", launch_app_path="home\\doc\\test_path.lnk"
        )
        data = launcher_usecase.get_launch_path(key="test_key")
        assert data == "home\\doc\\test_path.lnk"

    def test_get_all_launch_path(self):
        """全てのlaunch_pathの取得機能をテスト"""
        launcher_usecase = LauncherUsecase()
        launcher_usecase.save_launch_path(
            key="test_key", launch_app_path="home\\doc\\test_path.lnk"
        )
        data = launcher_usecase.get_all_launch_path()
        assert data["test_key"] == "home\\doc\\test_path.lnk"

    def test_delete_launch_path(self):
        """launch_pathの削除機能をテスト"""
        launcher_usecase = LauncherUsecase()
        launcher_usecase.save_launch_path(
            key="test_key", launch_app_path="home\\doc\\test_path.lnk"
        )
        launcher_usecase.delete_launch_path(key="test_key")
        data = launcher_usecase.get_launch_path(key="test_key")
        assert data == ""