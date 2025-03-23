import json
import logging

logger = logging.getLogger("launcherLogger")

class FileUtility:

    def read_json_data(self, launcher_path : str) -> dict:
        """pathを読み込む、読み込めなければ空のdictを返す"""
        try:
            with open(launcher_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"FileNotFoundError read_launcher_data: {launcher_path}")
            return {}
        except json.JSONDecodeError:
            logger.error(f"JSONDecodeError read_launcher_data: {launcher_path}")
            return {}
        except Exception as e:
            logger.error(f"Exception read_launcher_data: error:{e} launcher_path:{launcher_path}")
            return {}