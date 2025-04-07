import os
import yaml
import logging
import logging.config

from app.config.settings import LOG_CONFIG_PATH
from app.ui.layout.layout import AppLayout
from app.utility.app_manager import set_app

# ログ設定の読み込みとエラーハンドリング
try:
    with open(LOG_CONFIG_PATH, "r") as f:
        log_config = yaml.safe_load(f)
    logging.config.dictConfig(log_config)
except FileNotFoundError:
    # ログ設定ファイルが見つからない場合の基本設定
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
        handlers=[logging.StreamHandler()]
    )
    logging.warning(f"Log config file not found: {LOG_CONFIG_PATH}. Using basic configuration.")
except Exception as e:
    # その他のエラー
    logging.basicConfig(level=logging.INFO)
    logging.error(f"Failed to configure logging: {e}")

def main():
    app = AppLayout()
    set_app(app)
    app.mainloop()

if __name__ == "__main__":
    main()