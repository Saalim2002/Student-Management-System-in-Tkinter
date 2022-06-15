from tkinter.ttk import *  # for combobox
from tkinter import *
import sqlite3

root = Tk()


    
root.title("Student Management System")
root.geometry("1525x770+0+0")
root.resizable(0,0)


#########################   ALL VARIABLES       #################################################

Var1 = StringVar()
Var2 = StringVar()
Var3 = StringVar()
Var4 = StringVar()
Var5 = StringVar()
Var6 = StringVar()



#########################   ADMIN TABLE      #################################################
def Create2():
    conn = sqlite3.connect("StudMang.db")
    c = conn.cursor()
    #c.execute("Create Table Admin(Name text, Phoneno text,Address text,Username text,Password text)")
    conn.commit()
    conn.close()
#Create2()

######################################     ALL FUNCTION     ############################################################
def AutoDelete():
    conn = sqlite3.connect("StudMang.db")
    c = conn.cursor()                                           
    c.execute("delete from Faculty4 where ID =''")
    print("Faculty Deleted")
    conn.commit()                   
    conn.close()
#AutoDelete()

def AutoDelete():
    conn = sqlite3.connect("StudMang.db")
    c = conn.cursor()                                           
    c.execute("delete from Student where Rollno =''")
    print("Faculty Deleted")
    conn.commit()                   
    conn.close()
#AutoDelete()


def Create():
    conn = sqlite3.connect("StudMang.db")
    c = conn.cursor()
    #c.execute("Create Table Faculty4 (ID text primary key not null,Name text, Phoneno text,Gender text,Address text,Subject text)")
    conn.commit()
    conn.close()
Create()

def DELETE():    
       conn = sqlite3.connect("StudMang.db")
       c = conn.cursor()                                           
       c.execute("delete from Faculty4 where ID LIKE '%"+str(Var1.get())+"%'")
       print("Faculty Deleted")
       
       conn.commit()
       conn.close()
#Faculty
            


#FRAME1    
frame = Frame(root,bg="Yellow",height=300)    
bt1 = Button(frame,text="ADMIN",font=("times new roman",16,"bold"),bg="yellow",fg="green",activebackground="red",activeforeground="blue",padx=20,pady=5)
bt1.pack(side=LEFT,fill=X)
bt2 = Button(frame,text="FACULTY",font=("times new roman",16,"bold"),bg="yellow",fg="green",activebackground="red",activeforeground="blue",padx=20,pady=5)
bt2.pack(side=LEFT,fill=X)
bt3 = Button(frame,text="STUDENT",font=("times new roman",16,"bold"),bg="yellow",fg="green",activebackground="red",activeforeground="blue",padx=20,pady=5)
bt3.pack(side=LEFT,fill=X)
bt3 = Button(frame,text="ABOUT AS",font=("times new roman",16,"bold"),bg="yellow",fg="green",activebackground="red",activeforeground="blue",padx=20,pady=5)
bt3.pack(side=LEFT,fill=X)
label = Label(frame,text="Student Management System Timing(8am to 10pm)",font=("times new roman",16,"bold"),bg="yellow",fg="green")
label.pack(side=RIGHT,padx=30)
frame.pack(side=TOP,fill=X)

# Admin page 1

def Admin1():


    admin1=Toplevel(root)
    admin1.title("Student Management System")
    admin1.geometry("1535x800+0+0")
    admin1.resizable(0,0)


#FRAME1    
    frame = Frame(admin1,bg="yellow",height=300)    
    bt1 = Button(frame,text="ADMIN",font=("times new roman",16,"bold"),bg="yellow",fg="green",activebackground="red",activeforeground="blue",padx=20,pady=5)
    bt1.pack(side=LEFT,fill=X)
    label = Label(frame,text="Student Management System Timing(8am to 10pm)",font=("times new roman",16,"bold"),bg="yellow",fg="green")
    label.pack(side=RIGHT,padx=30)
    frame.pack(side=TOP,fill=X)
###########################################################################################
        #######                   MANAGE FRAME           #######################
############################################################################################
    Tab = ttk.Notebook(admin1)
