from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = "vertical"
        self.spacing = 10
        self.padding = [50, 20, 50, 20]

        self.username_input = TextInput(hint_text='Username', multiline=False)
        self.password_input = TextInput(hint_text='Password', password=True, multiline=False)
        self.login_button = Button(text='Login', on_press=self.login)
        self.register_button = Button(text='Register', on_press=self.register)

        self.add_widget(Label(text='login / registro', font_size='20sp'))
        self.add_widget(self.username_input)
        self.add_widget(self.password_input)
        self.add_widget(self.login_button)
        self.add_widget(self.register_button)

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        

    def register(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        

class LoginApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    LoginApp().run()
