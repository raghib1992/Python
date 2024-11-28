from tkinter import *

# Create window
window = Tk()
# window.geometry("300x300")
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

# screen and label to Enter Mile value
entry = Entry()
entry.grid(row=0,column=1)

label = Label(text="mile",font=("Arial",18,"bold"))
label.grid(row=0,column=2)

label_eq = Label(text="is equal to",font=("Arial",18,"bold"))
label_eq.grid(row=1,column=0)

entry_eq = Entry()
entry_eq.grid(row=1,column=1)

label_km = Label(text="Km",font=("Arial",18,"bold"))
label_km.grid(row=1,column=2)

# Create Button
def calculate():
    mile_input = entry.get()
    km_output = str(int(mile_input)*1.61)
    entry_eq.insert(END,string=km_output)
    
button = Button(text="calculate",command=calculate)
button.grid(row=2,column=1)

window.mainloop()