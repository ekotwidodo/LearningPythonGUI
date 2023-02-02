from tkinter import *

window = Tk()
width = 720
height = 640

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

x = int((screenWidth/2) - (width/2))
y = int((screenHeight/2) - (height/2))

window.geometry(f"{width}x{height}+{x}+{y}")
window.resizable(0,0)
# window.minsize(width, height)
# window.maxsize(width, height)
window.title("Users System Management")

# Widget Button
def buttonClick1():
    print("Button 1 Clicked!")

def buttonClick2():
    button1.invoke() # click button1
    print("Button 2 Clicked!")

def buttonClick3(arg):
    print("Button 3 Clicked! Show value: ", arg)

button1 = Button(window, text="Button 1", activebackground="#ff0000", activeforeground="#fff000", command=buttonClick1) # activebackground, activeforeground while clicking
button1.pack() 

button2 = Button(window, text="Button 2", activebackground="#fff", activeforeground="#ff0000", command=buttonClick2) # activebackground, activeforeground while clicking
button2.pack() 

button3 = Button(window, text="Button 3", activebackground="#fff", activeforeground="#000", command=lambda : buttonClick3("This is arguments")) # activebackground, activeforeground while clicking
button3.pack() 

window.mainloop()