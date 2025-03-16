import tkinter as tk
from app.utility.app_manager import restart_app, exit_app

class MenuLayout(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

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
        self.config.add_command(label="設定", command=self.to_settings)
        self.config.add_command(label="リロード(CTRL+R)", command=self.reload_window)
        self.config.add_separator()
        self.config.add_command(label="終了(CTRL+Q)", command=self.exit)
        # add_cascadeすることで、設定メニューを表示できる
        self.menu.add_cascade(label="設定", menu=self.config)

    def reload_window(self):
        restart_app()

    def exit(self):
        exit_app()

    def to_settings(self):
        pass
