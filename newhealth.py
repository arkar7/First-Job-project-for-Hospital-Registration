from logging import root
from math import expm1
from tkinter import *
from tkinter import messagebox
import mysql.connector



def ok():
      Name = e1.get()
      Birthday= e2.get()
      Address = e3.get()
      Weight = e4.get()
      Temperature= e5.get()
      Heart_rate= e6.get()
      Blood_pressure= e7.get()



      mysqldb=mysql.connector.connect(host='localhost',                
                                         database='amitdb',
                                         user='Arkar',
                                         password='mysql12345')
      mycursor=mysqldb.cursor()
      
      try:
         sql = "INSERT INTO amitdb.patient (Name,Birthday,Address,Weight,Temperature,Heart_rate,Blood_pressure) VALUES(%s,%s,%s,%s,%s,%s,%s)"
         val = (Name,Birthday,Address,Weight,Temperature,Heart_rate,Blood_pressure)
         mycursor.execute(sql,val)
         mysqldb.commit()
         messagebox.showinfo("information","Record inserted successful...")

         

      except Exception as e:
         print(e)
         mysqldb.rollback()
         mysqldb.close()


root =Tk()
root.title("Patient Registation")
root.geometry("800x500")
global e1 


Label(root, text="Name").place(x=10, y=10)
Label(root, text="Birthday").place(x=10, y=40)
Label(root, text="Address").place(x=10, y=70)
Label(root, text="Weight").place(x=10, y=100)
Label(root, text="Temperature").place(x=10, y=130)
Label(root, text="Heart_rate").place(x=10, y=160)
Label(root, text="Blood_pressure").place(x=10, y=190)

e1 = Entry(root)
e1.place(x=148, y=10)

e2 = Entry(root)
e2.place(x=148, y=40)

e3 = Entry(root)
e3.place(x=148, y=70)

e4 = Entry(root)
e4.place(x=148, y=100)

e5 = Entry(root)
e5.place(x=148, y=130)

e6 = Entry(root)
e6.place(x=148, y=160)

e7 = Entry(root)
e7.place(x=148, y=190)



Button(root, text="Add", command=ok,height=3,width=13).place(x=149, y=220)

root.mainloop()
