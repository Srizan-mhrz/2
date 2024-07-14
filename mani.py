import tkinter as tk
import sqlite3
import tkinter.messagebox as myMessagebox

conn =sqlite3.connect("college.sqlite3")
cursor=conn.cursor()
def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    address TEXT)
    """)
    conn.commit()

create_table()    
app=tk.Tk()
app.title("STUDENT  RECORD")
app.geometry("500x500")


nameLebel=tk.Label(app,text="name")
nameLebel.grid(row=0,column=0,padx=10,pady=10)
name=tk.Entry(app)
name.grid(row=0,column=1)
emailLebel=tk.Label(app,text="email")
emailLebel.grid(row=1,column=0,padx=10,pady=10)
email=tk.Entry(app)
email.grid(row=1,column=1)
addressLebel=tk.Label(app,text="address")
addressLebel.grid(row=2,column=0,padx=10,pady=10)
address=tk.Entry(app)
address.grid(row=2,column=1)

def insert():
    iname=name.get()
    iemail=email.get()
    iaddress=address.get()
    cursor.execute("""
    INSERT INTO student(name,email,address)
    VALUES(?,?,?) """,(iname,iemail,iaddress))
    conn.commit()
    
   
    name.delete(0,tk.END)
    email.delete(0,tk.END)
    address.delete(0,tk.END)
    myMessagebox.showinfo("success","record inserted succesfully")

    
button=tk.Button(app,text="add record",command=insert)
button.grid(row=3,column=1)

def delete(id):
    cursor.execute("DELETE FROM student WHERE id=?",(id,))
    conn.commit()

    myMessagebox.showinfo("Success","record deleted succesfully")
    show()

def show():
    cursor.execute("SELECT * FROM student")
    records=cursor.fetchall()
    tk.Label(app,text='name').grid(row=5,column=0)
    tk.Label(app,text='email').grid(row=5,column=1)
    tk.Label(app,text='address').grid(row=5,column=2)
    tk.Label(app,text='action').grid(row=5,column=3)
    
    for i, record in enumerate(records):
        tk.Label(app,text=record[1]).grid(row=i+6,column=0)
        tk.Label(app,text=record[2]).grid(row=i+6,column=1)
        tk.Label(app,text=record[3]).grid(row=i+6,column=2)
        tk.Button(app,text="edit").grid(row=i+6,column=3)
        tk.Button(app,text="delete",command=lambda id_=record[0]: delete(id_)).grid(row=i+6,column=4)
        
show()        

app.mainloop()    
