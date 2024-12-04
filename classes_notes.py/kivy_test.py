from kivy.app import App
from kivy.lang import Builder

class HelloWorldApp(App):
    def build(self):
        return Builder.load_file('main.kv')


HelloWorldApp().run()

#URL or path to the thing's location
#A label is used to display text on the screen. You can also set fontsize
#When the button is pressed, the button sends some signal to something else.
#A blank box used to give the user ideas of what to put in the thing. You can set it to be false.
#You can also make checkboxes. Orientation tells you where the box should be.