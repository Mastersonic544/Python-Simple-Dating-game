from tkinter import *

root = Tk()

root.title("Dating Game <3")
root.configure(background="light coral")
root.geometry("300x500")


f=open("girl.txt",'w')
qts=open("quest.txt",'r')

def next():
    option=r.get()
    f=open("girl.txt",'a')
    
    qq=""
    q1=""
    q2=""
    q3=""
    q4=""
    for i in range(5):
        if i==0:
            qq=qts.readline()
        elif i==1:
            q1=qts.readline()
        elif i==2:
            q2=qts.readline()
        elif i==3:
            q3=qts.readline()
        else:
            q4=qts.readline()
    qt.set(qq[0:len(qq)-1])
    qb1t.set(q1[0:len(q1)-1])
    qb2t.set(q2[0:len(q2)-1])
    qb3t.set(q3[0:len(q3)-1])
    qb4t.set(q4[0:len(q4)-1])
    f.write(qq[0:len(qq)-1]+' :\n')
    if option==0:
        f.write(q1)
    elif option==1:
        f.write(q2)
    elif option==2:
        f.write(q3)
    else:
        f.write(q4)
    f.write('\n')





qt=StringVar()
q = Label(root, textvariable=qt, bg="light coral")
qt.set('1. Question')
q.place(relx = 0.5 , rely = 0.15, anchor='center')





r = IntVar()

qb1t=StringVar()
qb1= Radiobutton(textvariable=qb1t,variable=r, value=0, highlightthickness=0, bg="light coral")
qb1t.set('a) Option1')
qb1.place(relx = 0.5 , rely = 0.2, anchor='center')

qb2t=StringVar()
qb2 = Radiobutton(textvariable=qb2t, variable=r, value=1, highlightthickness=0, bg="light coral")
qb2t.set('b) Option2')
qb2.place(relx = 0.5 , rely = 0.25, anchor='center')

qb3t=StringVar()
qb3 = Radiobutton(textvariable=qb3t, variable=r, value=2, highlightthickness=0, bg="light coral")
qb3t.set('c) Option3')
qb3.place(relx = 0.5 , rely = 0.3, anchor='center')

qb4t=StringVar()
qb4 = Radiobutton(textvariable=qb4t, variable=r, value=3, highlightthickness=0, bg="light coral")
qb4t.set('d) Option4')
qb4.place(relx = 0.5 , rely = 0.35, anchor='center')


nxt= Button(root, text=" Next >>", command=next)
nxt.pack()
nxt.place(relx = 0.5 , rely = 0.45, anchor='center')



root.mainloop()