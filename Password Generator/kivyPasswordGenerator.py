from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window

import string
import random
from threading import Thread
from functools import partial

Window.size = (300, 400)

class PasswordGeneratorApp(App):
    def getPasswordLength(self):
        #collect the length of password from the user
        #basic error handling 
        try:
            length = int(self.LengthofPassword.text)#max length is 94

            if length < 8:
                self.errLabel.text = "  Password must be more \nthan 8  in length. Try Again."
            elif length > 94:
                self.errLabel.text = "  Password can't be more \nthan 94  in length. Try Again."
            else:
                self.errLabel.text = "" 
                self.GeneratingLabel.text = "Generating..."
                return length
            
        except ValueError:
            self.errLabel.text = "      Invalid Input. \nPlase enter a number."
        

    def generatePassword(self, length):
        #code block to generate the password
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        symbols = string.punctuation
        numbers = string.digits

        merge = upper + lower + symbols + numbers
        shuffle = random.sample(merge, length)#Cannot generate more than 94length of password
        password = "".join(shuffle)
        print(f"Password is: {password}")
        self.GeneratingLabel.text = "Generated"
        self.GeneratedPasswordDisplay.text = password


    def generator(self, event):
        #Thread to call function to generate password
        length = self.getPasswordLength()
        #password = self.generatePassword(length)

        if length is not None:
            #self.GeneratingLabel.text = "Generated"
            self.genpass_thread = Thread(target = partial(self.generatePassword, length))
            self.genpass_thread.start() #start thread
        else:
            self.errLabel.text = "  Password must be more \nthan 8 in length. Try Again."


    def build(self):
        layout = RelativeLayout()

        with layout.canvas.before:
            Color(0.4, 0.4, 0.9, 1)
            self.rect = Rectangle(pos = layout.pos, size = layout.size)
            layout.bind(pos = self._update_rect, size = self._update_rect)

        #widgets
        self.TitleTag = Label(text = "Password Generator", pos_hint = {"center_x": 0.5, "center_y": 0.9},
                              font_size = 28, font_name = "Verdana", color = (0.3, 0.3, 0.3), bold = True)
        
        self.PasswordLengthLabel = Label(text = "Enter Length of Password:", font_size = 24, font_name = "Tahoma",
                                        pos_hint = {"center_x": 0.5, "center_y": 0.78})
        
        self.LengthofPassword = TextInput(text = "", size_hint = (0.7, 0.09), font_size = 18,
                                          pos_hint = {"center_x": 0.5, "center_y": 0.68},)
        
        self.generateButton = Button(text = "Generate", font_size = 18, font_name = "Tahoma", size_hint = (0.4, 0.13),
                                    pos_hint = {"center_x": 0.5, "center_y": 0.53}, on_press = self.generator)
        
        self.errLabel = Label(text = "", font_size = 20, font_name = "Tahoma", color = (0.3, 0.3, 0.3),
                             pos_hint = {"center_x": 0.5, "center_y": 0.4})
        
        self.GeneratingLabel = Label(text = "", font_size = 20, font_name = "Tahoma", color = (0.3, 0.3, 0.3),
                                    pos_hint = {"center_x": 0.5, "center_y": 0.4})

        self.GeneratedPasswordLabel = Label(text = "Generated Password:", font_size = 24, font_name = "Tahoma",
                                           pos_hint = {"center_x": 0.5, "center_y": 0.3})
        
        self.GeneratedPasswordDisplay = Label(text = "", font_size = 24, font_name = "Verdana", bold = True,
                                              size_hint = (0.7, 0.09), pos_hint = {"center_x": 0.5, "center_y": 0.2})


        #add widgets to layout
        layout.add_widget(self.GeneratedPasswordDisplay)
        layout.add_widget(self.GeneratedPasswordLabel)
        layout.add_widget(self.GeneratingLabel)
        layout.add_widget(self.errLabel)
        layout.add_widget(self.generateButton)
        layout.add_widget(self.LengthofPassword)
        layout.add_widget(self.PasswordLengthLabel)
        layout.add_widget(self.TitleTag)
        return layout
    
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
PasswordGeneratorApp().run()