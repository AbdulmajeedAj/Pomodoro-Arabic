from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUE = "#52b8f7"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_mark_count = ""
timer = None
time_passed = 0
SECOND = 1000
with open("data.txt", "r") as r_file:
    HISTORY_PASSED_TIME = int(r_file.readline())

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps, HISTORY_PASSED_TIME, time_passed
    # Creating a board that contains what have been done
    HISTORY_PASSED_TIME += time_passed
    score_window = Toplevel(pady=20, padx=20)
    score_window.config(pady=50, padx=50)
    score_label = Label(score_window, text=f"time passed in this session ➡️ {time_passed // 60} minutes and {time_passed % 60} seconds ",
                        font=(FONT_NAME, 30, "bold"))
    history_label = Label(score_window, text=f"time passed in this session ➡️ {HISTORY_PASSED_TIME // 60} minutes"
                                             f" and {HISTORY_PASSED_TIME % 60} seconds", font=(FONT_NAME, 30, "bold"))
    score_label.pack()
    history_label.pack()

    # Resetting the window
    window.after_cancel(timer)
    timer_title.config(text="مؤقت", font=(FONT_NAME, 50, "bold"), fg=RED, bg=YELLOW)
    check_mark.config(text="", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
    canvas.itemconfig(timer_text, text=f"{english_to_arabic(WORK_MIN)}:٠٠")
    reps = 0

    # adding last session time to the history time - in condition if SECOND is equal to the regular second duration -
    if SECOND == 1000:
        with open("data.txt", "w") as w_file:
            w_file.write(str(HISTORY_PASSED_TIME))
            time_passed = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def add_check_mark():
    global check_mark_count
    check_mark_count += "✔"
    if len(check_mark_count) > 8:
        check_mark.config(text=f"{len(check_mark_count)}: ✔")
    else:
        check_mark.config(text=check_mark_count)


def start_timer():
    global reps
    reps += 1
    if reps % 2 == 1:
        count_down(60 * WORK_MIN)
        timer_title.config(text="شغل", fg=RED)

    elif reps % 8 == 0:
        count_down(60 * LONG_BREAK_MIN)
        timer_title.config(text="راحة مطولة", fg=BLUE)
        add_check_mark()

    else:
        count_down(60 * SHORT_BREAK_MIN)
        timer_title.config(text="راحة", fg=GREEN)
        add_check_mark()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


arabic_numbers = ["٠", "١", "٢", "٣", "٤", "٥", "٦", "٧", "٨", "٩"]


def english_to_arabic(number):
    """converting english number to arabic number 'only for two-digit number'"""
    if number > 9:
        str_number = str(number)
        number1 = arabic_numbers[int(str_number[0])]
        number2 = arabic_numbers[int(str_number[1])]
        number = number1 + number2
    else:
        number = arabic_numbers[number]

    if number in arabic_numbers:
        number = "٠" + number

    return number


def count_down(count):
    global timer, time_passed
    """counting down from argument inserted until reaches zero in arabic numbers"""

    number_in_minute = count // 60
    number_in_second = count % 60

    number_in_second = english_to_arabic(number_in_second)
    number_in_minute = english_to_arabic(number_in_minute)

    canvas.itemconfig(timer_text, text=f"{number_in_minute}:{number_in_second}")
    if count > 0:
        timer = window.after(SECOND, count_down, count - 1)
        time_passed += 1

    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #


# Window
window = Tk()
window.title("طماطم")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text=f"{english_to_arabic(WORK_MIN)}:٠٠", font=(FONT_NAME, 35, "bold"))

canvas.grid(row=2, column=2)


# Labels
timer_title = Label(text="مؤقت", font=(FONT_NAME, 50, "bold"), fg=RED, bg=YELLOW)
check_mark = Label(text="", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)

timer_title.grid(row=1, column=2)
check_mark.grid(row=4, column=2)

# Buttons
start_button = Button(text="إبدأ", bg=YELLOW, highlightbackground=YELLOW, command=start_timer)
reset_button = Button(text="إعادة", bg=YELLOW, highlightbackground=YELLOW, command=reset_timer)

start_button.grid(row=3, column=1)
reset_button.grid(row=3, column=3)

window.mainloop()

