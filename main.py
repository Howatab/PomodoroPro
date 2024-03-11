import ttkbootstrap as ttk
import tkinter
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT=('Montserrat', 35, 'bold')
BLACK_SQUARE = "■"
reps = 0
running = False
countdown_id = None
state = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def Start_button_click():
    if start_button_var.get() == False:
        reset_button.state(['!disabled'])
        start_button.config(text="Running")
        start_button_var.set(True)
        start_button.configure(style='CircularButtonActive.TButton')
        start_button.state(['disabled'])
        start_timer()
        
    else : 
        start_button.config(text="Start")
        start_button_var.set(False)
        start_button.configure(style='CircularButton.TButton',)

def Reset_button_click():
    start_button.state(['!disabled'])
    start_button.config(text="Start")
    start_button_var.set(False)
    start_button.configure(style='CircularButton.TButton',)
    reset_button.state(['disabled'])
    reset()
    
def cancel_all_after(window):
    scheduled_events = window.after_info()
    for event_id in scheduled_events:
        # Cancel each scheduled event
        window.after_cancel(event_id)

def reset():
    global running,reps
    canvas.itemconfig(timer_text, text="25:00")
    running = False
    ticks.set("□ □ □ □")
    running = False
    reps = 0
    state = ""
    

        

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global running,reps,state
    
    if start_button_var.get():
        running = True
        print(reps,state)
        reps += 1
        if reps%8 == 0: 
            state = 'break'
            ticks.set("□ □ □ □")
            countdown(LONG_BREAK_MIN*60)
            
        elif reps%2 == 0:
            state = 'break'
            countdown(SHORT_BREAK_MIN*60)
        
        else:
            state = 'work'
            countdown(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    minutes = count // 60
    seconds = count % 60
    global running,state
    if running:
        canvas.itemconfig(timer_text,text = f'{minutes:02}:{seconds:02}')
    print(count, reps,state)
    if count>0 and running:
         window.after(1000,countdown,count - 1)
    else:
        if state == 'work' and running:
            current_ticks = ticks.get()
            new_ticks = current_ticks.replace("□", BLACK_SQUARE, 1)
            ticks.set(new_ticks)
        window.after(1000,start_timer)
        
        


# ---------------------------- UI SETUP ------------------------------- #
window = ttk.Window(themename="darkly")
window.geometry('500x600')

s = ttk.Style()
s.configure('CircularButton.TButton', padding=(25, 10), borderwidth=0, relief="flat", background="green")
s.configure('CircularButtonActive.TButton', padding=(25, 10), borderwidth=0, relief="flat", background="red")

label1 = ttk.Label(text="Pomodoro", master=window , font=('Montserrat', 35, 'bold'))
label1.config(foreground='white')
label1.grid(column=1,row=0)

canvas = ttk.Canvas(width=500 , height= 400)
image = ttk.PhotoImage(file="tomato.png")
canvas.create_image(250,180,image= image)
canvas.scale("all", 250, 180, 15, 15)
timer_text = canvas.create_text(250,200,text="25:00" , fill= 'white' , font= FONT)
canvas.grid(column=1,row=1)

frame = ttk.Frame(master=window)
frame.grid(column=1,row=2)

start_button_var = ttk.BooleanVar(value=False)
start_button = ttk.Button(text= " Start ", master= frame,style='CircularButton.TButton' ,command= Start_button_click)
start_button.grid(column=1,row=2)
reset_button = ttk.Button(text= " \u21BA" , master= frame,command=Reset_button_click )
reset_button.configure(style='CircularButtonActive.TButton',padding=(10, 10))
reset_button.grid(column=2,row=2,pady=20,padx=20)


ticks = ttk.StringVar(value="□ □ □ □")
label = ttk.Label(text="",master=window,foreground='green',font=('calibri',15,'normal'),textvariable=ticks)
label.grid(column=1,row=3)


window.mainloop()