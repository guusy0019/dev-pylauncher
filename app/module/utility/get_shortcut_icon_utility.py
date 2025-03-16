import win32com.client
import win32gui
import win32ui
import win32con
import win32api
from PIL import Image

import tkinter as tk
from PIL import Image, ImageTk


class IconExtractor:
    def __init__(self, icon_size=(32, 32)):
        self.icon_size = icon_size
        self.ico_x = icon_size[0]
        self.ico_y = icon_size[1]

    def get_icon(self, icon_path):
        try:
            # ショートカットかどうかを確認し、ショートカットならターゲットを取得
            if icon_path.lower().endswith(".lnk"):
                shell = win32com.client.Dispatch("WScript.Shell")
                shortcut = shell.CreateShortCut(icon_path)
                icon_path = shortcut.TargetPath

            large, small = win32gui.ExtractIconEx(icon_path, 0)
            if not large:
                raise ValueError(f"アイコンを抽出できませんでした: {icon_path}")

            hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
            hbmp = win32ui.CreateBitmap()
            hbmp.CreateCompatibleBitmap(hdc, self.ico_x, self.ico_y)
            hdc = hdc.CreateCompatibleDC()

            hdc.SelectObject(hbmp)
            hdc.DrawIcon((0, 0), large[0])

            bmpstr = hbmp.GetBitmapBits(True)
            img = Image.frombuffer(
                "RGBA", (self.ico_x, self.ico_y), bmpstr, "raw", "BGRA", 0, 1
            )

            win32gui.DestroyIcon(large[0])
            win32gui.DestroyIcon(small[0])

            return img

        except Exception as e:
            raise RuntimeError(f"アイコンの抽出中にエラーが発生しました: {e}")

    def get_pillow_image(self, icon_path):
        pil_img = self.get_icon(icon_path)
        # pil_img example => <PIL.Image.Image image mode=RGBA size=64x64 at 0x1A26FB3CFA0>
        return pil_img
