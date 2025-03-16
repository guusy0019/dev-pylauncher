import tkinter as tk
from app.utility.app_manager import restart_app, exit_app
from app.utility.i18n import I18n

class MenuLayout(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.i18n = I18n()

        self.setup_menu()
        # Ctrl + Rのキーバインドを追加
        self.master.bind('<Control-r>', lambda event: self.reload_window())
        # Ctrl + Qのキーバインドを追加
        self.master.bind('<Control-q>', lambda event: self.exit())

    def setup_menu(self):
        self.menu = tk.Menu(self)
        self.master.config(menu=self.menu)

        # 設定メニュー
        self.config = tk.Menu(self.menu, tearoff=0)
        self.config.add_command(
            label=self.i18n.get_text("menu.settings"),
            command=self.to_settings
        )
        self.config.add_command(
            label=self.i18n.get_text("menu.reload"),
            command=self.reload_window
        )
        self.config.add_separator()
        self.config.add_command(
            label=self.i18n.get_text("menu.exit"),
            command=self.exit
        )
        # add_cascadeすることで、設定メニューを表示できる
        self.menu.add_cascade(
            label=self.i18n.get_text("menu.settings"),
            menu=self.config
        )

    def reload_window(self):
        restart_app()

    def exit(self):
        exit_app()

    def to_settings(self):
        pass
