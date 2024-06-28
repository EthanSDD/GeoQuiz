# Import dependencies
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from customtkinter import *
from PIL import Image, ImageTk
import json

# Set root geometry and scaling
root = CTk()
root.title("GeoQuiz")
root.geometry("1000x600")
root.minsize(1000, 600)
root.maxsize(1000, 600)
set_widget_scaling(1.8)

# Initialise Variables
TypedMode = True
Size = "Medium"
Country = "USA"
Answer = "Test"
Submitted = False
Score = 0
CurrentCountryIndex = 0
Finished = False
CountryNum = 0
SkipQ = False
InGame = False
InfoLabel = CTkLabel(root, text="Test", font=("Arial", 10))

# Load country list
with open('data.json', 'r') as file:
    data = json.load(file)

def HighScoreUpdate(): # Update the highscore count
    global HighScore
    HighScore = data.get("highscore", 0)
HighScoreUpdate()

def QuizPlacement(): # Place the image for quiz or region function
    global Submitted, Country, ImageLabel
    Submitted = False
    image_tk = ImageTk.PhotoImage(image_original)
    ImageLabel = tk.Label(root, text="", image=image_tk)
    ImageLabel.image = image_tk
    ImageLabel.place(relx=0.5, rely=0.45, anchor="center")
    ImageLabel.lower()

def Quiz(Region, CountryNum): # Quiz function, asks what the country is
    global Country, Finished, image_original
    CountryList = data['regions'][Region]
    if CountryNum >= (len(CountryList) - 1): # If it is the last country in the list the quiz will end after answering
        Finished = True
    Country = CountryList[CountryNum]
    image_original = Image.open(f"images/{Region}/{Country.lower()}.png").resize((1000, 750))
    QuizPlacement()
    CheckAnswer(Country, Region)

def Learn(Region): # Learn function, displays image of the region
    global image_original
    image_original = Image.open(f"images/{Region}.png").resize((1000, 750))
    QuizPlacement()

def CheckAnswer(Country, Region): # Check if the user inputted the correct country
    global Submitted, Answer, Score, HighScore, CountryNum, ImageLabel, Finished, data, SkipQ
    if SkipQ: # Check for skip
        SkipQ = False
        CountryNum += 1
        ImageLabel.place_forget()
        if Finished:
            Finished = False
            CountryNum = 0
            messagebox.showinfo(title="Result", message=f"Finished Quiz! Score: {Score}")
            if Score > HighScore: # Update highscore if beaten
                data["highscore"] = Score
                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=2)
            EndQuiz()
        else:
            Quiz(Region, CountryNum)
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
            if Score > HighScore: # Update highscore if beaten
                data["highscore"] = Score
                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=2)
            EndQuiz()
        else: # If not finished with quiz move to next country
            CountryNum += 1
            ImageLabel.place_forget()
            Quiz(Region, CountryNum)

def BeginQuiz(): # Start the learn or quiz function
    global Score, CountryNum, InGame
    Score = 0
    CountryNum = 0
    MenuFrame.place_forget()
    ImageLabelBk.place_forget()
    if CurrentMode.get() == "Learn (l)": # If mode is set to learn initialise Learn
        MenuButton.place(relx=0.983, rely=0.98, anchor="se")
        Learn(Region)
    else: # If mode is set to quiz initialise quiz
        InGame = True
        EntryFieldElement.place(relx=0.5, rely=0.95, anchor="center")
        EntryFieldElement.delete(0, END)
        EntryFieldElement.focus_set()
        if Size == "Small": # Place items at intervals relative to size
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
        Quiz(Region, CountryNum)

def GoToMenu(): # Place menu items
    global ImageLabelBk
    MenuFrame.place(relx=0.5, rely=0.5, anchor="center")
    Title.place(relx=0.5, rely=0.25, anchor="center")
    Description.place(relx=0.5, rely=0.4, anchor="center")
    BeginButton.place(relx=0.5, rely=0.5, anchor="center")
    RegionMenu.place(relx=0.5, rely=0.625, anchor="center")
    ModeButton.place(relx=0.5, rely=0.75, anchor="center")
    ScoreLabel.place(relx=0.5, rely=0.9, anchor="center")

    # Menu Background Image Init
    image_original = Image.open("images/Menu.png").resize((1496, 990))
    image_tk = ImageTk.PhotoImage(image_original)
    ImageLabelBk = tk.Label(root, text="", image=image_tk)
    ImageLabelBk.image = image_tk
    ImageLabelBk.place(relx=0, rely=-0.05)
    ImageLabelBk.lower()

