# Fullscreen stopwatch program with GUI
# using Tkinter and Time libraries

# importing the required libraries
from tkinter import *
import time

# Create variables
# is_run stores two bool values (is timer started, is timer paused)
is_run = [False, True]
start_time = 0
min, sec, msec = 0, 0, 0

# App fonts and background color
app_font_main = 'Calibri 200 bold'
app_font_additional = 'Calibri 70 bold'
app_font_text = 'Calibri 10'
app_font_buttons = 'Calibri 36'
app_bg = '#F2F4F3'
text_fg = '#C5C5C5'

# Start stopwatch
def start():
    global start_time
    global is_run
    if is_run[1]:
        start_time = time.time()
    is_run[0],is_run[1] = True, False
    update()
    btn_start.grid_forget()
    btn_pause.grid(row=0, column=0)
    btn_reset.configure(state=NORMAL)

# Pause stopwatch
def pause():
    global is_run
    is_run[0] = False
    root.after_cancel(update)
    btn_pause.grid_forget()
    btn_start.grid(row=0, column=0)

# Reset stopwatch
def reset():
    global is_run, min, sec, msec
    root.after_cancel(update)
    min, sec, msec = 0, 0, 0
    lbl_stopwatch_min.configure(text='00')
    lbl_stopwatch_sec.configure(text='00')
    lbl_stopwatch_ms.configure(text='00')
    if is_run[0]:
        btn_pause.grid_forget()
        btn_start.grid(row=0, column=0)
    btn_reset.configure(state=DISABLED)
    is_run[0], is_run[1] = False, True

# Update stopwatch
def update():
    global min, sec, msec, start_time
    if is_run[0]:
        cur_time = time.time() - start_time
        min, sec, msec = format_time(cur_time)
        lbl_stopwatch_min.configure(text=min)
        lbl_stopwatch_sec.configure(text=sec)
        lbl_stopwatch_ms.configure(text=msec)
        # Update every 20 miliseconds
        root.after(20, update)

# Format caclucated time into min, sec, msec
def format_time(time):
    min = int(time / 60)
    sec = int(time - min * 60.0)
    msec = int((time - min * 60.0 - sec) * 100)
    # Create string valuet for min, sec and ms
    #msec = '0' + str(msec) if (msec < 10) else str(msec)
    return '%02d' % min, '%02d' % sec, '%02d' % msec

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
root.iconbitmap('stopwatch.ico')

frame_main = Frame(root, bg=app_bg)
frame_main.grid(row=0, column=0)

lbl_text_min = Label(frame_main,
                    text='minutes',
                    font=app_font_text,
                    bg=app_bg,
                    fg=text_fg)
lbl_text_min.grid(row=0, column=0, sticky=E, padx=(0, 30))

lbl_text_sec = Label(frame_main,
                    text='seconds',
                    font=app_font_text,
                    bg=app_bg,
                    fg=text_fg)
lbl_text_sec.grid(row=0, column=1, sticky=E, padx=(0, 20))

lbl_text_ms = Label(frame_main,
                    text='miliseconds',
                    font=app_font_text,
                    bg=app_bg,
                    fg=text_fg)
lbl_text_ms.grid(row=0, column=2, sticky=E, padx=(0, 5))

lbl_stopwatch_min = Label(frame_main,
                    text='00',
                    font=app_font_main,
                    bg=app_bg)
lbl_stopwatch_min.grid(row=1, column=0, padx=(0,20))

lbl_stopwatch_sec = Label(frame_main,
                    text='00',
                    font=app_font_main,
                    bg=app_bg)
lbl_stopwatch_sec.grid(row=1, column=1, pady=0)

lbl_stopwatch_ms = Label(frame_main,
                        text='00',
                        font=app_font_additional,
                        bg=app_bg)
lbl_stopwatch_ms.grid(row=1, column=2, pady=(0, 70))

frame_btns = Frame(frame_main, bg=app_bg)
frame_btns.grid(row=2, column=0, columnspan=3, pady=(50,0))
btn_start = Button(frame_btns,
                text='Start',
                command=start,
                font=app_font_buttons,
                bg=app_bg,
                width=7)
btn_start.grid(row=0, column=0)

btn_pause = Button(frame_btns,
                text='Pause',
                command=pause,
                font=app_font_buttons,
                bg=app_bg,
                width=7,
                state=NORMAL)

btn_reset = Button(frame_btns,
                text='Reset',
                command=reset,
                font=app_font_buttons,
                bg=app_bg,
                width=7,
                state=DISABLED)
btn_reset.grid(row=0, column=1, padx=50)

root.mainloop()