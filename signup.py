import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import mysql.connector

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)


        conn = mysql.connector.connect(
			host = "localhost", 
			user = "root",
			passwd = "",
			database = "signup",
			)
        
        cursor = conn.cursor()
        # cursor.execute("CREATE DATABASE IF NOT EXISTS signup")
        cursor.execute("""CREATE TABLE if not exists customers( id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
			fname VARCHAR(50), lname VARCHAR(50), gender VARCHAR(10), email VARCHAR(150))
		 """)

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

        self.button = Button(text="SignUp", font_size = 33)
        #bind the button
        self.button.bind(on_press =  self.submitToDB)
        self.add_widget(self.button)

        


    def submitToDB(self, instance):
        conn = mysql.connector.connect(
			host = "localhost", 
			user = "root",
			passwd = "",
			database = "signup",
			)
        
        cursor = conn.cursor()
        
        gender =    self.gender.text
        email =     self.email.text
        fname =     self.fname.text
        lname =     self.lname.text
        if gender.__len__() > 0 and email.__len__() > 0 and fname.__len__() > 0 and lname.__len__():
            sql = "INSERT INTO customers (fname, lname, gender, email) VALUES (%s, %s, %s, %s)"
            values = (fname, lname, gender, email)
            cursor.execute(sql, values)
            self.add_widget(Label(text = f"Account for {lname} created successfully!"))
        else:
            self.add_widget(Label(text = f"All fields must be filled!"))



class First(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    First().run()
