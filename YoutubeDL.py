# yeet this a comment
from tkinter import *
import subprocess

win = Tk()

win.title("YOUTUBE DOWNLOADER by Jeric")
win.geometry("350x160")


# win.resizable(False, True)


def copy():
    win2 = Toplevel(win)
    win2.geometry("519x538")
    temp = OneUrl.get()
    # print("youtube-dl.exe", "-F", temp)
    p = subprocess.Popen(["youtube-dl.exe", "-F", temp], shell=True, stdout=subprocess.PIPE)
    output = p.stdout.read()
    logg = Label(win2, text=output, anchor=W, justify=LEFT)
    logg.grid(row=0, column=0, sticky=W)
    # subprocess.call(["youtube-dl.exe", "-F", temp])


def number():
    temp = OneUrl.get()
    num = TwoUrl.get()
    # p = subprocess.Popen(["youtube-dl.exe", "-f", num, temp], shell=True, stdout=subprocess.PIPE)
    # output = p.stdout.read()
    # print("youtube-dl.exe", "-F", num, temp)
    subprocess.call(["youtube-dl.exe", "-f", num, temp])
    print("DONE, BOIIIIII!!!")
    donn = Label(win, text="DONE!!!", bg="black", fg="white")
    donn.grid(row=5, column=1, sticky=W)


def closeapp():
    sys.exit()


oneLabel = Label(win, text="1. Put your link here")
oneLabel.grid(row=0, column=0, sticky=W)
OneUrl = Entry(win, width=50)
OneUrl.grid(row=1, column=0, sticky=W)
oneButton = Button(win, text="OKAY!", command=copy)
oneButton.grid(row=2, column=0, sticky=W)
twoLabel = Label(win, text="2. choose format code ex. (video+audio) (316+251)")
twoLabel.grid(row=3, column=0, sticky=W)
TwoUrl = Entry(win, width=10)
TwoUrl.grid(row=4, column=0, sticky=W)
twoButton = Button(win, text="OKAY!!", command=number)
twoButton.grid(row=5, column=0, sticky=W)
threeLabel = Label(win, text="El Psy Kongroo...")
threeLabel.grid(row=6, column=0, sticky=W)
exitButton = Button(win, text="EXIT", command=closeapp)
exitButton.grid(row=6, column=1, sticky=W)

win.mainloop()
