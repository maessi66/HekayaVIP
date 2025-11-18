from kivy.uix.screenmanager import Screen
from hekaya_core import HekayaCore

core = HekayaCore()

class MainScreen(Screen):

    def on_enter(self, *args):
        user = core.get_user()

        if user:
            self.ids.user_info.text = (
                "[color=#FFD700][b]👑 بيانات المستخدم VIP 👑[/b][/color]\n\n"
                f"[color=#00FFAA]📧 الإيميل: [/color][color=#FFFFFF]{user['email']}[/color]\n"
                f"[color=#00FFAA]🔐 كلمة المرور: [/color][color=#FFFFFF]{user['password']}[/color]\n"
                f"[color=#00FFAA]📱 رقم الهاتف: [/color][color=#FFFFFF]{user['phone']}[/color]"
            )
        else:
            self.ids.user_info.text = (
                "[color=#FF4444]⚠ لا توجد بيانات مستخدم![/color]"
            )
