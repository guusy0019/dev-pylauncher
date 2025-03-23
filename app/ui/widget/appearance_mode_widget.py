import logging
import customtkinter
from app.config.settings import USER_DATA_PATH
from app.module.application.usecase.userdata_usecase import UserDataUsecase
from app.module.infrastructure.repository.userdata_repository import UserDataRepository

logger = logging.getLogger("launcherLogger")

class AppearanceModeWidget(customtkinter.CTkOptionMenu):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            values=["System", "Light", "Dark"],
            command=self.change_appearance_mode_event,
            **kwargs
        )

    def change_appearance_mode_event(self, new_appearance_mode):
        try:
            self.set_appearance_mode(new_appearance_mode)
            user_data_usecase = UserDataUsecase(userdata_repository=UserDataRepository())
            user_data_usecase.save_user_data(key="appearance_mode", value=new_appearance_mode, user_data_path=USER_DATA_PATH)
        except Exception as e:
            logger.error(f"Error change_appearance_mode_event: {e}")
            return
        
    @staticmethod
    def set_appearance_mode(appearance_mode):
        customtkinter.set_appearance_mode(appearance_mode)
        logger.info(f"Change appearance mode: {appearance_mode}")
