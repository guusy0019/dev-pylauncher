import customtkinter


class HomePage(customtkinter.CTkFrame):
    def __init__(self, master, large_test_image, image_icon_image):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(
            self, text="", image=large_test_image
        )
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(
            self, text="", image=image_icon_image, command=lambda: None
        )
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.home_frame_button_2 = customtkinter.CTkButton(
            self,
            text="CTkButton",
            image=image_icon_image,
            command=lambda: None,
            anchor="right",
        )
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.home_frame_button_3 = customtkinter.CTkButton(
            self,
            text="CTkButton",
            image=image_icon_image,
            command=lambda: None,
            anchor="top",
        )
        self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.home_frame_button_4 = customtkinter.CTkButton(
            self,
            text="CTkButton",
            image=image_icon_image,
            command=lambda: None,
            anchor="bottom",
        )
        self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)
