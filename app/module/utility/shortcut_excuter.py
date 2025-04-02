import logging
import os
import subprocess
import win32gui
import win32con
import win32process
import psutil
from win32com.client import Dispatch

logger = logging.getLogger("launcherLogger")

class ShortcutExecutor:

    @staticmethod
    def get_process_name_by_shortcut_path(*, shortcut_path: str):
        """
        ショートカットファイルのパスからプロセス名を取得する
        
        Args:
            shortcut_path: ショートカットファイルのパス
        
        Returns:
            str: プロセス名
        """
        if not os.path.exists(shortcut_path):
            logger.error(f"get_process_name_by_shortcut_path error. Shortcut not found: {shortcut_path}")
            raise FileNotFoundError(f"Shortcut not found: {shortcut_path}")

        try:
            shell = Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(shortcut_path)
            target_path = shortcut.TargetPath
            return os.path.basename(target_path)
        except Exception as e:
            logger.error(f"get_process_name_by_shortcut_path error. Error getting process name: {e}")
            raise Exception(f"Error getting process name: {e}")
        
    @staticmethod
    def check_shortcut_path(*, shortcut_path: str) -> bool:
        """
        ショートカットファイルのパスが正しいか確認する
        
        Args:
            shortcut_path: ショートカットファイルのパス
            
        Returns:
            bool: ショートカットファイルのパスが正しいかどうか

        """
        if not os.path.exists(shortcut_path):
            logger.error(f"check_shortcut_extension error. Shortcut not found: {shortcut_path}")
            return False
        
        if not os.path.splitext(shortcut_path)[1] == ".lnk":
            logger.error(f"check_shortcut_path error. Invalid file extension: {shortcut_path}")
            return False
        
        return True
            
    @staticmethod
    def exec_shortcut_by_shortcut_path(*, shortcut_path: str):
        """
        ショートカットファイルを実行する
        
        Args:
            shortcut_path: ショートカットファイルのパス
        """
        try:
            subprocess.run(f'start "" "{shortcut_path}"', shell=True, check=False)
            logger.info(f"Shortcut executed: {shortcut_path}")
        except FileNotFoundError:
            logger.error(f"FileNotFoundError: Shortcut not found: {shortcut_path}")
            raise FileNotFoundError(f"Shortcut not found: {shortcut_path}")
        except Exception as e:
            logger.error(f"Error executing shortcut: {e}")
            raise Exception(f"Error executing shortcut: {e}")

    @classmethod
    def quit_app_by_shortcut_path(cls, *, shortcut_path: str):
        """
        ショートカットファイルで起動したアプリケーションを終了させる
        
        Args:
            shortcut_path: ショートカットファイルのパス
        """
        process_name = cls.get_process_name_by_shortcut_path(shortcut_path=shortcut_path)

        try:
            subprocess.run(["taskkill", "/f", "/im", process_name], 
                            check=False, capture_output=True)
            logger.info(f"Process terminated: {process_name}")
        except Exception as e:
            logger.error(f"Error terminating process: {e}")
            raise Exception(f"Error terminating process: {e}")

    @classmethod
    def minimize_app_by_shortcut_path(cls, *, shortcut_path: str):
        """
        ショートカットファイルで起動したアプリケーションを最小化する
        
        Args:
            shortcut_path: ショートカットファイルのパス
        """
        try:
            process_name = cls.get_process_name_by_shortcut_path(shortcut_path=shortcut_path)
            
            # プロセス名が取得できた場合、そのプロセスを探してウィンドウハンドルを取得
            if process_name:
                # プロセスを検索
                for process in psutil.process_iter(['pid', 'name']):
                    if process.info['name'] == process_name:
                        pid = process.info['pid']
                        
                        # プロセスIDからウィンドウハンドルを取得
                        def enum_window_callback(hwnd, pid):
                            tid, current_pid = win32process.GetWindowThreadProcessId(hwnd)
                            if current_pid == pid and win32gui.IsWindowVisible(hwnd):
                                cls.window_handles.append(hwnd)
                            return True
                        
                        cls.window_handles = []
                        win32gui.EnumWindows(enum_window_callback, pid)
                        
                        # 取得したすべてのウィンドウを最小化
                        for hwnd in cls.window_handles:
                            win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

        except Exception as e:
            logger.error(f"Error minimizing app: {e}")
            raise Exception(f"Error minimizing app: {e}")