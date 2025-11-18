# main.py
import webbrowser
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

# Load KV layout
Builder.load_file("app.kv")

class MyScreenManager(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return MyScreenManager()

    def open_telegram(self):
        # افتح رابط التليجرام المرسل منك
        webbrowser.open("https://t.me/maessi2012")

    def logout(self):
        # اعد الى شاشة الدخول
        # بعض الشاشات يستخدمون self.root.manager او self.root ... نستخدم root الحالية
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
