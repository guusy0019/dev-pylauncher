import customtkinter
from app.utility.app_manager import restart_app, exit_app

class ConfigPage(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)

        self.setup()

    def setup(self):
        # Ctrl + Rのキーバインドを追加
        self.master.bind('<Control-r>', lambda event: self.reload_window())
        # Ctrl + Qのキーバインドを追加
        self.master.bind('<Control-q>', lambda event: self.exit())

        self.setup_menu()

    def setup_menu(self):
        self.config_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.config_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="ew")

        self.config_frame.grid_columnconfigure(0, weight=1)
        self.config_frame.grid_columnconfigure(1, weight=1)
        self.config_frame.grid_columnconfigure(2, weight=1)
        self.config_frame.grid_columnconfigure(3, weight=1)
        
        # リロードボタンの追加
        # 右側に配置するため、column=2を指定
        self.reload_button = customtkinter.CTkButton(
            self.config_frame, 
            text="リロード", 
            command=self.reload_window,
            width=100,
            height=32
        )
        self.reload_button.grid(row=0, column=2, padx=10, pady=10, sticky="e")
        
        # 終了ボタンの追加
        # 一番右側に配置するため、column=3を指定
        self.exit_button = customtkinter.CTkButton(
            self.config_frame, 
            text="終了", 
            command=self.exit,
            width=100,
            height=32,
            fg_color="#E74C3C"  # 赤色で警告色を設定
        )
        self.exit_button.grid(row=0, column=3, padx=10, pady=10, sticky="e")
        
        # ショートカットキーの説明ラベルを追加
        self.shortcut_label = customtkinter.CTkLabel(
            self.config_frame,
            text="ショートカット: Ctrl+R (リロード), Ctrl+Q (終了)",
            font=("", 12)
        )
        self.shortcut_label.grid(row=1, column=0, columnspan=4, padx=10, pady=(0, 10), sticky="w")

    def reload_window(self):
        restart_app()

    def exit(self):
        exit_app()