import customtkinter


class AppearanceModeWidget(customtkinter.CTkOptionMenu):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            values=["System", "Light", "Dark"],
            command=self.change_appearance_mode_event,
            **kwargs
        )

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
