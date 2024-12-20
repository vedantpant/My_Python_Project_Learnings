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
def reset_timer():
    window.after_cancel(timer)
    # timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1

    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED, font=(FONT_NAME, 50), bg=YELLOW, highlightthickness=0)
        count_down(long_break_sec)
    if reps % 2 == 0:
        timer_label.config(text="Short Break", fg=PINK, font=(FONT_NAME, 50), bg=YELLOW, highlightthickness=0)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW, highlightthickness=0)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds == 0:
        count_seconds = "00"
    elif count_seconds < 10:
        count_seconds = "0" + str(count_seconds)

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)


# timer label
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW, highlightthickness=0)
timer_label.config()
timer_label.grid(column=1, row=0)

# start button
start = Button(text="Start", bg="white", command=start_timer, font=(FONT_NAME, 8, "bold"), highlightthickness=0)
start.grid(row=2, column=0)

# reset button
reset = Button(text="Reset", bg="white", font=(FONT_NAME, 8, "bold"), highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)

# checkbox
checkmark = Label(fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 10, "bold"))
checkmark.config(pady=5)
checkmark.grid(row=3, column=1)

window.mainloop()
