# Fullscreen stopwatch program with GUI
# using Tkinter library

# importing the required libraries
from tkinter import *
import time

# Create variables
is_run = False
minutes, seconds, miliseconds = 0, 0, 0

# App fonts and background color
app_font1 = 'Calibri 200 bold'
app_font2 = 'Calibri 36'
app_bg = '#F2F4F3'

# Re-maps a number from one range to another
def map_values(x, in_min, in_max, out_min, out_max):
    return (x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min

# Start stopwatch
def start():
    print('start')
    global is_run
    is_run = True
    update()
    btn_start.grid_forget()
    btn_pause.grid(row=1, column=0)
    btn_reset.configure(state=NORMAL)
    #btn_start.configure(state=tk.DISABLED)
    #btn_reset.configure(state=tk.NORMAL)

# Pause stopwatch
def pause():
    global is_run
    is_run = False
    lbl_stopwatch.after_cancel(update)
    btn_pause.grid_forget()
    btn_start.grid(row=1, column=0)

# Reset stopwatch
def reset():
    global is_run, minutes, seconds, miliseconds
    lbl_stopwatch.after_cancel(update)
    minutes, seconds, miliseconds = 0, 0, 0
    lbl_stopwatch.configure(text='00 00')
    lbl_stopwatch_ms.configure(text='00')
    if is_run:
        btn_pause.grid_forget()
        btn_start.grid(row=1, column=0, pady=10)
    btn_reset.configure(state=DISABLED)
    is_run = False

# Update stopwatch
def update():
    global minutes, seconds, miliseconds
    #print(running)
    if is_run:
        if miliseconds > 999:
            seconds += 1
            miliseconds = 0
        if seconds > 59:
            minutes += 1
            seconds = 0
        # Create string valuet for min, sec and ms
        str_minutes = '0' + str(minutes) if (minutes < 10) else str(minutes)
        str_seconds = '0' + str(seconds) if (seconds < 10) else str(seconds)
        str_miliseconds = '0' + str(int(miliseconds/10)) if ((int(miliseconds/10)) < 10) else str(int(miliseconds/10))
        new_lbl_text = str_minutes + ' ' + str_seconds
        lbl_stopwatch.configure(text=new_lbl_text)
        lbl_stopwatch_ms.configure(text=str_miliseconds)
        # Update every second
        #time.sleep(0.001)
        #print(miliseconds/10)
        lbl_stopwatch_ms.after(20, update)
        miliseconds += 20

# Create 'root' app window
root = Tk()
root.title('Stopwatch')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root_size = str(screen_width) + 'x' + str(screen_height)
root.geometry(root_size)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.configure(bg=app_bg)

frame_main = Frame(root, bg=app_bg)
frame_main.grid(row=0, column=0)

lbl_minutes = Label(frame_main,
                    text='')

lbl_stopwatch = Label(frame_main,
                    text='00 00',
                    font=app_font1,
                    bg=app_bg)
lbl_stopwatch.grid(row=0, column=0, pady=50)

lbl_stopwatch_ms = Label(frame_main,
                        text='00',
                        font='Calibri 70 bold',
                        bg=app_bg)
lbl_stopwatch_ms.grid(row=0, column=1, pady=(0, 70))

frame_btns = Frame(frame_main, bg=app_bg)
frame_btns.grid(row=1, column=0, columnspan=2)
btn_start = Button(frame_btns,
                text='Start',
                command=start,
                font=app_font2,
                bg=app_bg,
                width=7)
btn_start.grid(row=1, column=0)

btn_pause = Button(frame_btns,
                text='Pause',
                command=pause,
                font=app_font2,
                bg=app_bg,
                width=7,
                state=NORMAL)

btn_reset = Button(frame_btns,
                text='Reset',
                command=reset,
                font=app_font2,
                bg=app_bg,
                width=7,
                state=DISABLED)
btn_reset.grid(row=1, column=1, padx=50)

root.mainloop()