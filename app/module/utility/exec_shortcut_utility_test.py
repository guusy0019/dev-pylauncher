import unittest

from app.module.utility.exec_shortcut_utility import ShortcutExecutor


class TestShortcutExecutor(unittest.TestCase):

    def test_execute_shortcut(self):
        shortcut_executor = ShortcutExecutor()
        shortcut_executor.execute_shortcut(
            shortcut_path="C:/ProgramData/Microsoft/Windows/Start Menu/Programs/OneNote.lnk"
        )
        self.assertTrue(True)
