import os

MODE = os.getenv("LAUNCH_MODE", "DEBUG")

# プロジェクトのルートディレクトリ main.pyがあるディレクトリ
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
IMAGE_DIR = os.path.join(BASE_DIR, "app", "assets", "images")
THEME_DIR = os.path.join(BASE_DIR, "app", "assets", "themes")

ICON_PATH = os.path.join(BASE_DIR, "app", "assets", "icon.ico")
LOG_FILE_PATH = os.path.join(BASE_DIR, "app", "logs", "app.log")
