import webbrowser
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Sinewave Web Browser")
root.geometry("480x360")

def search():
	webbrowser.open(url.get())

label = Label(text="Sinewave Search", font="12", pady="10")
label.pack(side=TOP)

url = Entry(root, width=50)
url.pack(side=TOP)

btn = Button(text="Search", background="#989898", foreground="#ffffff", padx="0", pady="0", font="12", command=search)
btn.pack(side=BOTTOM)

root.mainloop()
