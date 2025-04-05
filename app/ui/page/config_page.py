import customtkinter
from app.utility.app_manager import restart_app, exit_app

class ConfigPage(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")

        self.setup()

    def setup(self):
        self.config_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.config_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="ew")
        
        self.reload_button = customtkinter.CTkButton(
            self.config_frame, 
            text="リロード( Ctrl + r )", 
            command=self.reload_window,
        )
        self.reload_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        
        self.exit_button = customtkinter.CTkButton(
            self.config_frame, 
            text="終了( Ctrl + q )", 
            command=self.exit,
        )
        self.exit_button.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

    def reload_window(self):
        restart_app()

    def exit(self):
        exit_app()