from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector.dbapi import ROWID, Date

# from newfunc2 import add_new, delete_customer, update_customer


def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('','end',values=i)

def search():
    q2 = q.get()
    query = "SELECT ID,Date,Name,Birthday,Address,Weight,Temperature,Heart_rate,Blood_pressure FROM mydatatable.mypatient WHERE ID LIKE '%"+q2+"%' OR Name LIKE '%"+q2+"%' OR Birthday LIKE '%"+q2+"%'" 
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)

def clear():
    query = "SELECT ID,Date,Name,Birthday,Address,Weight,Temperature,Heart_rate,Blood_pressure FROM mydatatable.mypatient"
    cursor.execute(query)
    rows=cursor.fetchall()
    update(rows)

def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])
    t4.set(item['values'][3])
    t5.set(item['values'][4])
    t6.set(item['values'][5])
    t7.set(item['values'][6])
    t8.set(item['values'][7])
    t9.set(item['values'][8])


def update_customer():
    Date = t2.get()
    Name = t3.get()
    Birthday = t4.get()
    Address = t5.get()
    Weight = t6.get()
    Temperature = t7.get()
    Heart_rate = t8.get()
    Blood_pressure = t9.get()
    custid = t1.get()

    if messagebox.askyesno("Confirm Please", "Aru you sure you want to update this customer?"):
        query="UPDATE mydatatable.mypatient SET Date= %s, Name = %s,Birthday= %s, Address = %s, Weight = %s, Temperature = %s,Heart_rate=%s,Blood_pressure=%s WHERE ID = %s"
        cursor.execute(query,(Date,Name,Birthday,Address,Weight,Temperature,Heart_rate,Blood_pressure,custid))
        mydb.commit()
        clear()
    else:
        return True

def add_new():
    ID  = t1.get()
    Date = t2.get()
    Name = t3.get()
    Birthday = t4.get()
    Address = t5.get()
    Weight = t6.get()
    Temperature = t7.get()
    Heart_rate = t8.get()
    Blood_pressure = t9.get()


    Temperature = t7.get()
    # Temperature Error Hendling
    t = float(Temperature)
    if t < 37.6:
        print('Your temperature is Normal')
    else:
     messagebox.showerror("Error", "Normal Temperature is 36.5–37.6 °C :>Please go to Emergency room in First Floor ")

    query = "INSERT INTO mydatatable.mypatient(ID,Date,Name,Birthday,Address,Weight,Temperature,Heart_rate,Blood_pressure)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(ID,Date,Name,Birthday,Address,Weight,Temperature,Heart_rate,Blood_pressure))
    mydb.commit()
    clear()
 

def delete_customer():
    customer_id = t1.get()
    if messagebox.askyesno("Confirm Delete?","Are you  sure you want to delete this customer?"):
        query ="DELETE FROM mydatatable.mypatient WHERE id = " +customer_id
        cursor.execute(query)
        mydb.commit()
        clear()
    else:
        return True

mydb = mysql.connector.connect(host="localhost",user="Arkar",passwd="mysql12345",database="mydatatable")#,auth_plugin="myaql_native_psssword")
cursor = mydb.cursor()

root = Tk()
q = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()
t7 = StringVar()
t8 = StringVar()
t9 = StringVar()

wrapper1 = LabelFrame(root, text="Patient List")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame(root, text="Patient Data")

wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7,8,9), show="headings", height="6")

trv.pack(side=LEFT)
trv.place(x=0,y=0)
trv.heading(1,text="ID")
trv.heading(2, text="Date")
trv.heading(3, text="Name")
trv.heading(4, text="Birthday")
trv.heading(5, text="Address")
trv.heading(6, text="Weight")
trv.heading(7, text="Temperature")
trv.heading(8, text="Heart_rate")
trv.heading(9, text="Blood_pressure")
trv.column('1',width=125,minwidth=210)
trv.column('2',width=125,minwidth=210)
trv.column('3',width=125,minwidth=210)
trv.column('4',width=125,minwidth=210)
trv.column('5',width=125,minwidth=210)
trv.column('6',width=125,minwidth=210)
trv.column('7',width=125,minwidth=210)
trv.column('8',width=125,minwidth=210)
trv.column('9',width=125,minwidth=210)



