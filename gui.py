import Tkinter
import tkMessageBox
t = Tkinter
tkMB = tkMessageBox
from Tkinter import *



top = Tkinter.Tk()
intro = top
top.title('Anglemania:Start')

def helloCallback():
   #create child window
   about = Toplevel()
   about.title("What is Anglemania!")
   #display message
   Label(about, text="Anglemania! is a math game about angles.").pack()
def level1Callback():
   #create child window
   about = Toplevel()
   about.title("About Anglemania!")
   #display message
   Label(about, text="Anglemania! 1.0 (1)").pack()
   Label(about).pack()
   Label(about, text="CREDITS: (NOT AFFILIATED WITH ANY OF THESE SITES)").pack()
   Label(about).pack()
   Label(about, text="Thanks to tiny.cc/tkinterguide for providing a guide.").pack
   Label(about, text="Thanks to tiny.cc/tkintertitle (see the one by user8875910) for the title bar").pack()
   Label(about, text="Thanks also to shields.io for the README.md badges").pack()
   Label(about, text="Thanks also to pythonprogramming.net/tkinter-adding-text-images/ for a nice article (can't remember what it taught me though)").pack()
   Label(about, text="Thanks so much to the Python Software Foundation and TkInter -- without you this wouldn't exist!").pack()
   Label(about, text="Thanks to smallguysit.com/index.php/2017/03/10/tkinter-create-window/ for 'from Tkinter import *'").pack()
   Label(about, text="Thanks to tiny.cc/childwindow for the guide on child windows -- it helped with this window!").pack()
   Label(about).pack()
   Label(about, text="Thanks to all!").pack()
   #quit child window and return to root window
   #the button is optional here, simply use the corner x of the child window
   Button(about, text='OK', command=about.destroy).pack()
def badaCallback():
   BSem.pack()
def notCodedCallback():
   tkMB.showerror("Sorry", "Not coded yet")
def showMoreCallback():
   BBada.pack()
def badaCB():
   BAbt.pack()
   Button(top, text='Exit', command=top.destroy).pack()
   Button(top, command=easterEggCallback).pack()
def messageWindow():
    #create child window
    newWindow = Toplevel()
    #display message
    message = "This is the child window"
    Label(newWindow, text=message).pack()
    #quit child window and return to root window
    #the button is optional here, simply use the corner x of the child window
    Button(newWindow, text='OK', command=newWindow.destroy).pack()
def easterEggCallback():
  txt3.pack()
def menuCB():
   notCodedCallback()

B = t.Button(top, text ="What is Anglemania!", command = helloCallback)
BAbt = t.Button(top, text ="About...", command=aboutCallback)
BSm = t.Button(top, text ="START", command= badaCallback)
BSem = t.Button(top, text ="Show even more...", command= showMoreCallback)
BBada = t.Button(top, text ="Badaboom!", command=badaCB)
BMenu = t.Button(top, text="Show menubar", command=menuCB).pack()

txt2 = Label(top, text="Welcome to gui-app!")

txt2.pack()
B.pack()
BSm.pack()
b = Button(top, image=play, command=on_button, relief=FLAT)
b.pack()
tkMB.showerror("Willkommen!", "Welcome to gui-app")


top.mainloop()
