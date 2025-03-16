from app.ui.layout.layout import AppLayout
from app.utility.app_manager import set_app

def main():
    app = AppLayout()
    set_app(app)
    app.mainloop()

if __name__ == "__main__":
    main()
