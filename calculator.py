from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = None
        self.last_was_equal = False

        layout = GridLayout(cols=4)

        self.display = TextInput(font_size=55, readonly=True, halign='right', multiline=False)
        layout.add_widget(self.display)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        for button in buttons:
            layout.add_widget(Button(text=button, on_press=self.on_button_press))

        return layout

    def on_button_press(self, instance):
        current = self.display.text
        button_text = instance.text

        if button_text == 'C':
            self.display.text = ''
        elif button_text == '=':
            if current and not self.last_was_equal:
                try:
                    self.display.text = str(eval(current))
                except Exception:
                    self.display.text = 'Error'
            self.last_was_equal = True
        else:
            if (self.last_was_equal and button_text in self.operators) or \
                    (current == '' and button_text in self.operators):
                return
            else:
                self.last_was_equal = False
                self.display.text += button_text

        self.last_was_operator = button_text in self.operators

if __name__ == '__main__':
    CalculatorApp().run()
