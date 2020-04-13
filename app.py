"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import *


class My_Application(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        
        #Boxes definition
        main_box = toga.Box()
        name_box = toga.Box()
        age_box = toga.Box()
        email_box = toga.Box()
        
        
        #Label definition
        Title_Label = toga.Label("Account Set Up", style= Pack(text_align = CENTER))
        Intro_Label = toga.Label("Welcome into the Cybergen App, please fill the below informations to create your account.", style = Pack(text_align = LEFT, padding_left = 10))
        name_label = toga.Label("Input your name : ")
        age_label = toga.Label("Input your age : ")
        email_label = toga.Label("Input your email adress : ")
        
        
        #Text input
        self.name_input = toga.TextInput()
        self.age_input = toga.TextInput()
        self.email_input = toga.TextInput()
        
        #Button
        account_button = toga.Button('Create account', on_press = self.create_account)
        
        #Creation of the architecture of the App
        name_box.add(name_label)
        name_box.add(self.name_input)
        age_box.add(age_label)
        age_box.add(self.age_input)
        email_box.add(email_label)
        email_box.add(self.email_input)
        
        
        main_box.add(Title_Label)
        main_box.add(Intro_Label)
        main_box.add(name_box)
        main_box.add(age_box)
        main_box.add(email_box)
        main_box.add(account_button)
        
        #Style definition
        
        #Box style
        main_box.style.update(direction = COLUMN, padding = 20)
        name_box.style.update(direction = ROW, padding_top = 30, width = 60)
        age_box.style.update(direction = ROW, padding_top = 7, width = 60)
        email_box.style.update(direction = ROW, padding_top = 7)
        
        #Label style
        Title_Label.style.update(flex = 1)
        Intro_Label.style.update(flex = 1, padding_top = 15)
        name_label.style.update(flex = 1, padding_left = 10)
        age_label.style.update(flex = 1, padding_left = 10)
        email_label.style.update(padding_left = 10)
        
        #Input style
        self.email_input.style.update( width = 250)
        
        #Button style
        account_button.style.update(direction = COLUMN, padding = 20)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
    
    def create_account(self, widget):
        mail = str(self.email_input.value)
        name = str(self.name_input.value)
        
        self.main_window.info_dialog(
        'Account successfully created !',
        'Welcome {}, please go check out the mail that we just sent to {} to verify your account'.format(name, mail)
        )
    


def main():
    return My_Application()
