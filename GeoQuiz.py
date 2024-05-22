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
HighScore = 0

def BeginQuiz():
    BeginButton.place_forget()
    RegionMenu.place_forget()
    ModeButton.place_forget()
    ScoreLabel.place_forget()
    ButtonsBG.place(relx=1.0, rely=1.0, anchor='se')
    SubmitButton.place(relx=0.97, rely=0.74, anchor='se')
    SkipButton.place(relx=0.97, rely=0.82, anchor='se')
    NewAttemptButton.place(relx=0.99, rely=0.9, anchor='se')
    EndQuizButton.place(relx=0.975, rely=0.98, anchor='se')
    ImageLabel.place(relx=0.5, rely=0.5, anchor='center')
    if CurrentMode.get() == "Typed Mode":
        EntryFieldElement.place(relx=0.5, rely=0.95, anchor='center')
    elif CurrentMode.get() == "Select Mode":
        print("select")

def GoToMenu():
    BeginButton.place(relx=0.5, rely=0.35, anchor='center')
    RegionMenu.place(relx=0.5, rely=0.5, anchor='center')
    ModeButton.place(relx=0.5, rely=0.6, anchor='center')
    ScoreLabel.place(relx=0.5, rely=0.7, anchor='center')

def Submit():
    Answer = EntryFieldElement.get()
    print(Answer)

def Skip():
    print()

def NewAttempt():
    print()

def EndQuiz():
    ImageLabel.place_forget()
    ButtonsBG.place_forget()
    SubmitButton.place_forget()
    SkipButton.place_forget()
    NewAttemptButton.place_forget()
    EndQuizButton.place_forget()
    EntryFieldElement.place_forget()
    GoToMenu()

def EntryField():
    print()

# Menu Buttons
BeginButton = CTkButton(root, width=250, height=50, text="Begin Quiz", command=BeginQuiz, font=("Arial", 25))
Region = "North America"
def RegChange(selected_value):
    global Region
    Region = selected_value
    ImportImage()
RegionMenu = CTkOptionMenu(root, width=100, height=25, values=["North America", "South America", "Europe", "Asia", "Africa", "Oceania"], font=("Arial", 10), command=RegChange)
CurrentMode = tk.Variable()
CurrentMode.set("Select Mode")
ModeButton = CTkSegmentedButton(root, width=100, height=25, values=["Select Mode", "Typed Mode"], font=("Arial", 10), variable=CurrentMode)
ScoreLabel = CTkLabel(root, text=f"High Score: {HighScore}", font=("Arial", 10))

def ImportImage(): # Import Image
    image_original = Image.open(f"{Region}.png").resize((500, 500))
    image_tk = ImageTk.PhotoImage(image_original)
    global ImageLabel
    ImageLabel = tk.Label(root, text="", image=image_tk)
    ImageLabel.image = image_tk
ImportImage()

# Quiz Buttons
ButtonsBG = CTkLabel(root, width=82, height=113, text="", fg_color='#b8b8b8')
SubmitButton = CTkButton(root, width=50, height=20, text="Submit", command=Submit, font=("Arial", 10), bg_color="#b8b8b8")
SkipButton = CTkButton(root, width=50, height=20, text="Skip", command=Skip, font=("Arial", 10), bg_color="#b8b8b8")
NewAttemptButton = CTkButton(root, width=50, height=20, text="New Attempt", command=NewAttempt, font=("Arial", 10), bg_color="#b8b8b8")
EndQuizButton = CTkButton(root, width=50, height=20, text="End Quiz", command=EndQuiz, font=("Arial", 10), bg_color="#b8b8b8")
EntryFieldElement = CTkEntry(root, width=200, height=20, placeholder_text="Type answer here")

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