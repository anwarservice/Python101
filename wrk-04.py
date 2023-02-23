# Import the required libraries
# Created by : Donrofad Sohhad 
# 2023.02.22
# e-mail : donrofad.s@banpamai.ac.th
# line id : yhafar
from csv import *
import csv
import pandas
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk #theme of tk

data=''
window=Tk()
window.title("โปรแกรมบันทึกข้อมูล")
window.geometry("840x600")
main_lst=[]

# frame label
LF2 = ttk.LabelFrame(window, text='Report')
LF2.place(x=20, y=150)

# สร้างตาราง GUI ด้วย Pandas    
table_header=('ชื่อ','อายุ','เบอร์โทร')
table = ttk.Treeview(LF2,columns=table_header,show='headings')

for column in table_header:
    table.heading(column, text=column)
table.pack(fill="both", expand=True)

def CreateNew():   #สร้างข้อมูลใหม่
   with open("data_entry.csv","w") as file:
      Writer=writer(file)
      Writer.writerow(["Name","Age","Contact"])
      #Writer.writerows(main_lst)
      messagebox.showinfo("แจ้งข้อมูล","สร้างไฟล์เรียบร้อย ครับ")
      
def Save():
       with open("data_entry.csv","a",encoding='utf-8',newline='') as file:
            Writer=writer(file)
            
            main_lst.clear()
            lst=[name.get(),age.get(),contact.get()]
            main_lst.append(lst)
            Writer.writerows(main_lst)
            
            # ให้ textbox ว่างหลังจากบันทึกแล้ว
            v_name.set('')
            v_age.set('')
            v_contact.set('')
            
            messagebox.showinfo("Information","บันทึกข้อมูลเรียบร้อย ครับ")
            file.close()
            read_data_pandas()  #แสดงข้อมูลใหม่
            
def Clear():
   name.delete(0,END)
   age.delete(0,END)
   contact.delete(0,END)

#read data
def read_data_pandas():
    df = pandas.read_csv('data_entry.csv',encoding='utf-8')
    
    # ลบรายการที่มีอยู่ก่อน
    for i in table.get_children():
           table.delete(i)
    # นำข้อมูลที่อ่านจากไฟล์ csv ใส่ในตาราง       
    for index, row in df.iterrows():
        table.insert("", index, text=index, values=tuple(row))
   
      
def readcsv():
    with open('data_entry.csv', encoding='utf-8', newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
    return data

# กำหนด event เมื่อคลิกรายการ
def item_selected(event):
    for selected_item in table.selection():
        item = table.item(selected_item)
        record = item['values']
        # show a message
        messagebox.showinfo('Information', record)

table.bind('<<TreeviewSelect>>', item_selected)


# 3 labels, 4 buttons,3 entry fields
lbl_name=Label(window,text="Name: ",padx=20,pady=10)
lbl_age=Label(window,text="Age: ",padx=20,pady=10)
lbl_contact=Label(window,text="Contact: ",padx=20,pady=10)

# textbox
v_name=StringVar()
name=Entry(window,width=30,borderwidth=3,textvariable=v_name)
v_age=StringVar()
age=Entry(window,width=30,borderwidth=3,textvariable=v_age)
v_contact=StringVar()
contact=Entry(window,width=30,borderwidth=3,textvariable=v_contact)

#  button
btn_save=Button(window,text="Save",padx=20,pady=10,command=Save)
btn_new=Button(window,text="New File",padx=20,pady=10,command=CreateNew)
btn_clear=Button(window,text="Clear",padx=20,pady=10,command=Clear)
btn_display=Button(window,text="Show Data",padx=20,pady=10,command=read_data_pandas)
btn_Exit=Button(window,text="Exit",padx=20,pady=10,command=window.quit)

# ตำแหน่งข้อความ Name Age Contact
lbl_name.grid(row=0,column=0)
lbl_age.grid(row=1,column=0)
lbl_contact.grid(row=2,column=0)

lbl_create_new=Label(window,text="* * คำสั่ง New File เขียนทับข้อมูลเดิม : ",padx=20,pady=10)
lbl_create_new.grid(row=2,column=2,columnspan=3)
lbl_create_new.config(bg='red',fg='yellow')

# ตำแหน่ง textbox
name.grid(row=0,column=1)
age.grid(row=1,column=1)
contact.grid(row=2,column=1)

# ตำแหน่ง button
btn_new.grid(row=3,column=0,sticky=W)
btn_save.grid(row=3,column=1,sticky=W)
btn_clear.grid(row=3,column=2,sticky=W)
btn_display.grid(row=3,column=3,sticky=W)
btn_Exit.grid(row=3,column=4,sticky=W)

#readData()
read_data_pandas()

window.mainloop()

