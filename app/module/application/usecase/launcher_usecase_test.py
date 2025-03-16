import unittest
from app.module.application.usecase.launcher_usecase import LauncherUsecase


class TestLauncherUseCase(unittest.TestCase):

    def test_save_launch_path(self):
        launcher_usecase = LauncherUsecase()
        launcher_usecase.save_launch_path(
            key="test_key", launch_app_path="home\\doc\\test_path.lnk"
        )
        data = launcher_usecase.get_launch_path(key="test_key")
        self.assertEqual(data, "home\\doc\\test_path.lnk")

    def test_get_launch_path(self):
        launcher_usecase = LauncherUsecase()
        launcher_usecase.save_launch_path(
            key="test_key", launch_app_path="home\\doc\\test_path.lnk"
        )
        data = launcher_usecase.get_launch_path(key="test_key")
        self.assertEqual(data, "home\\doc\\test_path.lnk")

    def test_get_all_launch_path(self):
        launcher_usecase = LauncherUsecase()
        launcher_usecase.save_launch_path(
            key="test_key", launch_app_path="home\\doc\\test_path.lnk"
        )
        data = launcher_usecase.get_all_launch_path()
        self.assertEqual(data["test_key"], "home\\doc\\test_path.lnk")

    def test_delete_launch_path(self):
        launcher_usecase = LauncherUsecase()
        launcher_usecase.save_launch_path(
            key="test_key", launch_app_path="home\\doc\\test_path.lnk"
        )
        launcher_usecase.delete_launch_path(key="test_key")
        data = launcher_usecase.get_launch_path(key="test_key")
        self.assertEqual(data, "")
