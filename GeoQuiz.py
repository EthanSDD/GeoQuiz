from tkinter import *
from tkinter import messagebox
import tkinter as tk
from customtkinter import *
from PIL import Image, ImageTk
import pyttsx3

root = CTk()
root.title("GeoQuiz")
root.geometry("1000x600")
root.minsize(1000, 600)
root.maxsize(1000, 600)
set_widget_scaling(1.8)

# Initialise Values
TypedMode = True
HighScore = 0
Size = "Medium"
Country = "USA"
Answer = "Test"
Submitted = False
Score = 0
CurrentCountryIndex = 0
Finished = False
CountryNum = 0
InfoLabel = CTkLabel(root, text="Test", font=("Arial", 10))

def QuizPlacement():
    global Submitted, Country, ImageLabel
    Submitted = False
    image_original = Image.open(f"images/{Country.lower()}.png").resize((1000, 750))
    image_tk = ImageTk.PhotoImage(image_original)
    ImageLabel = tk.Label(root, text="", image=image_tk)
    ImageLabel.image = image_tk
    ImageLabel.place(relx=0.5, rely=0.45, anchor="center")
    ImageLabel.lower()

def Quiz(Region, CountryNum):
    global Country, Finished
    if Region == "North America":
        CountryList = ("USA", "Mexico", "Canada")
        if CountryNum >= (len(CountryList) - 1):
            Finished = True
        Country = CountryList[CountryNum]
        QuizPlacement()
        CheckAnswer(Country, Region)

    elif Region == "South America":
        CountryList = ("Brazil", "Argentina", "Colombia")
        if CountryNum >= (len(CountryList) - 1):
            Finished = True
        Country = CountryList[CountryNum]
        QuizPlacement()
        CheckAnswer(Country, Region)

    elif Region == "Europe":
        CountryList = ("Germany", "France", "Russia")
        if CountryNum >= (len(CountryList) - 1):
            Finished = True
        Country = CountryList[CountryNum]
        QuizPlacement()
        CheckAnswer(Country, Region)

    elif Region == "Asia":
        CountryList = ("Japan", "Korea", "India")
        if CountryNum >= (len(CountryList) - 1):
            Finished = True
        Country = CountryList[CountryNum]
        QuizPlacement()
        CheckAnswer(Country, Region)

    elif Region == "Africa":
        CountryList = ("Egypt", "Ethiopia", "Tanzania")
        if CountryNum >= (len(CountryList) - 1):
            Finished = True
        Country = CountryList[CountryNum]
        QuizPlacement()
        CheckAnswer(Country, Region)

    elif Region == "Oceania":
        CountryList = ("Fiji", "New Zealand", "Vanuatu")
        if CountryNum >= (len(CountryList) - 1):
            Finished = True
        Country = CountryList[CountryNum]
        QuizPlacement()
        CheckAnswer(Country, Region)

