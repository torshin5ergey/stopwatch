from tkinter import *

is_run = False
minutes, seconds, miliseconds = 0, 0, 0

app_font1 = 'Arial 52 bold'
app_font2 = 'Arial 24'
app_bg = '#F2F4F3'

def map_values(x, in_min, in_max, out_min, out_max):
    return (x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min

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
    global is_run, minutes, seconds, miliseconds
    lbl_stopwatch.after_cancel(update)
    minutes, seconds, miliseconds = 0, 0, 0
    lbl_stopwatch.configure(text='00:00:00')
    if is_run:
        btn_pause.grid_forget()
        btn_start.grid(row=1, column=0, pady=10)
    btn_reset.configure(state=DISABLED)
    is_run = False
    canvas_idle_state()


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

        update_canvas()

def canvas_idle_state():
    global arc_miliseconds,arc_seconds,arc_minutes,circle_toplevel
    cnv.delete("all")
    arc_miliseconds = cnv.create_arc(10,10,290,290, start=90, extent=-359.9,
                                outline='#D6BFED', fill='#D6BFED')
    arc_seconds = cnv.create_arc(15,15,285,285, start=90, extent=-359.9,
                                outline='#A06CD5', fill='#A06CD5')
    arc_minutes = cnv.create_arc(20,20,280,280, start=90, extent=-359.9,
                                outline='#6247AA', fill='#6247AA')
    circle_toplevel = cnv.create_oval(30,30,270,270, outline=app_bg, fill=app_bg)
    cnv.create_window(150,150, window=lbl_stopwatch)

def update_canvas():
    global arc_miliseconds,arc_seconds,arc_minutes,circle_toplevel,miliseconds
    cnv.delete("all")
    #print(miliseconds/1000)
    ms_end = map_values(miliseconds, 0, 1000, 0, -359)
    s_end = map_values(seconds, 0, 60, 0, -359) - miliseconds/180
    m_end = map_values(minutes, 0, 60, 0, -359) - seconds/10
    arc_miliseconds = cnv.create_arc(10,10,290,290, start=90, extent=ms_end,
                                outline='#D6BFED', fill='#D6BFED')
    arc_seconds = cnv.create_arc(15,15,285,285, start=90, extent=s_end,
                                outline='#A06CD5', fill='#A06CD5')
    arc_minutes = cnv.create_arc(20,20,280,280, start=90, extent=m_end,
                                outline='#6247AA', fill='#6247AA')
    circle_toplevel = cnv.create_oval(30,30,270,270, outline=app_bg, fill=app_bg)
    cnv.create_window(150,150, window=lbl_stopwatch)

root = Tk()
root.title('Stopwatch')
root.configure(bg=app_bg)

#Canvas
frame_canvas = Frame(root,bg=app_bg)
frame_canvas.grid(row=0, column=0, padx=30, pady=30)
cnv = Canvas(frame_canvas, bg=app_bg, width=300, height=300,highlightbackground=app_bg)
#animated seconds circle GUI
arc_miliseconds = cnv.create_arc(10,10,290,290, start=90, extent=-359.9,
                                outline='#D6BFED', fill='#D6BFED')
arc_seconds = cnv.create_arc(15,15,285,285, start=90, extent=-359.9,
                                outline='#A06CD5', fill='#A06CD5')
arc_minutes = cnv.create_arc(20,20,280,280, start=90, extent=-359.9,
                                outline='#6247AA', fill='#6247AA')
circle_toplevel = cnv.create_oval(30,30,270,270, outline=app_bg, fill=app_bg)
cnv.grid(row=0, column=0, pady=(0,50))

frame_buttons = Frame(root,bg=app_bg)
frame_buttons.grid(row=1, column=0, padx=30, pady=(0,30))

lbl_stopwatch = Label(cnv,
                    text='00:00:00',
                    font=app_font1,
                    bg=app_bg)
lbl_stopwatch.grid(row=0, column=0)
cnv.create_window(150,150, window=lbl_stopwatch)

btn_start = Button(frame_buttons,
                text='Start',
                command=start,
                font=app_font2,
                bg=app_bg,
                width=7)
btn_start.grid(row=1, column=0, pady=10)

btn_pause = Button(frame_buttons,
                text='Pause',
                command=pause,
                font=app_font2,
                bg=app_bg,
                width=7,
                state=NORMAL)

btn_reset = Button(frame_buttons,
                text='Reset',
                command=reset,
                font=app_font2,
                bg=app_bg,
                width=7,
                state=DISABLED)
btn_reset.grid(row=1, column=1, pady=10, padx=(15,0))

root.mainloop()