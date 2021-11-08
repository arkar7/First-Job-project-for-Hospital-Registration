import tkinter as tk
import mysql.connector
from tkinter import *
  
 
def submitact():
     
    user = Username.get()
    passw = password.get()
  
    print(f"The name entered by you is {user} {passw}")
  
    logintodb(user, passw)
  
 
def logintodb(user, passw):
     
    # If password is enetered by the
    # user
    if passw:
        db = mysql.connector.connect(host ="localhost",
                                     user = user,
                                     password = passw,
                                     db ="MYSQL")
        cursor = db.cursor()
     # SELECT * FROM mydatabase.content;   
    # If no password is enetered by the
    # user
    else:
        db = mysql.connector.connect(host ="localhost",
                                     user = user,
                                     db ="MYSQL")
        cursor = db.cursor()
         
    # A Table in the database
    savequery = "select * from  mydatabase.content"
     
    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()
         
        # Printing the result of the
        # query
        for x in myresult:
            print(x)
        print("Query Excecuted successfully")
         
    except:
        db.rollback()
        print("Error occured")
  
 
root = tk.Tk()
root.geometry("300x300")
root.title("DBMS Login Page")
  
 
# Defining the first row
lblfrstrow = tk.Label(root, text ="Username -", )
lblfrstrow.place(x = 50, y = 20)
 
Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)
  
lblsecrow = tk.Label(root, text ="Password -")
lblsecrow.place(x = 50, y = 50)
 
password = tk.Entry(root, width = 35)
password.place(x = 150, y = 50, width = 100)
 
submitbtn = tk.Button(root, text ="Login",
                      bg ='blue', command = submitact)
submitbtn.place(x = 150, y = 135, width = 55)
 
root.mainloop()



from tkinter import *
import mysql.connector
from tkinter import ttk
import tkinter.messagebox


window=Tk()
window.title("Search form")
label=Label(window,text="Search form",font=('arial',20,'bold'),bg="black",fg="white")
label.pack(side=TOP,fill=X)
label=Label(window,text="Search form",font=('arial',15,'bold'),bg="black",fg="white")
label.pack(side=BOTTOM,fill=X)

label=Label(window,text="Name",font=('arial',13,'bold'))
label.place(x=30,y=60)

name_entry=ttk.Entry(window)
name_entry.place(x=170,y=60)
name_entry.focus()

label=Label(window,text="Date_of_Birth",font=('arial',13,'bold'))
label.place(x=30,y=100)

name_entry2=ttk.Entry(window)
name_entry2.place(x=170,y=100)

btn= ttk.Button(window,text='Search data')
btn.place(x=170,y=160,width=125,height=30)

window.geometry('400x400')
window.resizable(False,False)
window.mainloop()




window=Tk()
window.title("Content form")
label=Label(window,text="Content form",font=('arial',20,'bold'),bg="black",fg="white")
label.pack(side=TOP,fill=X)
label=Label(window,text="Content form",font=('arial',15,'bold'),bg="black",fg="white")
label.pack(side=BOTTOM,fill=X)

label=Label(window,text="Name",font=('arial',13,'bold'))
label.place(x=30,y=60)

name_entry=ttk.Entry(window)
name_entry.place(x=170,y=60)
name_entry.focus()

label=Label(window,text="Date_of_Birth",font=('arial',13,'bold'))
label.place(x=30,y=100)

name_entry2=ttk.Entry(window)
name_entry2.place(x=170,y=100)

label=Label(window,text="Address",font=('arial',13,'bold'))
label.place(x=30,y=140)

name_entry2=ttk.Entry(window)
name_entry2.place(x=170,y=140)

label=Label(window,text="Weight",font=('arial',13,'bold'))
label.place(x=30,y=180)

name_entry2=ttk.Entry(window)
name_entry2.place(x=170,y=180)


label=Label(window,text="Temperature",font=('arial',13,'bold'))
label.place(x=30,y=220)

name_entry2=ttk.Entry(window)
name_entry2.place(x=170,y=220)

label=Label(window,text="Heart_Rate",font=('arial',13,'bold'))
label.place(x=30,y=260)

name_entry2=ttk.Entry(window)
name_entry2.place(x=170,y=260)

label=Label(window,text="Blood_pressure",font=('arial',13,'bold'))
label.place(x=30,y=300)

name_entry2=ttk.Entry(window)
name_entry2.place(x=170,y=300)



window.geometry('400x400')
window.resizable(False,False)
window.mainloop()