trv.bind('<Double 1>', getrow)

#Vertical scroll bar
yscrollbar = ttk.Scrollbar(wrapper1,orient="vertical",command=trv.yview)
yscrollbar.pack(side=RIGHT,fill="y")

#Horizontal scroll bar
xscrollbar = ttk.Scrollbar(wrapper1,orient="horizontal",command=trv.xview)
xscrollbar.pack(side=BOTTOM,fill="x")

trv.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)


query = "SELECT ID,Date,Name,Birthday,Address,Weight,Temperature,Heart_rate,Blood_pressure FROM mydatatable.mypatient "
cursor.execute(query)
rows = cursor.fetchall()
update(rows)

#search
lbl =Label(wrapper2, text="Search")
lbl.pack(side=tk.LEFT,padx=10)
ent = Entry(wrapper2, textvariable=q)
ent.pack(side=tk.LEFT,padx=6)
btn = Button(wrapper2, text="search", command=search)
btn.pack(side=tk.LEFT,padx=6)
cbtn = Button(wrapper2,text="Clear",command=clear)
cbtn.pack(side=tk.LEFT, padx=6)

#user data function
lbl1 = Label(wrapper3, text="ID")
lbl1.grid(row=0,column=0,padx=5,pady=3)
ent1 = Entry(wrapper3,textvariable=t1)
ent1.grid(row=0, column=1, padx=5, pady=3)

lbl2 = Label(wrapper3, text="Date")
lbl2.grid(row=1,column=0,padx=5,pady=3)
ent2 = Entry(wrapper3,textvariable=t2)
ent2.grid(row=1, column=1, padx=5, pady=3)

lbl3= Label(wrapper3, text="Name")
lbl3.grid(row=2,column=0,padx=5,pady=3)
ent3 = Entry(wrapper3,textvariable=t3)
ent3.grid(row=2, column=1, padx=5, pady=3)

lbl4 = Label(wrapper3, text="Birthday")
lbl4.grid(row=3,column=0,padx=5,pady=3)
ent4 = Entry(wrapper3,textvariable=t4)
ent4.grid(row=3, column=1, padx=5, pady=3)

lbl5 = Label(wrapper3, text="Address")
lbl5.grid(row=4,column=0,padx=5,pady=3)
ent5 = Entry(wrapper3,textvariable=t5)
ent5.grid(row=4, column=1, padx=5, pady=3)

lbl6 = Label(wrapper3, text="Weight")
lbl6.grid(row=5,column=0,padx=5,pady=3)
ent6 = Entry(wrapper3,textvariable=t6)
ent6.grid(row=5, column=1, padx=5, pady=3)

lbl7 = Label(wrapper3, text="Temperature")
lbl7.grid(row=6,column=0,padx=5,pady=3)
ent7 = Entry(wrapper3,textvariable=t7)
ent7.grid(row=6, column=1, padx=5, pady=3)

lbl8 = Label(wrapper3, text="Heart_rate")
lbl8.grid(row=7,column=0,padx=5,pady=3)
ent8 = Entry(wrapper3,textvariable=t8)
ent8.grid(row=7, column=1, padx=5, pady=3)

lbl9= Label(wrapper3, text="Blood_pressure")
lbl9.grid(row=8,column=0,padx=5,pady=3)
ent9 = Entry(wrapper3,textvariable=t9)
ent9.grid(row=8, column=1, padx=5, pady=3)

up_btn = Button(wrapper3, text="Update" , command=update_customer)
add_btn = Button(wrapper3, text="Add New",command=add_new)
delete_btn=Button(wrapper3, text="Delete" , command=delete_customer)

add_btn.grid(row=9, column=0, padx=5, pady=3)
up_btn.grid(row=9, column=1, padx=5, pady=3)
delete_btn.grid(row=9, column=2, padx=5, pady=3)

root.title("Patient Rigistration")
root.geometry("1200x800")
root.resizable(False,False)
root.mainloop()
