import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Text to Speech")
root.geometry("900x450+200+200")
root.resizable(False, False)
root.configure(bg="#305065")

#icon
image_icon =PhotoImage(file="speak.png") 
root.iconphoto(False, image_icon)

#top frame
Top_frame = Frame(root, bg="white", width=900, height=100)
Top_frame.place(x=0, y=0)

Logo = PhotoImage(file="speaker logo.png")
Label(Top_frame, image = Logo, bg="white").place(x=15, y=5)

Label(Top_frame, text="TEXT TO SPEECH", font="arial 20 bold", bg="white", fg="black").place(x=100, y=30)

######
text_area = Text(root, font="Robot 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

gender_combobox = Combobox(root, values=['Male', 'Female'], font='arial 14', state='r', width=10)
gender_combobox.place(x=550, y=200)

speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font='arial 14', state='r', width=10)
speed_combobox.place(x=730, y=200)

root.mainloop()