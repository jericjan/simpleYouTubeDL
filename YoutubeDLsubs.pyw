# yeet this a comment
from tkinter import *
import subprocess
import tkinter.scrolledtext as tkst

win = Tk()

win.title("YT DL w/ subs by Jeric")
win.geometry("360x250")
win.resizable(False, False)


def copy():
    win2 = Toplevel(win)
    win2.title("List of format codes")
    win2.geometry("519x538")

    temp = OneUrl.get()
    p = subprocess.Popen(["youtube-dl.exe", "-F", temp], shell=True, stdout=subprocess.PIPE)
    output = p.stdout.read()
    logg = Label(win2, text=output, anchor=W, justify=LEFT)
    logg.grid(row=0, column=0, sticky=W)
    # print("youtube-dl.exe", "-F", temp)
    # subprocess.call('color 0a', shell=True)
    # subprocess.call(["youtube-dl.exe", "-F", temp])


def number():
    win3 = Toplevel(win)
    win3.title("list of subs")
    win3.geometry("450x640")
    url = OneUrl.get()
    p = subprocess.Popen(["youtube-dl.exe", "--list-subs", url], shell=True, stdout=subprocess.PIPE)
    output = p.stdout.read()
    lang_frame = Frame(
        master=win3,
        bg='#808000',
    )
    lang_frame.grid(row=0, column=0, sticky=W)

    textscrollbox = tkst.ScrolledText(
        master=lang_frame,
        undo=True,
        width="53",
        height="40"

    )

    textscrollbox.pack(side=LEFT, expand=True, fill='both')
    textscrollbox.insert(INSERT, output)


def last():
    lang = ThreeUrl.get()
    temp = OneUrl.get()
    num = TwoUrl.get()
    subprocess.call(["youtube-dl.exe", "--sub-lang", lang, "--write-sub", "--convert-subs", "srt", "-f", num, temp])
    print("DONE, BOIIIIII!!!")
    donn = Label(win, text="DONE!!!", bg="black", fg="white")
    donn.grid(row=9, column=1, sticky=W)


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

threeLabel = Label(win, text="3. Choose your language format (do not choose automatic)")
threeLabel.grid(row=6, column=0, sticky=W)
ThreeUrl = Entry(win, width=10)
ThreeUrl.grid(row=7, column=0, sticky=W)
threeButton = Button(win, text="OKAY!!!", command=last)
threeButton.grid(row=8, column=0, sticky=W)

threeLabel = Label(win, text="El Psy Kongroo...")
threeLabel.grid(row=9, column=0, sticky=W)
exitButton = Button(win, text="EXIT", command=closeapp)
exitButton.grid(row=10, column=1, sticky=W)
win.mainloop()
