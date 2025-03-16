import unittest
import json

from app.module.repository.launcher_repositpry import LauncherRepository


class TestLauncherRepository(unittest.TestCase):

    def test_save_launch_path(self):
        launcher_repository = LauncherRepository()
        launcher_repository.save_launch_path(
            key="test_key", launch_app_path="home\\doc\\test_path.lnk"
        )
        with open(launcher_repository.save_path, "r") as f:
            data = json.load(f)
            self.assertEqual(data["test_key"], "home\\doc\\test_path.lnk")

    def test_get_launch_path(self):
        launcher_repository = LauncherRepository()
        launcher_repository.get_launch_path(key="test_key")
        data = launcher_repository.get_launch_path(key="test_key")
        self.assertEqual(data, "home\\doc\\test_path.lnk")

    def test_get_all_launch_path(self):
        launcher_repository = LauncherRepository()
        launcher_repository.save_launch_path(
            key="test_key", launch_app_path="home\\doc\\test_path.lnk"
        )
        data = launcher_repository.get_all_launch_path()
        self.assertEqual(data["test_key"], "home\\doc\\test_path.lnk")

    def test_delete_launch_path(self):
        launcher_repository = LauncherRepository()
        launcher_repository.save_launch_path(
            key="test_key", launch_app_path="home\\doc\\test_path.lnk"
        )
        launcher_repository.delete_launch_path(key="test_key")
        data = launcher_repository.get_launch_path(key="test_key")
        self.assertEqual(data, "")
