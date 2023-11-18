from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown


COMPONENT_HEIGHT = 50


class MonitorControlScreen(Screen):  
    def __init__(self, **kwargs):
        super(MonitorControlScreen, self).__init__(**kwargs)
        self.add_widget(MonitorControl())


class MonitorControl(BoxLayout):
    def __init__(self, **kwargs):
        super(MonitorControl, self).__init__(**kwargs)
        self.orientation = "vertical"

        self.title = Label(
            text="Monitor Control",
            font_size=32,
            size_hint_y=None,
            height=COMPONENT_HEIGHT*2,
            bold=True
        )
        self.add_widget(self.title)

        self.list_display_component()
        self.metadata_component()
        self.brightness_component(50)
        self.contrast_component(50)
    

    def list_display_component(self, options=['Option 1', 'Option 2']):
        self.list_display = GridLayout(
            cols=2, 
            height=COMPONENT_HEIGHT,
            size_hint_y=None
        )
        self.ld_title = Label(
            text="List Monitors", 
            size_hint=(0.3, None), 
            height=COMPONENT_HEIGHT,
            bold=True
        )

        # create a dropdown
        self.ld_dropdown = DropDown()
        for option in options:
            btn = Button(text=option, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.ld_dropdown.select(btn.text))
            self.ld_dropdown.add_widget(btn)

        self.select_btn_box = BoxLayout(
            padding=(20, 3), 
            size_hint=(0.7, None),
            height=COMPONENT_HEIGHT
        )
        self.select_btn = Button(
            text=options[0] if len(options) > 0 else "", 
            size_hint_y=None,
            height=44
        )

        # show the dropdown menu when the main button is released
        self.select_btn.bind(on_release=self.ld_dropdown.open)

        # assign the data to the button text.
        self.ld_dropdown.bind(
            on_select=lambda instance, x: setattr(self.select_btn, 'text', x)
        )

        self.select_btn_box.add_widget(self.select_btn)
        self.list_display.add_widget(self.ld_title)
        self.list_display.add_widget(self.select_btn_box)
        
        return self.add_widget(self.list_display)

    def metadata_component(
        self, 
        name="Monitor", 
        scrn_width=100, 
        scrn_height=100, 
        is_primary=False
    ):
        self.metadata = GridLayout(cols=1, rows=4)
        box_style = {
            "orientation": "horizontal", 
            "height": COMPONENT_HEIGHT,
            "size_hint_y": None,
        }
        title_style = {
            "size_hint": (0.3, None),
            "height": COMPONENT_HEIGHT,
            "bold": True
        }
        value_style = {
            "size_hint": (0.7, None),
            "valign": "middle",
            "height": COMPONENT_HEIGHT,
        }

        # Name
        self.name_box = BoxLayout(**box_style)
        self.name_title = Label(
            text="Name", 
            **title_style
        )
        self.name_value = Label(
            text=f"{name}", 
            **value_style
        )
        self.name_value.bind(size=self.name_value.setter('text_size')) 
        self.name_box.add_widget(self.name_title)
        self.name_box.add_widget(self.name_value)

        # Screen Width
        self.scrn_width_box = BoxLayout(**box_style)
        self.scrn_width_title = Label(
            text="Screen Width", 
            **title_style
        )
        self.scrn_width_value = Label(
            text=f"{scrn_width}", 
            **value_style
        )
        self.scrn_width_value.bind(size=self.scrn_width_value.setter('text_size')) 
        self.scrn_width_box.add_widget(self.scrn_width_title)
        self.scrn_width_box.add_widget(self.scrn_width_value)

        # Screen Height
        self.scrn_height_box = BoxLayout(**box_style)
        self.scrn_height_title = Label(
            text="Screen Height", 
            **title_style
        )
        self.scrn_height_value = Label(
            text=f"{scrn_height}", 
            **value_style
        )
        self.scrn_height_value.bind(size=self.scrn_height_value.setter('text_size')) 
        self.scrn_height_box.add_widget(self.scrn_height_title)
        self.scrn_height_box.add_widget(self.scrn_height_value)

        # Is Primary
        self.is_primary_box = BoxLayout(**box_style)
        self.is_primary_title = Label(
            text="Screen Height", 
            **title_style
        )
        self.is_primary_value = Label(
            text=f"{is_primary}", 
            **value_style
        )
        self.is_primary_value.bind(size=self.is_primary_value.setter('text_size')) 
        self.is_primary_box.add_widget(self.is_primary_title)
        self.is_primary_box.add_widget(self.is_primary_value)

        self.metadata.add_widget(self.name_box)
        self.metadata.add_widget(self.scrn_width_box)
        self.metadata.add_widget(self.scrn_height_box)
        self.metadata.add_widget(self.is_primary_box)
        return self.add_widget(self.metadata)

    def brightness_component(self, default_slider_value=0):
        self.brightness = BoxLayout(
            orientation="horizontal",
            height=COMPONENT_HEIGHT,
            size_hint_y=None
        )
        self.brightness_title = Label(
            text="Brightness", 
            size_hint=(0.3, None),
            height=COMPONENT_HEIGHT,
            bold=True
        )
        self.brightness_value = Label(
            text=f"{default_slider_value}", 
            width=30, 
            height=COMPONENT_HEIGHT,
            size_hint=(None, None)
        )
        self.brightness_slider = Slider(
            min=0, 
            max=100, 
            value=default_slider_value, 
            size_hint=(0.7, None),
            height=COMPONENT_HEIGHT
        )
        self.brightness_slider.bind(on_touch_up=self.on_brightness_slider_touch_up)

        self.brightness.add_widget(self.brightness_title)
        self.brightness.add_widget(self.brightness_value)
        self.brightness.add_widget(self.brightness_slider)

        return self.add_widget(self.brightness)
    
    def contrast_component(self, default_slider_value=0):
        self.contrast = GridLayout(
            cols=3, 
            height=COMPONENT_HEIGHT,
            size_hint_y=None
        )
        self.contrast_title = Label(
            text="Contrast", 
            height=COMPONENT_HEIGHT,
            size_hint=(0.3, None),
            bold=True
        )
        self.contrast_value = Label(
            text=f"{default_slider_value}", 
            width=30, 
            height=COMPONENT_HEIGHT,
            size_hint=(None, None)
        )
        self.contrast_slider = Slider(
            min=0, 
            max=100, 
            value=default_slider_value, 
            size_hint=(0.7, None),
            height=COMPONENT_HEIGHT,
        )
        self.contrast_slider.bind(on_touch_up=self.on_contrast_slider_touch_up)

        self.contrast.add_widget(self.contrast_title)
        self.contrast.add_widget(self.contrast_value)
        self.contrast.add_widget(self.contrast_slider)
        return self.add_widget(self.contrast)

    def on_brightness_slider_touch_up(self, instance, touch):
        if self.brightness_slider.collide_point(*touch.pos):
            self.brightness_value.text = f"{int(instance.value)}"

    def on_contrast_slider_touch_up(self, instance, touch):
        if self.contrast_slider.collide_point(*touch.pos):
            self.contrast_value.text = f"{int(instance.value)}"
