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

# Widget Label
label1 = Label(text="Label 1", anchor="w", bd=2, fg="#ff0000", padx=5, pady=10)
label1.pack()

label2 = Label(text="Label 2", anchor="ne", bg="#ff0000", underline=6, width=20, height=5)
label2.pack()

window.mainloop()