def Learn(Region):
    global Country, ImageLabel, InfoLabel

    if Region == "North America":

        Country = "USA"
        image_original = Image.open(f"images/{Country.lower()}.png").resize((500, 500))
        image_tk = ImageTk.PhotoImage(image_original)
        ImageLabel = tk.Label(root, text="", image=image_tk)
        ImageLabel.image = image_tk
        ImageLabel.place(relx=0.5, rely=0.5, anchor="center")
        ImageLabel.lower()
        InfoLabel = CTkLabel(root, text="USA", font=("Arial", 10))
        InfoLabel.place(relx=0.5, rely=0.05, anchor="center")
        engine = pyttsx3.init()
        engine.say("USA")
        engine.runAndWait

    elif Region == "South America":
        
        Country = "Brazil"
        image_original = Image.open(f"images/{Country.lower()}.png").resize((500, 500))
        image_tk = ImageTk.PhotoImage(image_original)
        ImageLabel = tk.Label(root, text="", image=image_tk)
        ImageLabel.image = image_tk
        ImageLabel.place(relx=0.5, rely=0.5, anchor="center")
        ImageLabel.lower()
        InfoLabel = CTkLabel(root, text="Brazil", font=("Arial", 10))
        InfoLabel.place(relx=0.5, rely=0.05, anchor="center")
        engine = pyttsx3.init()
        engine.say("Brazil")
        engine.runAndWait

    elif Region == "Europe":
        
        Country = "Germany"
        image_original = Image.open(f"images/{Country.lower()}.png").resize((500, 500))
        image_tk = ImageTk.PhotoImage(image_original)
        ImageLabel = tk.Label(root, text="", image=image_tk)
        ImageLabel.image = image_tk
        ImageLabel.place(relx=0.5, rely=0.5, anchor="center")
        ImageLabel.lower()
        InfoLabel = CTkLabel(root, text="Germany", font=("Arial", 10))
        InfoLabel.place(relx=0.5, rely=0.05, anchor="center")
        engine = pyttsx3.init()
        engine.say("Germany")
        engine.runAndWait

    elif Region == "Asia":
        
        Country = "Japan"
        image_original = Image.open(f"images/{Country.lower()}.png").resize((500, 500))
        image_tk = ImageTk.PhotoImage(image_original)
        ImageLabel = tk.Label(root, text="", image=image_tk)
        ImageLabel.image = image_tk
        ImageLabel.place(relx=0.5, rely=0.5, anchor="center")
        ImageLabel.lower()
        InfoLabel = CTkLabel(root, text="Japan", font=("Arial", 10))
        InfoLabel.place(relx=0.5, rely=0.05, anchor="center")
        engine = pyttsx3.init()
        engine.say("Japan")
        engine.runAndWait

    elif Region == "Africa":
        
        Country = "Egypt"
        image_original = Image.open(f"images/{Country.lower()}.png").resize((500, 500))
        image_tk = ImageTk.PhotoImage(image_original)
        ImageLabel = tk.Label(root, text="", image=image_tk)
        ImageLabel.image = image_tk
        ImageLabel.place(relx=0.5, rely=0.5, anchor="center")
        ImageLabel.lower()
        InfoLabel = CTkLabel(root, text="Egypt", font=("Arial", 10))
        InfoLabel.place(relx=0.5, rely=0.05, anchor="center")
        engine = pyttsx3.init()
        engine.say("Egypt")
        engine.runAndWait

    elif Region == "Oceania":

        Country = "Fiji"
        image_original = Image.open(f"images/{Country.lower()}.png").resize((500, 500))
        image_tk = ImageTk.PhotoImage(image_original)
        ImageLabel = tk.Label(root, text="", image=image_tk)
        ImageLabel.image = image_tk
        ImageLabel.place(relx=0.5, rely=0.5, anchor="center")
        ImageLabel.lower()
        InfoLabel = CTkLabel(root, text="Fiji", font=("Arial", 10))
        InfoLabel.place(relx=0.5, rely=0.05, anchor="center")
        engine = pyttsx3.init()
        engine.say("Fiji")
        engine.runAndWait

def CheckAnswer(Country, Region):
    global Submitted, Answer, Score, HighScore, CountryNum, ImageLabel, Finished
    if Submitted: # Check if user has submitted a response
        if Answer.lower() == Country.lower(): # Correct answer
            Score += 1
            messagebox.showinfo(title="Result", message="Correct Answer!")
        else: # Incorrect answer
            messagebox.showinfo(title="Result", message=f"Incorrect! Answer was: {Country}")
        if Finished: # End of quiz
            Finished = False
            CountryNum = 0
            messagebox.showinfo(title="Result", message=f"Finished Quiz! Score: {Score}")
            if Score > HighScore:
                HighScore = Score
            EndQuiz()
        else:
            CountryNum += 1
            ImageLabel.place_forget()
            Quiz(Region, CountryNum)

def BeginQuiz():
    global Score, CountryNum
    Score = 0
    CountryNum = 0
    BeginButton.place_forget()
    RegionMenu.place_forget()
    ModeButton.place_forget()
    ScoreLabel.place_forget()
    if Size == "Small":
        ButtonsBGS.place(relx=1.0, rely=1.0, anchor="se")
        SubmitButton.place(relx=0.978, rely=0.83, anchor="se")
        SkipButton.place(relx=0.978, rely=0.88, anchor="se")
        NewAttemptButton.place(relx=0.99, rely=0.93, anchor="se")
        EndQuizButton.place(relx=0.983, rely=0.98, anchor="se")
    elif Size == "Medium":
        ButtonsBGM.place(relx=1.0, rely=1.0, anchor="se")
        SubmitButton.place(relx=0.97, rely=0.74, anchor="se")
        SkipButton.place(relx=0.97, rely=0.82, anchor="se")
        NewAttemptButton.place(relx=0.99, rely=0.9, anchor="se")
        EndQuizButton.place(relx=0.975, rely=0.98, anchor="se")
    elif Size == "Large":
        ButtonsBGL.place(relx=1.0, rely=1.0, anchor="se")
        SubmitButton.place(relx=0.97, rely=0.68, anchor="se")
        SkipButton.place(relx=0.97, rely=0.78, anchor="se")
        NewAttemptButton.place(relx=0.99, rely=0.88, anchor="se")
        EndQuizButton.place(relx=0.975, rely=0.98, anchor="se")
    if CurrentMode.get() == "Learn":
        Learn(Region)
    elif CurrentMode.get() == "Quiz":
        EntryFieldElement.place(relx=0.5, rely=0.95, anchor="center")
        EntryFieldElement.delete(0, END)
        Quiz(Region, CountryNum)

