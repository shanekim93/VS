from tkinter import *

win = Tk() 
win.geometry("300x100")
win.option_add("*Font", "궁서 20")

ent = Entry(win)
ent.pack()

def lotto_p():
    import requests
    from bs4 import BeautifulSoup
    n = ent.get()
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(n)
    req = requests.get(url)
    suop = BeautifulSoup(req.text, "html.parser")
    txt = suop.find("div", attrs = {"class", "win_result"}).get_text()
    num_list = txt.split("\n")[7:13]
    bonus = txt.split("\n")[-4]
    print("당첨번호")
    print(num_list)
    print("보너스 번호")
    print(bonus)



btn = Button(win)
btn.config(text="로또 당첨번호 확인")
btn.pack()
btn.config(command = lotto_p)

win.mainloop() #창 실행


