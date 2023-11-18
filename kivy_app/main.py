from kivy.app import App
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager

from monitor_control.monitor_control import MonitorControlScreen
from about.about import AboutScreen


class ScreenManager(ScreenManager):
    monitor_control_screen = MonitorControlScreen()
    about_screen = AboutScreen()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.monitor_control_screen.add_widget(self.monitor_control_screen)
        self.ids.about_screen.add_widget(self.about_screen)


class MainApp(App):
    def build(self):
        Window.size = (600, 450)
        Window.minimum_width = 500
        Window.minimum_height = 450
        return Builder.load_file('main.kv')


if __name__ == "__main__":
    MainApp().run()