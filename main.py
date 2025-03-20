import yaml
import logging
import logging.config

from app.config.settings import LOG_CONFIG_PATH
from app.ui.layout.layout import AppLayout
from app.utility.app_manager import set_app

with open(LOG_CONFIG_PATH, "r") as f:
    log_config = yaml.safe_load(f)

logging.config.dictConfig(log_config)

def main():

    app = AppLayout()
    set_app(app)
    app.mainloop()

if __name__ == "__main__":
    main()