def GoToMenu():
    BeginButton.place(relx=0.5, rely=0.35, anchor="center")
    RegionMenu.place(relx=0.5, rely=0.5, anchor="center")
    ModeButton.place(relx=0.5, rely=0.6, anchor="center")
    ScoreLabel.place(relx=0.5, rely=0.7, anchor="center")

def Submit():
    global Submitted, Answer
    Answer = EntryFieldElement.get()
    Submitted = True
    CheckAnswer(Country, Region)

def Skip():
    EndQuiz()

def NewAttempt():
    EndQuiz()
    BeginQuiz()

# Forgets the labels to end the quiz and updates high score
def EndQuiz():
    ImageLabel.place_forget()
    ButtonsBGS.place_forget()
    ButtonsBGM.place_forget()
    ButtonsBGL.place_forget()
    SubmitButton.place_forget()
    SkipButton.place_forget()
    NewAttemptButton.place_forget()
    EndQuizButton.place_forget()
    EntryFieldElement.place_forget()
    ScoreLabel.configure(text=f"High Score: {HighScore}")
    InfoLabel.place_forget()
    GoToMenu()

# Menu Buttons
BeginButton = CTkButton(root, width=250, height=50, text="Begin Quiz", command=BeginQuiz, font=("Arial", 25))
Region = "North America"
def RegChange(selected_value):
    global Region
    Region = selected_value
RegionMenu = CTkOptionMenu(root, width=100, height=25, values=["North America", "South America", "Europe", "Asia", "Africa", "Oceania"], font=("Arial", 10), command=RegChange)
CurrentMode = tk.Variable()
CurrentMode.set("Quiz")
ModeButton = CTkSegmentedButton(root, width=100, height=25, values=["Quiz", "Learn"], font=("Arial", 10), variable=CurrentMode)
ScoreLabel = CTkLabel(root, text=f"High Score: {HighScore}", font=("Arial", 10))

# Quiz Buttons
ButtonsBGS = CTkLabel(root, width=95, height=127, text="", fg_color="#b8b8b8")
ButtonsBGM = CTkLabel(root, width=82, height=110, text="", fg_color="#b8b8b8")
ButtonsBGL = CTkLabel(root, width=78, height=100, text="", fg_color="#b8b8b8")
SubmitButton = CTkButton(root, width=50, height=20, text="Submit", command=Submit, font=("Arial", 10), bg_color="#b8b8b8")
SkipButton = CTkButton(root, width=50, height=20, text="Skip", command=Skip, font=("Arial", 10), bg_color="#b8b8b8")
NewAttemptButton = CTkButton(root, width=50, height=20, text="New Attempt", command=NewAttempt, font=("Arial", 10), bg_color="#b8b8b8")
EndQuizButton = CTkButton(root, width=50, height=20, text="End Quiz", command=EndQuiz, font=("Arial", 10), bg_color="#b8b8b8")
EntryFieldElement = CTkEntry(root, width=200, height=20, placeholder_text="Type answer here")
GoToMenu()

# Sizing
def Small():
    set_widget_scaling(1.0)
    global Size
    Size = "Small"
    
def Medium():
    set_widget_scaling(1.8)
    global Size
    Size = "Medium"

def Large():
    set_widget_scaling(2.4)
    global Size
    Size = "Large"

# About Popup
def about():
    messagebox.showinfo(title="GeoQuiz", message="By Ethan \
                    https://github.com/EthanSDD/GeoQuiz \
                    Licensed under GPL-3.0 \
                    Images by Vemaps.com")

# Create File toolbar
menubar = Menu(root)
root.configure(menu=menubar)

menufile = Menu(menubar, tearoff=0)
menuthem = Menu(menubar, tearoff=0)
menufont = Menu(menubar, tearoff=0)
menutran = Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=menufile)
menubar.add_cascade(label="Theme", menu=menuthem)
menubar.add_cascade(label="Zoom", menu=menufont)

menufile.add_command(label="About", command=about)
menufile.add_separator()
menufile.add_command(label="Exit", command=root.destroy)

menuthem.add_cascade(label="Dark", command=lambda: set_appearance_mode("dark"))
menuthem.add_cascade(label="Light", command=lambda: set_appearance_mode("light"))

menufont.add_command(label="Small", command=Small)
menufont.add_command(label="Medium", command=Medium)
menufont.add_command(label="Large", command=Large)

root.mainloop()