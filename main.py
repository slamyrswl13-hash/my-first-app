__version__ = "1.0.0"

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MyApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            spacing=20,
            padding=30
        )

        title = Label(
            text="My First App",
            font_size=30
        )

        name_input = TextInput(
            hint_text="Enter your name",
            font_size=22,
            multiline=False
        )

        button = Button(
            text="Say Hello",
            font_size=24
        )

        result = Label(
            text="",
            font_size=24
        )

        button.bind(
            on_press=lambda instance:
            self.say_hello(name_input, result)
        )

        layout.add_widget(title)
        layout.add_widget(name_input)
        layout.add_widget(button)
        layout.add_widget(result)

        return layout

    def say_hello(self, name_input, result):
        name = name_input.text
        result.text = "Hello " + name + "!"


MyApp().run()