from kivy.uix.screenmanager import Screen
from hekaya_core import HekayaCore

core = HekayaCore()

class MainScreen(Screen):
    def on_enter(self, *args):
        user = core.get_user()
        if user:
            self.ids.user_info.text = (
                "[color=#FFD700][b]👑 الجنيرال سيد المصري VIP 👑[/b][/color]\n\n"
                f"[color=#00ffaa]📧 الإيميل: [/color]{user['email']}\n"
                f"[color=#00ffaa]🔐 كلمة السر: [/color]{user['password']}\n"
                f"[color=#00ffaa]📱 الهاتف: [/color]{user['phone']}"
            )
        else:
            self.ids.user_info.text = "[color=#ff4444]لا توجد بيانات[/color]"
