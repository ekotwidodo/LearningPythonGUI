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

# Belajar Place
# place() memungkinkan memposisikan widget dengan tepat di dalam window menggunakan sistem koordinat
# Options: x, y, height, width, relx, rely, relwidth, relheight, anchor, bordermode
# anchor: N (atas), E (kanan), S (bawah), W (kiri), NE, NW, SE, or SW
# bordermode: INSIDE, OUTSIDE

firstButton = Button(text="This is first button")
firstButton.place(x=100, y=100, width="100", height="50")

secondButton = Button(text="This is second button")
secondButton.place(anchor=W, y=200, width="150", height="50")

thirdButton = Button(text="This is third button")
thirdButton.place(relwidth=0.2, relheight=0.1, relx=0.5, rely=0.5) # 50% dari x/y window

window.mainloop()