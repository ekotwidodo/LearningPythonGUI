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

# Belajar Grid
# grid() menempatkan widget dalam tabel 2 dimensi. Widget master dibagi menjadi beberapa baris dan kolom dan setiap cell di tabel yang dihasilkan dapat menampung widget.
# Option: sticky, column, row, columnspan, rowspan, padx, pady, ipadx, ipady
# Sticky: Atas -> n, Bawah -> s, Kiri -> w, Kanan -> h

# konfigurasi kolom (akan ada 5 kolom)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)

# konfigurasi rowspan
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

button1 = Button(text="Button1")
button2 = Button(text="Button2")
button3 = Button(text="Button3")
button4 = Button(text="Button4")

button1.grid(column=0, row=0, sticky="wens")
button2.grid(column=1, row=0, sticky="wens")
button3.grid(column=2, row=0, sticky="wens", columnspan=3)
button4.grid(column=0, row=1, sticky="wens", columnspan=5)

window.mainloop()