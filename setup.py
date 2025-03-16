import sys
import os
from cx_Freeze import setup, Executable

from app.config.settings import ICON_PATH

LAUNCH_MODE = os.getenv("LAUNCH_MODE", default="PROD")

# バージョン
VERSION = "1.0"
# アプリ名
APP_NAME = "pylauncher"
# exeファイル名
EXE_NAME = "pylauncher"
# アプリの説明
DESCRIPTION = "windows用のランチャーデスクトップアプリです。"
# 作成者
AUTHOR = "guusy0019"
# 必要なパッケージ
PACKAGES = [
    "customtkinter",
    "darkdetect",
    "PIL",
    "jpholiday",
    "openpyxl",
    "psutil",
]

# アセットファイルの指定を詳細に行う
INCLUDE_FILES = [
    ("app/assets/", "lib/app/assets/"),  # アセットフォルダ全体をコピー
]

# Pythonのソースコードファイル名
SCRIPT_FILENAME = "main.py"
# アイコンファイルパス
ICON_PATH = ICON_PATH
# デスクトップにショートカットを作成するか
ADD_DESKTOP_SHORTCUT = True
# スタートメニューにショートカットを追加するか
ADD_START_MENU_SHORTCUT = True
# コンソール画面を無効化するか
WITHOUT_CONSOLE = True
# UUID
UUID = "com.guusy0019.pylauncher"

# ビルドオプション
build_options = {
    "packages": PACKAGES,
    "includes": [],
    "include_files": INCLUDE_FILES,
    "excludes": [],
    # 追加のビルドオプション
    "include_msvcr": True,  # Visual C++ ランタイムを含める
    "constants": {
        "LAUNCH_MODE": LAUNCH_MODE
    }
}

# 実行ファイルの設定
base = "Win32GUI" if WITHOUT_CONSOLE else None
exe = Executable(
    script=SCRIPT_FILENAME,
    base=base,
    target_name=EXE_NAME,
    icon=ICON_PATH,
    shortcut_name=APP_NAME,
    shortcut_dir="DesktopFolder" if ADD_DESKTOP_SHORTCUT else None,
)

# セットアップ
setup(
    name=APP_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    options={"build_exe": build_options},
    executables=[exe]
)
