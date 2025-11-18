from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import BooleanProperty

from screens.login import LoginScreen
from screens.main_screen import MainScreen
from screens.splash import SplashScreen

KV = """
ScreenManager:
    SplashScreen:
    LoginScreen:
    MainScreen:
"""

class HekayaApp(App):
    def build(self):
        self.title = "Hekaya VIP"
        return Builder.load_string(KV)

if __name__ == "__main__":
    HekayaApp().run()
