from datetime import datetime
from pathlib import Path
from app.module.application.interface.attendance_interface import AttendanceRepositoryInterface
# from app.module.infrastructure.repository.attendance_repository import AttendanceRepository
from app.module.utility.xlsx_utility import XlsxUtility


class AttendanceUsecase:
    def __init__(self, attendance_repository: AttendanceRepositoryInterface):
        self.this_year: str = datetime.now().strftime("%Y")
        self.last_year: str = str(int(self.this_year) - 1)
        self.attendance_repository = attendance_repository

    def save_attendance_path(self, *, key=None, attendance_path: str):
        """パスから年度を含むキーを生成して保存する"""
        if key is None:
            # 今年度のパスとキーを生成
            updated_path = self._add_year_to_file_name(attendance_path, self.this_year)
            # 実際にワークブックのファイル名を変更する
            # こうしないと、一つのworkbookに12ヶ月 * 年度分のデータが保存されてしまうので、年度事に自動で作成する
            self._rename_file_name(attendance_path, updated_path.name)
            updated_key = updated_path.name
            self.attendance_repository.save_attendance_path(
                key=str(updated_key), attendance_path=str(updated_path)
            )
        else:
            self.attendance_repository.save_attendance_path(
                key=key, attendance_path=attendance_path
            )

    def get_attendance_path(self, *, key: str) -> str:
        """キーから出勤簿のパスを取得する"""
        if self._validate_key_including_year(key):
            return self.attendance_repository.get_attendance_path(key=key)
        else:
            raise ValueError("キーには20xxの年度が含まれていません")

    def get_initial_attendance_path(self) -> str:
        """今年の出勤簿のパスを取得し、なければ昨年のパスを基準に作成"""
        attendance_path = self.attendance_repository.get_attendance_path_by_year(
            year=self.this_year
        )

        if attendance_path:
            return attendance_path
        else:
            last_year_path = self._find_attendance_path_by_year(self.last_year)
            if last_year_path:
                # 昨年のパスを元に今年度のパスを生成
                updated_path = self._add_year_to_file_name(
                    last_year_path, self.this_year
                )
                XlsxUtility().save_workbook(str(updated_path))
                return str(updated_path)
            else:
                # 昨年のパスが見つからなかった場合、UI側で指定させる
                print("昨年度の出勤簿パスが見つかりません。")
                return ""

    def delete_attendance_path(self, *, key: str) -> None:
        """指定されたキーの出勤簿パスを削除する"""
        self.attendance_repository.delete_attendance_path(key=key)

    def _find_attendance_path_by_year(self, year: str) -> str:
        """特定の年度の出勤簿パスを取得"""
        return self.attendance_repository.get_attendance_path_by_year(year=year) or ""

    def _add_year_to_file_name(self, path: str, year: str) -> Path:
        """パスのファイル名の先頭に指定された年度を追加したパスを返す"""
        path_obj = Path(path)
        file_name = path_obj.name
        updated_file_name = f"{year}{file_name}"
        return path_obj.with_name(updated_file_name)

    def _rename_file_name(self, path: str, new_name: str) -> None:
        """パスのファイル名を変更したパスを返す"""
        path_obj = Path(path)
        # 新しいフルパスを作成
        new_path = path_obj.with_name(new_name)
        # ファイル名を変更
        path_obj.rename(new_path)
        return None

    def _validate_key_including_year(self, key: str) -> bool:
        """キーが20xxで始まるかどうかを確認"""
        return key.startswith("20")