#########################################
    frame1 = Frame(Tab,width=400,height=500,bg='crimson')
    title = Label(frame1,text="MANAGE FACULTY",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    title.grid(row = 0,columnspan=2,padx=90,pady=10)


    Name = Label(frame1,text="Name",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Name.grid(row = 2,column=0,pady=10,padx=10,sticky=W)
    entry1 = Entry(frame1,textvariable=Var2,font=("times new roman",14,"bold"))
    entry1.grid(row=2,column=1,padx=10,sticky=W)
    entry1.focus()

    Rollno = Label(frame1,text="ID",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Rollno.grid(row = 3,column=0,pady=10,padx=10,sticky=W)
    entry2 = Entry(frame1,textvariable=Var1,font=("times new roman",14,"bold"))
    entry2.grid(row=3,column=1,padx=10,sticky=W)

    Phoneno = Label(frame1,text="Phoneno",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Phoneno.grid(row = 4,column=0,pady=10,padx=10,sticky=W)
    entry3 = Entry(frame1,textvariable=Var3,font=("times new roman",14,"bold"))
    entry3.grid(row=4,column=1,padx=10,sticky=W)

    Gender = Label(frame1,text="Gender",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Gender.grid(row = 5,column=0,pady=10,padx=10,sticky=W)
    vlist = ["Male","Female","Other"]
    entry4 = Combobox(frame1,textvariable=Var4,values=vlist,font=("times new roman",13,"bold"))
    entry4.grid(row=5,column=1,padx=10,sticky=W)


    Address = Label(frame1,text="Address",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Address.grid(row = 6,column=0,pady=10,padx=10,sticky=W)
    entry5 = Entry(frame1,textvariable=Var6,font=("times new roman",14,"bold"))
    entry5.grid(row=6,column=1,padx=10,sticky=W)

    def ADDFaculty():    
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()                                           
        c.execute("Insert into Faculty4 values(?,?,?,?,?,?)",(Var1.get(),Var2.get(),Var3.get(),Var4.get(),Var6.get(),Var5.get()))
        print("Faculty Add")
       
        conn.commit()
        fetch_data()
        clear()
        conn.close()

    def UPDATE():    
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()                                           
        c.execute("Update Faculty4 set Name=?,Phoneno=?,Gender=?,Address=?,Subject=? where ID=?",(Var2.get(),Var3.get(),Var4.get(),Var6.get(),Var5.get(),Var1.get()))
        print("Faculty Updated")
        conn.commit()
        fetch_data()
        clear()
        conn.close()

    def Search():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Faculty4 WHERE  Name LIKE '%"+str(Var2.get())+"%'")
        rows=result.fetchall()
        if len(rows)!=0:
            Table.delete(*Table.get_children())
            for row in rows:
                Table.insert('',END,values=row)
            conn.commit()
        conn.close()
        
    def ViewAll():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Faculty4")
        rows=result.fetchall()
        if len(rows)!=0:
            Table.delete(*Table.get_children())
            for row in rows:
                Table.insert('',END,values=row)
            conn.commit()
        conn.close()
    
    Subject = Label(frame1,text="Subject",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Subject.grid(row = 8,column=0,pady=10,padx=10,sticky=W)
    vlist = ["Java","GAD","MIC","SEN","DCC"]
    entry6 = Combobox(frame1,values=vlist,textvariable=Var5,font=("times new roman",13,"bold"))
    entry6.grid(row=8,column=1,padx=10,sticky=W)

    frame2a = Frame(frame1,bg="crimson")
    add = Button(frame2a,text="ADD",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=ADDFaculty)
    add.grid(row = 1,column=0,pady=10,padx=10,sticky=W)

    upd = Button(frame2a,text="UPDATE",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=UPDATE)
    upd.grid(row = 1,column=1,pady=10,padx=10,sticky=W)

    def clear():
        Var1.set('')
        Var2.set('')
        Var3.set('')
        Var4.set('')
        Var5.set('')
        Var6.set('')
        
    
    clr = Button(frame2a,text="CLEAR",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=clear)
    clr.grid(row = 1,column=3,pady=10,padx=10,sticky=W)

    frame2a.place(x=0,y=400,width=400,height=50)
    frame1.pack(fill=BOTH,expand=1)
#######################################################################################################################################

########################################################################################################################################
    frame2 = Frame(Tab,width=400,height=500,bg='crimson')

    title = Label(frame2,text="MANAGE STUDENT",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    title.grid(row = 0,columnspan=2,padx=90,pady=10)

    Name = Label(frame2,text="Name",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Name.grid(row = 2,column=0,pady=10,padx=10,sticky=W)
    entry1 = Entry(frame2,textvariable=Var1,font=("times new roman",14,"bold"))
    entry1.grid(row=2,column=1,padx=10,sticky=W)
    entry1.focus()

    Rollno = Label(frame2,text="Rollno",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Rollno.grid(row = 3,column=0,pady=10,padx=10,sticky=W)
    entry2 = Entry(frame2,textvariable=Var2,font=("times new roman",14,"bold"))
    entry2.grid(row=3,column=1,padx=10,sticky=W)

    Phoneno = Label(frame2,text="Phoneno",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Phoneno.grid(row = 4,column=0,pady=10,padx=10,sticky=W)
    entry3 = Entry(frame2,textvariable=Var3,font=("times new roman",14,"bold"))
    entry3.grid(row=4,column=1,padx=10,sticky=W)

    Gender = Label(frame2,text="Gender",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Gender.grid(row = 5,column=0,pady=10,padx=10,sticky=W)
    vlist = ["Male","Female","Other"]
    entry4 = Combobox(frame2,textvariable=Var4,values=vlist,font=("times new roman",13,"bold"))
    entry4.grid(row=5,column=1,padx=10,sticky=W)

    Address = Label(frame2,text="Address",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Address.grid(row = 6,column=0,pady=10,padx=10,sticky=W)
    entry5 = Entry(frame2,textvariable=Var6,font=("times new roman",14,"bold"))
    entry5.grid(row=6,column=1,padx=10,sticky=W)

    
    def Create():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        #c.execute("Create Table Student (Rollno text,Name text, Phoneno text,Gender text,Address text,Class text)")
        #Alter table Student drop column Username,Password
        conn.commit()
        conn.close()
    Create()
    
    def ADDStudent():    
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()                                           
        c.execute("Insert into Student (Name,Rollno,Phoneno,Gender,Address,Class) values(?,?,?,?,?,?)",(Var1.get(),Var2.get(),Var3.get(),Var4.get(),Var6.get(),Var5.get()))
        print("Student Add")
        conn.commit()
        fetch_data1()
        clear()
        conn.close()

    def UPDATE1():    
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()                                           
        c.execute("Update Student set Name=?,Phoneno=?,Gender=?,Address=?,Class=? where Rollno=?",(Var2.get(),Var3.get(),Var4.get(),Var6.get(),Var5.get(),Var1.get()))
        print("Student Updated")
        conn.commit()
        fetch_data1()
        clear()
        conn.close()

    def DELETE1():    
       conn = sqlite3.connect("StudMang.db")
       c = conn.cursor()                                           
       c.execute("delete from Student where Rollno LIKE '%"+str(Var1.get())+"%'")
       print("Student Deleted")
       conn.commit()
       conn.close()
       
    def Search1():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Student WHERE  Name LIKE '%"+str(Var2.get())+"%'")
        rows=result.fetchall()
        if len(rows)!=0:
            Table1.delete(*Table1.get_children())
            for row in rows:
                Table1.insert('',END,values=row)
            conn.commit()
            print("Student Serach")
        conn.close()
        
    def ViewAll1():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Student")
        rows=result.fetchall()
        if len(rows)!=0:
            Table1.delete(*Table1.get_children())
            for row in rows:
                Table1.insert('',END,values=row)
            conn.commit()
        conn.close()
        
    Class = Label(frame2,text="Class",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Class.grid(row = 8,column=0,pady=10,padx=10,sticky=W)
    vlist = ["Class1","Class2","Class3","Class4","Class5"]
    entry6 = Combobox(frame2,textvariable=Var5,values=vlist,font=("times new roman",13,"bold"))
    entry6.grid(row=8,column=1,padx=10,sticky=W)

    frame2a = Frame(frame2,bg="crimson")
    add = Button(frame2a,text="ADD",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=ADDStudent)
    add.grid(row = 1,column=0,pady=10,padx=10,sticky=W)
    
    upd = Button(frame2a,text="UPDATE",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=UPDATE1)
    upd.grid(row = 1,column=1,pady=10,padx=10,sticky=W)

    clr = Button(frame2a,text="CLEAR",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=clear)
    clr.grid(row = 1,column=3,pady=10,padx=10,sticky=W)

    frame2a.place(x=0,y=400,width=400,height=50)
    frame2.pack(fill=BOTH,expand=1)
#################################################################################################################

#################################################################################################################
    Tab.add(frame1,text="Faculty")
    Tab.add(frame2,text="Student")
    Tab.place(x=5,y=55,width=400,height=500)
    style = ttk.Style()
    style.configure('TNotebook.Tab',foreground="Crimson",background="white",font=("times new roman",16,"bold"),padding=[5,2])
###################################################

##########################################################################################################
   #1                   ####################           DELETE FRAME      ########################
##########################################################################################################
    Tab2 =ttk.Notebook(admin1)
############################
    frame1 = Frame(Tab2,width=400,height=200,bg="crimson")
    title = Label(frame1,text="DELETE FACULTY",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    title.grid(row = 0,columnspan=2,padx=90,pady=10)

    ID = Label(frame1,text="FacultyID",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    ID.grid(row = 2,column=0,pady=10,padx=10,sticky=W)
    entry1 = Entry(frame1,textvariable=Var1,font=("times new roman",14,"bold"))
    entry1.grid(row=2,column=1,padx=10,sticky=W)
    entry1.focus()

               
    
    clr = Button(frame1,text="DELETE",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=DELETE)
    clr.grid(row =4 ,columnspan=2,pady=10,sticky=E)
    frame1.pack(fill=BOTH,expand=1)
#####################################################################33
#  2
######################################################################
    frame2 = Frame(Tab2,width=400,height=200,bg="crimson")
    title = Label(frame2,text="DELETE STUDENT",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    title.grid(row = 0,columnspan=2,padx=90,pady=10)

    RollNo = Label(frame2,text="Rollno",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    RollNo.grid(row = 2,column=0,pady=10,padx=10,sticky=W)
    entry1 = Entry(frame2,textvariable=Var1,font=("times new roman",14,"bold"))
    entry1.grid(row=2,column=1,padx=10,sticky=W)
    entry1.focus()

    clr = Button(frame2,text="DELETE",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=DELETE1)
    clr.grid(row =4 ,columnspan=2,pady=10,sticky=E)
    frame2.pack(fill=BOTH,expand=1)
##################################

##################################
    Tab2.add(frame1,text="Faculty")
    Tab2.add(frame2,text="Student")
    style1 = ttk.Style()
    style1.configure('TNotebook.Tab',foreground="Crimson",background="white",font=("times new roman",16,"bold"),padding=[5,2])
    Tab2.place(x=5,y=560,width=400,height=215)
####################################

###################################################################################
                ###################     DATABASE FRAME          ###################
###################################################################################
    Tab3 = Notebook(admin1)
    frame1 = Frame(Tab3,width=400,height=705,bg="crimson")
    Search = Button(frame1,text="Search By Name",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=Search)
    Search.place(x=855,y=10)
    entry1 = Entry(frame1,textvariable=Var2,font=("times new roman",14,"bold"))
    entry1.place(x=635,y=15)
    entry1.focus()
    label = Label(frame1,text="Search By",font=("times new roman",15,"bold"),fg="white",bg="crimson")
    label.place(x=150,y=15)
    Com2 = Combobox(frame1,values=['Name','Rollno'],font=("times new roman",14,"bold"))
    Com2.place(x=250,y=15)
    View = Button(frame1,text="View All",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=ViewAll)
    View.place(x=10,y=10)

    def fetch_data():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("Select * from Faculty4")
        rows=result.fetchall()
        if len(rows)!=0:
            Table.delete(*Table.get_children())
            for row in rows:
                Table.insert('',END,values=row)
            conn.commit()
        conn.close()
    frame1a = Frame(frame1,relief=RIDGE,bd=4,bg="crimson")

    scroll_x = Scrollbar(frame1a,orient=HORIZONTAL)
    scroll_v = Scrollbar(frame1a,orient=VERTICAL)
    Table = ttk.Treeview(frame1a,columns=("ID","Name","Phoneno","Gender","Address","Subject"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_v.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_v.pack(side=RIGHT,fill=Y)
    scroll_x.configure(command=Table.xview)
    scroll_v.configure(command=Table.yview)
    Table.heading("ID",text="ID")
    Table.heading("Name",text="Name")
    Table.heading("Phoneno",text="Phoneno")
    Table.heading("Gender",text="Gender")
    Table.heading("Address",text="Address")
    Table.heading("Subject",text="Subject")
    Table.column("ID",width=110)
    Table.column("Name",width=150)
    Table.column("Phoneno",width=110)
    Table.column("Gender",width=110)
    Table.column("Address",width=200)
    Table.column("Subject",width=110)
    Table['show']='headings'
    fetch_data()
    Table.pack(fill=BOTH,expand=1)

    frame1a.place(x=10,y=50,width=980,height=630)

    frame1.pack(fill=BOTH,expand=1)

################################

################################
    frame2 = Frame(Tab3,width=400,height=705,bg="crimson")

    Search = Button(frame2,text="Search By",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=Search1)
    Search.place(x=855,y=10)
    entry1 = Entry(frame2,textvariable=Var2, font=("times new roman",14,"bold"))
    entry1.place(x=635,y=15)
    entry1.focus()
    View = Button(frame2,text="View All",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=ViewAll1)
    View.place(x=10,y=1)

    def fetch_data1():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("Select * from Student")
        rows=result.fetchall()
        if len(rows)!=0:
            Table1.delete(*Table1.get_children())
            for row in rows:
                Table1.insert('',END,values=row)
            conn.commit()
        conn.close()

    
    
    frame1a = Frame(frame2,relief=RIDGE,bd=4,bg="crimson")


    scroll_x = Scrollbar(frame1a,orient=HORIZONTAL)
    scroll_v = Scrollbar(frame1a,orient=VERTICAL)
    Table1 = ttk.Treeview(frame1a,columns=("Rollno","Name","Phoneno","Gender","Address","Class"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_v.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_v.pack(side=RIGHT,fill=Y)
    scroll_x.configure(command=Table1.xview)
    scroll_v.configure(command=Table1.yview)
    Table1.heading("Rollno",text="Rollno")
    Table1.heading("Name",text="Name")
    Table1.heading("Phoneno",text="Phoneno")
    Table1.heading("Gender",text="Gender")
    Table1.heading("Address",text="Address")
    Table1.heading("Class",text="Class")
    Table1.column("Name",width=150)
    Table1.column("Rollno",width=110)
    Table1.column("Phoneno",width=110)
    Table1.column("Gender",width=110)
    Table1.column("Address",width=200)
    Table1.column("Class",width=110)
    
    Table1['show']='headings'
    fetch_data1()
    Table1.pack(fill=BOTH,expand=1)

    frame1a.place(x=10,y=50,width=980,height=630)
    frame2.pack(fill=BOTH,expand=1)

    Tab3.add(frame1,text="Faculty")
    Tab3.add(frame2,text="Student")
    Tab3.place(x=410,y=55,width=1000,height=720)

    Next = Button(admin1,text="Next->",font=("times new roman",16,"bold"),fg="white",bg="crimson",activebackground="white",activeforeground="crimson",command=Admin2)
    Next.pack(side=RIGHT,padx=20)



##################################################################      Admin 2         ########################################################
##################################################################                      ##########################################################

  
    
def Admin2():
    admin2=Toplevel()
    admin2.title("Student Management System")
    admin2.geometry("1535x800+0+0")
    admin2.resizable(0,0)

#FRAME1    
    frame = Frame(admin2,bg="yellow",height=300)    
    bt1 = Button(frame,text="ADMIN",font=("times new roman",16,"bold"),bg="yellow",fg="green",activebackground="red",activeforeground="blue",padx=20,pady=5)
    bt1.pack(side=LEFT,fill=X)
    label = Label(frame,text="Student Management System Timing(8am to 10pm)",font=("times new roman",16,"bold"),bg="yellow",fg="green")
    label.pack(side=RIGHT,padx=30)
    frame.pack(side=TOP,fill=X)


################################################################################################################
                        ########################        ALL CALCULATION         ################################
################################################################################################################


    
    def Create():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        #c.execute("Create Table Marksheet (Rollno text,Name text,CLASS text,JAVA int,JAVATW int, JAVAPR int ,GAD int,GADTW int,GADPR int,SEN int,SENTW int,SENPR int,DCC int,DCCTW int,DCCPR int,MIC int,MICTW int,MICPR int,TOTAL text,PERCENTAGE text,GRADE text)")
        conn.commit()
        conn.close()
    Create()
    
    def Search3():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Marksheet WHERE  Name LIKE '%"+str(Var2.get())+"%'")
        rows=result.fetchall()

        if len(rows)!=0:
            Marksheet.delete(*Marksheet.get_children())
            for row in rows:
                Marksheet.insert('',END,values=row)
            conn.commit()
            print("ok Search")
        conn.close()
        
    def ViewAll3():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Marksheet")
        rows=result.fetchall()
        if len(rows)!=0:
            Marksheet.delete(*Marksheet.get_children())
            for row in rows:
                Marksheet.insert('',END,values=row)
            conn.commit()
            print("okview")
        conn.close()
        
    frame3 = Frame(admin2,bg="crimson")


    Search = Button(frame3,text="Search By Name",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=Search3)
    Search.place(x=740,y=10)
    entry1 = Entry(frame3,textvariable=Var2,font=("times new roman",14,"bold"))
    entry1.place(x=530,y=15)
    entry1.focus()
    View = Button(frame3,text="View All",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=ViewAll3)
    View.place(x=5,y=10)

    
    def fetch_data2():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("Select * from Marksheet")
        rows=result.fetchall()
        if len(rows)!=0:
            Marksheet.delete(*Marksheet.get_children())
            for row in rows:
                Marksheet.insert('',END,values=row)
            conn.commit()
        conn.close()

        
    frame3a = Frame(frame3,relief=RIDGE,bd=4,bg="white")
    scroll_x = Scrollbar(frame3a,orient=HORIZONTAL)
    scroll_v = Scrollbar(frame3a,orient=VERTICAL)
    Marksheet = ttk.Treeview(frame3a,columns=("Rollno","Name","CLASS","JAVA","JAVATW","JAVAPR" ,"GAD","GADTW","GADPR","SEN","SENTW","SENPR","DCC","DCCTW","DCCPR","MIC","MICTW","MICPR","TOTAL","PERCENTAGE","GRADE"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_v.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_v.pack(side=RIGHT,fill=Y)

    scroll_x.configure(command=Marksheet.xview)
    scroll_v.configure(command=Marksheet.yview)

    Marksheet.heading("Rollno",text="ROLLNO")
    Marksheet.heading("Name",text="NAME")
    Marksheet.heading("CLASS",text="CLASS")
    Marksheet.heading("JAVA",text="JAVA")
    Marksheet.heading("JAVATW",text="JAVATW")
    Marksheet.heading("JAVAPR",text="JAVAPR")
    Marksheet.heading("GAD",text="GAD")
    Marksheet.heading("GADTW",text="GADTW")
    Marksheet.heading("GADPR",text="GADPR")
    Marksheet.heading("SEN",text="SEN")
    Marksheet.heading("SENTW",text="SENTW")
    Marksheet.heading("SENPR",text="SENPR")
    Marksheet.heading("DCC",text="DCC")
    Marksheet.heading("DCCTW",text="DCCTW")
    Marksheet.heading("DCCPR",text="DCCPR")
    Marksheet.heading("MIC",text="MIC")
    Marksheet.heading("MICTW",text="MICTW")
    Marksheet.heading("MICPR",text="MICPR")
    Marksheet.heading("TOTAL",text="TOTAL")
    Marksheet.heading("PERCENTAGE",text="PERCENTAGE")
    Marksheet.heading("GRADE",text="GRADE")
    
    Marksheet['show']='headings'

    Marksheet.column("Rollno",width=100)
    Marksheet.column("Name",width=100)
    Marksheet.column("CLASS",width=100)
    Marksheet.column("JAVA",width=100)
    Marksheet.column("JAVATW",width=100)
    Marksheet.column("JAVAPR",width=100)
    Marksheet.column("GAD",width=100)
    Marksheet.column("GADTW",width=100)
    Marksheet.column("GADPR",width=100)  
    Marksheet.column("SEN",width=100)
    Marksheet.column("SENTW",width=100)
    Marksheet.column("SENPR",width=100)
    Marksheet.column("DCC",width=100)
    Marksheet.column("DCCTW",width=100)
    Marksheet.column("DCCPR",width=100)
    Marksheet.column("MIC",width=100)
    Marksheet.column("MICTW",width=100)
    Marksheet.column("MICPR",width=100)
    Marksheet.column("TOTAL",width=100)
    Marksheet.column("PERCENTAGE",width=100)
    Marksheet.column("GRADE",width=100)
    Marksheet.pack(fill=BOTH,expand=1)
    
    frame3a.place(x=5,y=95,width=890,height=610)
    frame3.place(x=10,y=60,width=900,height=715)
########################################################################
             #############           AVERAGE             ###############
########################################################################
    frame3b = Frame(admin2,width=490,height=180,relief=RIDGE,bd=4,bg="crimson")

    title = Label(frame3b,text="Average passing marks of classes",font=("times new roman",20,"bold"),fg="white",bg="crimson")
    title.grid(row = 1,columnspan=3,pady=40,padx=50,sticky=W)

    #entry2 = Combobox(frame3b,textvariable=,values=['Class1','Class2','Class3']font=("times new roman",14,"bold"))
    #entry2.grid(row=2,column=1,pady=30,padx=10,sticky=W)

    def getclass1():
        conn = sqlite3.connect("StudMang.db")
        c=conn.cursor()
        avg = c.execute("Select avg(TOTAL) from Marksheet where CLASS='Class1'")
        average = avg.fetchall()
        entry01.config(text=str(average[0]))
        print("Average of ",average)
        conn.commit()
        conn.close()

    def getclass2():
        conn = sqlite3.connect("StudMang.db")
        c=conn.cursor()
        avg = c.execute("Select avg(TOTAL) from Marksheet where CLASS='Class2'")
        average = avg.fetchall()
        entry02.config(text=str(average[0]))
        print("Average of ",average)
        conn.commit()
        conn.close()

    def getclass3():
        conn = sqlite3.connect("StudMang.db")
        c=conn.cursor()
        avg = c.execute("Select avg(TOTAL) from Marksheet where CLASS='Class3'")
        average = avg.fetchall()
        entry03.config(text=str(average[0]))
        print("Average of ",average)
        conn.commit()
        conn.close()
    
    
    CLASS1 = Button(frame3b,text="Class1",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=getclass1)
    CLASS1.grid(row =3 ,column=0,pady=10,padx=10,sticky=W)
    CLASS2 = Button(frame3b,text="Class2",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=getclass2)
    CLASS2.grid(row =4 ,column=0,pady=10,padx=10,sticky=W)
    CLASS3 = Button(frame3b,text="Class3",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=getclass3)
    CLASS3.grid(row =5 ,column=0,pady=10,padx=10,sticky=W)
    
    entry01 = Label(frame3b,font=("times new roman",14,"bold"),width=25,height=1)
    entry01.grid(row=3,column=1,pady=10,padx=10,sticky=W)
    entry02 = Label(frame3b,font=("times new roman",14,"bold"),width=25,height=1)
    entry02.grid(row=4,column=1,pady=10,padx=10,sticky=W)
    entry03 = Label(frame3b,font=("times new roman",14,"bold"),width=25,height=1)
    entry03.grid(row=5,column=1,pady=10,padx=10,sticky=W)
    
    frame3b.place(x=920,y=60,width=590,height=380)

    fetch = StringVar()
         
    frame3c = Frame(admin2,relief=RIDGE,bd=4,bg="crimson")

    Var = StringVar()
     
    def getjava():
        conn = sqlite3.connect("StudMang.db")
        c=conn.cursor()
        avg = c.execute("Select avg(JAVA) from Marksheet")
        average = avg.fetchall()
        entry1.config(text=str(average[0]))
        print("Average of ",average)
        conn.commit()
        conn.close()

    def getgad():
        conn = sqlite3.connect("StudMang.db")
        c=conn.cursor()
        avg = c.execute("Select avg(GAD) from Marksheet")
        average = avg.fetchall()
        entry2.config(text=str(average[0]))
        print("Average of ",average)
        conn.commit()
        conn.close()

    def getsen():
        conn = sqlite3.connect("StudMang.db")
        c=conn.cursor()
        avg = c.execute("Select avg(SEN) from Marksheet")
        average = avg.fetchall()
        entry3.config(text=str(average[0]))
        print("Average of ",average)
        conn.commit()
        conn.close()

    def getdcc():
        conn = sqlite3.connect("StudMang.db")
        c=conn.cursor()
        avg = c.execute("Select avg(DCC) from Marksheet")
        average = avg.fetchall()
        entry4.config(text=str(average[0]))
        print("Average of ",average)
        conn.commit()
        conn.close()

    def getmic():
        conn = sqlite3.connect("StudMang.db")
        c=conn.cursor()
        avg = c.execute("Select avg(MIC) from Marksheet")
        average = avg.fetchall()
        entry5.config(text=str(average[0]))
        print("Average of ",average)
        conn.commit()
        conn.close() 
        
    title = Label(frame3c,text="Average passing marks of Subjects",font=("times new roman",20,"bold"),fg="white",bg="crimson")
    title.grid(row = 1,columnspan=3,pady=5,padx=50,sticky=W)
    JAVA = Button(frame3c,text="JAVA",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=getjava)
    JAVA.grid(row =2 ,column=0,pady=2,padx=10,sticky=W)
    GAD = Button(frame3c,text="GAD",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=getgad)
    GAD.grid(row =3 ,column=0,pady=2,padx=10,sticky=W)
    SEN = Button(frame3c,text="SEN",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=getsen)
    SEN.grid(row =4 ,column=0,pady=2,padx=10,sticky=W)
    DCC = Button(frame3c,text="DCC",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=getdcc)
    DCC.grid(row =5 ,column=0,pady=2,padx=10,sticky=W)
    MIC = Button(frame3c,text="MIC",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=getmic)
    MIC.grid(row =6 ,column=0,pady=2,padx=10,sticky=W)
        
    entry1 = Label(frame3c,font=("times new roman",12,"bold"),width=25,height=1,bg="white")
    entry1.grid(row=2,column=1,pady=2,padx=10,sticky=W)
    entry2 = Label(frame3c,font=("times new roman",12,"bold"),width=25,height=1,bg="white")
    entry2.grid(row=3,column=1,pady=2,padx=10,sticky=W)
    entry3 = Label(frame3c,font=("times new roman",12,"bold"),width=25,height=1,bg="white")
    entry3.grid(row=4,column=1,pady=2,padx=10,sticky=W)
    entry4 = Label(frame3c,font=("times new roman",12,"bold"),width=25,height=1,bg="white")
    entry4.grid(row=5,column=1,pady=2,padx=10,sticky=W)
    entry5 = Label(frame3c,font=("times new roman",12,"bold"),width=25,height=1,bg="white")
    entry5.grid(row=6,column=1,pady=2,padx=10,sticky=W)
    Back = Button(frame3c,text="<-Back",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=Admin1)
    Back.grid(row=4,column=2,padx=10,pady=20,sticky=E)
    frame3c.place(x=920,y=450,width=590,height=310)

#####################################################################################################################################################
    ##############################################          Student window          #################################################################
#####################################################################################################################################################
def Student():

    stu=Toplevel()
    stu.title("Student Management System")
    stu.geometry("1535x800+0+0")
    stu.resizable(0,0)


#FRAME1

    stud = StringVar()
    
    def Search4():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Marksheet WHERE  Name LIKE '%"+str(stud.get())+"%'")
        rows=result.fetchall()

        if len(rows)!=0:
            Marksheet.delete(*Marksheet.get_children())
            for row in rows:
                Marksheet.insert('',END,values=row)
            conn.commit()
        print("ok Search")
        conn.close()
        
    
    frame = Frame(stu,bg="yellow",height=300)    
    bt1 = Button(frame,text="STUDENT",font=("times new roman",16,"bold"),bg="yellow",fg="green",activebackground="red",activeforeground="blue",padx=20,pady=5)
    bt1.pack(side=LEFT,fill=X)
    label = Label(frame,text="Student Management System Timing(8am to 10pm)",font=("times new roman",16,"bold"),bg="yellow",fg="green")
    label.pack(side=RIGHT,padx=30)
    frame.pack(side=TOP,fill=X)

    frame3 = Frame(stu,bg="crimson")

    Enter = Label(frame3,text="Enter password",font=("times new roman",16,"bold"),bg="crimson",fg="white")
    Enter.place(x=5,y=10)
    entry = Entry(frame3,textvariable=stud,font=("times new roman",16,"bold"))
    entry.place(x=200,y=10)
    View = Button(frame3,text="View Marksheet",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=Search4)
    View.place(x=450,y=10)

    frame3a = Frame(frame3,relief=RIDGE,bd=4,bg="white")
    scroll_x = Scrollbar(frame3a,orient=HORIZONTAL)
    scroll_v = Scrollbar(frame3a,orient=VERTICAL)
    Marksheet = ttk.Treeview(frame3a,columns=("Rollno","Name","CLASS","JAVA","JAVATW","JAVAPR","GAD","GADTW","GADPR","SEN","SENTW","SENPR","DCC","DCCTW","DCCPR","MIC","MICTW","MICPR","TOTAL","PERCENTAGE","GRADE"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_v.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_v.pack(side=RIGHT,fill=Y)

    scroll_x.configure(command=Marksheet.xview)
    scroll_v.configure(command=Marksheet.yview)

    Marksheet.heading("Rollno",text="ROLLNO")
    Marksheet.heading("Name",text="NAME")
    Marksheet.heading("CLASS",text="CLASS")
    Marksheet.heading("JAVA",text="JAVA")
    Marksheet.heading("JAVATW",text="JAVATW")
    Marksheet.heading("JAVAPR",text="JAVAPR")
    Marksheet.heading("GAD",text="GAD")
    Marksheet.heading("GADTW",text="GADTW")
    Marksheet.heading("GADPR",text="GADPR")
    Marksheet.heading("SEN",text="SEN")
    Marksheet.heading("SENTW",text="SENTW")
    Marksheet.heading("SENPR",text="SENPR")
    Marksheet.heading("DCC",text="DCC")
    Marksheet.heading("DCCTW",text="DCCTW")
    Marksheet.heading("DCCPR",text="DCCPR")
    Marksheet.heading("MIC",text="MIC")
    Marksheet.heading("MICTW",text="MICTW")
    Marksheet.heading("MICPR",text="MICPR")
    Marksheet.heading("TOTAL",text="TOTAL")
    Marksheet.heading("PERCENTAGE",text="PERCENTAGE")
    Marksheet.heading("GRADE",text="GRADE")
    Marksheet.heading("CLASS",text="CLASS")
    
    Marksheet['show']='headings'

    Marksheet.column("Rollno",width=100)
    Marksheet.column("Name",width=100)
    Marksheet.column("CLASS",width=100)
    Marksheet.column("JAVA",width=100)
    Marksheet.column("JAVATW",width=100)
    Marksheet.column("JAVAPR",width=100)
    Marksheet.column("GAD",width=100)
    Marksheet.column("GADTW",width=100)
    Marksheet.column("GADPR",width=100)  
    Marksheet.column("SEN",width=100)
    Marksheet.column("SENTW",width=100)
    Marksheet.column("SENPR",width=100)
    Marksheet.column("DCC",width=100)
    Marksheet.column("DCCTW",width=100)
    Marksheet.column("DCCPR",width=100)
    Marksheet.column("MIC",width=100)
    Marksheet.column("MICTW",width=100)
    Marksheet.column("MICPR",width=100)
    Marksheet.column("TOTAL",width=100)
    Marksheet.column("PERCENTAGE",width=100)
    Marksheet.column("GRADE",width=100)   

    Marksheet.pack(fill=BOTH,expand=1)
    frame3a.place(x=5,y=95,width=990,height=610)
    frame3.place(x=10,y=60,width=1000,height=715)





###################################################################################################################################################################################
    #######################################################         FACULTY PAGE  ###########################################################
###################################################################################################################################################################################
def Faculty():

    facult=Toplevel(root)
    facult.title("Student Management System")
    facult.geometry("1535x800+0+0")
    facult.resizable(0,0)

    
#FRAME1

    rollno = StringVar()
    name = StringVar()
    java = StringVar()
    java2 = StringVar()
    java3 = StringVar()
    Class = StringVar()

    def fetch_data3():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("Select * from Marksheet")
        rows=result.fetchall()
        if len(rows)!=0:
            Marksheet.delete(*Marksheet.get_children())
            for row in rows:
                Marksheet.insert('',END,values=row)
            conn.commit()
        conn.close()

    def clear1():
        Var1.set('')
        Var2.set('')
        Var3.set('')
        Var4.set('')
        Var5.set('')
        Var6.set('')
        
    def AddMarks():    
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()                                           
        c.execute("Insert into Marksheet(Rollno,Name,JAVA,JAVATW,JAVAPR,CLASS) values(?,?,?,?,?,?)",(rollno.get(),name.get(),java.get(),java2.get(),java3.get(),Class.get()))
        print("Student Add")
        conn.commit()
        fetch_data3()
        clear1()
        conn.close()

    
    frame = Frame(facult,bg="yellow",height=300)    
    bt1 = Button(frame,text="FACULTY",font=("times new roman",16,"bold"),bg="yellow",fg="green",activebackground="red",activeforeground="blue",padx=20,pady=5)
    bt1.pack(side=LEFT,fill=X)
    label = Label(frame,text="Student Management System Timing(8am to 10pm)",font=("times new roman",16,"bold"),bg="yellow",fg="green")
    label.pack(side=RIGHT,padx=30)
    frame.pack(side=TOP,fill=X)

    frame1 = Frame(facult,relief=RIDGE,bd=4,bg="crimson")
    Title = Label(frame1,text="MANAGE MARKS ",font=("times new roman",20,"bold"),fg="white",bg="crimson")
    Title.grid(row = 1,columnspan=2,pady=20,padx=10,sticky=E)

    Name = Label(frame1,text="Name",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Name.grid(row = 2,column=0,pady=10,padx=10,sticky=W)
    entry4 = Entry(frame1,textvariable=name,font=("times new roman",14,"bold"))
    entry4.grid(row=2,column=1,padx=10,sticky=W)

    Rollno = Label(frame1,text="RollNo",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Rollno.grid(row = 3,column=0,pady=10,padx=10,sticky=W)
    entry5 = Entry(frame1,textvariable=rollno,font=("times new roman",14,"bold"))
    entry5.grid(row=3,column=1,padx=10,sticky=W)

    JAVA = Label(frame1,text="JAVA",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    JAVA.grid(row = 4,column=0,pady=10,padx=10,sticky=W)
    entry1 = Entry(frame1,textvariable=java,font=("times new roman",14,"bold"))
    entry1.grid(row=4,column=1,padx=10,sticky=W)
    entry1.focus()
    
    JAVATW = Label(frame1,text="Termwork",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    JAVATW.grid(row = 5,column=0,pady=10,padx=10,sticky=W)
    entry2 = Entry(frame1,textvariable=java2,font=("times new roman",14,"bold"))
    entry2.grid(row=5,column=1,padx=10,sticky=W)
    
    practicle = Label(frame1,text="Practicle",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    practicle.grid(row = 6,column=0,pady=10,padx=10,sticky=W)
    entry3 = Entry(frame1,textvariable=java3,font=("times new roman",14,"bold"))
    entry3.grid(row=6,column=1,padx=10,sticky=W)
    
    Class1 = Label(frame1,text="Select Class",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Class1.grid(row = 7,column=0,pady=10,padx=10,sticky=W)
    entry3 = Combobox(frame1,textvariable=Class,values=["Class1","Class2","Class3"],font=("times new roman",14,"bold"))
    entry3.grid(row=7,column=1,padx=10,sticky=W)

    SHOW = Button(frame1,text="ADD",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=AddMarks)
    SHOW.grid(row =7 ,column=3,pady=10,padx=20,sticky=W)    

    nam = StringVar()
    def Search5():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Student WHERE  Name LIKE '%"+str(nam.get())+"%'")
        rows=result.fetchall()

        if len(rows)!=0:
            Table3.delete(*Table3.get_children())
            for row in rows:
                Table3.insert('',END,values=row)
            conn.commit()
        print("okSearch")
        conn.close()

    def Search6():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Student")
        rows=result.fetchall()

        if len(rows)!=0:
            Table3.delete(*Table3.get_children())
            for row in rows:
                Table3.insert('',END,values=row)
            conn.commit()
        print("okSearch")
        conn.close()
    
    frame1.place(x=10,y=55,width=700,height=390)

    frame2 = Frame(facult,relief=RIDGE,bd=4,bg="crimson")

    Search = Button(frame2,text="Search By Name",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=Search5)
    Search.place(x=555,y=10)
    entry1 = Entry(frame2,textvariable=nam,font=("times new roman",14,"bold"))
    entry1.place(x=335,y=15)
    entry1.focus()
    View = Button(frame2,text="View All",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=Search6)
    View.place(x=10,y=10)

    frame1a = Frame(frame2,relief=RIDGE,bd=4,bg="crimson")

    scroll_x = Scrollbar(frame1a,orient=HORIZONTAL)
    scroll_v = Scrollbar(frame1a,orient=VERTICAL)
    Table3 = ttk.Treeview(frame1a,columns=("Rollno","Name","Phoneno","Gender","Address","Class"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_v.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_v.pack(side=RIGHT,fill=Y)
    scroll_x.configure(command=Table3.xview)
    scroll_v.configure(command=Table3.yview)
    Table3.heading("Rollno",text="ID")
    Table3.heading("Name",text="Name")
    Table3.heading("Phoneno",text="Phoneno")
    Table3.heading("Gender",text="Gender")
    Table3.heading("Address",text="Address")
    Table3.heading("Class",text="Class")
    Table3.column("Rollno",width=110)
    Table3.column("Name",width=150)
    Table3.column("Phoneno",width=110)
    Table3.column("Gender",width=110)
    Table3.column("Address",width=200)
    Table3.column("Class",width=110)
    Table3['show']='headings'
    Table3.pack(fill=BOTH,expand=1)

    ################################################  ZAIBA MALIK ##################################################################

    def Average1():
        conn = sqlite3.connect("StudMang.db")
        c=conn.cursor()
        avg = c.execute("Select avg(JAVA) from Marksheet")
        average = avg.fetchall()
        entry2.config(text=str(average[0]))
        print("Average of ",average)
        conn.commit()
        conn.close()
    
    frame1a.place(x=10,y=60,width=580,height=300)
    frame2.place(x=725,y=55,width=760,height=380)

    frame3 = Frame(facult,relief=RIDGE,bd=4,bg="crimson")
    title = Label(frame3,text="Average passing marks of Subjects",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    title.grid(row = 1,columnspan=3,pady=10,padx=50,sticky=W)
    Select = Label(frame3,text="Select",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Select.grid(row = 2,column=0,pady=10,padx=10,sticky=W)
    vlist = ["JAVA"]
    entry = Combobox(frame3,values=vlist,font=("times new roman",13,"bold"))
    entry.grid(row=2,column=1,padx=10,sticky=W)
    SHOW = Button(frame3,text="SHOW",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=Average1)
    SHOW.grid(row =4 ,column=0,pady=40,padx=10,sticky=W)
    entry2 = Label(frame3,font=("times new roman",14,"bold"),width=20,height=1)
    entry2.grid(row=4,column=1,pady=40,padx=10,sticky=W)
    frame3.place(x=10,y=445,width=700,height=310)

    sam = StringVar()
    
    def Search6():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Marksheet WHERE  Name LIKE '%"+str(sam.get())+"%'")
        rows=result.fetchall()

        if len(rows)!=0:
            Marksheet.delete(*Marksheet.get_children())
            for row in rows:
                Marksheet.insert('',END,values=row)
            conn.commit()
        print("okSearch")
        conn.close()

    def Search7():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Marksheet")
        rows=result.fetchall()

        if len(rows)!=0:
            Marksheet.delete(*Marksheet.get_children())
            for row in rows:
                Marksheet.insert('',END,values=row)
            conn.commit()
        print("okSearch")
        conn.close()
    
    frame4 = Frame(facult,relief=RIDGE,bd=4,bg="crimson")
    Title = Label(frame4,text="Marksheet Of Students",font=("times new roman",15,"bold"),fg="white",bg="crimson")
    Title.place(x=130,y=10,width=200)
    Search = Button(frame4,text="Search By Name",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=Search6)
    Search.place(x=615,y=10)
    entry1 = Entry(frame4,textvariable=sam,font=("times new roman",14,"bold"))
    entry1.place(x=385,y=15)
    entry1.focus()
    View = Button(frame4,text="View All",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=Search7)
    View.place(x=10,y=10)


    frame3a=Frame(frame4,relief=RIDGE,bd=4,bg="white")
    scroll_x = Scrollbar(frame3a,orient=HORIZONTAL)
    scroll_v = Scrollbar(frame3a,orient=VERTICAL)
    Marksheet = ttk.Treeview(frame3a,columns=("Rollno","Name","CLASS","JAVA","JAVATW","JAVAPR" ,"GAD","GADTW","GADPR","SEN","SENTW","SENPR","DCC","DCCTW","DCCPR","MIC","MICTW","MICPR","TOTAL","PERCENTAGE","GRADE"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_v.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_v.pack(side=RIGHT,fill=Y)

    scroll_x.configure(command=Marksheet.xview)
    scroll_v.configure(command=Marksheet.yview)

    Marksheet.heading("Rollno",text="ROLLNO")
    Marksheet.heading("Name",text="NAME")
    Marksheet.heading("CLASS",text="CLASS")
    Marksheet.heading("JAVA",text="JAVA")
    Marksheet.heading("JAVATW",text="JAVATW")
    Marksheet.heading("JAVAPR",text="JAVAPR")
    Marksheet.heading("GAD",text="GAD")
    Marksheet.heading("GADTW",text="GADTW")
    Marksheet.heading("GADPR",text="GADPR")
    Marksheet.heading("SEN",text="SEN")
    Marksheet.heading("SENTW",text="SENTW")
    Marksheet.heading("SENPR",text="SENPR")
    Marksheet.heading("DCC",text="DCC")
    Marksheet.heading("DCCTW",text="DCCTW")
    Marksheet.heading("DCCPR",text="DCCPR")
    Marksheet.heading("MIC",text="MIC")
    Marksheet.heading("MICTW",text="MICTW")
    Marksheet.heading("MICPR",text="MICPR")
    Marksheet.heading("TOTAL",text="TOTAL")
    Marksheet.heading("PERCENTAGE",text="PERCENTAGE")
    Marksheet.heading("GRADE",text="GRADE")
    Marksheet.heading("CLASS",text="CLASS")
    
    Marksheet['show']='headings'

    Marksheet.column("Rollno",width=100)
    Marksheet.column("Name",width=100)
    Marksheet.column("CLASS",width=100)
    Marksheet.column("JAVA",width=100)
    Marksheet.column("JAVATW",width=100)
    Marksheet.column("JAVAPR",width=100)
    Marksheet.column("GAD",width=100)
    Marksheet.column("GADTW",width=100)
    Marksheet.column("GADPR",width=100)  
    Marksheet.column("SEN",width=100)
    Marksheet.column("SENTW",width=100)
    Marksheet.column("SENPR",width=100)
    Marksheet.column("DCC",width=100)
    Marksheet.column("DCCTW",width=100)
    Marksheet.column("DCCPR",width=100)
    Marksheet.column("MIC",width=100)
    Marksheet.column("MICTW",width=100)
    Marksheet.column("MICPR",width=100)
    Marksheet.column("TOTAL",width=100)
    Marksheet.column("PERCENTAGE",width=100)
    Marksheet.column("GRADE",width=100)


    Marksheet.pack(fill=BOTH,expand=1)

    frame3a.place(x=0,y=80,width=750,height=225)
    frame4.place(x=725,y=435,width=760,height=320)

def Ali():
    facult=Toplevel(root)
    facult.title("Student Management System")
    facult.geometry("1535x800+0+0")
    facult.resizable(0,0)

    
#FRAME1

    rollno = StringVar()
    name = StringVar()
    DCC = StringVar()
    DCC2 = StringVar()
    DCC3 = StringVar()
    Class = StringVar()

    def fetch_data3():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("Select * from Marksheet")
        rows=result.fetchall()
        if len(rows)!=0:
            Marksheet.delete(*Marksheet.get_children())
            for row in rows:
                Marksheet.insert('',END,values=row)
            conn.commit()
        conn.close()

    def clear1():
        Var1.set('')
        Var2.set('')
        Var3.set('')
        Var4.set('')
        Var5.set('')
        Var6.set('')
        
    def AddMarks():    
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()                                           
        c.execute("Insert into Marksheet(Rollno,Name,DCC,DCCTW,DCCPR,CLASS) values(?,?,?,?,?,?)",(rollno.get(),name.get(),DCC.get(),DCC2.get(),DCC3.get(),Class.get()))
        print("Student Add")
        conn.commit()
        fetch_data3()
        clear1()
        conn.close()

    
    frame = Frame(facult,bg="yellow",height=300)    
    bt1 = Button(frame,text="FACULTY",font=("times new roman",16,"bold"),bg="yellow",fg="green",activebackground="red",activeforeground="blue",padx=20,pady=5)
    bt1.pack(side=LEFT,fill=X)
    label = Label(frame,text="Student Management System Timing(8am to 10pm)",font=("times new roman",16,"bold"),bg="yellow",fg="green")
    label.pack(side=RIGHT,padx=30)
    frame.pack(side=TOP,fill=X)

    frame1 = Frame(facult,relief=RIDGE,bd=4,bg="crimson")
    Title = Label(frame1,text="MANAGE MARKS ",font=("times new roman",20,"bold"),fg="white",bg="crimson")
    Title.grid(row = 1,columnspan=2,pady=20,padx=10,sticky=E)

    Name = Label(frame1,text="Name",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Name.grid(row = 2,column=0,pady=10,padx=10,sticky=W)
    entry4 = Entry(frame1,textvariable=name,font=("times new roman",14,"bold"))
    entry4.grid(row=2,column=1,padx=10,sticky=W)

    Rollno = Label(frame1,text="RollNo",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Rollno.grid(row = 3,column=0,pady=10,padx=10,sticky=W)
    entry5 = Entry(frame1,textvariable=rollno,font=("times new roman",14,"bold"))
    entry5.grid(row=3,column=1,padx=10,sticky=W)

    dcc = Label(frame1,text="DCC",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    dcc.grid(row = 4,column=0,pady=10,padx=10,sticky=W)
    entry1 = Entry(frame1,textvariable=DCC,font=("times new roman",14,"bold"))
    entry1.grid(row=4,column=1,padx=10,sticky=W)
    entry1.focus()
    
    dccTW = Label(frame1,text="Termwork",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    dccTW.grid(row = 5,column=0,pady=10,padx=10,sticky=W)
    entry2 = Entry(frame1,textvariable=DCC2,font=("times new roman",14,"bold"))
    entry2.grid(row=5,column=1,padx=10,sticky=W)
    
    practicle = Label(frame1,text="Practicle",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    practicle.grid(row = 6,column=0,pady=10,padx=10,sticky=W)
    entry3 = Entry(frame1,textvariable=DCC3,font=("times new roman",14,"bold"))
    entry3.grid(row=6,column=1,padx=10,sticky=W)
    
    Class1 = Label(frame1,text="Select Class",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Class1.grid(row = 7,column=0,pady=10,padx=10,sticky=W)
    entry3 = Combobox(frame1,textvariable=Class,values=["Class1","Class2","Class3"],font=("times new roman",14,"bold"))
    entry3.grid(row=7,column=1,padx=10,sticky=W)

    SHOW = Button(frame1,text="ADD",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=AddMarks)
    SHOW.grid(row =7 ,column=3,pady=10,padx=20,sticky=W)    

    nam = StringVar()
    def SearchDCC():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Student WHERE  Name LIKE '%"+str(nam.get())+"%'")
        rows=result.fetchall()

        if len(rows)!=0:
            Table3.delete(*Table3.get_children())
            for row in rows:
                Table3.insert('',END,values=row)
            conn.commit()
        print("okSearch")
        conn.close()

    def SearchDCC1():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Student")
        rows=result.fetchall()

        if len(rows)!=0:
            Table3.delete(*Table3.get_children())
            for row in rows:
                Table3.insert('',END,values=row)
            conn.commit()
        print("okSearch")
        conn.close()
    
    frame1.place(x=10,y=55,width=700,height=390)

    frame2 = Frame(facult,relief=RIDGE,bd=4,bg="crimson")

    Search = Button(frame2,text="Search By Name",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=SearchDCC)
    Search.place(x=555,y=10)
    entry1 = Entry(frame2,textvariable=nam,font=("times new roman",14,"bold"))
    entry1.place(x=335,y=15)
    entry1.focus()
    View = Button(frame2,text="View All",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=SearchDCC1)
    View.place(x=10,y=10)

    frame1a = Frame(frame2,relief=RIDGE,bd=4,bg="crimson")

    scroll_x = Scrollbar(frame1a,orient=HORIZONTAL)
    scroll_v = Scrollbar(frame1a,orient=VERTICAL)
    Table3 = ttk.Treeview(frame1a,columns=("Rollno","Name","Phoneno","Gender","Address","Class"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_v.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_v.pack(side=RIGHT,fill=Y)
    scroll_x.configure(command=Table3.xview)
    scroll_v.configure(command=Table3.yview)
    Table3.heading("Rollno",text="ID")
    Table3.heading("Name",text="Name")
    Table3.heading("Phoneno",text="Phoneno")
    Table3.heading("Gender",text="Gender")
    Table3.heading("Address",text="Address")
    Table3.heading("Class",text="Class")
    Table3.column("Rollno",width=110)
    Table3.column("Name",width=150)
    Table3.column("Phoneno",width=110)
    Table3.column("Gender",width=110)
    Table3.column("Address",width=200)
    Table3.column("Class",width=110)
    Table3['show']='headings'
    Table3.pack(fill=BOTH,expand=1)
    def Average1():
        conn = sqlite3.connect("StudMang.db")
        c=conn.cursor()
        avg = c.execute("Select avg(DCC) from Marksheet")
        average = avg.fetchall()
        entry2.config(text=str(average[0]))
        print("Average of ",average)
        conn.commit()
        conn.close()
    
    frame1a.place(x=10,y=60,width=580,height=300)
    frame2.place(x=725,y=55,width=760,height=380)

    frame3 = Frame(facult,relief=RIDGE,bd=4,bg="crimson")
    title = Label(frame3,text="Average passing marks of Subjects",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    title.grid(row = 1,columnspan=3,pady=10,padx=50,sticky=W)
    Select = Label(frame3,text="Select",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Select.grid(row = 2,column=0,pady=10,padx=10,sticky=W)
    vlist = ["DCC"]
    entry = Combobox(frame3,values=vlist,font=("times new roman",13,"bold"))
    entry.grid(row=2,column=1,padx=10,sticky=W)
    SHOW = Button(frame3,text="SHOW",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=Average1)
    SHOW.grid(row =4 ,column=0,pady=40,padx=10,sticky=W)
    entry2 = Label(frame3,font=("times new roman",14,"bold"),width=20,height=1)
    entry2.grid(row=4,column=1,pady=40,padx=10,sticky=W)
    frame3.place(x=10,y=445,width=700,height=310)

    sam = StringVar()
    
    def Search6():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Marksheet WHERE  Name LIKE '%"+str(sam.get())+"%'")
        rows=result.fetchall()

        if len(rows)!=0:
            Marksheet.delete(*Marksheet.get_children())
            for row in rows:
                Marksheet.insert('',END,values=row)
            conn.commit()
        print("okSearch")
        conn.close()

    def Search7():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Marksheet")
        rows=result.fetchall()

        if len(rows)!=0:
            Marksheet.delete(*Marksheet.get_children())
            for row in rows:
                Marksheet.insert('',END,values=row)
            conn.commit()
        print("okSearch")
        conn.close()
    
    frame4 = Frame(facult,relief=RIDGE,bd=4,bg="crimson")
    Title = Label(frame4,text="Marksheet Of Students",font=("times new roman",15,"bold"),fg="white",bg="crimson")
    Title.place(x=130,y=10,width=200)
    Search = Button(frame4,text="Search By Name",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=Search6)
    Search.place(x=615,y=10)
    entry1 = Entry(frame4,textvariable=sam,font=("times new roman",14,"bold"))
    entry1.place(x=385,y=15)
    entry1.focus()
    View = Button(frame4,text="View All",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=Search7)
    View.place(x=10,y=10)


    frame3a=Frame(frame4,relief=RIDGE,bd=4,bg="white")
    scroll_x = Scrollbar(frame3a,orient=HORIZONTAL)
    scroll_v = Scrollbar(frame3a,orient=VERTICAL)
    Marksheet = ttk.Treeview(frame3a,columns=("Rollno","Name","CLASS","JAVA","JAVATW","JAVAPR" ,"GAD","GADTW","GADPR","SEN","SENTW","SENPR","DCC","DCCTW","DCCPR","MIC","MICTW","MICPR","TOTAL","PERCENTAGE","GRADE"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_v.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_v.pack(side=RIGHT,fill=Y)

    scroll_x.configure(command=Marksheet.xview)
    scroll_v.configure(command=Marksheet.yview)

    Marksheet.heading("Rollno",text="ROLLNO")
    Marksheet.heading("Name",text="NAME")
    Marksheet.heading("CLASS",text="CLASS")
    Marksheet.heading("JAVA",text="JAVA")
    Marksheet.heading("JAVATW",text="JAVATW")
    Marksheet.heading("JAVAPR",text="JAVAPR")
    Marksheet.heading("GAD",text="GAD")
    Marksheet.heading("GADTW",text="GADTW")
    Marksheet.heading("GADPR",text="GADPR")
    Marksheet.heading("SEN",text="SEN")
    Marksheet.heading("SENTW",text="SENTW")
    Marksheet.heading("SENPR",text="SENPR")
    Marksheet.heading("DCC",text="DCC")
    Marksheet.heading("DCCTW",text="DCCTW")
    Marksheet.heading("DCCPR",text="DCCPR")
    Marksheet.heading("MIC",text="MIC")
    Marksheet.heading("MICTW",text="MICTW")
    Marksheet.heading("MICPR",text="MICPR")
    Marksheet.heading("TOTAL",text="TOTAL")
    Marksheet.heading("PERCENTAGE",text="PERCENTAGE")
    Marksheet.heading("GRADE",text="GRADE")
    Marksheet.heading("CLASS",text="CLASS")
    
    Marksheet['show']='headings'

    Marksheet.column("Rollno",width=100)
    Marksheet.column("Name",width=100)
    Marksheet.column("CLASS",width=100)
    Marksheet.column("JAVA",width=100)
    Marksheet.column("JAVATW",width=100)
    Marksheet.column("JAVAPR",width=100)
    Marksheet.column("GAD",width=100)
    Marksheet.column("GADTW",width=100)
    Marksheet.column("GADPR",width=100)  
    Marksheet.column("SEN",width=100)
    Marksheet.column("SENTW",width=100)
    Marksheet.column("SENPR",width=100)
    Marksheet.column("DCC",width=100)
    Marksheet.column("DCCTW",width=100)
    Marksheet.column("DCCPR",width=100)
    Marksheet.column("MIC",width=100)
    Marksheet.column("MICTW",width=100)
    Marksheet.column("MICPR",width=100)
    Marksheet.column("TOTAL",width=100)
    Marksheet.column("PERCENTAGE",width=100)
    Marksheet.column("GRADE",width=100)


    Marksheet.pack(fill=BOTH,expand=1)

    frame3a.place(x=0,y=80,width=750,height=225)
    frame4.place(x=725,y=435,width=760,height=320)

    root.mainloop()




def GAD():
    facult=Toplevel(root)
    facult.title("Student Management System")
    facult.geometry("1535x800+0+0")
    facult.resizable(0,0)

    
#FRAME1

    rollno = StringVar()
    name = StringVar()
    GAD = StringVar()
    GAD2 = StringVar()
    GAD3 = StringVar()
    Class = StringVar()

    def fetch_data3():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("Select * from Marksheet")
        rows=result.fetchall()
        if len(rows)!=0:
            Marksheet.delete(*Marksheet.get_children())
            for row in rows:
                Marksheet.insert('',END,values=row)
            conn.commit()
        conn.close()

    def clear1():
        Var1.set('')
        Var2.set('')
        Var3.set('')
        Var4.set('')
        Var5.set('')
        Var6.set('')
        
    def AddMarks():    
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()                                           
        c.execute("Insert into Marksheet(Rollno,Name,GAD,GADTW,GADPR,CLASS) values(?,?,?,?,?,?)",(rollno.get(),name.get(),GAD.get(),GAD2.get(),GAD3.get(),Class.get()))
        print("Student Add")
        conn.commit()
        fetch_data3()
        clear1()
        conn.close()

    
    frame = Frame(facult,bg="yellow",height=300)    
    bt1 = Button(frame,text="FACULTY",font=("times new roman",16,"bold"),bg="yellow",fg="green",activebackground="red",activeforeground="blue",padx=20,pady=5)
    bt1.pack(side=LEFT,fill=X)
    label = Label(frame,text="Student Management System Timing(8am to 10pm)",font=("times new roman",16,"bold"),bg="yellow",fg="green")
    label.pack(side=RIGHT,padx=30)
    frame.pack(side=TOP,fill=X)

    frame1 = Frame(facult,relief=RIDGE,bd=4,bg="crimson")
    Title = Label(frame1,text="MANAGE MARKS ",font=("times new roman",20,"bold"),fg="white",bg="crimson")
    Title.grid(row = 1,columnspan=2,pady=20,padx=10,sticky=E)

    Name = Label(frame1,text="Name",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Name.grid(row = 2,column=0,pady=10,padx=10,sticky=W)
    entry4 = Entry(frame1,textvariable=name,font=("times new roman",14,"bold"))
    entry4.grid(row=2,column=1,padx=10,sticky=W)

    Rollno = Label(frame1,text="RollNo",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Rollno.grid(row = 3,column=0,pady=10,padx=10,sticky=W)
    entry5 = Entry(frame1,textvariable=rollno,font=("times new roman",14,"bold"))
    entry5.grid(row=3,column=1,padx=10,sticky=W)

    gad = Label(frame1,text="GAD",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    gad.grid(row = 4,column=0,pady=10,padx=10,sticky=W)
    entry1 = Entry(frame1,textvariable=GAD,font=("times new roman",14,"bold"))
    entry1.grid(row=4,column=1,padx=10,sticky=W)
    entry1.focus()
    
    gadTW = Label(frame1,text="Termwork",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    gadTW.grid(row = 5,column=0,pady=10,padx=10,sticky=W)
    entry2 = Entry(frame1,textvariable=GAD2,font=("times new roman",14,"bold"))
    entry2.grid(row=5,column=1,padx=10,sticky=W)
    
    practicle = Label(frame1,text="Practicle",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    practicle.grid(row = 6,column=0,pady=10,padx=10,sticky=W)
    entry3 = Entry(frame1,textvariable=GAD3,font=("times new roman",14,"bold"))
    entry3.grid(row=6,column=1,padx=10,sticky=W)
    
    Class1 = Label(frame1,text="Select Class",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Class1.grid(row = 7,column=0,pady=10,padx=10,sticky=W)
    entry3 = Combobox(frame1,textvariable=Class,values=["Class1","Class2","Class3"],font=("times new roman",14,"bold"))
    entry3.grid(row=7,column=1,padx=10,sticky=W)

    SHOW = Button(frame1,text="ADD",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=AddMarks)
    SHOW.grid(row =7 ,column=3,pady=10,padx=20,sticky=W)    

    nam = StringVar()
    def SearchDCC():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Student WHERE  Name LIKE '%"+str(nam.get())+"%'")
        rows=result.fetchall()

        if len(rows)!=0:
            Table3.delete(*Table3.get_children())
            for row in rows:
                Table3.insert('',END,values=row)
            conn.commit()
        print("okSearch")
        conn.close()

    def SearchDCC1():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Student")
        rows=result.fetchall()

        if len(rows)!=0:
            Table3.delete(*Table3.get_children())
            for row in rows:
                Table3.insert('',END,values=row)
            conn.commit()
        print("okSearch")
        conn.close()
    
    frame1.place(x=10,y=55,width=700,height=390)

    frame2 = Frame(facult,relief=RIDGE,bd=4,bg="crimson")

    Search = Button(frame2,text="Search By Name",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=SearchDCC)
    Search.place(x=555,y=10)
    entry1 = Entry(frame2,textvariable=nam,font=("times new roman",14,"bold"))
    entry1.place(x=335,y=15)
    entry1.focus()
    View = Button(frame2,text="View All",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=SearchDCC1)
    View.place(x=10,y=10)

    frame1a = Frame(frame2,relief=RIDGE,bd=4,bg="crimson")

    scroll_x = Scrollbar(frame1a,orient=HORIZONTAL)
    scroll_v = Scrollbar(frame1a,orient=VERTICAL)
    Table3 = ttk.Treeview(frame1a,columns=("Rollno","Name","Phoneno","Gender","Address","Class"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_v.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_v.pack(side=RIGHT,fill=Y)
    scroll_x.configure(command=Table3.xview)
    scroll_v.configure(command=Table3.yview)
    Table3.heading("Rollno",text="ID")
    Table3.heading("Name",text="Name")
    Table3.heading("Phoneno",text="Phoneno")
    Table3.heading("Gender",text="Gender")
    Table3.heading("Address",text="Address")
    Table3.heading("Class",text="Class")
    Table3.column("Rollno",width=110)
    Table3.column("Name",width=150)
    Table3.column("Phoneno",width=110)
    Table3.column("Gender",width=110)
    Table3.column("Address",width=200)
    Table3.column("Class",width=110)
    Table3['show']='headings'
    Table3.pack(fill=BOTH,expand=1)
    def Average1():
        conn = sqlite3.connect("StudMang.db")
        c=conn.cursor()
        avg = c.execute("Select avg(GAD) from Marksheet")
        average = avg.fetchall()
        entry2.config(text=str(average[0]))
        print("Average of ",average)
        conn.commit()
        conn.close()
    
    frame1a.place(x=10,y=60,width=580,height=300)
    frame2.place(x=725,y=55,width=760,height=380)

    frame3 = Frame(facult,relief=RIDGE,bd=4,bg="crimson")
    title = Label(frame3,text="Average passing marks of Subjects",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    title.grid(row = 1,columnspan=3,pady=10,padx=50,sticky=W)
    Select = Label(frame3,text="Select",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Select.grid(row = 2,column=0,pady=10,padx=10,sticky=W)
    vlist = ["GAD"]
    entry = Combobox(frame3,values=vlist,font=("times new roman",13,"bold"))
    entry.grid(row=2,column=1,padx=10,sticky=W)
    SHOW = Button(frame3,text="SHOW",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=Average1)
    SHOW.grid(row =4 ,column=0,pady=40,padx=10,sticky=W)
    entry2 = Label(frame3,font=("times new roman",14,"bold"),width=20,height=1)
    entry2.grid(row=4,column=1,pady=40,padx=10,sticky=W)
    frame3.place(x=10,y=445,width=700,height=310)

    sam = StringVar()
    
    def Search6():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Marksheet WHERE  Name LIKE '%"+str(sam.get())+"%'")
        rows=result.fetchall()

        if len(rows)!=0:
            Marksheet.delete(*Marksheet.get_children())
            for row in rows:
                Marksheet.insert('',END,values=row)
            conn.commit()
        print("okSearch")
        conn.close()

    def Search7():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Marksheet")
        rows=result.fetchall()

        if len(rows)!=0:
            Marksheet.delete(*Marksheet.get_children())
            for row in rows:
                Marksheet.insert('',END,values=row)
            conn.commit()
        print("okSearch")
        conn.close()
    
    frame4 = Frame(facult,relief=RIDGE,bd=4,bg="crimson")
    Title = Label(frame4,text="Marksheet Of Students",font=("times new roman",15,"bold"),fg="white",bg="crimson")
    Title.place(x=130,y=10,width=200)
    Search = Button(frame4,text="Search By Name",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=Search6)
    Search.place(x=615,y=10)
    entry1 = Entry(frame4,textvariable=sam,font=("times new roman",14,"bold"))
    entry1.place(x=385,y=15)
    entry1.focus()
    View = Button(frame4,text="View All",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=Search7)
    View.place(x=10,y=10)


    frame3a=Frame(frame4,relief=RIDGE,bd=4,bg="white")
    scroll_x = Scrollbar(frame3a,orient=HORIZONTAL)
    scroll_v = Scrollbar(frame3a,orient=VERTICAL)
    Marksheet = ttk.Treeview(frame3a,columns=("Rollno","Name","CLASS","JAVA","JAVATW","JAVAPR" ,"GAD","GADTW","GADPR","SEN","SENTW","SENPR","DCC","DCCTW","DCCPR","MIC","MICTW","MICPR","TOTAL","PERCENTAGE","GRADE"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_v.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_v.pack(side=RIGHT,fill=Y)

    scroll_x.configure(command=Marksheet.xview)
    scroll_v.configure(command=Marksheet.yview)

    Marksheet.heading("Rollno",text="ROLLNO")
    Marksheet.heading("Name",text="NAME")
    Marksheet.heading("CLASS",text="CLASS")
    Marksheet.heading("JAVA",text="JAVA")
    Marksheet.heading("JAVATW",text="JAVATW")
    Marksheet.heading("JAVAPR",text="JAVAPR")
    Marksheet.heading("GAD",text="GAD")
    Marksheet.heading("GADTW",text="GADTW")
    Marksheet.heading("GADPR",text="GADPR")
    Marksheet.heading("SEN",text="SEN")
    Marksheet.heading("SENTW",text="SENTW")
    Marksheet.heading("SENPR",text="SENPR")
    Marksheet.heading("DCC",text="DCC")
    Marksheet.heading("DCCTW",text="DCCTW")
    Marksheet.heading("DCCPR",text="DCCPR")
    Marksheet.heading("MIC",text="MIC")
    Marksheet.heading("MICTW",text="MICTW")
    Marksheet.heading("MICPR",text="MICPR")
    Marksheet.heading("TOTAL",text="TOTAL")
    Marksheet.heading("PERCENTAGE",text="PERCENTAGE")
    Marksheet.heading("GRADE",text="GRADE")
    Marksheet.heading("CLASS",text="CLASS")
    
    Marksheet['show']='headings'

    Marksheet.column("Rollno",width=100)
    Marksheet.column("Name",width=100)
    Marksheet.column("CLASS",width=100)
    Marksheet.column("JAVA",width=100)
    Marksheet.column("JAVATW",width=100)
    Marksheet.column("JAVAPR",width=100)
    Marksheet.column("GAD",width=100)
    Marksheet.column("GADTW",width=100)
    Marksheet.column("GADPR",width=100)  
    Marksheet.column("SEN",width=100)
    Marksheet.column("SENTW",width=100)
    Marksheet.column("SENPR",width=100)
    Marksheet.column("DCC",width=100)
    Marksheet.column("DCCTW",width=100)
    Marksheet.column("DCCPR",width=100)
    Marksheet.column("MIC",width=100)
    Marksheet.column("MICTW",width=100)
    Marksheet.column("MICPR",width=100)
    Marksheet.column("TOTAL",width=100)
    Marksheet.column("PERCENTAGE",width=100)
    Marksheet.column("GRADE",width=100)


    Marksheet.pack(fill=BOTH,expand=1)

    frame3a.place(x=0,y=80,width=750,height=225)
    frame4.place(x=725,y=435,width=760,height=320)

    root.mainloop()

def MIC():
    facult=Toplevel(root)
    facult.title("Student Management System")
    facult.geometry("1535x800+0+0")
    facult.resizable(0,0)

    
#FRAME1

    rollno = StringVar()
    name = StringVar()
    MIC = StringVar()
    MIC2 = StringVar()
    MIC3 = StringVar()
    Class = StringVar()

    def fetch_data3():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("Select * from Marksheet")
        rows=result.fetchall()
        if len(rows)!=0:
            Marksheet.delete(*Marksheet.get_children())
            for row in rows:
                Marksheet.insert('',END,values=row)
            conn.commit()
        conn.close()

    def clear1():
        Var1.set('')
        Var2.set('')
        Var3.set('')
        Var4.set('')
        Var5.set('')
        Var6.set('')
        
    def AddMarks():    
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()                                           
        c.execute("Insert into Marksheet(Rollno,Name,MIC,MICTW,MICPR,CLASS) values(?,?,?,?,?,?)",(rollno.get(),name.get(),MIC.get(),MIC2.get(),MIC3.get(),Class.get()))
        print("Student Add")
        conn.commit()
        fetch_data3()
        clear1()
        conn.close()

    
    frame = Frame(facult,bg="yellow",height=300)    
    bt1 = Button(frame,text="FACULTY",font=("times new roman",16,"bold"),bg="yellow",fg="green",activebackground="red",activeforeground="blue",padx=20,pady=5)
    bt1.pack(side=LEFT,fill=X)
    label = Label(frame,text="Student Management System Timing(8am to 10pm)",font=("times new roman",16,"bold"),bg="yellow",fg="green")
    label.pack(side=RIGHT,padx=30)
    frame.pack(side=TOP,fill=X)

    frame1 = Frame(facult,relief=RIDGE,bd=4,bg="crimson")
    Title = Label(frame1,text="MANAGE MARKS ",font=("times new roman",20,"bold"),fg="white",bg="crimson")
    Title.grid(row = 1,columnspan=2,pady=20,padx=10,sticky=E)

    Name = Label(frame1,text="Name",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Name.grid(row = 2,column=0,pady=10,padx=10,sticky=W)
    entry4 = Entry(frame1,textvariable=name,font=("times new roman",14,"bold"))
    entry4.grid(row=2,column=1,padx=10,sticky=W)

    Rollno = Label(frame1,text="RollNo",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Rollno.grid(row = 3,column=0,pady=10,padx=10,sticky=W)
    entry5 = Entry(frame1,textvariable=rollno,font=("times new roman",14,"bold"))
    entry5.grid(row=3,column=1,padx=10,sticky=W)

    gad = Label(frame1,text="MIC",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    gad.grid(row = 4,column=0,pady=10,padx=10,sticky=W)
    entry1 = Entry(frame1,textvariable=MIC,font=("times new roman",14,"bold"))
    entry1.grid(row=4,column=1,padx=10,sticky=W)
    entry1.focus()
    
    gadTW = Label(frame1,text="Termwork",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    gadTW.grid(row = 5,column=0,pady=10,padx=10,sticky=W)
    entry2 = Entry(frame1,textvariable=MIC2,font=("times new roman",14,"bold"))
    entry2.grid(row=5,column=1,padx=10,sticky=W)
    
    practicle = Label(frame1,text="Practicle",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    practicle.grid(row = 6,column=0,pady=10,padx=10,sticky=W)
    entry3 = Entry(frame1,textvariable=MIC3,font=("times new roman",14,"bold"))
    entry3.grid(row=6,column=1,padx=10,sticky=W)
    
    Class1 = Label(frame1,text="Select Class",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Class1.grid(row = 7,column=0,pady=10,padx=10,sticky=W)
    entry3 = Combobox(frame1,textvariable=Class,values=["Class1","Class2","Class3"],font=("times new roman",14,"bold"))
    entry3.grid(row=7,column=1,padx=10,sticky=W)

    SHOW = Button(frame1,text="ADD",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=AddMarks)
    SHOW.grid(row =7 ,column=3,pady=10,padx=20,sticky=W)    

    nam = StringVar()
    def SearchDCC():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Student WHERE  Name LIKE '%"+str(nam.get())+"%'")
        rows=result.fetchall()

        if len(rows)!=0:
            Table3.delete(*Table3.get_children())
            for row in rows:
                Table3.insert('',END,values=row)
            conn.commit()
        print("okSearch")
        conn.close()

    def SearchDCC1():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Student")
        rows=result.fetchall()

        if len(rows)!=0:
            Table3.delete(*Table3.get_children())
            for row in rows:
                Table3.insert('',END,values=row)
            conn.commit()
        print("okSearch")
        conn.close()
    
    frame1.place(x=10,y=55,width=700,height=390)

    frame2 = Frame(facult,relief=RIDGE,bd=4,bg="crimson")

    Search = Button(frame2,text="Search By Name",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=SearchDCC)
    Search.place(x=555,y=10)
    entry1 = Entry(frame2,textvariable=nam,font=("times new roman",14,"bold"))
    entry1.place(x=335,y=15)
    entry1.focus()
    View = Button(frame2,text="View All",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=SearchDCC1)
    View.place(x=10,y=10)

    frame1a = Frame(frame2,relief=RIDGE,bd=4,bg="crimson")

    scroll_x = Scrollbar(frame1a,orient=HORIZONTAL)
    scroll_v = Scrollbar(frame1a,orient=VERTICAL)
    Table3 = ttk.Treeview(frame1a,columns=("Rollno","Name","Phoneno","Gender","Address","Class"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_v.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_v.pack(side=RIGHT,fill=Y)
    scroll_x.configure(command=Table3.xview)
    scroll_v.configure(command=Table3.yview)
    Table3.heading("Rollno",text="ID")
    Table3.heading("Name",text="Name")
    Table3.heading("Phoneno",text="Phoneno")
    Table3.heading("Gender",text="Gender")
    Table3.heading("Address",text="Address")
    Table3.heading("Class",text="Class")
    Table3.column("Rollno",width=110)
    Table3.column("Name",width=150)
    Table3.column("Phoneno",width=110)
    Table3.column("Gender",width=110)
    Table3.column("Address",width=200)
    Table3.column("Class",width=110)
    Table3['show']='headings'
    Table3.pack(fill=BOTH,expand=1)
    def Average1():
        conn = sqlite3.connect("StudMang.db")
        c=conn.cursor()
        avg = c.execute("Select avg(MIC) from Marksheet")
        average = avg.fetchall()
        entry2.config(text=str(average[0]))
        print("Average of ",average)
        conn.commit()
        conn.close()
    
    frame1a.place(x=10,y=60,width=580,height=300)
    frame2.place(x=725,y=55,width=760,height=380)

    frame3 = Frame(facult,relief=RIDGE,bd=4,bg="crimson")
    title = Label(frame3,text="Average passing marks of Subjects",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    title.grid(row = 1,columnspan=3,pady=10,padx=50,sticky=W)
    Select = Label(frame3,text="Select",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Select.grid(row = 2,column=0,pady=10,padx=10,sticky=W)
    vlist = ["MIC"]
    entry = Combobox(frame3,values=vlist,font=("times new roman",13,"bold"))
    entry.grid(row=2,column=1,padx=10,sticky=W)
    SHOW = Button(frame3,text="SHOW",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=Average1)
    SHOW.grid(row =4 ,column=0,pady=40,padx=10,sticky=W)
    entry2 = Label(frame3,font=("times new roman",14,"bold"),width=20,height=1)
    entry2.grid(row=4,column=1,pady=40,padx=10,sticky=W)
    frame3.place(x=10,y=445,width=700,height=310)

    sam = StringVar()
    
    def Search6():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Marksheet WHERE  Name LIKE '%"+str(sam.get())+"%'")
        rows=result.fetchall()

        if len(rows)!=0:
            Marksheet.delete(*Marksheet.get_children())
            for row in rows:
                Marksheet.insert('',END,values=row)
            conn.commit()
        print("okSearch")
        conn.close()

    def Search7():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Marksheet")
        rows=result.fetchall()

        if len(rows)!=0:
            Marksheet.delete(*Marksheet.get_children())
            for row in rows:
                Marksheet.insert('',END,values=row)
            conn.commit()
        print("okSearch")
        conn.close()
    
    frame4 = Frame(facult,relief=RIDGE,bd=4,bg="crimson")
    Title = Label(frame4,text="Marksheet Of Students",font=("times new roman",15,"bold"),fg="white",bg="crimson")
    Title.place(x=130,y=10,width=200)
    Search = Button(frame4,text="Search By Name",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=Search6)
    Search.place(x=615,y=10)
    entry1 = Entry(frame4,textvariable=sam,font=("times new roman",14,"bold"))
    entry1.place(x=385,y=15)
    entry1.focus()
    View = Button(frame4,text="View All",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=Search7)
    View.place(x=10,y=10)


    frame3a=Frame(frame4,relief=RIDGE,bd=4,bg="white")
    scroll_x = Scrollbar(frame3a,orient=HORIZONTAL)
    scroll_v = Scrollbar(frame3a,orient=VERTICAL)
    Marksheet = ttk.Treeview(frame3a,columns=("Rollno","Name","CLASS","JAVA","JAVATW","JAVAPR" ,"GAD","GADTW","GADPR","SEN","SENTW","SENPR","DCC","DCCTW","DCCPR","MIC","MICTW","MICPR","TOTAL","PERCENTAGE","GRADE"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_v.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_v.pack(side=RIGHT,fill=Y)

    scroll_x.configure(command=Marksheet.xview)
    scroll_v.configure(command=Marksheet.yview)

    Marksheet.heading("Rollno",text="ROLLNO")
    Marksheet.heading("Name",text="NAME")
    Marksheet.heading("CLASS",text="CLASS")
    Marksheet.heading("JAVA",text="JAVA")
    Marksheet.heading("JAVATW",text="JAVATW")
    Marksheet.heading("JAVAPR",text="JAVAPR")
    Marksheet.heading("GAD",text="GAD")
    Marksheet.heading("GADTW",text="GADTW")
    Marksheet.heading("GADPR",text="GADPR")
    Marksheet.heading("SEN",text="SEN")
    Marksheet.heading("SENTW",text="SENTW")
    Marksheet.heading("SENPR",text="SENPR")
    Marksheet.heading("DCC",text="DCC")
    Marksheet.heading("DCCTW",text="DCCTW")
    Marksheet.heading("DCCPR",text="DCCPR")
    Marksheet.heading("MIC",text="MIC")
    Marksheet.heading("MICTW",text="MICTW")
    Marksheet.heading("MICPR",text="MICPR")
    Marksheet.heading("TOTAL",text="TOTAL")
    Marksheet.heading("PERCENTAGE",text="PERCENTAGE")
    Marksheet.heading("GRADE",text="GRADE")
    Marksheet.heading("CLASS",text="CLASS")
    
    Marksheet['show']='headings'

    Marksheet.column("Rollno",width=100)
    Marksheet.column("Name",width=100)
    Marksheet.column("CLASS",width=100)
    Marksheet.column("JAVA",width=100)
    Marksheet.column("JAVATW",width=100)
    Marksheet.column("JAVAPR",width=100)
    Marksheet.column("GAD",width=100)
    Marksheet.column("GADTW",width=100)
    Marksheet.column("GADPR",width=100)  
    Marksheet.column("SEN",width=100)
    Marksheet.column("SENTW",width=100)
    Marksheet.column("SENPR",width=100)
    Marksheet.column("DCC",width=100)
    Marksheet.column("DCCTW",width=100)
    Marksheet.column("DCCPR",width=100)
    Marksheet.column("MIC",width=100)
    Marksheet.column("MICTW",width=100)
    Marksheet.column("MICPR",width=100)
    Marksheet.column("TOTAL",width=100)
    Marksheet.column("PERCENTAGE",width=100)
    Marksheet.column("GRADE",width=100)


    Marksheet.pack(fill=BOTH,expand=1)

    frame3a.place(x=0,y=80,width=750,height=225)
    frame4.place(x=725,y=435,width=760,height=320)

    root.mainloop()

def SEN():
    facult=Toplevel(root)
    facult.title("Student Management System")
    facult.geometry("1535x800+0+0")
    facult.resizable(0,0)

    
#FRAME1

    rollno = StringVar()
    name = StringVar()
    SEN = StringVar()
    SEN2 = StringVar()
    SEN3 = StringVar()
    Class = StringVar()

    def fetch_data3():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("Select * from Marksheet")
        rows=result.fetchall()
        if len(rows)!=0:
            Marksheet.delete(*Marksheet.get_children())
            for row in rows:
                Marksheet.insert('',END,values=row)
            conn.commit()
        conn.close()

    def clear1():
        Var1.set('')
        Var2.set('')
        Var3.set('')
        Var4.set('')
        Var5.set('')
        Var6.set('')
        
    def AddMarks():    
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()                                           
        c.execute("Insert into Marksheet(Rollno,Name,SEN,SENTW,SENPR,CLASS) values(?,?,?,?,?,?)",(rollno.get(),name.get(),SEN.get(),SEN2.get(),SEN3.get(),Class.get()))
        print("Student Add")
        conn.commit()
        fetch_data3()
        clear1()
        conn.close()

    
    frame = Frame(facult,bg="yellow",height=300)    
    bt1 = Button(frame,text="FACULTY",font=("times new roman",16,"bold"),bg="yellow",fg="green",activebackground="red",activeforeground="blue",padx=20,pady=5)
    bt1.pack(side=LEFT,fill=X)
    label = Label(frame,text="Student Management System Timing(8am to 10pm)",font=("times new roman",16,"bold"),bg="yellow",fg="green")
    label.pack(side=RIGHT,padx=30)
    frame.pack(side=TOP,fill=X)

    frame1 = Frame(facult,relief=RIDGE,bd=4,bg="crimson")
    Title = Label(frame1,text="MANAGE MARKS ",font=("times new roman",20,"bold"),fg="white",bg="crimson")
    Title.grid(row = 1,columnspan=2,pady=20,padx=10,sticky=E)

    Name = Label(frame1,text="Name",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Name.grid(row = 2,column=0,pady=10,padx=10,sticky=W)
    entry4 = Entry(frame1,textvariable=name,font=("times new roman",14,"bold"))
    entry4.grid(row=2,column=1,padx=10,sticky=W)

    Rollno = Label(frame1,text="RollNo",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Rollno.grid(row = 3,column=0,pady=10,padx=10,sticky=W)
    entry5 = Entry(frame1,textvariable=rollno,font=("times new roman",14,"bold"))
    entry5.grid(row=3,column=1,padx=10,sticky=W)

    sen = Label(frame1,text="SEN",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    sen.grid(row = 4,column=0,pady=10,padx=10,sticky=W)
    entry1 = Entry(frame1,textvariable=SEN,font=("times new roman",14,"bold"))
    entry1.grid(row=4,column=1,padx=10,sticky=W)
    entry1.focus()
    
    senTW = Label(frame1,text="Termwork",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    senTW.grid(row = 5,column=0,pady=10,padx=10,sticky=W)
    entry2 = Entry(frame1,textvariable=SEN2,font=("times new roman",14,"bold"))
    entry2.grid(row=5,column=1,padx=10,sticky=W)
    
    practicle = Label(frame1,text="Practicle",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    practicle.grid(row = 6,column=0,pady=10,padx=10,sticky=W)
    entry3 = Entry(frame1,textvariable=SEN3,font=("times new roman",14,"bold"))
    entry3.grid(row=6,column=1,padx=10,sticky=W)
    
    Class1 = Label(frame1,text="Select Class",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Class1.grid(row = 7,column=0,pady=10,padx=10,sticky=W)
    entry3 = Combobox(frame1,textvariable=Class,values=["Class1","Class2","Class3"],font=("times new roman",14,"bold"))
    entry3.grid(row=7,column=1,padx=10,sticky=W)

    SHOW = Button(frame1,text="ADD",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=AddMarks)
    SHOW.grid(row =7 ,column=3,pady=10,padx=20,sticky=W)    

    nam = StringVar()
    def SearchDCC():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Student WHERE  Name LIKE '%"+str(nam.get())+"%'")
        rows=result.fetchall()

        if len(rows)!=0:
            Table3.delete(*Table3.get_children())
            for row in rows:
                Table3.insert('',END,values=row)
            conn.commit()
        print("okSearch")
        conn.close()

    def SearchDCC1():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Student")
        rows=result.fetchall()

        if len(rows)!=0:
            Table3.delete(*Table3.get_children())
            for row in rows:
                Table3.insert('',END,values=row)
            conn.commit()
        print("okSearch")
        conn.close()
    
    frame1.place(x=10,y=55,width=700,height=390)

    frame2 = Frame(facult,relief=RIDGE,bd=4,bg="crimson")

    Search = Button(frame2,text="Search By Name",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=SearchDCC)
    Search.place(x=555,y=10)
    entry1 = Entry(frame2,textvariable=nam,font=("times new roman",14,"bold"))
    entry1.place(x=335,y=15)
    entry1.focus()
    View = Button(frame2,text="View All",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=SearchDCC1)
    View.place(x=10,y=10)

    frame1a = Frame(frame2,relief=RIDGE,bd=4,bg="crimson")

    scroll_x = Scrollbar(frame1a,orient=HORIZONTAL)
    scroll_v = Scrollbar(frame1a,orient=VERTICAL)
    Table3 = ttk.Treeview(frame1a,columns=("Rollno","Name","Phoneno","Gender","Address","Class"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_v.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_v.pack(side=RIGHT,fill=Y)
    scroll_x.configure(command=Table3.xview)
    scroll_v.configure(command=Table3.yview)
    Table3.heading("Rollno",text="ID")
    Table3.heading("Name",text="Name")
    Table3.heading("Phoneno",text="Phoneno")
    Table3.heading("Gender",text="Gender")
    Table3.heading("Address",text="Address")
    Table3.heading("Class",text="Class")
    Table3.column("Rollno",width=110)
    Table3.column("Name",width=150)
    Table3.column("Phoneno",width=110)
    Table3.column("Gender",width=110)
    Table3.column("Address",width=200)
    Table3.column("Class",width=110)
    Table3['show']='headings'
    Table3.pack(fill=BOTH,expand=1)
    def Average1():
        conn = sqlite3.connect("StudMang.db")
        c=conn.cursor()
        avg = c.execute("Select avg(SEN) from Marksheet")
        average = avg.fetchall()
        entry2.config(text=str(average[0]))
        print("Average of ",average)
        conn.commit()
        conn.close()
    
    frame1a.place(x=10,y=60,width=580,height=300)
    frame2.place(x=725,y=55,width=760,height=380)

    frame3 = Frame(facult,relief=RIDGE,bd=4,bg="crimson")
    title = Label(frame3,text="Average passing marks of Subjects",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    title.grid(row = 1,columnspan=3,pady=10,padx=50,sticky=W)
    Select = Label(frame3,text="Select",font=("times new roman",16,"bold"),fg="white",bg="crimson")
    Select.grid(row = 2,column=0,pady=10,padx=10,sticky=W)
    vlist = ["SEN"]
    entry = Combobox(frame3,values=vlist,font=("times new roman",13,"bold"))
    entry.grid(row=2,column=1,padx=10,sticky=W)
    SHOW = Button(frame3,text="SHOW",font=("times new roman",14,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=Average1)
    SHOW.grid(row =4 ,column=0,pady=40,padx=10,sticky=W)
    entry2 = Label(frame3,font=("times new roman",14,"bold"),width=20,height=1)
    entry2.grid(row=4,column=1,pady=40,padx=10,sticky=W)
    frame3.place(x=10,y=445,width=700,height=310)

    sam = StringVar()
    
    def Search6():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Marksheet WHERE  Name LIKE '%"+str(sam.get())+"%'")
        rows=result.fetchall()

        if len(rows)!=0:
            Marksheet.delete(*Marksheet.get_children())
            for row in rows:
                Marksheet.insert('',END,values=row)
            conn.commit()
        print("okSearch")
        conn.close()

    def Search7():
        conn = sqlite3.connect("StudMang.db")
        c = conn.cursor()
        result=c.execute("SELECT * FROM Marksheet")
        rows=result.fetchall()

        if len(rows)!=0:
            Marksheet.delete(*Marksheet.get_children())
            for row in rows:
                Marksheet.insert('',END,values=row)
            conn.commit()
        print("okSearch")
        conn.close()
    
    frame4 = Frame(facult,relief=RIDGE,bd=4,bg="crimson")
    Title = Label(frame4,text="Marksheet Of Students",font=("times new roman",15,"bold"),fg="white",bg="crimson")
    Title.place(x=130,y=10,width=200)
    Search = Button(frame4,text="Search By Name",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=Search6)
    Search.place(x=615,y=10)
    entry1 = Entry(frame4,textvariable=sam,font=("times new roman",14,"bold"))
    entry1.place(x=385,y=15)
    entry1.focus()
    View = Button(frame4,text="View All",font=("times new roman",12,"bold"),fg="crimson",bg="white",activebackground="crimson",activeforeground="white",command=Search7)
    View.place(x=10,y=10)


    frame3a=Frame(frame4,relief=RIDGE,bd=4,bg="white")
    scroll_x = Scrollbar(frame3a,orient=HORIZONTAL)
    scroll_v = Scrollbar(frame3a,orient=VERTICAL)
    Marksheet = ttk.Treeview(frame3a,columns=("Rollno","Name","CLASS","JAVA","JAVATW","JAVAPR" ,"GAD","GADTW","GADPR","SEN","SENTW","SENPR","DCC","DCCTW","DCCPR","MIC","MICTW","MICPR","TOTAL","PERCENTAGE","GRADE"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_v.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_v.pack(side=RIGHT,fill=Y)

    scroll_x.configure(command=Marksheet.xview)
    scroll_v.configure(command=Marksheet.yview)

    Marksheet.heading("Rollno",text="ROLLNO")
    Marksheet.heading("Name",text="NAME")
    Marksheet.heading("CLASS",text="CLASS")
    Marksheet.heading("JAVA",text="JAVA")
    Marksheet.heading("JAVATW",text="JAVATW")
    Marksheet.heading("JAVAPR",text="JAVAPR")
    Marksheet.heading("GAD",text="GAD")
    Marksheet.heading("GADTW",text="GADTW")
    Marksheet.heading("GADPR",text="GADPR")
    Marksheet.heading("SEN",text="SEN")
    Marksheet.heading("SENTW",text="SENTW")
    Marksheet.heading("SENPR",text="SENPR")
    Marksheet.heading("DCC",text="DCC")
    Marksheet.heading("DCCTW",text="DCCTW")
    Marksheet.heading("DCCPR",text="DCCPR")
    Marksheet.heading("MIC",text="MIC")
    Marksheet.heading("MICTW",text="MICTW")
    Marksheet.heading("MICPR",text="MICPR")
    Marksheet.heading("TOTAL",text="TOTAL")
    Marksheet.heading("PERCENTAGE",text="PERCENTAGE")
    Marksheet.heading("GRADE",text="GRADE")
    Marksheet.heading("CLASS",text="CLASS")
    
    Marksheet['show']='headings'

    Marksheet.column("Rollno",width=100)
    Marksheet.column("Name",width=100)
    Marksheet.column("CLASS",width=100)
    Marksheet.column("JAVA",width=100)
    Marksheet.column("JAVATW",width=100)
    Marksheet.column("JAVAPR",width=100)
    Marksheet.column("GAD",width=100)
    Marksheet.column("GADTW",width=100)
    Marksheet.column("GADPR",width=100)  
    Marksheet.column("SEN",width=100)
    Marksheet.column("SENTW",width=100)
    Marksheet.column("SENPR",width=100)
    Marksheet.column("DCC",width=100)
    Marksheet.column("DCCTW",width=100)
    Marksheet.column("DCCPR",width=100)
    Marksheet.column("MIC",width=100)
    Marksheet.column("MICTW",width=100)
    Marksheet.column("MICPR",width=100)
    Marksheet.column("TOTAL",width=100)
    Marksheet.column("PERCENTAGE",width=100)
    Marksheet.column("GRADE",width=100)


    Marksheet.pack(fill=BOTH,expand=1)

    frame3a.place(x=0,y=80,width=750,height=225)
    frame4.place(x=725,y=435,width=760,height=320)

    root.mainloop()


###################################################################################################################################################################################
    #######################################################         LOGIN OR MAIN PAGE  ###########################################################
###################################################################################################################################################################################
#FRAME2
frame2 = Frame(root,height=200,bg="white",relief=SUNKEN)
canva = Canvas(frame2,width=100,height=100,bg="crimson")
canva.pack(side=LEFT,padx=30,pady=10)
Title = Label(frame2,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="white",fg="blue",relief=RAISED,bd=10)
Title.pack(side=LEFT,padx=40)
frame2.pack(side=TOP,fill=X)




                                                
                                               #####################STUDENT LOGIN##################

Studname = StringVar()
Studpass = StringVar()

def CreateFack():
    conn = sqlite3.connect("StudMang.db")
    c = conn.cursor()
    #c.execute("Create Table fack1 (name text,passw text)")
    #c.execute("Insert into fack values(?,?)",(Studname.get(),Studpass.get()))
    #name =  c.execute("SELECT * FROM fack WHERE  name  LIKE '%"+str(Studname.get())+"%'")  #len(nrow)!=0
    passw = c.execute("SELECT * FROM Student WHERE  Password LIKE '%"+str(Studpass.get())+"%'") 
    #nrow = name.fetchall()
    prow = passw.fetchall()
    if (len(prow)!=0):
        Student()
    conn.commit()
    conn.close()


#FRAME3
frame3 = Frame(root,relief=SUNKEN,bd=5,bg="crimson")
login = Label(frame3,text=" Student Login",font=("times new roman",25,"bold"),fg="white",bg="crimson")
login.grid(row=1,columnspan=2,pady=20,padx=40)
name = Label(frame3,text="Username",font=("times new roman",16,"bold"),fg="white",bg="crimson")
name.grid(row=3,column=0,pady=10)
userentry = Entry(frame3,textvariable=Studname,font=("times new roman",16,"bold"))
userentry.grid(row=3,column=1,padx=30,pady=10)
userentry.focus()




password = Label(frame3,text="Password",font=("times new roman",16,"bold"),fg="white",bg="crimson")
password.grid(row=4,column=0,pady=10)
passentry = Entry(frame3,textvariable=Studpass,font=("times new roman",16,"bold"))
passentry.grid(row=4,column=1,padx=30,pady=10)
btlogin = Button(frame3,text="Login",font=("times new roman",16,"bold"),fg="white",bg='blue',activebackground="red",activeforeground="blue",command=CreateFack)
btlogin.grid(row=6,columnspan=2,pady=20)
frame3.place(x=1100,y=300,width=400,heigh=350)

                                        ##################### ADMIN LOGIN ##################

uservalue = StringVar()
passvalue = StringVar()



#FRAME4
frame4 = Frame(root,relief=SUNKEN,bd=5,bg="crimson")
login = Label(frame4,text="Admin Login",font=("times new roman",25,"bold"),fg="white",bg="crimson")
login.grid(row=1,columnspan=2,pady=20,padx=40)

name = Label(frame4,text="Username",font=("times new roman",16,"bold"),fg="white",bg="crimson")
name.grid(row=3,column=0,pady=10)
userentry = Entry(frame4,textvariable=uservalue,font=("times new roman",16,"bold"))
userentry.grid(row=3,column=1,padx=30,pady=10)
userentry.focus()

password = Label(frame4,text="Password",font=("times new roman",16,"bold"),fg="white",bg="crimson")
password.grid(row=4,column=0,pady=10)
passentry = Entry(frame4,textvariable=passvalue,font=("times new roman",16,"bold"))
passentry.grid(row=4,column=1,padx=30,pady=10)
frame4.place(x=50,y=300,width=400,heigh=350)



    
def login():
    userget = str(uservalue.get())
    passget = str(passvalue.get())

    if (userget == "Anupam" or userget=="anupam") and (passget == "18430" ):
        Admin1()
    elif (userget == "Saalim" or userget=="saalim") and (passget == "18427" ):
        Admin1()
    
btlogin = Button(frame4,text="Login",font=("times new roman",16,"bold"),fg="white",bg='blue',activebackground="red",activeforeground="blue",command=login)
btlogin.grid(row=6,columnspan=2,pady=20)
    
        
                                #####################FACULTY LOGIN##################
uservalue1 = StringVar()
passvalue1 = StringVar()
use = StringVar()

#FRAME5
frame5 = Frame(root,relief=SUNKEN,bd=5,bg="crimson")
login = Label(frame5,text="Faculty Login",font=("times new roman",25,"bold"),fg="white",bg="crimson")
login.grid(row=1,columnspan=2,pady=20,padx=40)
name = Label(frame5,text="Username",font=("times new roman",16,"bold"),fg="white",bg="crimson")
name.grid(row=3,column=0,pady=10)
userentry = Entry(frame5,textvariable=uservalue1,font=("times new roman",16,"bold"))
userentry.grid(row=3,column=1,padx=30,pady=10)
userentry.focus()
 
password = Label(frame5,text="Password",font=("times new roman",16,"bold"),fg="white",bg="crimson")
password.grid(row=5,column=0,pady=10)
passentry = Entry(frame5,textvariable=passvalue1,font=("times new roman",16,"bold"))
passentry.grid(row=5,column=1,padx=30,pady=10)

def login1():
    userget = str(uservalue1.get())
    useget = str(use.get())
    passget = str(passvalue1.get())
    if (userget == "Zaiba Malik" and passget == "200"):
        Faculty()
    elif (userget == "Ali" and passget == "201"):
        Ali()
    elif (userget == "Shafaque" and passget == "202"):
        GAD()
    elif (userget == "Kausar" and passget == "203"):
        MIC()
    elif (userget == "Zaid" and passget == "204"):
        SEN()
            
btlogin = Button(frame5,text="Login",font=("times new roman",16,"bold"),fg="white",bg='blue',activebackground="red",activeforeground="blue",command=login1)
btlogin.grid(row=7,columnspan=2,pady=20)
frame5.place(x=560,y=300,width=400,heigh=350)





root.mainloop()
