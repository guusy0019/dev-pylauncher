import os
import sys
import json
import logging
import logging.config
import yaml

MODE = os.getenv("LAUNCH_MODE", "PROD")  # デフォルトを本番環境に設定

# アプリ名定義（settings.py内で使用するため）
APP_NAME = "pylauncher"  # ここでAPP_NAMEを定義

# 実行ファイルのパスを取得（cx_Freezeでビルドされた場合を考慮）
if getattr(sys, 'frozen', False):
    # 実行ファイルが存在するディレクトリ
    BASE_DIR = os.path.dirname(sys.executable)
    # リソースディレクトリはlib内
    RESOURCE_DIR = os.path.join(BASE_DIR, "lib", "app")
else:
    # 開発環境
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    RESOURCE_DIR = os.path.join(BASE_DIR, "app")

# リソースパスを設定
IMAGE_DIR = os.path.join(RESOURCE_DIR, "assets", "images")
THEME_DIR = os.path.join(RESOURCE_DIR, "assets", "themes")
LOCALE_DIR = os.path.join(RESOURCE_DIR, "locales")
LOG_CONFIG_DIR = os.path.join(RESOURCE_DIR, "config")
ICON_PATH = os.path.join(RESOURCE_DIR, "assets", "icon.ico")

# データディレクトリをアプリケーションデータフォルダに変更
if getattr(sys, 'frozen', False):
    # 実行環境でのデータディレクトリはユーザーのAppDataフォルダなど
    DATA_DIR = os.path.join(os.environ.get('APPDATA', os.path.expanduser('~')), APP_NAME)
else:
    # 開発環境
    DATA_DIR = os.path.join(RESOURCE_DIR, "data")

# データ関連パスを設定
LOG_OUTPUT_PATH = os.path.join(DATA_DIR, "logs")
LAUNCHER_PATH = os.path.join(DATA_DIR, "launcher.json")
LAUNCHER_WORKSPACE_DIR = os.path.join(DATA_DIR, "workspace")
USER_DATA_PATH = os.path.join(DATA_DIR, "user_data.json")
LOG_FILE_PATH = os.path.join(LOG_OUTPUT_PATH, "app.log")

# 必要なディレクトリを作成
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(LAUNCHER_WORKSPACE_DIR, exist_ok=True)
os.makedirs(LOG_OUTPUT_PATH, exist_ok=True)

# ログ設定ファイルの指定
if MODE == "DEBUG":
    LOG_CONFIG_PATH = os.path.join(LOG_CONFIG_DIR, "logger.dev.yaml")
else:
    LOG_CONFIG_PATH = os.path.join(LOG_CONFIG_DIR, "logger.prod.yaml")

# 必要なJSONファイルの存在確認・初期化
def initialize_json_file(file_path, default_content={}):
    try:
        if not os.path.exists(file_path):
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(default_content, f, indent=2)
            return True
        return False
    except Exception as e:
        print(f"Error initializing file {file_path}: {e}")
        return False

# アプリ起動時に各種JSONファイルを初期化
initialize_json_file(LAUNCHER_PATH, {})
initialize_json_file(USER_DATA_PATH, {})