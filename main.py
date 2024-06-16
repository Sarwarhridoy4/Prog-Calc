from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput

# Set the window size and title
Window.size = (400, 600)
Window.title = "progCalc"
Window.icon = 'favicon.ico'


class CalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [20, 20, 20, 20]
        self.spacing = 10

        # Set a glassy background
        with self.canvas.before:
            Color(1, 1, 1, 0.1)  # semi-transparent white
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])
            self.bind(size=self._update_rect, pos=self._update_rect)

        # Add the app logo
        self.logo = Image(source='progCalcLogo.png', size_hint_y=None, height=100)
        self.add_widget(self.logo)

        self.result = TextInput(
            readonly=True,
            halign="right",
            font_size=32,
            size_hint_y=None,
            height=70,
            background_color=(1, 1, 1, 0.1),  # more transparent for glassy effect
            foreground_color=(255, 255, 255, 1),
            cursor_blink=True
        )
        self.add_widget(self.result)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['Bin', 'Hex', 'Dec', 'Clear']
        ]

        grid = GridLayout(cols=4, spacing=10, size_hint_y=None, height=300)
        for row in buttons:
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    size_hint=(0.25, 0.25),
                    background_color=(255, 255, 255, 0.2),  # semi-transparent for glassy effect
                    background_normal='',  # Removes the default background
                    color=(255, 255, 255, 1)  # black text
                )
                button.bind(on_release=self.on_button_press)
                grid.add_widget(button)

        self.add_widget(grid)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == 'Clear':
            self.result.text = ''
        elif button_text == '=':
            try:
                self.result.text = str(eval(current))
            except Exception as e:
                self.result.text = 'Error'
        elif button_text in ('Bin', 'Hex', 'Dec'):
            try:
                num = int(current)
                if button_text == 'Bin':
                    self.result.text = bin(num)[2:]
                elif button_text == 'Hex':
                    self.result.text = hex(num)[2:]
                elif button_text == 'Dec':
                    self.result.text = str(num)
            except ValueError:
                self.result.text = 'Error'
        else:
            self.result.text += button_text


class ProgrammingCalculatorApp(App):
    def build(self):
        return CalculatorLayout()


if __name__ == '__main__':
    ProgrammingCalculatorApp().run()
