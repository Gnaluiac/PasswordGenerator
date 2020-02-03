from tkinter import *
from PasswordGenerator import *


class Application():
    def create_widgets(self):
        self.label1 = Label(root, text="Select password length: ")
        self.length_slider = Scale(root, from_=1, to=60, orient=HORIZONTAL, command=self.generate_password)
        self.length_slider.set(1)
        self.password_label = Label(root, text="")
        self.nbsp_label = Label(root, text="")
        self.copy_button = Button(root, text="Copy", command=self.copy_password)

    def pack_widgets(self):
        self.label1.pack()
        self.length_slider.pack()
        self.password_label.pack()
        self.nbsp_label.pack()
        self.copy_button.pack()

    '''
    "Value" parameter fixes this error: generate_password() takes 1 positional argument but 2 were given.
    Only "Self" would be wrong because 2 parameters are sent in the command on line 8.
    https://python-forum.io/Thread-Tkinter-Takes-1-Positional-Argument-but-2-were-Given
    '''
    def generate_password(self, value):
        self.password = PasswordGenerator()
        self.password.set_length(self.length_slider.get())
        print(self.length_slider.get())
        self.password.make_password()
        self.pwd = self.password.get_password()
        self.password_label.config(text=self.pwd)

    def copy_password(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.pwd)

    def __init__(self, master=None):
        self.root = master
        root.geometry("500x150")
        root.title("Password generator")
        self.create_widgets()
        self.pack_widgets()


root = Tk()
app = Application(master=root)
root.mainloop()