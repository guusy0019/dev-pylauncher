import json
import os

from app.config.user_settings import USER_DATA_PATH
from app.module.application.interface.launcher_interface import LauncherRepositoryInterface


class LauncherRepository(LauncherRepositoryInterface):
    # サービス層でもたすように
    save_path = os.path.join(USER_DATA_PATH, "launcher_app.json")

    def save_launcher_path(self, *, key: str, launch_app_path: str):
        launch_data = {}

        # 拡張子がショートカットかどうかを確認
        if not launch_app_path.endswith(".lnk"):
            raise ValueError("launcher_save_path's Extension must be .lnk")

        if os.path.exists(self.save_path):
            with open(self.save_path, "r") as f:
                try:
                    # 既存のデータを読み込む
                    launch_data = json.load(f)
                except json.JSONDecodeError:
                    # ファイルが壊れているか、空の場合は無視する
                    launch_data = {}

        launch_data[key] = launch_app_path

        with open(self.save_path, "w") as f:
            json.dump(launch_data, f, indent=4)

    def get_launcher_path(self, *, key: str) -> str:

        if os.path.exists(self.save_path):
            with open(self.save_path, "r") as f:
                try:
                    launch_data: dict[str, str] = json.load(f)
                    # print("launch_data_type", type(launch_data))
                    return launch_data.get(key, "")
                except json.JSONDecodeError:
                    return ""

    def get_all_launcher_path(self) -> dict[str, str]:
        if os.path.exists(self.save_path):
            with open(self.save_path, "r") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}
        return {}

    def delete_launcher_path(self, *, key: str) -> None:
        if os.path.exists(self.save_path):
            with open(self.save_path, "r") as f:
                try:
                    launch_data = json.load(f)
                    launch_data.pop(key, None)
                    with open(self.save_path, "w") as f:
                        json.dump(launch_data, f, indent=4)
                except json.JSONDecodeError:
                    pass
