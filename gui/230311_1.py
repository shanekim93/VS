from tkinter import *
from datetime import datetime

win = Tk()
win.geometry("300x100")
win.title("What time?")
win.option_add("*Font","궁서 20")

def what_time():
    print(datetime.now())

def alert():
    print("버튼이 눌림")

btn = Button(win)
btn.config(text = "현재 시각")
btn.config(width = 10, height = 2)
btn.config(command = what_time)

btn.pack()

win.mainloop()

from datetime import datetime
print(datetime.now())



