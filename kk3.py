from tkinter import *
import random
import time
i2=Tk()
l=["Mercury","Venus","Mercury","Venus"]

random.shuffle(l)

print(l)

l1=[]
l2=[]
l3=[]

b1=Button(i2,text="1")
b2=Button(i2,text="1")
b3=Button(i2,text="1")
b4=Button(i2,text="1")

def a():
    global l1
    global l2
    global l3
    if b1 not in l2:
        l1.append(l[0])
        l2.append(b1)
        b1.configure(text=l[0])
        if len(l2)!=0:
            if len(l1)==2:
                b1.update_idletasks()
                time.sleep(2)
                if l1[0]!=l1[1]:
                    for i in l2:
                        i.configure(text="1")
                    l1=[]
                    l2=[]
                else:
                    for i in l2:
                        i.configure(command=lambda:None)
                    for i in l2:
                        l3.append(i)
                    l1=[]
                    l2=[]
    if len(l3)==4:
        i2.destroy()
        i3=Tk()
        p1=Label(i3,text="Congratulation!!\n You won",font="times 25 italic")
        i3.rowconfigure(0,weight=1)
        i3.columnconfigure(0,weight=1)
        p1.grid(row=0,column=0,sticky=NSEW)
def b():   
    global l1
    global l2
    global l3
    if b2 not in l2:
        l1.append(l[1])
        l2.append(b2)
        b2.configure(text=l[1])
        if len(l2)!=0:
            if len(l1)==2:
                b2.update_idletasks()
                time.sleep(2)
                if l1[0]!=l1[1]:
                    for i in l2:
                        i.configure(text="1")
                    l1=[]
                    l2=[]
                else:
                    for i in l2:
                        i.configure(command=lambda:None)
                    for i in l2:
                        l3.append(i)
                    l1=[]
                    l2=[]
    if len(l3)==4:
        i2.destroy()
        i3=Tk()
        p1=Label(i3,text="Congratulation!!\n You won",font="times 25 italic")
        i3.rowconfigure(0,weight=1)
        i3.columnconfigure(0,weight=1)
        p1.grid(row=0,column=0,sticky=NSEW)
        
def c():
    global l1
    global l2
    global l3
    if b3 not in l2:
        l1.append(l[2])
        l2.append(b3)
        b3.configure(text=l[2])
        if len(l2)!=0:
            if len(l1)==2:
                b3.update_idletasks()
                time.sleep(2)
                if l1[0]!=l1[1]:
                    for i in l2:
                        i.configure(text="1")
                    l1=[]
                    l2=[]
                else:
                    for i in l2:
                        i.configure(command=lambda:None)
                    for i in l2:
                        l3.append(i)
                    l1=[]
                    l2=[]
    if len(l3)==4:
        i2.destroy()
        i3=Tk()
        p1=Label(i3,text="Congratulation!!\n You won",font="times 25 italic")
        i3.rowconfigure(0,weight=1)
        i3.columnconfigure(0,weight=1)
        p1.grid(row=0,column=0,sticky=NSEW)
def d():
    global l1
    global l2
    global l3
    if b4 not in l2:
        l1.append(l[3])
        l2.append(b4)
        b4.configure(text=l[3])
        if len(l2)!=0:
            if len(l1)==2:
                b4.update_idletasks()
                time.sleep(2)
                if l1[0]!=l1[1]:
                    for i in l2:
                        i.configure(text="1")
                    l1=[]
                    l2=[]
                else:
                    for i in l2:
                        i.configure(command=lambda:None)
                    for i in l2:
                        l3.append(i)
                    l1=[]
                    l2=[]
    if len(l3)==4:
        i2.destroy()
        i3=Tk()
        p1=Label(i3,text="Congratulation!!\n You won",font="times 25 italic")
        i3.rowconfigure(0,weight=1)
        i3.columnconfigure(0,weight=1)
        p1.grid(row=0,column=0,sticky=NSEW)

b1.configure(command=a)
b2.configure(command=b)
b3.configure(command=c)
b4.configure(command=d)



i2.rowconfigure(0,weight=1)
i2.rowconfigure(1,weight=1)
i2.columnconfigure(0,weight=1)
i2.columnconfigure(1,weight=1)

b1.grid(row=0,column=0,sticky=NSEW)

b2.grid(row=0,column=1,sticky=NSEW)

b3.grid(row=1,column=0,sticky=NSEW)

b4.grid(row=1,column=1,sticky=NSEW)


i2.mainloop()