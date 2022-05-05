from tkinter import *  # be aware of bad practice importing *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

checkmark = '✓'
repetition = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """stops the time, reset timer_text, title_label, checkmark_label"""
    global checkmark
    global repetition
    canvas.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer', fg=GREEN)
    checkmark_label.config(text='')
    checkmark = ''
    repetition = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    """select work, break or long break phase based on repetition number"""
    global repetition
    repetition += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if repetition % 8 == 0:     # long break on 8 rep
        count_down(long_break_sec)
        title_label.config(text='break', fg=RED)
    elif repetition % 2 == 0:   # short break on 2/4/6 rep
        count_down(short_break_sec)
        title_label.config(text='break', fg=PINK)
    else:                       # work time on 1/3/5/7 rep
        count_down(work_sec)
        title_label.config(text='Work!', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    """countdown, display proper time format"""
    global repetition
    global checkmark
    global timer

    count_min = count // 60  # floor division returns whole integer
    count_sec = count % 60  # modulo operator returns remainder
    if count_sec < 10:
        count_sec = f'0{count_sec}'  # display seconds as 0:00

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')

    if count > 0:  # don't count in to negatives
        timer = canvas.after(1000, count_down, count-1)   # after each 1000ms call self
    elif count == 0:   # when count hits zero call start_timer()
        start_timer()  # start_timer() will take next phase (work or break)
        if repetition % 2 == 0:  # add checkmark after every work phase
            checkmark_label.config(text=checkmark)
            checkmark += checkmark


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

# canvas widget, holds the image and text
tomato_img = PhotoImage(file='tomato.png')
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(column=1, row=1)

# labels
title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, 'bold'))
title_label.grid(column=1, row=0)

checkmark_label = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
checkmark_label.grid(column=1, row=3)

# buttons
start_button = Button(text='Start', command=start_timer, width=3, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=reset_timer, width=3, highlightthickness=0)
reset_button.grid(column=2, row=2)



window.mainloop()

#modules: tkinter,
#tags: pomodoro, gui, after(), after_cancel(), canvas
