import logging
import customtkinter
import os

from app.module.infrastructure.repository.launcher_repositpry import LauncherRepository
from app.module.application.presenter.launcher_presenter import LauncherPresenter
from app.module.application.usecase.launcher_usecase import LauncherUsecase
from app.config.settings import LAUNCHER_WORKSPACE_DIR
from app.utility.i18n import I18n

logger = logging.getLogger("launcherLogger")

class WorkspaceUtilityWidget(customtkinter.CTkFrame):
    
    def __init__(self, master, workspace_file_path: str):
        super().__init__(master, fg_color="transparent")
        self.workspace_file_path = workspace_file_path
        self.launcher_repository = LauncherRepository()
        self.launcher_presenter = LauncherPresenter(launcher_repository=self.launcher_repository)
        self.launcher_usecase = LauncherUsecase()
        self.i18n = I18n()

        self.app_name = LauncherUsecase.get_app_name_from_shortcut_path(self.workspace_file_path)
        
        self.notiification_text = ""
        self.notification_label = customtkinter.CTkLabel(
            master=self,
            text=self.notiification_text,
            text_color="red",
        )
        
        self.setup()
        
    def setup(self):
        self.workspace_label = customtkinter.CTkLabel(
            self,
            text=f"{self.i18n.get_text('launch_page.save_launcher_list_label')}: {self.app_name}",
            font=customtkinter.CTkFont(size=15, weight="bold"),
        )
        self.workspace_label.grid(row=0, column=0, padx=20, sticky="ew")
        
        self.rename_workspace_button = customtkinter.CTkButton(
            self,
            text=self.i18n.get_text("launch_page.save_launcher_list_rename_button"),
            command=self.rename_workspace_button_callback,
        )
        self.rename_workspace_button.grid(row=0, column=1, padx=10)
            
        self.delete_workspace_button = customtkinter.CTkButton(
            self,
            text=self.i18n.get_text("launch_page.save_launcher_list_delete_button"),
            command=self.delete_workspace_button_callback,
        )
        self.delete_workspace_button.grid(row=0, column=2, padx=10)

    def rename_workspace_button_callback(self):
        dialog = customtkinter.CTkInputDialog(
            title=self.i18n.get_text("launch_page.save_launcher_list_dialog_title"), 
            text=self.i18n.get_text("launch_page.save_launcher_list_dialog_placeholder")
        )
        new_name = dialog.get_input()
        
        # 入力がキャンセルされた場合や空の場合は処理をスキップ
        if not new_name:
            return
            
        workspace_name = f"{new_name}.json"
        old_workspace_file_path = self.workspace_file_path
        new_workspace_file_path = os.path.join(LAUNCHER_WORKSPACE_DIR, workspace_name)
        
        val = self.launcher_presenter.rename_workspace_file(old_path=old_workspace_file_path, new_path=new_workspace_file_path)
        
        if val["status"] == "success":
            self.workspace_file_path = new_workspace_file_path
            
            self.app_name = new_name
            self.workspace_label.configure(text=f"{self.i18n.get_text('launch_page.save_launcher_list_label')}: {self.app_name}")
            
            self.notiification_text = val["message"]
            self.notification_label.configure(text=self.notiification_text, text_color="blue")
            self.notification_label.grid(row=0, column=3, padx=20, sticky="ew")
            
            self.master.master.master.master.workspace_frame.setup()
            
            logger.info(f"change workspace name. new_workspace_name: {self.app_name}")
        else:
            self.notiification_text = val["message"]
            self.notification_label.configure(text=self.notiification_text, text_color="red")
            self.notification_label.grid(row=0, column=3, padx=20, sticky="ew",)
    
    def delete_workspace_button_callback(self):
        self.confirm_dialog = customtkinter.CTkToplevel(self)
        self.confirm_dialog.title("ワークスペースの削除")
        self.confirm_dialog.geometry("400x150")
        self.confirm_dialog.transient(self.master)
        self.confirm_dialog.grab_set()
        
        confirm_label = customtkinter.CTkLabel(
            self.confirm_dialog,
            text=f"[{self.app_name}] {self.i18n.get_text('launch_page.save_launcher_list_dialog_confirm_label')}",
            wraplength=350
        )
        confirm_label.pack(pady=20)
        
        button_frame = customtkinter.CTkFrame(self.confirm_dialog, fg_color="transparent")
        button_frame.pack(fill="x", pady=10)
        
        delete_button = customtkinter.CTkButton(
            button_frame,
            text=self.i18n.get_text("launch_page.save_launcher_list_dialog_delete_button"),
            fg_color="red",
            hover_color="darkred",
            command=self.confirm_delete
        )
        delete_button.pack(side="left", padx=20)
        
        cancel_button = customtkinter.CTkButton(
            button_frame,
            text=self.i18n.get_text("launch_page.save_launcher_list_dialog_cancel_button"),
            command=self.confirm_dialog.destroy
        )
        cancel_button.pack(side="right", padx=20)
        
    def confirm_delete(self):
        self.confirm_dialog.destroy()
        
        val = self.launcher_presenter.delete_workspace_file(file_path=self.workspace_file_path)
        
        if val["status"] == "success":
            self.workspace_file_path = None
            self.notiification_text = val["message"]
            self.notification_label.configure(text=self.notiification_text, text_color="blue")
            self.notification_label.grid(row=0, column=3, padx=20, sticky="ew")
            self.master.master.master.master.workspace_frame.setup()
            
            # ワークスペース削除後、ランチャーページに遷移
            try:
                main_app = self.master.master.master.master
                if hasattr(main_app, "select_frame_by_name"):
                    main_app.select_frame_by_name("launcher")
            except Exception as e:
                logger.error(f"main page transition error: {e}")

        else:
            self.notiification_text = val["message"]
            self.notification_label.configure(text=self.notiification_text, text_color="red")
            self.notification_label.grid(row=0, column=3, padx=20, sticky="ew",)