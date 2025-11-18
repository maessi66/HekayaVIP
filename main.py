import webbrowser
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

# Load KV file
Builder.load_file("app.kv")

class MyScreenManager(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return MyScreenManager()

    def open_telegram(self):
        webbrowser.open("https://t.me/maessi2012")

    def logout(self):
        self.root.current = "login"


if __name__ == "__main__":
    MainApp().run()
