# main.py
# تم استخدام مكتبة plyer بدلاً من webbrowser القياسي لضمان عمله على Android
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from plyer import webbrowser # تم التعديل إلى plyer

# Load KV layout
Builder.load_file("app.kv")

class MyScreenManager(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return MyScreenManager()

    def open_telegram(self):
        # افتح رابط التليجرام باستخدام plyer
        webbrowser.open("https://t.me/maessi2012")

    def logout(self):
        # اعد الى شاشة الدخول
        try:
            self.root.current = "login"
        except Exception:
            # بديل عام
            for s in self.root.screens:
                if s.name == "login":
                    self.root.current = "login"
                    break

if __name__ == "__main__":
    MainApp().run()
