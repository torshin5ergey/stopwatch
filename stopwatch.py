from tkinter import *

def start():
    global is_run
    is_run = True
    update()
    btn_start.grid_forget()
    btn_pause.grid(row=1, column=0, pady=10)
    btn_reset.configure(state=NORMAL)
    #btn_start.configure(state=tk.DISABLED)
    #btn_reset.configure(state=tk.NORMAL)

def pause():
    global is_run
    is_run = False
    lbl_stopwatch.after_cancel(update)
    btn_pause.grid_forget()
    btn_start.grid(row=1, column=0, pady=10)

def reset():
    global is_run, miliseconds
    lbl_stopwatch.after_cancel(update)
    miliseconds = 0
    lbl_stopwatch.configure(text='00:00:00')
    if is_run:
        btn_pause.grid_forget()
        btn_start.grid(row=1, column=0, pady=10)
    btn_reset.configure(state=DISABLED)
    is_run = False


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
        str_miliseconds = '0' + str(int(miliseconds/10)) if (miliseconds/10 < 10) else str(int(miliseconds/10))
        str_seconds = '0' + str(seconds) if (seconds < 10) else str(seconds)
        str_minutes = '0' + str(minutes) if (minutes < 10) else str(minutes)
        new_lbl_text = str_minutes + ':' + str_seconds + ':' + str_miliseconds
        lbl_stopwatch.configure(text=new_lbl_text)
        miliseconds += 1
        lbl_stopwatch.after(1, update)

is_run = False
minutes, seconds, miliseconds = 0, 0, 0

app_font1 = 'Verdana 52 bold'
app_font2 = 'Verdana 24'

root = Tk()
root.title('Stopwatch')

frame_time = Frame(root)
frame_time.grid(row=0, column=0)
frame_buttons = Frame(root)
frame_buttons.grid(row=1, column=0)

lbl_stopwatch = Label(frame_time,
                    text='00:00:00',
                    font=app_font1)
lbl_stopwatch.grid(row=0, column=0)

btn_start = Button(frame_buttons,
                text='Start',
                command=start,
                font=app_font2,
                fg='blue',
                width=7)
btn_start.grid(row=1, column=0, pady=10)

btn_pause = Button(frame_buttons,
                text='Pause',
                command=pause,
                font=app_font2,
                width=7,
                state=NORMAL)

btn_reset = Button(frame_buttons,
                text='Reset',
                command=reset,
                font=app_font2,
                foreground='red',
                width=7,
                state=DISABLED)
btn_reset.grid(row=1, column=1, pady=10, padx=(15,0))

root.mainloop()