import unittest
from pathlib import Path
from app.module.application.usecase.attendance_usecase import AttendanceUsecase
from app.module.utility.date_utility import DateUtility


class TestAttendanceUseCase(unittest.TestCase):

    def setUp(self):
        self.test_year_date = "2024"
        self.attendance_usecase = AttendanceUsecase()

        self.plane_attendance_path = Path(
            "C:\\Users\\matty\\doc\\（sample）出勤簿.xlsx"
        )
        self.attendance_path = Path("C:\\Users\\matty\\doc\\2024（sample）出勤簿.xlsx")
        self.attendance_path_key = "2024（sample）出勤簿.xlsx"

    def test_save_attendance_path(self):
        self.attendance_usecase.save_attendance_path(
            attendance_path=str(self.plane_attendance_path)
        )
        saved_path = self.attendance_usecase.get_attendance_path(
            key=self.attendance_path_key
        )
        self.assertEqual(saved_path, str(self.attendance_path))

    def test_get_attendance_path(self):
        data = self.attendance_usecase.get_attendance_path(key=self.attendance_path_key)
        self.assertEqual(data, str(self.attendance_path))

    def test_delete_attendance_path(self):
        self.attendance_usecase.delete_attendance_path(key=self.attendance_path_key)
        deleted_path = self.attendance_usecase.get_attendance_path(
            key=self.attendance_path_key
        )
        self.assertEqual(deleted_path, "")

    def test_get_initial_attendance_path(self):
        initial_path = self.attendance_usecase.get_initial_attendance_path()
        self.assertEqual(initial_path, str(self.attendance_path))

    def test_add_year_to_file_name(self):
        updated_path = self.attendance_usecase._add_year_to_file_name(
            path=str(self.attendance_path), year=self.test_year_date
        )
        expected_path = Path(
            f"C:/Users/matty/doc/{self.test_year_date}（sample）出勤簿.xlsx"
        )
        self.assertEqual(updated_path, expected_path)

    def test_gen_key_name_by_attendance_path(self):
        date_utility = DateUtility()
        this_year = date_utility.get_this_year()
        file_name = self.attendance_path.name
        key = self.attendance_usecase._gen_key_name_by_attendance_path(
            attendance_path=str(self.attendance_path)
        )
        self.assertEqual(key, f"{this_year}{file_name}")
