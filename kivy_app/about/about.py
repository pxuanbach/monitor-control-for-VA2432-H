from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen


# Builder is neccesary to work with multiple files
Builder.load_string(
    """
<AboutScreen>:
    orientation: 'vertical'
    info_label: info_label

    Label:
        id: info_label
        text: 'Personal Information'
    """
)

class AboutScreen(Screen):  
    pass

