import os
import sys
import sqlite3
import hashlib
from PyQt6.QtWidgets import QApplication, QStackedWidget

from ui.login_ui import LoginUI
from ui.register_ui import RegisterUI
from ui.main_window_ui import MainWindowUI
from modules.login_module import LoginModule
from modules.register_module import RegisterModule
from core.database import init_db,ensure_default_admin
from core.hot_reload import HotReload


class AuthContainer(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("图片内容智能审核与违规检测系统-认证中心")
        self.setFixedSize(450, 640)

        self.login_ui = LoginUI()
        self.register_ui = RegisterUI()

        self.login_logic = LoginModule(self.login_ui)
        self.register_logic = RegisterModule(self.register_ui)

        self.addWidget(self.login_ui)
        self.addWidget(self.register_ui)

        self.login_ui.register_clicked.connect(self._goto_register)
        self.register_ui.login_clicked.connect(self._goto_login)

        self.register_logic.register_success.connect(self._goto_login)
        self.login_logic.login_success.connect(self._on_login_verified)

    def _goto_register(self):
        self.register_ui.refresh_captcha()
        self.setCurrentIndex(1)

    def _goto_login(self):
        self.login_ui.captcha_widget.update_captcha()
        self.login_ui.captcha_input.clear()
        self.setCurrentIndex(0)

    def _on_login_verified(self, username):
        role = "auditor"
        try:
            conn = sqlite3.connect("data/app.db")
            cursor = conn.cursor()
            cursor.execute("SELECT role FROM users WHERE username=?", (username,))
            row = cursor.fetchone()
            if row:
                role = row[0]
            conn.close()
        except Exception as e:
            print(f"角色查询失败: {e}")

        self.main_window = MainWindowUI(username, role)
        self.main_window.show()
        self.close()


def main():

    from PyQt6.QtCore import Qt
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )
    app = QApplication(sys.argv)

    reloader = HotReload(watch_dir="modules", enabled=True)
    reloader.start()


    init_db()

    ensure_default_admin()

    auth = AuthContainer()
    auth.show()
    reloader.stop()
    sys.exit(app.exec())



if __name__ == "__main__":
    main()