#yeet this a comment
from tkinter import *
import subprocess

win = Tk()

win.title("YT DL w/ subs by Jeric")
win.geometry("350x250")
win.resizable(False, False)

def copy():
    temp = OneUrl.get()
    #print("youtube-dl.exe", "-F", temp)
    subprocess.call(["youtube-dl.exe", "-F", temp])

def number():
    temp = OneUrl.get()
    
    subprocess.call(["youtube-dl.exe", "--list-subs", temp])
    #print("youtube-dl.exe", "-f", num, temp)
    
    #print("DONE, BOIIIIII!!!")

def last():
    lang = ThreeUrl.get()
    temp = OneUrl.get()
    num = TwoUrl.get()
    subprocess.call(["youtube-dl.exe", "--sub-lang", lang, "--write-sub", "--convert-subs", "srt", "-f", num, temp])
    print("DONE, BOIIIIII!!!")
    
def closeapp():
    sys.exit()

oneLabel = Label(win, text="1. Put your link here")
oneLabel.grid(row=0, column=0, sticky=W)
OneUrl = Entry(win, width=50)
OneUrl.grid(row=1, column=0, sticky=W)
oneButton = Button(win, text="OKAY!", command = copy)
oneButton.grid(row=2, column=0, sticky=W)
twoLabel = Label(win, text= "2. choose format code ex. (video+audio) (316+251)")
twoLabel.grid(row=3, column=0, sticky=W)
TwoUrl = Entry(win, width=10)
TwoUrl.grid(row=4, column=0, sticky=W)
twoButton = Button(win, text="OKAY!!", command = number)
twoButton.grid(row=5, column=0, sticky=W)

threeLabel = Label(win, text= "3. Choose your language format")
threeLabel.grid(row=6, column=0, sticky=W)
ThreeUrl = Entry(win, width=10)
ThreeUrl.grid(row=7, column=0, sticky=W)
threeButton = Button(win, text="OKAY!!!", command = last)
threeButton.grid(row=8, column=0, sticky=W)

threeLabel = Label(win, text= "El Psy Kongroo...")
threeLabel.grid(row=9, column=0,sticky=W)
exitButton = Button(win, text="EXIT", command = closeapp)
exitButton.grid(row=10, column=1, sticky=W)
win.mainloop()
