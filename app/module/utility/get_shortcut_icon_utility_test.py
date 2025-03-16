import unittest
from app.module.utility.get_shortcut_icon_utility import IconExtractor


class TestIconExtractor(unittest.TestCase):

    def test_extract_icon(self):
        icon_extractor = IconExtractor(icon_size=(64, 64))
        icon = icon_extractor.get_icon(
            icon_path="C:/ProgramData/Microsoft/Windows/Start Menu/Programs/OneNote.lnk"
        )
        # icon <PIL.Image.Image image mode=RGBA size=64x64 at 0x1A26FB3CFA0>
        self.assertIsNotNone(icon)  # アイコンがNoneでないことを確認

    def test_get_pillow_image(self):
        icon_extractor = IconExtractor(icon_size=(64, 64))
        pil_img = icon_extractor.get_pillow_image(
            icon_path="C:/ProgramData/Microsoft/Windows/Start Menu/Programs/OneNote.lnk"
        )
        # pil_img <PIL.Image.Image image mode=RGBA size=64x64 at 0x1A26FB3CFA0>
        # pillowのimageを表示する
        pil_img.show()
        self.assertIsNotNone(pil_img)
