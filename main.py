from tkinter import *
import math
from tkinter import messagebox  


# ---------------------------- CONSTANTS ------------------------------- #
# Define color constants and other UI-related constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# Time durations in minutes (can be adjusted for real use)
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Global variables to track repetitions and the timer reference
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Resets the timer to the initial state and clears the check marks."""
    window.after_cancel(timer)  # Cancel any scheduled countdowns
    canvas.itemconfig(timer_text, text="00:00")  # Reset timer display
    title_label.config(text="Timer")  # Reset title
    check_marks.config(text="")  # Clear checkmarks
    global reps
    reps = 0  # Reset repetition counter


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Starts the timer based on the current repetition cycle."""
    messagebox.askokcancel(title="FYI", message=f"Work time {WORK_MIN} mins\nShort Break {SHORT_BREAK_MIN} mins\nLong Break {LONG_BREAK_MIN} mins\n")
    global reps
    reps += 1

    # Convert minutes to seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Determine which session to start based on repetition count
    if reps % 8 == 0:
        # Every 8th rep is a long break
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)

    elif reps % 2 == 0:
        # Even reps (but not 8th) are short breaks
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)


    else:
        # Odd reps are work sessions
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Counts down from the specified time and updates the UI every second."""
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # Update timer display
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        # Schedule the countdown to continue after 1 second
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # When countdown finishes, start the next session
        start_timer()

        # Update the check marks after each work session
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- GET DROPDOWN SELECTION ------------------------------- #
def get_work_min(*args):
    global WORK_MIN
    selected = dropdown_var.get()
    WORK_MIN = int(selected)
    print(f"WORK_MIN = {selected}")

def get_short_min(*args):
    global SHORT_BREAK_MIN
    selected = dropdown_var2.get()
    SHORT_BREAK_MIN = int(selected)
    print(f"SHORT_BREAK_MIN = {selected}")

def get_long_min(*args):
    global LONG_BREAK_MIN
    selected = dropdown_var3.get()
    LONG_BREAK_MIN = int(selected)
    print(f"LONG_BREAK_MIN = {selected}")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# Timer canvas with tomato image and time display
# highlightthickness=0 eliminates the white border around the image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)


timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

# --- Dropdown Menu --- #

dropdown_var = StringVar(value="Work Time")
dropdown_var.trace_add("write", get_work_min)  # Automatically call when value changes

dropdown_var2 = StringVar(value="Short Break Time")
dropdown_var2.trace_add("write", get_short_min)  # Automatically call when value changes


dropdown_var3 = StringVar(value="Long Break Time")
dropdown_var3.trace_add("write", get_long_min)  # Automatically call when value changes

options = [1]
for i in range(5, 65, 5):
  options.append(i)

dropdown_work = OptionMenu(window, dropdown_var, *options)
dropdown_work.grid(column=0, row=4)

dropdown_short = OptionMenu(window, dropdown_var2, *options)
dropdown_short.grid(column=1, row=4)

dropdown_long = OptionMenu(window, dropdown_var3, *options)
dropdown_long.grid(column=2, row=4)


window.mainloop()
