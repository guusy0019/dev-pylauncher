from app.config.settings import MODE

# アプリケーションインスタンスをグローバルに管理
app = None

def get_app():
    global app
    return app

def set_app(application):
    global app
    app = application

def restart_app():
    if MODE == "DEBUG":
        _restart_app()

        
    else:
        global app
        if app is not None:
            app.destroy()
            from app.ui.layout.layout import AppLayout
            app = AppLayout()
            app.mainloop()

def _restart_app():
    global app
    
    if app is not None:
        # 現在のウィンドウを閉じる
        app.destroy()
        
        # 関連するすべてのモジュールを再読み込み
        import sys
        import importlib
        
        # appパッケージに関連するすべてのモジュールを見つける
        modules_to_reload = [
            mod_name for mod_name in sys.modules
            if mod_name.startswith('app') and mod_name in sys.modules
        ]
        
        # 各モジュールを再読み込み（逆順で依存関係の問題を減らす）
        for mod_name in sorted(modules_to_reload, reverse=True):
            try:
                importlib.reload(sys.modules[mod_name])
                print(f"モジュール {mod_name} を再読み込みしました")
            except:
                print(f"モジュール {mod_name} の再読み込みに失敗しました")
        
        # 新しいインスタンスを作成
        from app.ui.layout.layout import AppLayout
        from app.utility.app_manager import set_app
        
        app = AppLayout()
        set_app(app)
        app.mainloop()

def exit_app():
    global app
    if app is not None:
        app.quit()
        app.destroy()
        app = None 