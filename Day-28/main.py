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
reps=0
time=None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(time)
    #timer_text 00:00
    #title_label "Timer"
    # reset check_marks
    timer_text.config(text="Timer")
    canvas.itemconfig(timer,text="00:00")
    check_mark.config(text="")
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec= LONG_BREAK_MIN*60


    if reps%8 == 0:
        count_down(long_break_sec)
        timer_text.config(text="Break",fg=RED)

    elif reps %2==0:
        count_down(short_break_sec)
        timer_text.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        timer_text.config(text="Work",fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #Even driven (check every time)
def count_down(count):

    count_min =math.floor(count /60)
    count_sec = count % 60

    if count_sec ==0:# using the dynamic typing to change from int to str and use the str
        count_sec="00"

    if int(count_sec) <=9 and int(count_sec) >0:
        count_sec=f"0{count_sec}"


    canvas.itemconfig(timer,text=f"{count_min}:{count_sec}")
    if count>0:
        global time
        time=window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark = ""
        work_session =math.floor(reps/2)
        for _ in range(work_session):
            mark+="✔"
        check_mark.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()# open a window
window.config(padx=100,pady=50,bg=YELLOW) #give more space and color
window.title("Pomodoro timer") # give a title


canvas=Canvas(width=220,height=240,bg=YELLOW,highlightthickness=0) # a place to put things , color , remove the border
tomato_pic=PhotoImage(file="tomato.png") #create an image and save it
canvas.create_image(100,112,image=tomato_pic)# put the image into the canvas
timer=canvas.create_text(100,130,text="00:00",font=(FONT_NAME,35,"bold"),fill="white")
canvas.grid(column=2,row=2)

timer_text=Label(text="Timer",font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW)
timer_text.grid(column=2,row=0)

start_button=Button(text="Start",command=start_timer)
start_button.grid(column=0,row=3)

reset_button=Button(text="Reset",command=reset_timer)
reset_button.grid(column=3,row=3)

check_mark=Label(fg=GREEN,font=(FONT_NAME,15,"bold"),bg=YELLOW)
check_mark.grid(column=2,row=4)

window.mainloop()
