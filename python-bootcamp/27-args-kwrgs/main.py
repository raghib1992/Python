import tkinter


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=600, height=300)


# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

# Change the label
# my_label["text"] = "New Text"
# my_label.config(text="Button has been")


# Button
# def function to work when button clicked
def button_clicked():
    my_label["text"] = "New Text"
    some_text = input.get()
    my_label.config(text=some_text)

button = tkinter.Button(text="click me", command=button_clicked)
button.pack()

    
# Entry
input = tkinter.Entry()
input.pack()










window.mainloop()
