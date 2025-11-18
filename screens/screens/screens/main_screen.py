from kivy.uix.screenmanager import Screen
from hekaya_core import HekayaCore

core = HekayaCore()


class MainScreen(Screen):

    def on_enter(self, *args):
        user = core.get_user()
        if user:
            self.ids.user_info.text = (
                f"Email: {user['email']}\n"
                f"Password: {user['password']}\n"
                f"Phone: {user['phone']}"
            )
