from tkinter import *
import requests #url 주소를 이용해서 html 정보 가져옴
from bs4 import BeautifulSoup

win = Tk()
win.geometry("300x200")
win.title("Lotto")

ent = Entry(win)
ent.pack()

def lotto():
    n = ent.get()
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(n)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    txt = soup.find("div", attrs = {"class", "win_result"}).get_text()
    num_list = txt.split("\n")[7:13]
    bonus = txt.split("\n")[-4]
    print("당첨번호 {}, 보너스 번호 {}".format(num_list, bonus))

btn = Button(win)
btn.config(text = "회차번호 입력")
btn.config(command = lotto)
btn.pack()

win.mainloop()

