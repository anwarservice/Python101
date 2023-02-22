# Import the required libraries
# Created by : Donrofad Sohhad 
# 2023.02.22
# e-mail : donrofad.s@banpamai.ac.th
# line id : yhafar
from csv import *
# import csv
import pandas
from tkinter import *
from tkinter import messagebox

data=''
window=Tk()
window.title("โปรแกรมบันทึกข้อมูล")
window.geometry("700x350")
main_lst=[]


def CreateNew():   #กำหนดหัวตารางข้อมูลใหม่
   with open("data_entry.csv","w") as file:
      Writer=writer(file)
      Writer.writerow(["Name","Age","Contact"])
      #Writer.writerows(main_lst)
      messagebox.showinfo("แจ้งข้อมูล","สร้างไฟล์เรียบร้อย ครับ")
      
def Save():
       with open("data_entry.csv","a",encoding='utf-8',newline='') as file:
            Writer=writer(file)
            #Writer.writerow(["Name","Age","Contact"])
            main_lst.clear()
            lst=[name.get(),age.get(),contact.get()]
            main_lst.append(lst)
            Writer.writerows(main_lst)
            
            messagebox.showinfo("แจ้งข้อมูล","บันทึกข้อมูลเรียบร้อย ครับ")
            
def Clear():
   name.delete(0,END)
   age.delete(0,END)
   contact.delete(0,END)

#read data
def read_data_pandas():
    df = pandas.read_csv('data_entry.csv')
    # lst_data=list(df)
    print(df)
    # messagebox.showinfo('ข้อมูล',lst_data)
    


# 3 labels, 4 buttons,3 entry fields
lbl_name=Label(window,text="Name: ",padx=20,pady=10)
lbl_age=Label(window,text="Age: ",padx=20,pady=10)
lbl_contact=Label(window,text="Contact: ",padx=20,pady=10)

# textbox
name=Entry(window,width=30,borderwidth=3)
age=Entry(window,width=30,borderwidth=3)
contact=Entry(window,width=30,borderwidth=3)

#  button
btn_save=Button(window,text="Save",padx=20,pady=10,command=Save)
btn_new=Button(window,text="New File",padx=20,pady=10,command=CreateNew)
btn_clear=Button(window,text="Clear",padx=18,pady=10,command=Clear)
btn_display=Button(window,text="Show Data",padx=20,pady=10,command=read_data_pandas)
btn_Exit=Button(window,text="Exit",padx=20,pady=10,command=window.quit)

lbl_name.grid(row=0,column=0)
lbl_age.grid(row=1,column=0)
lbl_contact.grid(row=2,column=0)

lbl_create_new=Label(window,text="* * เขียนทับข้อมูลเดิม : ",padx=20,pady=10)
lbl_create_new.grid(row=3,column=1)
lbl_create_new.config(bg='red')


name.grid(row=0,column=1)
age.grid(row=1,column=1)
contact.grid(row=2,column=1)

btn_new.grid(row=3,column=0,columnspan=2,sticky=W)
btn_save.grid(row=4,column=0,columnspan=2,sticky=W)
btn_clear.grid(row=5,column=0,columnspan=2,sticky=W)
btn_display.grid(row=6,column=0,columnspan=2,sticky=W)
btn_Exit.grid(row=7,column=0,columnspan=2,sticky=W)

#readData()

window.mainloop()

