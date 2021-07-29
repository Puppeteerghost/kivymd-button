# pip install kivymd
from kivymd.app import App
from kivy.uix.button import Button

# "MainApp" is just an application winch that you will run!
class MainApp(App):
    def build(self):
        return Button(
            text="Your text",
            # Size button and...
            # ...First number is width, the second is the height.
            size_hint=(.1, .1),
            # Position button
            pos_hint=({'center_x': .5, 'center_y': .5})
        )

# Run app
MainApp().run()
