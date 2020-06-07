from tkinter import *
from tkinter import messagebox
window=Tk()

window.title('krestiki noliki')
window.geometry('300x400')
lbl=Label(window,text='Game',font=('Helvetica','15'))
lbl.grid(row=0,column=0)
lbl=Label(window,text='Player X:',font=('Helvetica','10'))
lbl.grid(row=1,column=0)
lbl=Label(window,text='Player O:',font=('Helvetica','10'))
lbl.grid(row=2,column=0)

turn = 1

#creating window
#logic
#loop


def clicked1():
    global turn
    if bt1["text"]==" ":
        if turn==1:
            turn=2
            bt1["text"]="X"
        elif turn==2:
            turn=1
            bt1["text"]="O"
        check()

def clicked2():
    global turn
    if bt2["text"]==" ":
        if turn==1:
            turn=2
            bt2["text"]="X"
        elif turn==2:
            turn=1
            bt2["text"]="O"
        check()

def clicked3():
    global turn
    if bt3["text"]==" ":
        if turn==1:
            turn=2
            bt3["text"]="X"
        elif turn==2:
            turn=1
            bt3["text"]="O"
        check()


def clicked4():
    global turn
    if bt4["text"]==" ":
        if turn==1:
            turn=2
            bt4["text"]="X"
        elif turn==2:
            turn=1
            bt4["text"]="O"
        check()

def clicked5():
    global turn
    if bt5["text"]==" ":
        if turn==1:
            turn=2
            bt5["text"]="X"
        elif turn==2:
            turn=1
            bt5["text"]="O"
        check()

def clicked6():
    global turn
    if bt6["text"]==" ":
        if turn==1:
            turn=2
            bt6["text"]="X"
        elif turn==2:
            turn=1
            bt6["text"]="O"
        check()

def clicked7():
    global turn
    if bt7["text"]==" ":
        if turn==1:
            turn=2
            bt7["text"]="X"
        elif turn==2:
            turn=1
            bt7["text"]="O"
        check()

def clicked8():
    global turn
    if bt8["text"]==" ":
        if turn==1:
            turn=2
            bt8["text"]="X"
        elif turn==2:
            turn=1
            bt8["text"]="O"
        check()

def clicked9():
    global turn
    if bt9["text"]==" ":
        if turn==1:
            turn=2
            bt9["text"]="X"
        elif turn==2:
            turn=1
            bt9["text"]="O"
        check()

def check():
    flag=0
    b1 = bt1["text"]
    b2 = bt2["text"]
    b3 = bt3["text"]
    b4 = bt4["text"]
    b5 = bt5["text"]
    b6 = bt6["text"]
    b7 = bt7["text"]
    b8 = bt8["text"]
    b9 = bt9["text"]
    flag=flag+1

    if b1==b2 and b1==b3 and b1=="O" or b1==b2 and b1==b3 and b1=="X":
        win(bt1["text"])
    if b4==b5 and b4==b6 and b4=="O" or b4==b5 and b4==b6 and b4=="X":
        win(bt4["text"])
    if b7==b8 and b7==b9 and b7=="O" or b7==b8 and b7==b9 and b7=="X":
        win(bt7["text"])
    if b1==b4 and b1==b7 and b1=="O" or b1==b4 and b1==b7 and b1=="X":
        win(bt1["text"])
    if b2 == b5 and b2 == b8 and b2 == "O" or b2 == b5 and b2 == b8 and b2 == "X":
        win(bt2["text"])
    if b3 == b6 and b3 == b9 and b3 == "O" or b3 == b6 and b3 == b9 and b3 == "X":
        win(bt3["text"])
    if b1 == b5 and b1 == b9 and b1 == "O" or b1 == b5 and b1 == b9 and b1 == "X":
        win(bt1["text"])
    if b7 == b5 and b7 == b3 and b7 == "O" or b7 == b5 and b7 == b3 and b7 == "X":
        win(bt7["text"])
    if flag==10:
        messagebox.showinfo('Try again!')
        window.destroy()



def win(player):
    ans = "Game complete " + player + " wins "
    messagebox.showinfo("COngrats",ans)
    window.destroy()

bt1=Button(window,text=" ",fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
bt1.grid(column=3,row=30)
bt2=Button(window,text=" ",fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
bt2.grid(column=4,row=30)
bt3=Button(window,text=" ",fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
bt3.grid(column=5,row=30)
bt4=Button(window,text=" ",fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked4)
bt4.grid(column=5,row=40)
bt5=Button(window,text=" ",fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked5)
bt5.grid(column=4,row=40)
bt6=Button(window,text=" ",fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked6)
bt6.grid(column=3,row=40)
bt7=Button(window,text=" ",fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked7)
bt7.grid(column=3,row=50)
bt8=Button(window,text=" ",fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked8)
bt8.grid(column=4,row=50)
bt9=Button(window,text=" ",fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked9)
bt9.grid(column=5,row=50)
window.mainloop()



