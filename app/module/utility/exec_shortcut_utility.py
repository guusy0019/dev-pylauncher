import os


class ShortcutExecutor:

    @staticmethod
    def execute_shortcut(*, shortcut_path: str):
        # ショートカットファイルを実行
        if os.path.exists(shortcut_path):
            os.startfile(shortcut_path)
        else:
            print(f"Shortcut not found: {shortcut_path}")
