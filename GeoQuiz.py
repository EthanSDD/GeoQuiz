from tkinter import *
from tkinter import messagebox
from customtkinter import *
from PIL import Image, ImageTk

root = CTk()
root.title("GeoQuiz")
root.geometry("1000x600")
root.minsize(1000, 600)
set_widget_scaling(1.8)
Frame(root, bg="blue").pack(fill="both", expand=True)

TypedMode = True

#import image
image_original = Image.open('map.jpg').resize((2932,1860))
image_tk = ImageTk.PhotoImage(image_original)

#create label
Label2 = CTkLabel(root, text="", image=image_tk)

def BeginQuiz():
    Button1.grid_remove()
    Label2.place(x=10, y=10)
    Button1.place(x=10, y=10)
    Label2.grid_remove()

Button1 = CTkButton(root, width=80, text="Begin Quiz", command=BeginQuiz, font=("Arial", 10))
Button1.place(x=10, y=10)

class DragManage():
    def addDragWidget(self, widget):
        self.widget = widget
        self.root = widget.winfo_toplevel()
        self.widget.bind("<B1-Motion>", self.on_drag)
        self.widget.bind("<Button-1>", self.clickwin)
        self.offset_x = 0
        self.offset_y = 0
    def clickwin(self, event):
        self.offset_x = event.x
        self.offset_y = event.y
    def on_drag(self, event):
        self.widget.place(x=event.x_root - self.offset_x - 141, y=event.y_root - self.offset_y - 141)

drag1 = DragManage()
drag1.addDragWidget(Label2)

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

# About popup

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