def Submit(): # Submit current answer
    global Submitted, Answer
    Answer = EntryFieldElement.get()
    Submitted = True
    CheckAnswer(Country, Region)

def Skip(): # Go to next question
    global SkipQ
    SkipQ = True
    CheckAnswer(Country, Region)

def NewAttempt(): # Retry the quiz
    EndQuiz()
    BeginQuiz()

def PressEnter(event): # When enter is pressed submit the answer
    if InGame:
        Submit()

def callback(event):
    if InGame == False: # If in menu
        if event.char == "b": # Detect b key press
            BeginButton.invoke() # Perform the task pressing the button would do
        if event.char == "q":
            ModeButton.set("Quiz (q)")
        if event.char == "l":
            ModeButton.set("Learn (l)")
root.bind_all("<b>", callback) # Bind b
root.bind_all("<q>", callback)
root.bind_all("<l>", callback)

def EndQuiz(): # Forget the labels to end the quiz and updates high score
    global InGame
    InGame = False
    ImageLabel.place_forget()
    ButtonsBGS.place_forget()
    ButtonsBGM.place_forget()
    ButtonsBGL.place_forget()
    SubmitButton.place_forget()
    SkipButton.place_forget()
    NewAttemptButton.place_forget()
    MenuButton.place_forget()
    EndQuizButton.place_forget()
    EntryFieldElement.place_forget()
    HighScoreUpdate()
    ScoreLabel.configure(text=f"High Score: {HighScore}")
    InfoLabel.place_forget()
    GoToMenu()

# Menu Buttons
MenuFrame = CTkFrame(root, width=250, height=250)
Title = CTkLabel(MenuFrame, width=250, height=50, text="GeoQuiz", font=("Arial", 50))
Description = CTkLabel(MenuFrame, width=100, height=25, text="A geography quiz for learning countries.")
BeginButton = CTkButton(MenuFrame, width=100, height=25, text="Begin (b)", command=BeginQuiz, font=("Arial", 15))
Region = "North America"
def RegChange(selected_value):
    global Region
    Region = selected_value
RegionMenu = CTkOptionMenu(MenuFrame, width=100, height=25, values=["North America", "South America", "Europe", "Asia", "Africa", "Oceania"], font=("Arial", 10), command=RegChange)
CurrentMode = tk.Variable()
CurrentMode.set("Quiz (q)")
ModeButton = CTkSegmentedButton(MenuFrame, width=100, height=25, values=["Quiz (q)", "Learn (l)"], font=("Arial", 10), variable=CurrentMode)
ScoreLabel = CTkLabel(MenuFrame, text=f"High Score: {HighScore}", font=("Arial", 10))

# Quiz Buttons
ButtonsBGS = CTkLabel(root, width=95, height=130, text="", fg_color="#b8b8b8")
ButtonsBGM = CTkLabel(root, width=82, height=110, text="", fg_color="#b8b8b8")
ButtonsBGL = CTkLabel(root, width=78, height=105, text="", fg_color="#b8b8b8")
SubmitButton = CTkButton(root, width=50, height=20, text="Submit", command=Submit, font=("Arial", 10), bg_color="#b8b8b8")
SkipButton = CTkButton(root, width=50, height=20, text="Skip", command=Skip, font=("Arial", 10), bg_color="#b8b8b8")
NewAttemptButton = CTkButton(root, width=50, height=20, text="New Attempt", command=NewAttempt, font=("Arial", 10), bg_color="#b8b8b8")
EntryFieldElement = CTkEntry(root, width=200, height=20, placeholder_text="Type answer here")
EntryFieldElement.bind("<Return>", PressEnter)
MenuButton = CTkButton(root, width=50, height=20, text="Menu", command=EndQuiz, font=("Arial", 10))
EndQuizButton = CTkButton(root, width=50, height=20, text="End Quiz", command=EndQuiz, font=("Arial", 10), bg_color="#b8b8b8")
GoToMenu()

def Small(): # Set elements to small scale
    set_widget_scaling(1.0)
    global Size
    Size = "Small"
    
def Medium(): # Set elements to medium scale
    set_widget_scaling(1.8)
    global Size
    Size = "Medium"

def Large(): # Set elements to large scale
    set_widget_scaling(2.4)
    global Size
    Size = "Large"

# About Popup
def about():
    messagebox.showinfo(title="GeoQuiz", message=
    "By Ethan \
                    https://github.com/EthanSDD/GeoQuiz \
Images by Vemaps.com \
                      Licensed under GPL-3.0")

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