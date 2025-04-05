import customtkinter

class NotificationWindowWidget:
    def __init__(self, master: customtkinter.CTk):
        self.master = master

    def open_toplevel(
            self,
            *,
            textbox_text: str, 
            title: str="エラーが発生しました。",
            text_color: str="red",
            wrap: str="word",
            width: int=400,
            height: int=200,
            is_editable: bool=False
            ):
        window = customtkinter.CTkToplevel(self.master)
        window.geometry(f"{width}x{height}")
        window.title(title)
        
        text_box = customtkinter.CTkTextbox(
            window,
            text_color=text_color,
            wrap=wrap,
            height=height
        )
        text_box.pack(padx=20, pady=20, fill="both", expand=True)
        text_box.insert("1.0", textbox_text)
        text_box.configure(state="normal" if is_editable else "disabled")


