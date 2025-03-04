import tkinter
import pymysql
from tkinter import*
from tkinter import messagebox
def showcustomersave():
    t=tkinter.Tk()
    t.geometry('800x800')
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='mydbone')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=e3.get()
        xd=int(e4.get())
        sql="insert into customerdata values(%d,'%s','%s',%d)"%(xa,xb,xc,xd)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','Saved')
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
    a=Label(t,text='CustId')
    a.place(x=50,y=40)
    b=Label(t,text='Name')
    b.place(x=50,y=90)
    c=Label(t,text='City')
    c.place(x=50,y=130)
    d=Label(t,text='Bill')
    d.place(x=50,y=170)
    
    e1=Entry(t,width=30)
    e1.place(x=250,y=40)
    e2=Entry(t,width=30)
    e2.place(x=250,y=90)
    e3=Entry(t,width=30)
    e3.place(x=250,y=130)
    e4=Entry(t,width=30)
    e4.place(x=250,y=170)
    
    s=Button(t,text='Save',font='arial',command=savedata)
    s.place(x=50,y=250)
    
    t.mainloop()