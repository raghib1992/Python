# download tkinter
# sudo apt-get install python3-tk

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def timer_reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    title_label.config(text="TIMER", fg=GREEN)
    check_mark.config()
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
# Start timer mechanism
def start_timer():
    global reps
    work_sec = WORK_MIN * 1
    short_break_sec = SHORT_BREAK_MIN * 1
    long_break_min = LONG_BREAK_MIN * 1

    reps += 1
    TEXT = "✓"

    match reps:
        case 1 | 3 | 5 | 7:
            count_down(work_sec)
            title_label.config(text="Work", fg=GREEN)
            for _ in range(math.floor(reps/2)):
                TEXT += "✓"
            check_mark.config(text=TEXT)

        case 2 | 4 | 6:
            count_down(short_break_sec)
            title_label.config(text="Break", fg=PINK)
        case 8 :
            count_down(long_break_min)
            title_label.config(text="Break", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# count down mechanism using after argument which create events after mention msec
def count_down(count):
    global timer

    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# Create Window using tkinter library
window = Tk()

# Title of window
window.title("Pomodoro")
# resize the window
# Add background colour, get form colourhunt websites using argumnet bg
window.config(padx=100, pady=50, bg=YELLOW)


# Add label on Screen
title_label = Label(text="Timer", fg=GREEN,bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)


# Show image on window by using canvas class
# change background colour of canvas to match with window backgroun use bg argument
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Show images on canvas
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# Add text on image to show time
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# SHow canvas on window using grid
canvas.grid(column=1, row=1)




# Add start and reset button
start_button = Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

stop_button = Button(text="stop", highlightthickness=0, command=timer_reset)
stop_button.grid(column=2, row=2)

# Add checkmark
# TEXT = "✓"
check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35,"bold"))
check_mark.grid(column=1, row=3)


# Either we can use pack or grid to show canvas on window                 
# canvas.pack()



window.mainloop()










