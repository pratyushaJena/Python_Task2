from tkinter import *
import tkinter.messagebox as MsgBox
import mysql.connector as mysql

root = Tk()
root.geometry("400x300")
root.title("LogIn")

mydb0 = mysql.connect(host="localhost", user="Pratyusha", passwd="pratyusha12345")
mycursor0 = mydb0.cursor()
mycursor0.execute("create database if not exists StudentInformation")
mycursor0.execute("use StudentInformation")
mycursor0.execute("show tables like 'Information'")
res = mycursor0.fetchone()
if not res:
    mycursor0.execute("create table Information(Name varchar(50),Branch varchar(20),Registration_ID int,Subject varchar(20),Marks int)")
    MsgBox.showinfo("Database Creation","Databse successfully created")


class First:
    def __init__(self, master):
        self.mainframe = Frame(master, bg='purple',bd='10',height='100',width='200')
        self.mainframe.pack(side=BOTTOM,fill=BOTH,expand=1)
        self.one = Label(self.mainframe, text="User Name:", font='timesnewroman',bd='20', fg='cyan',anchor='center',bg='purple')
        self.two = Label(self.mainframe, text="Password:", font='verdana',bd='20',fg='cyan',anchor='center',bg='purple')
        self.one.grid(row=0,sticky=E)
        self.two.grid(row=1,sticky=E)

        self.Entry1 = Entry(self.mainframe)
        self.Entry2 = Entry(self.mainframe)
        self. Entry1.grid(row=0, column=1)
        self.Entry2.grid(row=1, column=1)

        self.bsubmit = Button(self.mainframe, text="Submit", command=self.Login, bd='10', font='verdana', bg='green', fg='yellow')
        self.bsubmit.grid(columnspan=10)
        self.bsubmit2 = Button(self.mainframe, text="New USER? Please SIGN UP first!", command=self.sqllogin, bd='10',font='Aerial', bg='black', fg='pink')
        self.bsubmit2.grid(columnspan=10)

    def Login(self):
        self.g1 = self.Entry1.get()
        self.g2 = self.Entry2.get()
        self.c = 0
        mydb2 = mysql.connect(host="localhost", user="Pratyusha", passwd="pratyusha12345",database="StudentInformation")
        mycursor2 = mydb2.cursor()
        mycursor2.execute("select Username,Password from SignIn")
        for i in mycursor2:
            if (i == (self.g1, self.g2)):
                self.c = self.c + 1
        if (self.c == 0):
            MsgBox.showinfo("Login Status", "Invalid Username or Password")
            self.Entry1.delete(0, 'end')
            self.Entry2.delete(0, 'end')
            mydb2.close()
        else:
            top1 = Toplevel(root)
            top1.geometry("400x300")
            top1.title("GUI(1)")
            top1.configure(bg='green')

            self.s1 = Label(top1, text="Name:", font='timesnewroman', bd='15', fg='black',bg='green')
            self.s2 = Label(top1, text="Branch:", font='timesnewroman', bd='15', fg='black',bg='green')
            self.s3 = Label(top1, text="Registration ID:", font='timesnewroman', bd='15', fg='black',bg='green')

            self.se1 = Entry(top1)
            self.se2 = Entry(top1)
            self.se3 = Entry(top1)

            self.s1.grid(row=0, sticky=E)
            self.s2.grid(row=1, sticky=E)
            self.s3.grid(row=2, sticky=E)

            self.se1.grid(row=0, column=1)
            self.se2.grid(row=1, column=1)
            self.se3.grid(row=2, column=1)

            self.subut2 = Button(top1, text="Submit", font='verdana', bd='15', fg='white', bg='purple', command=self.datasave)
            self.subut2.grid(columnspan=40)
            top1.mainloop()
    def datasave(self):
            self.v1 = self.se1.get()
            self.v2 = self.se2.get()
            self.v3 = self.se3.get()
            self.d = 0
            self.o = int(self.v3)
            mydb3 = mysql.connect(host="localhost", user="Pratyusha", passwd="pratyusha12345",database="StudentInformation")
            mycursor3 = mydb3.cursor()
            mycursor3.execute("select Branch, Registration_ID from Information")
            for i in mycursor3:
                if (i == (self.v2,self.o)):
                    self.d = self.d + 1

            if (self.d == 0):
                mycursor3.execute("insert into Information(Name,Branch,Registration_ID) values('"+self.v1+"','"+self.v2+"','"+self.v3+"')")
                mycursor3.execute("commit")
                MsgBox.showinfo("Saving Data","Data saved successfully")
            mydb3.close()

            top2 = Toplevel()
            top2.title("GUI(2)")
            top2.geometry("550x300")
            top2.configure(bg='black')
            self.thbut1 = Button(top2, text="Computer", font='TIMESNEWROMAN', bd='20', fg='BLUE', bg='cyan',command=lambda:  self.Entermarks("Computer"))
            self.thbut1.grid(columnspan=4,row=2,column=15)
            self.thbut2 = Button(top2, text="English", font='timesnewroman', bd='20', fg='purple', bg='ORANGE',command=lambda: self.Entermarks("English"))
            self.thbut2.grid(columnspan=4,row=4,column=20)
            self.thbut3 = Button(top2, text="Mathematics", font='timesnewroman', bd='20', fg='BROWN', bg='PEACHPUFF',command=lambda: self.Entermarks("Mathematics"))
            self.thbut3.grid(columnspan=4,row=6,column=30)
            self.thbut4 = Button(top2, text="Submit", font='timesnewroman', bd='25', fg='YELLOW', bg='GREEN',command=self.submitMark)
            self.thbut4.grid(columnspan=4,row=8,column=45)
            top2.mainloop()
    def Entermarks(self,str):
       toplevel2 = Toplevel()
       toplevel2.geometry("400x200")
       toplevel2.title("Input Marks")
       toplevel2.configure(bg='BROWN')
       self.s = str
       self.em1 = Label(toplevel2, text="Enter Marks:", font='TIMESNEWROMAN', bd='30', fg='WHITE',bg='brown')
       self.em1.grid(row=0,sticky=E)
       self.ent = Entry(toplevel2)
       self.ent.grid(row=0,column=1)

       toplevel2.mainloop()

    def submitMark(self):
      self.br = self.se2.get()
      self.re = self.se3.get()
      self.ir = int(self.re)
      mydb4 = mysql.connect(host="localhost", user="Pratyusha", passwd="pratyusha12345", database="StudentInformation")
      mycursor4 = mydb4.cursor()
      self.gm = self.ent.get()
      self.i = self.s
      mycursor4.execute("update Information set  Marks = '"+self.gm+"' , Subject = '"+self.s+"'  where (Branch = '"+self.br+"'  AND Registration_ID = '"+self.re+"' )")
      mydb4.close()

      top4 = Toplevel()
      top4.geometry("500x300")
      top4.title("GUI(3)")
      top4.configure(bg='black')
      self.but1 = Button(top4, text="CGPA", font='TIMESNEWROMAN', bd='20', fg='BROWN', bg='violet', command=self.calcCGPA)
      self.but1.grid(columnspan=4,row=2,column=15)
      self.but2 = Button(top4, text="GRADE", font='TIMESNEWROMAN', bd='20', fg='YELLOW', bg='GREEN', command=self.grade)
      self.but2.grid(columnspan=4,row=4,column=20)
      self.but3 = Button(top4, text="New Input", font='TIMESNEWROMAN', bd='20', fg='BLUE', bg='CYAN', command=self.new)
      self.but3.grid(columnspan=4,row=6,column=30)
      self.but4 = Button(top4, text="CLOSE", font='TIMESNEWROMAN', bd='20', fg='black', bg='RED', command=self.close)
      self.but4.grid(columnspan=4,row=8,column=40)
      top4.mainloop()

    def calcCGPA(self):
        self.mark = int(self.ent.get())
        self.res = round((self.mark / 9.5),3)
        MsgBox.showinfo("CGPA on range of 10", self.res)

    def grade(self):
        self.m = int(self.ent.get())
        self.grd = self.m / 9.5
        if (self.grd > 9 and self.grd <= 10):
            MsgBox.showinfo("Grade", "Grade = O")
        elif (self.grd > 8 and self.grd <= 9):
            MsgBox.showinfo("Grade", "Grade = E")
        elif (self.grd > 7 and self.grd <= 8):
            MsgBox.showinfo("Grade", "Grade = A")
        elif (self.grd > 6 and self.grd <= 7):
            MsgBox.showinfo("Grade", "Grade = B")
        elif (self.grd > 5 and self.grd <= 6):
            MsgBox.showinfo("Grade", "Grade = C")
        elif (self.grd > 4 and self.grd <= 5):
            MsgBox.showinfo("Grade", "Grade = D")
        else:
            MsgBox.showinfo("Grade", "Grade = F")

    def close(self):
        root.destroy()

    def new(self):
        self.Login()

    def sqllogin(self):
        prat1 = Tk()
        prat1.geometry("400x300")
        prat1.title("SIGN UP")
        prat1.configure(bg='cyan')

        self.label2 = Label(prat1, text="Name:", font='Verdana', bd='20', fg='purple',bg='cyan')
        self.label2.grid(row=1, sticky=E)
        self.label3 = Label(prat1, text="Username:", font='Verdana', bd='20', fg='purple',bg='cyan')
        self.label3.grid(row=2, sticky=E)
        self.label4 = Label(prat1, text="Password:", font='Verdana', bd='20', fg='purple',bg='cyan')
        self.label4.grid(row=3, sticky=E)

        self.enter2 = Entry(prat1)
        self.enter2.grid(row=1, column=1)
        self.enter3 = Entry(prat1)
        self.enter3.grid(row=2, column=1)
        self.enter4 = Entry(prat1)
        self.enter4.grid(row=3, column=1)

        self.butt = Button(prat1, text="Sign Up", command=self.Save, font='timesnewroman', bd='15', fg='peachpuff', bg='purple')
        self.butt.grid(columnspan=150)

        prat1.mainloop()

    def Save(self):
        self.e2 = self.enter2.get()
        self.e3 = self.enter3.get()
        self.e4 = self.enter4.get()
        self.c = 0
        mydb1 = mysql.connect(host="localhost", user="Pratyusha", passwd="pratyusha12345",database="StudentInformation")
        mycursor1 = mydb1.cursor()
        mycursor1.execute("show tables like 'SignIN'")
        table = mycursor1.fetchone()
        if not table:
            mycursor1.execute("create table SignIN(Name varchar(50),Username varchar(20),Password varchar(30))")
            MsgBox.showinfo("Table Creation", "Table successfully created")
        mycursor1.execute("select Username,Password from SignIN")
        for t in mycursor1:
            if (t == (self.e3, self.e4)):
                    self.c = self.c + 1
        if (self.c != 0):
                MsgBox.showinfo("SignUp Status", "Username already used!")
                self.enter3.delete(0,'end')
        else:
          mycursor1.execute("insert into SignIN(Name,Username,Password) values('"+self.e2+"','"+self.e3+"','"+self.e4+"')")
          mycursor1.execute("commit")
          mycursor1.execute("select * from SignIN")
          MsgBox.showinfo("Insert Status", "All the information saved")
          mydb1.close()

f = First(root)
root.mainloop()