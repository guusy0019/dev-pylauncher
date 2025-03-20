import os
import logging
import logging.config
import yaml

MODE = os.getenv("LAUNCH_MODE", "DEBUG")

# プロジェクトのルートディレクトリ main.pyがあるディレクトリ
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
IMAGE_DIR = os.path.join(BASE_DIR, "app", "assets", "images")
THEME_DIR = os.path.join(BASE_DIR, "app", "assets", "themes")
LOCALE_DIR = os.path.join(BASE_DIR, "app", "locales")
LOG_CONFIG_DIR = os.path.join(BASE_DIR, "app", "config")
ICON_PATH = os.path.join(BASE_DIR, "app", "assets", "icon.ico")
LOG_FILE_PATH = os.path.join(BASE_DIR, "app", "logs", "app.log")
LOG_OUTPUT_PATH = os.path.join(BASE_DIR, "app", "logs")

LAUNCHER_PATH = os.path.join(BASE_DIR, "app", "data", "launcher.json")# ランチャーのデータを保存するパス
USER_DATA_PATH = os.path.join(BASE_DIR, "app", "data", "user_data.json")# ユーザーが設定したデータ（テーマや、言語等の情報を格納する）


if MODE == "DEBUG":
    LOG_CONFIG_PATH = os.path.join(LOG_CONFIG_DIR, "logger.dev.yaml")
else:
    LOG_CONFIG_PATH = os.path.join(LOG_CONFIG_DIR, "logger.prod.yaml")
