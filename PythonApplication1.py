import time
from tkinter import *
from tkinter import messagebox
 
 
# Create object
root = Tk()

# Define the geometry of the window
root.geometry("400x400")

#define title
root.title("Countdown timer")

# set background color
root.config(bg='#000')
  
# declaration of variables
hour=StringVar()
minute=StringVar()
second=StringVar()
  
# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")


hour_box= Entry(
	root, 
	width=3, 
	font=("Arial",25,""),
    bg = "#000",
    fg = "#fff",
    bd = 0,
	textvariable=hour
	)

hour_box.place(x=90,y=40)
  
mins_box = Entry(
	root, 
	width=3, 
	font=("Arial",25,""),
    bg = "#000",
    fg = "#fff",
    bd = 0,
	textvariable=minute)

mins_box.place(x=190,y=40)
  
sec_box = Entry(
	root, 
	width=3, 
	font=("Arial",25,""),
    bg = "#000",
    fg = "#fff",
    bd = 0,
	textvariable=second)

sec_box.place(x=290,y=40)
  
running = True 

def countdowntimer():
    try:
        # store the user input
        ctime = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        messagebox.showwarning('', 'Invalid Input!')
    while ((ctime >-1) and (running)):
         
        # divmod(firstvalue = user_input//60, secondvalue = user_input%60)
        mins,secs = divmod(ctime,60)
  
        # Converting the input entered in mins or secs to hours,
        hours=0
        if mins >60:

            hours, mins = divmod(mins, 60)
         
        # store the value up to two decimal places
        # using the format() method
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
  
        # updating the GUI window 
        root.update()
        time.sleep(1)
  
        ctime += 1

def on_start():
   global running
   running = True
   countdowntimer()

# Define a function to stop the loop
def on_stop():
   global running
   running = False
   root.update()

def reset():
    hour.set("00")
    minute.set("00")
    second.set("00")
    root.update()
 
# button widget
btn_start = Button(root, text='Start/Resume', bd='5',
             command=on_start)
btn_start.place(x = 170,y = 150)

btn_pause = Button(root, text='Pause', bd='5',
             command=on_stop)
btn_pause.place(x = 190,y = 210)

btn_reset = Button(root, text='Reset', bd='5',
             command=reset)
btn_reset.place(x = 190,y = 270)
  
root.mainloop()
