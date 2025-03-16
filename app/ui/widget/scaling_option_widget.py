import customtkinter


class ScalingOptionWidget(customtkinter.CTkOptionMenu):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.change_scaling_event,
            **kwargs
        )
        self.set("100%")  # 100%を初期値に設定

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
