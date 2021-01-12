from plyer import notification
import requests
from bs4 import BeautifulSoup
import tkinter as tk

def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="E:\Downloads\corona virus icon.ico",
        timeout=1
    )

def geturl(url):
    r = requests.get(url)
    return r.text

def getdata():
    myHtmlData = geturl("https://www.mohfw.gov.in/")

    soup = BeautifulSoup(myHtmlData, 'html.parser')

    my_div = soup.find('div', class_="col-xs-8 site-stats-count").find_all('strong', class_="mob-hide")

    flag = 0
    count = 0

    text = ""
    value = ""

    res=""
    for i in my_div:
        count += 1
        if not flag:
            text = (i.get_text())
            flag = 1
        else:
            value = (i.get_text())
            flag = 0
        if count % 2 == 0:
            res+=(text + " : " + value+" cases updated")+"\n"
            notifyMe(text,value+" cases updated")
    return res

def get_gui():
    root = tk.Tk()
    root.geometry("700x450")
    root.title("Covid-19 Cases Notifier")
    root.configure(background='white')
    f = ("Times New Roman", 20, "bold")

    imgae_source=tk.PhotoImage(file="E:\Downloads\corona virus.png")
    image_label=tk.Label(root,image=imgae_source)
    image_label.pack()

    get_label = tk.Label(root, text=getdata(), font=f, bg="white")
    get_label.pack()

    refresh=tk.Button(root,text="REFRESH",font=f)
    refresh.pack()

    root.mainloop()

def refresh():
    data=getdata()
    get_label['text']=data

if __name__ == '__main__':
    getdata()
    get_gui()

