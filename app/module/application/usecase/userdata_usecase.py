import logging
from app.module.infrastructure.repository.userdata_repository import UserDataRepository
from app.module.application.interface.userdata_interface import UserDataRepositoryInterface

logger = logging.getLogger("userdataLogger")

class UserDataUsecase:
    
        def __init__(self, userdata_repository: UserDataRepositoryInterface = None):
            self.userdata_repository = userdata_repository or UserDataRepository()
    
        def save_user_data(self, *, key: str, value: str, user_data_path: str) -> None:
            return self.userdata_repository.save_user_data(key=key, value=value, user_data_path=user_data_path)
        
        def get_all_user_data(self, *, user_data_path: str) -> dict:
            return self.userdata_repository.get_all_user_data(user_data_path=user_data_path)