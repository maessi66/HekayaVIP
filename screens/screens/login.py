from kivy.uix.screenmanager import Screen
from hekaya_core import HekayaCore

core = HekayaCore()


class LoginScreen(Screen):

    def login_user(self):
        email = self.ids.email.text
        password = self.ids.password.text
        phone = self.ids.phone.text

        ok, msg = core.login(email, password, phone)

        self.ids.status.text = msg

        if ok:
            self.manager.current = "main"
