from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
# window.geometry("300x300")
window.config(padx=100,pady=50, bg=YELLOW)


# Label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 34, "bold"))
timer_label.grid(row=0,column=1)

check_label = Label(text='✓', bg=YELLOW, fg=GREEN, font=(FONT_NAME ,34,"bold") )
check_label.grid(row=2,column=1)

# Button
def start():
    print("start")
    
def stop():
    print("stop")
start_button = Button(text="start",command=start)
start_button.grid(row=2,column=0)

stop_button = Button(text="stop",command=stop)
stop_button.grid(row=2,column=2)

# Create canvas
canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(102,112,image=tomato_image)
canvas.create_text(102,130,text="00:00",font=(FONT_NAME,35,"bold"),fill="white")
canvas.grid(row=1,column=1)





window.mainloop()