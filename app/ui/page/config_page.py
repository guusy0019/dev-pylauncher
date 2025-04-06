import customtkinter
import logging
from app.utility.app_manager import restart_app, exit_app
from app.ui.widget.lang_option_widget import LangOptionWidget
from app.utility.i18n import I18n

logger = logging.getLogger("launcherLogger")

class ConfigPage(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")

        self.i18n = I18n()

        self.setup()

    def setup(self):

        self.shortcut_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.shortcut_frame.grid(row=0, column=0, padx=10, pady=20, sticky="ew")
        self.shortcut_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.shortcut_label = customtkinter.CTkLabel(
            self.shortcut_frame,
            text=self.i18n.get_text("config_page.shortcut_settings"),
            font=customtkinter.CTkFont(size=18, weight="bold"),
        )
        self.shortcut_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        self.reload_button = customtkinter.CTkButton(
            self.shortcut_frame, 
            text=self.i18n.get_text("config_page.reload"), 
            command=self.reload_window,
        )
        self.reload_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        
        self.exit_button = customtkinter.CTkButton(
            self.shortcut_frame, 
            text=self.i18n.get_text("config_page.exit"), 
            command=self.exit,
        )
        self.exit_button.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

        self.lang_option_widget = LangOptionWidget(self)
        self.lang_option_widget.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    def reload_window(self):
        restart_app()

    def exit(self):
        exit_app()