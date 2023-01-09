import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 1

        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        #add widgets to the inner GridLayout
        self.top_grid.add_widget(Label(text = "First Name"))
        self.fname = TextInput(multiline = False)
        self.top_grid.add_widget(self.fname)

        self.top_grid.add_widget(Label(text = "Last Name"))
        self.lname = TextInput(multiline = False)
        self.top_grid.add_widget(self.lname)

        self.top_grid.add_widget(Label(text = "Email"))
        self.email = TextInput(multiline = False)
        self.top_grid.add_widget(self.email)

        self.top_grid.add_widget(Label(text = "Gender"))
        self.gender = TextInput(multiline = False)
        self.top_grid.add_widget(self.gender)

        #add widget (the top_grid) to the main GridLyout which is the class we are in
        self.add_widget(self.top_grid)

        self.button = Button(text="SignUp", font_size = 32)
        #bind the button
        self.button.bind(on_press =  self.showOnTerminal)
        self.add_widget(self.button)

        


    def showOnTerminal(self, instance):
        gender =    self.gender.text
        email =     self.email.text
        fname =     self.fname.text
        lname =     self.lname.text
        if gender.__len__() > 0 and email.__len__() > 0 and fname.__len__() > 0 and lname.__len__():
            self.add_widget(Label(text = f"Hello {lname} {fname}, with email address {email}\nYou are a {gender}."))
        

class First(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    First().run()

