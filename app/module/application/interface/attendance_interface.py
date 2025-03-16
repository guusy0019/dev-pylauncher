from abc import ABC, abstractmethod

class AttendanceRepositoryInterface(ABC):
    @abstractmethod
    def save_attendance_path(self, *, key: str, attendance_path: str) -> None:
        pass

    @abstractmethod
    def get_attendance_path(self, *, key: str) -> str:
        pass

    @abstractmethod
    def get_attendance_path_by_year(self, *, year: str) -> str:
        pass

    @abstractmethod
    def delete_attendance_path(self, *, key: str) -> None:
        pass