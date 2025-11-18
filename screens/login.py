from kivy.uix.screenmanager import Screen
from hekaya_core import HekayaCore

core = HekayaCore()

class LoginScreen(Screen):

    def login_user(self):
        email = self.ids.email.text.strip()
        password = self.ids.password.text.strip()
        phone = self.ids.phone.text.strip()

        if not email or "@" not in email:
            self.ids.status.text = "[color=#ff4444]اكتب إيميل صحيح[/color]"
            return

        if len(password) < 4:
            self.ids.status.text = "[color=#ff4444]كلمة السر قصيرة[/color]"
            return

        if len(phone) < 10:
            self.ids.status.text = "[color=#ff4444]رقم الهاتف غير صحيح[/color]"
            return

        ok, msg = core.login(email, password, phone)
        if ok:
            self.ids.status.text = "[color=#FFD700]تم تسجيل الدخول بنجاح ✔️[/color]"
            self.manager.current = "main"
        else:
            self.ids.status.text = f"[color=#ff4444]{msg}[/color]"
