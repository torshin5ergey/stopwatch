# Fullscreen stopwatch program with GUI
# using Tkinter and Time libraries

# importing the required libraries
from tkinter import *
import time, darkdetect

# Create variables

# Main digits font
app_font_main = 'Calibri 200 bold'
# Miliseconds digits font
app_font_additional = 'Calibri 70 bold'
# Microtext font
app_font_text = 'Calibri 10'
# Buttons font
app_font_buttons = 'Calibri 36'

# is_run stores two bool values (is timer started, is timer paused)
is_run = [False, True]
start_time = 0
diff_time = 0
cur_time = 0
min, sec, msec = 0, 0, 0

# Start stopwatch
def start():
    global start_time, diff_time
    global is_run
    if is_run[1]:
        diff_time = 0
    start_time = time.time()
    is_run[0],is_run[1] = True, False
    update()
    # Switch "Start" to "Pause"
    btn_start.grid_forget()
    btn_pause.grid(row=0, column=0)
    btn_reset.configure(state=NORMAL)

# Pause stopwatch
def pause():
    global is_run, diff_time, cur_time
    diff_time = cur_time
    is_run[0] = False
    root.after_cancel(update)
    # Switch "Pause" to "Start"
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
    # Switch "Pause" to "Start" if it needs
    if is_run[0]:
        btn_pause.grid_forget()
        btn_start.grid(row=0, column=0)
    btn_reset.configure(state=DISABLED)
    is_run[0], is_run[1] = False, True

# Update stopwatch
def update():
    global min, sec, msec, start_time, cur_time
    if is_run[0]:
        cur_time = time.time() - start_time + diff_time
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
    # Create string value for min, sec and ms
    return '%02d' % min, '%02d' % sec, '%02d' % msec

# App fonts and background color
def app_appearance():
    global app_bg, microtext_fg, maintext_fg
    # Detect Dark appearance in system
    if darkdetect.theme() == 'Dark':
        app_bg = '#252525'
        microtext_fg = '#555555' 
        maintext_fg = '#DADADA'
    else:
        app_bg = '#F2F4F3'
        microtext_fg = '#C5C5C5'
        maintext_fg = '#080808'
    root.configure(bg=app_bg)

# Create 'root' app window
root = Tk()
root.title('Stopwatch')
screen_width = root.winfo_screenwidth() - 100
screen_height = root.winfo_screenheight() - 100
root.geometry("%dx%d+%d+%d" % (screen_width, screen_height, 0, 0))
root.minsize(800, 600)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.iconbitmap('stopwatch.ico')

# Set window appearance
app_appearance()

frame_main = Frame(root, bg=app_bg)
frame_main.grid(row=0, column=0)

lbl_text_min = Label(frame_main,
                    text='minutes',
                    font=app_font_text,
                    bg=app_bg,
                    fg=microtext_fg)
lbl_text_min.grid(row=0, column=0, sticky=E, padx=(0, 50))

lbl_text_sec = Label(frame_main,
                    text='seconds',
                    font=app_font_text,
                    bg=app_bg,
                    fg=microtext_fg)
lbl_text_sec.grid(row=0, column=1, sticky=E, padx=(0, 50))

lbl_text_ms = Label(frame_main,
                    text='miliseconds',
                    font=app_font_text,
                    bg=app_bg,
                    fg=microtext_fg)
lbl_text_ms.grid(row=0, column=2, sticky=E, padx=(0, 5))

lbl_stopwatch_min = Label(frame_main,
                    text='00',
                    font=app_font_main,
                    bg=app_bg,
                    fg=maintext_fg)
lbl_stopwatch_min.grid(row=1, column=0, padx=(0,30))

lbl_stopwatch_sec = Label(frame_main,
                    text='00',
                    font=app_font_main,
                    bg=app_bg,
                    fg=maintext_fg)
lbl_stopwatch_sec.grid(row=1, column=1, pady=0, padx=(0,30))

lbl_stopwatch_ms = Label(frame_main,
                        text='00',
                        font=app_font_additional,
                        bg=app_bg,
                        fg=maintext_fg)
lbl_stopwatch_ms.grid(row=1, column=2, pady=(0, 70))

frame_btns = Frame(frame_main, bg=app_bg)
frame_btns.grid(row=2, column=0, columnspan=3, pady=(50,0))
btn_start = Button(frame_btns,
                text='Start',
                command=start,
                font=app_font_buttons,
                bg=app_bg,
                fg=maintext_fg,
                width=7,
                activebackground='#505050',
                activeforeground=maintext_fg)
btn_start.grid(row=0, column=0)

btn_pause = Button(frame_btns,
                text='Pause',
                command=pause,
                font=app_font_buttons,
                bg=app_bg,
                fg=maintext_fg,
                width=7,
                state=NORMAL,
                activebackground='#505050',
                activeforeground=maintext_fg)

btn_reset = Button(frame_btns,
                text='Reset',
                command=reset,
                font=app_font_buttons,
                bg=app_bg,
                fg=maintext_fg,
                width=7,
                state=DISABLED,
                activebackground='#282828',
                activeforeground=maintext_fg)
btn_reset.grid(row=0, column=1, padx=50)

root.mainloop()