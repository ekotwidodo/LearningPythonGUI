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

# Widget Entry
def buttonClick():
    # entry1.delete(0, 2)
    # print("You have just deleted 2 first string")
    # text = entry1.get()
    # print("this is text input: ", text)
    # position = entry1.index(INSERT)
    # print("position of index of text", position)
    # entry1.insert(0, "addition_")
    # entry1.insert(END, "_addition")
    # entry1.select_adjust(5)
    # entry1.select_clear()
    # entry1.select_from(1)
    # entry1.select_to(6)
    # isActive = entry1.select_present()
    # print(isActive)
    entry1.select_range(1,6)

entry1 = Entry(window, bg="#fff000", bd=3, cursor="clock", font=("Arial", 9, "underline"))
entry1.pack()

button1 = Button(text="Submit", command=buttonClick)
button1.pack()

window.mainloop()