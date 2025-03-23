import logging
import customtkinter

from app.config.settings import USER_DATA_PATH
from app.module.application.usecase.userdata_usecase import UserDataUsecase
from app.module.infrastructure.repository.userdata_repository import UserDataRepository


class ScalingOptionWidget(customtkinter.CTkOptionMenu):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.change_scaling_event,
            **kwargs
        )
        self.set("100%")  # 100%を初期値に設定

    def change_scaling_event(self, new_scaling: str):
        try:
            self.set_scaling(new_scaling)
            user_data_usecase = UserDataUsecase(userdata_repository=UserDataRepository())
            user_data_usecase.save_user_data(key="scaling_option", value=new_scaling, user_data_path=USER_DATA_PATH)
        except Exception as e:
            logging.error(f"Error change_scaling_event: {e}")
            return
        
    @staticmethod
    def set_scaling(scaling: str):
        new_scaling_float = int(scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
        logging.info(f"Change scaling: {scaling}")
