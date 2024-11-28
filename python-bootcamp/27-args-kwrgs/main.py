import tkinter
# Used to creat GUI
# REF [tkinter](https://tcl.tk/man/tcl8.6/TkCmd/pack.htm)


# create window object from Tk() class
window = tkinter.Tk() #Create a windo do a task and end the window
# window.mainloop() # this should be at very end of the program its keep window open
window.title("My First GUI Program") # Give the title to window
window.minsize(width=600, height=300)

# Use Label Class
label = tkinter.Label(text="I am Label",font=('Calibre',24,'bold'))
label.pack(expand=True)

### Change text in label
label["text"]="I am raghib"
label.config(text="I am Uzma")

# Button Class to create button

def button_clicked():
    entry = input.get()
    label.config(text=entry)
    print("Button got clicked")
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack(expand=True)


## Entry Class

input = tkinter.Entry()
input.get()
input.pack()
print(input.get())









window.mainloop()
