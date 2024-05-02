from tkinter import *
from tkinter import messagebox
import tkinter as tk
from customtkinter import *
from PIL import Image, ImageTk

root = CTk()
root.title("GeoQuiz")
root.geometry("1000x600")
root.minsize(1000, 600)
set_widget_scaling(1.8)

# Initialise Values
TypedMode = True
CountryImage = "France.png"
HighScore = 0

def BeginQuiz():
    BeginButton.destroy()
    RegionMenu.destroy()
    ModeButton.destroy()
    ScoreLabel.destroy()
    ImageLabel.place(relx=0.5, rely=0.5, anchor='center')
    if CurrentMode.get() == "Typed Mode":
        print("typed")
    elif CurrentMode.get() == "Select Mode":
        print("select")

def GoToMenu():
    BeginButton.place(relx=0.5, rely=0.35, anchor='center')
    RegionMenu.place(relx=0.5, rely=0.5, anchor='center')
    ModeButton.place(relx=0.5, rely=0.6, anchor='center')
    ScoreLabel.place(relx=0.5, rely=0.7, anchor='center')

# Import Image
image_original = Image.open(CountryImage).resize((500, 500))
image_tk = ImageTk.PhotoImage(image_original)
ImageLabel = tk.Label(root, text="", image=image_tk)

# Menu Buttons
BeginButton = CTkButton(root, width=250, height=50, text="Begin Quiz", command=BeginQuiz, font=("Arial", 25))
RegionMenu = CTkOptionMenu(root, width=100, height=25, values=["North America", "South America", "Europe", "Asia", "Africa", "Oceania"], font=("Arial", 10))
CurrentMode = tk.Variable()
CurrentMode.set("Select Mode")
ModeButton = CTkSegmentedButton(root, width=100, height=25, values=["Select Mode", "Typed Mode"], font=("Arial", 10), variable=CurrentMode)
ScoreLabel = CTkLabel(root, text=f"High Score: {HighScore}", font=("Arial", 10))

# Quiz Buttons

GoToMenu()

# Sizing
def small():
    set_widget_scaling(1.0)
    root.minsize(1000, 600)
    root.geometry("1000x600")
    
def medium():
    set_widget_scaling(1.8)
    root.minsize(1000, 600)
    root.geometry("1000x600")

def large():
    set_widget_scaling(2.4)
    root.minsize(1000, 600)
    root.geometry("1000x600")

# About Popup
def about():
    messagebox.showinfo(title="GeoQuiz", message="By Ethan \
                    https://github.com/EthanSDD/GeoQuiz \
                    Licensed under GPL-3.0")

# Create File toolbar
menubar = Menu(root)
root.configure(menu=menubar)

menufile = Menu(menubar, tearoff=0)
menuthem = Menu(menubar, tearoff=0)
menufont = Menu(menubar, tearoff=0)
menutran = Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=menufile)
menubar.add_cascade(label="Language", menu=menutran)
menubar.add_cascade(label="Theme", menu=menuthem)
menubar.add_cascade(label="Zoom", menu=menufont)
menubar.add_cascade(label="TTS", menu=menutran)

menufile.add_command(label="About", command=about)
menufile.add_separator()
menufile.add_command(label="Exit", command=root.destroy)

menuthem.add_cascade(label="Dark", command=lambda: set_appearance_mode("dark"))
menuthem.add_cascade(label="Light", command=lambda: set_appearance_mode("light"))

menufont.add_command(label="Small", command=small)
menufont.add_command(label="Medium", command=medium)
menufont.add_command(label="Large", command=large)

root.mainloop()