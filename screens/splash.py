from kivy.uix.screenmanager import Screen
from kivy.clock import Clock


class SplashScreen(Screen):

    def on_enter(self, *args):
        Clock.schedule_once(self.go_login, 2)

    def go_login(self, dt):
        self.manager.current = "login"
