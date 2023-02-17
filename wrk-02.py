#Create by : Yhafar
#EP2. Python 101 by Uncle
#2023.02.14

from tkinter import *
from tkinter.ttk import * #theme of tk
from tkinter import messagebox


GUI = Tk()  #main screen
GUI.title('โปรแกรมบันทึกข้อมูล : Python 101 Basic 16 Hour by Uncle')  #title
GUI.geometry('500x400')  #windows size



#Lbl = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
#Lbl.place(x=30,y=20)

courses = ['Hello world','Variable and Data type','Fuction and Loop','Dictionary']
r = ['course']



def message_1():
    text = courses[0]
    messagebox.showinfo('Day#1',text)

def message_2():
    text = courses[1]
    messagebox.showinfo('Day#2',text)

def message_3():
    text = courses[2]
    messagebox.showinfo('Day#3',text)

def message_4():
    text = courses[3]
    messagebox.showinfo('Day#4',text)
    

Fb1 = Frame(GUI)
Fb1.place(x=150,y=100)
Btn1 = Button(Fb1,text='Day#1',command = message_1)
Btn1.pack(ipadx=20,ipady=20)

Fb2 = Frame(GUI)
Fb2.place(x=300,y=100)
Btn2 = Button(Fb2,text='Day#2',command = message_2)
Btn2.pack(ipadx=20,ipady=20)

Fb3 = Frame(GUI)
Fb3.place(x=150,y=200)
Btn4 = Button(Fb3,text='Day#3',command = message_3)
Btn4.pack(ipadx=20,ipady=20)

Fb4 = Frame(GUI)
Fb4.place(x=300,y=200)
Btn4 = Button(Fb4,text='Day#4',command = message_4)
Btn4.pack(ipadx=20,ipady=20)



GUI.mainloop()
