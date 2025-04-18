import json
import logging
import os
logger = logging.getLogger("launcherLogger")

class FileUtility:

    def read_json_data(self, path : str) -> dict:
        """pathを読み込む、読み込めなければ空のdictを返す"""
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"FileNotFoundError read_json_data: {path}")
            return {}
        except json.JSONDecodeError:
            logger.error(f"JSONDecodeError read_json_data: {path}")
            return {}
        except Exception as e:
            logger.error(f"Exception read_json_data: error:{e} path:{path}")
            return {}
        

    def rename_file(self, old_name, new_name):
        try:
            os.rename(old_name, new_name)
            logger.info(f"'{old_name}' to '{new_name}'.")
        except FileNotFoundError:
            logger.error(f"file '{old_name}' not found.")
        except PermissionError:
            logger.error("permission error, can't rename file.")    
        except FileExistsError:
            logger.error(f"file '{new_name}' already exists.")
        except Exception as e:
            logger.error(f"error: {e}")


    def delete_file(self, file_path: str) -> None:
        try:
            os.remove(file_path)
            logger.info(f"file '{file_path}' deleted.")
        except FileNotFoundError:
            logger.error(f"file '{file_path}' not found.")
        except PermissionError:
            logger.error("permission error, can't delete file.")
        except Exception as e:
            logger.error(f"error: {e}")
