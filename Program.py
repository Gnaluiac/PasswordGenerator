from tkinter import *
from PasswordGenerator import *

root = Tk()
root.geometry("500x150")
root.title("Password generator")


def create_widgets():
    label1 = Label(root, text="Select password length: ")
    label1.pack()
    global length_slider
    length_slider = Scale(root, from_=1, to=60, orient=HORIZONTAL, command=generate_password)
    length_slider.set(1)
    length_slider.pack()
    global password_label
    password_label = Label(root, text="")
    password_label.pack()
    nbsp_label = Label(root, text="")
    nbsp_label.pack()
    global copy_button
    copy_button = Button(root, text="Copy", command=copy_password)
    copy_button.pack()


def generate_password(event):
    password = PasswordGenerator()
    password.set_length(length_slider.get())
    password.make_password()
    global pwd
    pwd = password.get_password()
    password_label.config(text=pwd)


def copy_password():
    root.clipboard_clear()
    root.clipboard_append(pwd)


create_widgets()
root.mainloop()