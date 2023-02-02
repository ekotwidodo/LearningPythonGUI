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

# Belajar Pack
# pack() mengatur widget dalam kotak horizontal dan vertikal yang terbatas pada posisi kiri, kanan, atas, bawah, offset, dan relatif satu sama lain dalam bingkai (frame)
# side: TOP (default), BOTTOM, LEFT, RIGHT
# fill: NONE (default), X (fill horizontally), Y (fill vertically), BOTH
# expand: YES, NO
# padding: padx, pady, ipadx, ipady

firstName = Label(text="First Name")
firstName.pack(side=TOP, expand=YES, padx=20, pady=10)
lastName = Label(text="Last Name")
lastName.pack(side=LEFT, expand=YES, padx=10, pady=20)
age = Label(text="Age")
age.pack(side=RIGHT, expand=YES, padx=10, pady=10)
# submit = Button(text="Submit")
# submit.pack(side=BOTTOM, expand=YES, padx=10, pady=30)

window.mainloop()