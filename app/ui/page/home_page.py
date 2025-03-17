import customtkinter
from PIL import Image
import os
from app.config.settings import IMAGE_DIR
from app.utility.i18n import I18n


class HomePage(customtkinter.CTkFrame):
    def __init__(self, master, large_test_image, image_icon_image):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.i18n = I18n()

        # スクロール可能なフレームを作成
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, width=800, height=700)
        self.scrollable_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        
        # タイトル
        self.title_label = customtkinter.CTkLabel(
            self.scrollable_frame, 
            text="CustomTkinter Widget Showcase", 
            font=customtkinter.CTkFont(size=24, weight="bold")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        # セクション1: 基本的なウィジェット
        self.section1_label = customtkinter.CTkLabel(
            self.scrollable_frame, 
            text="1. Basic Widgets", 
            font=customtkinter.CTkFont(size=18, weight="bold")
        )
        self.section1_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="w")
        
        # ボタンのフレーム
        self.button_frame = customtkinter.CTkFrame(self.scrollable_frame)
        self.button_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.button_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        
        # 通常のボタン
        self.button_1 = customtkinter.CTkButton(
            self.button_frame, text="Standard Button", command=self.button_callback
        )
        self.button_1.grid(row=0, column=0, padx=10, pady=10)
        
        # 画像付きボタン
        self.button_2 = customtkinter.CTkButton(
            self.button_frame, text="Image Button", image=image_icon_image, 
            compound="right", command=self.button_callback
        )
        self.button_2.grid(row=0, column=1, padx=10, pady=10)
        
        # 無効化されたボタン
        self.button_3 = customtkinter.CTkButton(
            self.button_frame, text="Disabled Button", state="disabled"
        )
        self.button_3.grid(row=0, column=2, padx=10, pady=10)
        
        # 色付きボタン
        self.button_4 = customtkinter.CTkButton(
            self.button_frame, text="Colored Button", 
            fg_color="transparent", border_width=2,
            text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            command=self.button_callback
        )
        self.button_4.grid(row=0, column=3, padx=10, pady=10)
        
        # セクション2: 入力ウィジェット
        self.section2_label = customtkinter.CTkLabel(
            self.scrollable_frame, 
            text="2. Input Widgets", 
            font=customtkinter.CTkFont(size=18, weight="bold")
        )
        self.section2_label.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="w")
        
        # 入力ウィジェットのフレーム
        self.input_frame = customtkinter.CTkFrame(self.scrollable_frame)
        self.input_frame.grid(row=4, column=0, padx=20, pady=10, sticky="ew")
        self.input_frame.grid_columnconfigure((0, 1), weight=1)
        
        # エントリー
        self.entry_1 = customtkinter.CTkEntry(
            self.input_frame, placeholder_text="CTkEntry"
        )
        self.entry_1.grid(row=0, column=0, padx=10, pady=10)
        
        # パスワードエントリー
        self.entry_2 = customtkinter.CTkEntry(
            self.input_frame, placeholder_text="Password", show="*"
        )
        self.entry_2.grid(row=0, column=1, padx=10, pady=10)
        
        # テキストボックス
        self.textbox = customtkinter.CTkTextbox(self.input_frame, width=400, height=100)
        self.textbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        self.textbox.insert("0.0", "CTkTextbox\n\nThis is a multiline textbox with word wrap.")
        
        # セクション3: 選択ウィジェット
        self.section3_label = customtkinter.CTkLabel(
            self.scrollable_frame, 
            text="3. Selection Widgets", 
            font=customtkinter.CTkFont(size=18, weight="bold")
        )
        self.section3_label.grid(row=5, column=0, padx=20, pady=(20, 10), sticky="w")
        
        # 選択ウィジェットのフレーム
        self.selection_frame = customtkinter.CTkFrame(self.scrollable_frame)
        self.selection_frame.grid(row=6, column=0, padx=20, pady=10, sticky="ew")
        self.selection_frame.grid_columnconfigure((0, 1, 2), weight=1)
        
        # チェックボックス
        self.checkbox_1 = customtkinter.CTkCheckBox(
            self.selection_frame, text="CTkCheckBox"
        )
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=10)
        
        # ラジオボタン
        self.radio_var = customtkinter.IntVar(value=0)
        self.radio_1 = customtkinter.CTkRadioButton(
            self.selection_frame, text="CTkRadioButton 1", variable=self.radio_var, value=0
        )
        self.radio_1.grid(row=0, column=1, padx=10, pady=10)
        self.radio_2 = customtkinter.CTkRadioButton(
            self.selection_frame, text="CTkRadioButton 2", variable=self.radio_var, value=1
        )
        self.radio_2.grid(row=0, column=2, padx=10, pady=10)
        
        # スイッチ
        self.switch_1 = customtkinter.CTkSwitch(
            self.selection_frame, text="CTkSwitch"
        )
        self.switch_1.grid(row=1, column=0, padx=10, pady=10)
        
        # セグメントボタン
        self.segment_button = customtkinter.CTkSegmentedButton(
            self.selection_frame,
            values=["Value 1", "Value 2", "Value 3"],
            command=self.segment_button_callback
        )
        self.segment_button.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="ew")
        
        # セクション4: ドロップダウンとスライダー
        self.section4_label = customtkinter.CTkLabel(
            self.scrollable_frame, 
            text="4. Dropdown & Sliders", 
            font=customtkinter.CTkFont(size=18, weight="bold")
        )
        self.section4_label.grid(row=7, column=0, padx=20, pady=(20, 10), sticky="w")
        
        # ドロップダウンとスライダーのフレーム
        self.dropdown_frame = customtkinter.CTkFrame(self.scrollable_frame)
        self.dropdown_frame.grid(row=8, column=0, padx=20, pady=10, sticky="ew")
        self.dropdown_frame.grid_columnconfigure((0, 1), weight=1)
        
        # コンボボックス
        self.combobox = customtkinter.CTkComboBox(
            self.dropdown_frame,
            values=["Option 1", "Option 2", "Option 3", "Option 4"]
        )
        self.combobox.grid(row=0, column=0, padx=10, pady=10)
        
        # オプションメニュー
        self.optionmenu = customtkinter.CTkOptionMenu(
            self.dropdown_frame,
            values=["Option 1", "Option 2", "Option 3"],
            command=self.optionmenu_callback
        )
        self.optionmenu.grid(row=0, column=1, padx=10, pady=10)
        
        # スライダー
        self.slider_1 = customtkinter.CTkSlider(
            self.dropdown_frame, from_=0, to=100, number_of_steps=10
        )
        self.slider_1.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        
        # プログレスバー
        self.progressbar = customtkinter.CTkProgressBar(self.dropdown_frame)
        self.progressbar.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        self.progressbar.set(0.5)  # 50%に設定
        
        # セクション5: タブビューとスクロールバー
        self.section5_label = customtkinter.CTkLabel(
            self.scrollable_frame, 
            text="5. TabView & ScrollableFrame", 
            font=customtkinter.CTkFont(size=18, weight="bold")
        )
        self.section5_label.grid(row=9, column=0, padx=20, pady=(20, 10), sticky="w")
        
        # タブビュー
        self.tabview = customtkinter.CTkTabview(self.scrollable_frame, width=400, height=200)
        self.tabview.grid(row=10, column=0, padx=20, pady=10, sticky="ew")
        self.tabview.add("Tab 1")
        self.tabview.add("Tab 2")
        self.tabview.add("Tab 3")
        
        # タブ1にコンテンツを追加
        self.tab1_label = customtkinter.CTkLabel(
            self.tabview.tab("Tab 1"), text="Content of Tab 1"
        )
        self.tab1_label.grid(row=0, column=0, padx=20, pady=20)
        
        # タブ2にコンテンツを追加
        self.tab2_button = customtkinter.CTkButton(
            self.tabview.tab("Tab 2"), text="Button in Tab 2"
        )
        self.tab2_button.grid(row=0, column=0, padx=20, pady=20)
        
        # タブ3にコンテンツを追加
        self.tab3_switch = customtkinter.CTkSwitch(
            self.tabview.tab("Tab 3"), text="Switch in Tab 3"
        )
        self.tab3_switch.grid(row=0, column=0, padx=20, pady=20)
        
        # セクション6: ダイアログとトップレベルウィンドウ
        self.section6_label = customtkinter.CTkLabel(
            self.scrollable_frame, 
            text="6. Dialogs & Windows", 
            font=customtkinter.CTkFont(size=18, weight="bold")
        )
        self.section6_label.grid(row=11, column=0, padx=20, pady=(20, 10), sticky="w")
        
        # ダイアログのフレーム
        self.dialog_frame = customtkinter.CTkFrame(self.scrollable_frame)
        self.dialog_frame.grid(row=12, column=0, padx=20, pady=10, sticky="ew")
        self.dialog_frame.grid_columnconfigure((0, 1, 2), weight=1)
        
        # ダイアログボタン
        self.dialog_button = customtkinter.CTkButton(
            self.dialog_frame, text="Open Dialog", command=self.open_dialog
        )
        self.dialog_button.grid(row=0, column=0, padx=10, pady=10)
        
        # 入力ダイアログボタン
        self.input_dialog_button = customtkinter.CTkButton(
            self.dialog_frame, text="Input Dialog", command=self.open_input_dialog
        )
        self.input_dialog_button.grid(row=0, column=1, padx=10, pady=10)
        
        # トップレベルウィンドウボタン
        self.toplevel_button = customtkinter.CTkButton(
            self.dialog_frame, text="New Window", command=self.open_toplevel
        )
        self.toplevel_button.grid(row=0, column=2, padx=10, pady=10)
        
        # 最後に余白を追加
        self.final_padding = customtkinter.CTkLabel(
            self.scrollable_frame, text=""
        )
        self.final_padding.grid(row=13, column=0, padx=20, pady=20)

    def button_callback(self):
        print("Button clicked!")
        
    def segment_button_callback(self, value):
        print(f"Segment button clicked: {value}")
        
    def optionmenu_callback(self, choice):
        print(f"Option menu selection: {choice}")
        
    def open_dialog(self):
        dialog = customtkinter.CTkInputDialog(title="Dialog", text="This is a dialog")
        
    def open_input_dialog(self):
        dialog = customtkinter.CTkInputDialog(title="Input", text="Enter something:")
        print(f"Input dialog result: {dialog.get_input()}")
        
    def open_toplevel(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("400x300")
        window.title("New Window")
        label = customtkinter.CTkLabel(window, text="This is a new window")
        label.pack(padx=20, pady=20)
