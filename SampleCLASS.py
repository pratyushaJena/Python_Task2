from tkinter import *
import tkinter.messagebox as MsgBox
import mysql.connector as mysql

root = Tk()
root.geometry("600x300")
root.title("GUI1")

class First:
    def __init__(self, master):
        self.mainframe = Frame(master, bg='white')
        self.mainframe.pack()
        self.one = Label(self.mainframe, text="User Name:", font='Bold', bd='9', fg='Brown')
        self.two = Label(self.mainframe, text="Password:", font='Bold', bd='9', fg='Brown')
        self.one.grid(row=0,sticky=E)
        self.two.grid(row=1,sticky=E)

        self.Entry1 = Entry(self.mainframe)
        self.Entry2 = Entry(self.mainframe)
        self. Entry1.grid(row=0, column=1)
        self.Entry2.grid(row=1, column=1)

        self.bsubmit = Button(self.mainframe, text="Submit", command=self.Login, bd='4', font='Bold', bg='Black', fg='Yellow')
        self.bsubmit.grid(columnspan=4)
        self.bsubmit2 = Button(self.mainframe, text="New USER? Please SIGN UP first!", command=self.sqllogin, bd='4',font='Aerial', bg='Black', fg='Pink')
        self.bsubmit2.grid(columnspan=4)

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
        print(self.c)
        if (self.c == 0):
            MsgBox.showinfo("Login Status", "Invalid Password")
            self.Entry1.delete(0, 'end')
            self.Entry2.delete(0, 'end')
            mydb2.close()
        else:
            top1 = Toplevel(root)
            top1.geometry("600x300")
            top1.title("GUI2")

            self.s1 = Label(top1, text="Name", font='Bold', bd='10', fg='purple')
            self.s2 = Label(top1, text="Branch", font='Bold', bd='10', fg='purple')
            self.s3 = Label(top1, text="Registration ID", font='Bold', bd='10', fg='purple')

            self.se1 = Entry(top1)
            self.se2 = Entry(top1)
            self.se3 = Entry(top1)

            self.s1.grid(row=0, sticky=E)
            self.s2.grid(row=1, sticky=E)
            self.s3.grid(row=2, sticky=E)

            self.se1.grid(row=0, column=1)
            self.se2.grid(row=1, column=1)
            self.se3.grid(row=2, column=1)

            self.subut2 = Button(top1, text="Submit", font='Bold', bd='10', fg='purple', bg='green', command=self.datasave)
            self.subut2.grid(columnspan=4)
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
                mycursor3.execute("select * from Information")
                for j in mycursor3:
                    print(j)
                MsgBox.showinfo("Saving Data","Data saved successfully")
            mydb3.close()

            top2 = Toplevel()
            top2.title("GUI3")
            top2.geometry("600x300")
            self.thbut1 = Button(top2, text="Computer", font='Bold', bd='5', fg='Black', bg='Blue',command=self.Entermarks)
            self.thbut1.grid(columnspan=4)
            self.thbut2 = Button(top2, text="English", font='Bold', bd='10', fg='black', bg='purple',command=self.Entermarks)
            self.thbut2.grid(columnspan=4)
            self.thbut3 = Button(top2, text="Maths", font='Bold', bd='10', fg='black', bg='Red',command=self.Entermarks)
            self.thbut3.grid(columnspan=4)
            self.thbut4 = Button(top2, text="Submit", font='Bold', bd='10', fg='black', bg='white',command=self.submitMark)
            self.thbut4.grid(columnspan=4)
            top2.mainloop()
    def Entermarks(self):
       toplevel2 = Toplevel()
       toplevel2.geometry("200x200")
       toplevel2.title("Input Marks")
       self.em1 = Label(toplevel2, text="Enter Marks", font='Bold', bd='10', fg='purple')
       self.em1.grid(row=0,sticky=E)
       self.ent = Entry(toplevel2)
       self.ent.grid(row=0,column=1)

       toplevel2.mainloop()

    def submitMark(self):
      self.br = self.se2.get()
      self.re = self.se3.get()
      self.ir = int(self.re)
      print(self.br)
      print(self.ir)
      mydb4 = mysql.connect(host="localhost", user="Pratyusha", passwd="pratyusha12345", database="StudentInformation")
      mycursor4 = mydb4.cursor()
      self.gm = self.ent.get()
      self.i = int(self.gm)
      print(self.i)
      mycursor4.execute("update Information set Marks = '"+self.gm+"' where (Branch = '"+self.br+"'  AND Registration_ID = '"+self.re+"' )")
      mycursor4.execute("select * from Information")
      for m in mycursor4:
          print(m)
      mydb4.close()

      top4 = Toplevel()
      top4.geometry("600x300")
      top4.title("GUI4")
      self.but1 = Button(top4, text="CGPA", font='Bold', bd='10', fg='pink', bg='green', command=self.calcCGPA)
      self.but1.grid(columnspan=4)
      self.but2 = Button(top4, text="GRADE", font='Bold', bd='10', fg='blue', bg='yellow', command=self.grade)
      self.but2.grid(columnspan=4)
      self.but3 = Button(top4, text="New Input", font='Bold', bd='5', fg='black', bg='orange', command=self.new)
      self.but3.grid(columnspan=4)
      self.but4 = Button(top4, text="CLOSE", font='Bold', bd='10', fg='white', bg='red', command=self.close)
      self.but4.grid(columnspan=4)
      top4.mainloop()

    def calcCGPA(self):
        self.mark = int(self.ent.get())
        self.res = self.mark / 9.5
        print(self.res)
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
        toplevel5 = Toplevel(root)
        toplevel5.title("GUI1")
        toplevel5.geometry("600x300")
        self.mainframe1 = Frame(toplevel5, bg='white')
        self.mainframe1.pack()
        self.one = Label(self.mainframe1, text="User Name:", font='Bold', bd='9', fg='Brown')
        self.two = Label(self.mainframe1, text="Password:", font='Bold', bd='9', fg='Brown')
        self.one.grid(row=0, sticky=E)
        self.two.grid(row=1, sticky=E)

        self.Entry1 = Entry(self.mainframe1)
        self.Entry2 = Entry(self.mainframe1)
        self.Entry1.grid(row=0, column=1)
        self.Entry2.grid(row=1, column=1)

        self.bsubmit = Button(self.mainframe1, text="Submit", command=self.Login2, bd='4', font='Bold', bg='Black',
                              fg='Yellow')
        self.bsubmit.grid(columnspan=4)
        self.bsubmit2 = Button(self.mainframe1, text="New USER? Please SIGN UP first!", command=self.sqllogin, bd='4',
                               font='Aerial', bg='Black', fg='Pink')
        self.bsubmit2.grid(columnspan=4)

        toplevel5.mainloop()

    def Login2(self):
        self.g1 = self.Entry1.get()
        self.g2 = self.Entry2.get()
        self.c = 0
        mydb2 = mysql.connect(host="localhost", user="Pratyusha", passwd="pratyusha12345",database="StudentInformation")
        mycursor2 = mydb2.cursor()
        mycursor2.execute("select Username,Password from SignIn")
        for i in mycursor2:
            if (i == (self.g1, self.g2)):
                self.c = self.c + 1
        print(self.c)
        if (self.c == 0):
            MsgBox.showinfo("Login Status", "Invalid Password")
            self.Entry1.delete(0, 'end')
            self.Entry2.delete(0, 'end')
            mydb2.close()
        else:
            top6 = Toplevel(root)
            top6.geometry("600x300")
            top6.title("GUI2")

            self.s1 = Label(top6, text="Name", font='Bold', bd='10', fg='purple')
            self.s2 = Label(top6, text="Branch", font='Bold', bd='10', fg='purple')
            self.s3 = Label(top6, text="Registration ID", font='Bold', bd='10', fg='purple')

            self.se1 = Entry(top6)
            self.se2 = Entry(top6)
            self.se3 = Entry(top6)

            self.s1.grid(row=0, sticky=E)
            self.s2.grid(row=1, sticky=E)
            self.s3.grid(row=2, sticky=E)

            self.se1.grid(row=0, column=1)
            self.se2.grid(row=1, column=1)
            self.se3.grid(row=2, column=1)

            self.subut2 = Button(top6, text="Submit", font='Bold', bd='10', fg='purple', bg='green', command=self.datasave)
            self.subut2.grid(columnspan=4)
            top6.mainloop()

    def Entermarks1(self):
        top3 = Toplevel()
        self.em1 = Label(top3, text="Enter Marks", font='Bold', bd='10', fg='purple')
        self.em1.grid(row=0, sticky=E)
        self.ent = Entry(top3)
        self.ent.grid(row=0, column=1)
        top3.mainloop()

    def sqllogin(self):
        prat1 = Tk()
        prat1.geometry("600x300")
        prat1.title("SIGN UP")

        self.label2 = Label(prat1, text="Name", font='Bold', bd='10', fg='purple')
        self.label2.grid(row=1, sticky=E)
        self.label3 = Label(prat1, text="Username", font='Bold', bd='10', fg='purple')
        self.label3.grid(row=2, sticky=E)
        self.label4 = Label(prat1, text="Password", font='Bold', bd='10', fg='purple')
        self.label4.grid(row=3, sticky=E)

        self.enter2 = Entry(prat1)
        self.enter2.grid(row=1, column=1)
        self.enter3 = Entry(prat1)
        self.enter3.grid(row=2, column=1)
        self.enter4 = Entry(prat1)
        self.enter4.grid(row=3, column=1)

        self.butt = Button(prat1, text="Sign Up", command=self.Save, font='Bold', bd='10', fg='purple', bg='green')
        self.butt.grid(columnspan=4)

        prat1.mainloop()

    def Save(self):
        self.e2 = self.enter2.get()
        self.e3 = self.enter3.get()
        self.e4 = self.enter4.get()
        self.c = 0
        mydb1 = mysql.connect(host="localhost", user="Pratyusha", passwd="pratyusha12345",database="StudentInformation")
        mycursor1 = mydb1.cursor()
        mycursor1.execute("select Username,Password from SignIn")
        for t in mycursor1:
            if (t == (self.e3, self.e4)):
                    self.c = self.c + 1
        if (self.c != 0):
                MsgBox.showinfo("SignUp Status", "Username already used!")
                self.enter3.delete(0,'end')
        else:
          mycursor1.execute("insert into SignIn(Stu_Name,Username,Password) values('"+self.e2+"','"+self.e3+"','"+self.e4+"')")
          mycursor1.execute("commit")
          mycursor1.execute("select * from SignIn")
          for i in mycursor1:
              print(i)
          MsgBox.showinfo("Insert Status", "All the information saved")
          mydb1.close()



f = First(root)
root.mainloop()