from tkinter import*
import datetime
# import pymysql
# import pymysql.cursors
from tkinter import messagebox
import tkinter.messagebox as tkMessageBox
from tkinter import ttk
import tkinter as tk
#from tkinter import scrolledtext
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4
# import qrcode,webbrowser,os
import matplotlib.pyplot as plt

win=Tk()
win.geometry("1000x600")
win.title("ERP Software")
win.config(bg='lavender')
win.resizable(False,False)

class Vendor:
    def printvendors(self,obj,Data):
        try:
            os.mkdir("F:\\InvoiceGeneration\\Vendors\\")
        except:
            pass
        conn=pymysql.connect(host='localhost',user='root',password='',db='software')
        a=conn.cursor()
        a.execute('select CompanyName,Name,GST,PAN,Mobile,Email,Address,Locality,State from client')
        result=a.fetchall()
        cName=StringVar
        Name=StringVar
        G=StringVar
        P=StringVar
        M=StringVar
        E=StringVar
        Add=StringVar
        Loc=StringVar()
        sts=StringVar()            
        for i in result:
            cName=i[0]
            Name=i[1]
            G=i[2]
            P=i[3]
            M=i[4]
            E=i[5]
            Add=i[6]
            Loc=i[7]
            sts=i[8]
        
        now=datetime.datetime.today()
        Number='Vendors'+str(now.strftime('%y'))+str(now.strftime('%d'))+str(now.microsecond)
        Canvas(width=210,height=293)
        pdf= canvas.Canvas("F:\\InvoiceGeneration\\Vendors\\"+str(Number)+".pdf",pagesize=A4)
        width,height=A4
        pdf.setTitle("Vendors Report")
        pdf.line(20,815,560,815)
        pdf.setFont("Courier-Bold",25)
        pdf.drawString(150,795,cName)
        pdf.setFont("Courier-Bold",10)
        pdf.drawString(245,780,Name)
        pdf.drawString(245,765,"Gst:"+G)
        pdf.drawString(245,750,"Pan:"+P)
        pdf.drawString(150,735,"Mobile:"+M+"  Email:"+E)
        pdf.drawString(250,720,Add)
        pdf.drawString(150,705,Loc)
        pdf.drawString(250,690,sts)
        pdf.line(20,677,560,677)

        pdf.drawString(35,668,"Id")
        pdf.drawString(65,668,"Company Name")
        pdf.drawString(205,668,"Owner Name")
        pdf.drawString(280,668,"PAN")
        pdf.drawString(345,668,"GST")
        pdf.drawString(428,668,"Email-ID")
        pdf.drawString(515,668,"Contact")

        pdf.line(20,662,560,662)
        pdf.line(60,677,60,100)
        pdf.line(200,677,200,100)
        pdf.line(270,677,270,100)
        pdf.line(320,677,320,100)
        pdf.line(400,677,400,100)
        pdf.line(510,677,510,100)
        pdf.line(30,100,550,100)

        ycoordinate=IntVar()
        ycoordinate=650
        
        for i in Data:
            pdf.setFont("Courier-Bold",7)
            pdf.drawString(10,ycoordinate,i[0])
            pdf.drawString(65,ycoordinate,i[1])
            pdf.drawString(210,ycoordinate,i[2])
            pdf.drawString(275,ycoordinate,i[5])
            pdf.drawString(325,ycoordinate,i[4])
            pdf.drawString(410,ycoordinate,i[7])
            pdf.drawString(515,ycoordinate,i[6])
            ycoordinate = ycoordinate - 15
            
        pdf.save()
        webbrowser.open("F:\\InvoiceGeneration\\Vendors\\"+str(Number)+".pdf")
        
        
    def show(self,obj):
        
        Data=[]
        frame2=Frame(win,width=1000,height=600,bg="lavender").place(x=0,y=0)
        conn=pymysql.connect(host='localhost',user='root',password='',db='software')
        a=conn.cursor()
        a.execute('select ID,Company,Name,Gender,GST,PAN,Mobile,Email,State from venders')
        result=a.fetchall()
        count=a.rowcount

        frame3=Frame(win,width=960,height=407,bg="black").place(x=10,y=160)
        self.scrollbary = Scrollbar(frame3,orient=VERTICAL)
        self.tree = ttk.Treeview(frame3,columns=(1,2,3,4,5,6,7,8,9),show='headings',height=19, selectmode="extended", yscrollcommand=self.scrollbary.set)
        Update_data=self.tree.selection()
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        self.tree.place(x=10,y=160)
        self.tree.heading(1,text='Vendor ID')
        self.tree.heading(2,text='Company Name')
        self.tree.heading(3,text='Owner Name')
        self.tree.heading(4,text='Gender')
        self.tree.heading(5,text='GST Number')
        self.tree.heading(6,text='Pan Number')
        self.tree.heading(7,text='Mobile No.')
        self.tree.heading(8,text='Email-Id')
        self.tree.heading(9,text='State')

        self.tree.column(1,stretch=NO,width=85)
        self.tree.column(2,stretch=NO,width=165)
        self.tree.column(3,stretch=NO,width=97)
        self.tree.column(4,stretch=NO,width=60)
        self.tree.column(5,stretch=NO,width=120)
        self.tree.column(6,stretch=NO,width=90)
        self.tree.column(7,stretch=NO,width=80)
        self.tree.column(8,stretch=NO,width=170)
        self.tree.column(9,stretch=NO,width=90)
    
        for i in result:
            Data.append(i)
            self.tree.insert('','end',values=i)
            
        Label(frame2,text='VENDORS',font=('Times New Roman',73),fg='orangered',bg="lavender").place(x=300,y=0)
        self.pho=PhotoImage(file="home.png")
        Button(frame2,image=self.pho,border=0,compound=TOP,bg='lavender',command=obj.home).place(x=10,y=0)
        Button(frame2,text="Print",bd=2,width=6,height=1,relief="ridge",bg='gray25',fg='white',font=('Poor Richard',15),command=lambda:obj.printvendors(obj,Data)).place(x=830,y=100)
        Button(frame2,text="New",bd=2,width=10,height=1,relief="ridge",bg='purple3',fg='white',font=('Poor Richard',20),command=lambda:obj.New(obj)).place(x=800,y=20)
        
    def New(self,obj):
        frame1=Frame(win,width=1000,height=600,bg="lavender").place(x=0,y=0)
        
        Label(frame1,text="Vendor Registraion",font=('Times New Roman',73),fg='orangered',bg="lavender").place(x=100,y=0)
        
        vid=StringVar()
        vi=StringVar()
        cn=StringVar()
        pn=StringVar()
        gen=IntVar()
        gst=StringVar()
        pan=StringVar()
        mob=StringVar()
        plno=StringVar()
        loc=StringVar()
        dist=StringVar()
        email=StringVar()
        sdist=StringVar()
        st=StringVar()
        pinc=StringVar()
        rm=StringVar()
        Address=StringVar()
        now=datetime.datetime.today()
        vi=str('V')+now.strftime('%y')+str('-')+str(now.day)+str(now.microsecond)
        vid.set(vi)
        Label(frame1,text='Vendor Id',font=('Arail',15),bg="lavender").place(x=200,y=140)
        Entry(frame1,width=63,textvariable=vid,bg="lavender",border=0).place(x=360,y=146)
        
        Label(frame1,text="Company Name :",font=('Arail',15),bg="lavender").place(x=200,y=180)
        Entry(frame1,width=63,textvariable=cn).place(x=360,y=186)

        Label(frame1,text="Proprietor Name :",font=('Arail',15),bg="lavender").place(x=200,y=214)
        Entry(frame1,width=63,textvariable=pn).place(x=360,y=220)

        Label(frame1,text="Gender:",font=('Arail',15),bg="lavender").place(x=200,y=248)
        r1=tk.Radiobutton(frame1,text="Male",padx=20,value=0,bg="lavender",variable=gen).place(x=360,y=252)  
        r2=tk.Radiobutton(frame1,text='Female',padx=20,value=1,bg="lavender",variable=gen).place(x=450,y=252)
       
        
        Label(frame1,text="GST Number:",font=('Arail',15),bg="lavender").place(x=200,y=282)
        Entry(frame1,width=63,textvariable=gst).place(x=360,y=286)

        Label(frame1,text="PAN Number:",font=('Arail',15),bg="lavender").place(x=200,y=316)
        Entry(frame1,width=63,textvariable=pan).place(x=360,y=320)

        Label(frame1,text="Mobile Number:",font=('Arail',15),bg="lavender").place(x=200,y=350)
        Entry(frame1,width=63,textvariable=mob).place(x=360,y=354)

        Label(frame1,text="Email ID:",font=('Arail',15),bg="lavender").place(x=200,y=384)
        Entry(frame1,width=63,textvariable=email).place(x=360,y=390)

        Label(frame1,text="Plot no:",font=('Arail',15),bg="lavender").place(x=200,y=418)
        Entry(frame1,width=63,textvariable=plno).place(x=360,y=424)


        Label(frame1,text="Locality:",font=('Arail',15),bg="lavender").place(x=200,y=452)
        Entry(frame1,width=63,textvariable=loc).place(x=360,y=456)


        Label(frame1,text="District:",font=('Arail',15),bg="lavender").place(x=200,y=486)
        Entry(frame1,width=20,textvariable=dist).place(x=360,y=492)


        Label(frame1,text="Sub-Division:",font=('Arail',15),bg="lavender").place(x=500,y=486)
        Entry(frame1,width=20,textvariable=sdist).place(x=620,y=492)


        Label(frame1,text="State:",font=('Arail',15),bg="lavender").place(x=200,y=520)
        Entry(frame1,width=20,textvariable=st).place(x=360,y=526)

        
        Label(frame1,text="Pincode:",font=('Arail',15),bg="lavender").place(x=500,y=520)
        Entry(frame1,width=20,textvariable=pinc).place(x=620,y=526)
        

        Label(frame1,text="Remarks:",font=('Arail',15),bg="lavender").place(x=200,y=560)
        Entry(frame1,width=63,textvariable=rm).place(x=360,y=566)

        self.pho=PhotoImage(file="home.png")
        
        Button(frame1,image=self.pho,border=0,font=('Maiandra GD',20),compound=TOP,bg='lavender',command=obj.home).place(x=800,y=150)
        Button(frame1,text="Reload",bd=2,width=12,height=1,relief="ridge",bg='yellow',fg='black',font=('Poor Richard',20),command=lambda:obj.New(obj)).place(x=800,y=340)
        Button(frame1,text="Reset",bd=2,width=12,height=1,relief="ridge",bg='blue',fg='white',font=('Poor Richard',20),command=lambda:obj.rese(vid.set(''),cn.set(''),pn.set(''),gen.set(''),gst.set(''),pan.set(''),mob.set(''),email.set(''),plno.set(''),loc.set(''),dist.set(''),sdist.set(''),st.set(''),pinc.set(''),rm.set(''))).place(x=800,y=420)
      
        Button(frame1,text="Save",bd=2,width=12,height=1,relief="ridge",bg='Green',fg='white',font=('Poor Richard',20),command=lambda:obj.save(obj,vid.get(),cn.get(),pn.get(),gen.get(),gst.get(),pan.get(),mob.get(),email.get(),plno.get(),loc.get(),dist.get(),sdist.get(),st.get(),pinc.get(),rm.get())).place(x=800,y=500)
        
    def save(self,obj,vid,cn,pn,gen,gst,pan,mob,email,plno,loc,dist,sdist,st,pinc,rm):
        self.vid=vid
        self.cn=cn
        self.pn=pn
        self.gen=gen
        self.gst=gst
        self.pan=pan
        self.mob=mob
        self.email=email
        self.plno=plno
        self.loc=loc
        self.dist=dist
        self.sdist=sdist
        self.st=st
        self.pinc=pinc
        self.rm=rm
        gender=StringVar
        if self.gen == 0:
            gender='Male'
        else:
            gender='Female'
            
        try:
            conn=pymysql.connect(host='localhost',user='root',password='',db='software')
            a=conn.cursor()
            a.execute("insert into venders(ID,Company,Name,Gender,GST,PAN,Mobile,Email,Plot,Locality,District,Division,State,Pincode,Remarks)value('"+vid+"','"+cn+"','"+pn+"','"+gender+"','"+gst+"','"+pan+"','"+mob+"','"+email+"','"+plno+"','"+loc+"','"+dist+"','"+sdist+"','"+st+"','"+pinc+"','"+rm+"')")
            conn.commit()
            obj.New(obj)
            messagebox.showinfo("Status","Saved")
        except:
            conn.rollback()
            messagebox.showinfo("Status","Not Saved")
        conn.close()

    def update(self,obj,Update_data):
        self.Update_data=Update_data
        
    def rese(self,vid,cn,pn,gen,gst,pan,mob,email,plno,loc,dist,sdist,st,pinc,rm):
        messagebox.showinfo("Status","Reseted")

    def home(self):
        self.front=main(win)

class Customers:
    def printCustomers(self,obj,Data):
        try:
            os.mkdir("F:\\InvoiceGeneration\\Customers\\")
        except:
            pass
        conn=pymysql.connect(host='localhost',user='root',password='',db='software')
        a=conn.cursor()
        a.execute('select CompanyName,Name,GST,PAN,Mobile,Email,Address,Locality,State from client')
        result=a.fetchall()
        cName=StringVar
        Name=StringVar
        G=StringVar
        P=StringVar
        M=StringVar
        E=StringVar
        Add=StringVar
        Loc=StringVar()
        sts=StringVar()            
        for i in result:
            cName=i[0]
            Name=i[1]
            G=i[2]
            P=i[3]
            M=i[4]
            E=i[5]
            Add=i[6]
            Loc=i[7]
            sts=i[8]
        
        now=datetime.datetime.today()
        Number='Customers'+str(now.strftime('%y'))+str(now.strftime('%d'))+str(now.microsecond)
        Canvas(width=210,height=293)
        pdf= canvas.Canvas("F:\\InvoiceGeneration\\Customers\\"+str(Number)+".pdf",pagesize=A4)
        width,height=A4
        pdf.setTitle("Customers Report")
        pdf.line(20,815,560,815)
        pdf.setFont("Courier-Bold",25)
        pdf.drawString(150,795,cName)
        pdf.setFont("Courier-Bold",10)
        pdf.drawString(245,780,Name)
        pdf.drawString(245,765,"Gst:"+G)
        pdf.drawString(245,750,"Pan:"+P)
        pdf.drawString(150,735,"Mobile:"+M+"  Email:"+E)
        pdf.drawString(250,720,Add)
        pdf.drawString(150,705,Loc)
        pdf.drawString(250,690,sts)
        pdf.line(20,677,560,677)

        pdf.drawString(35,668,"Id")
        pdf.drawString(65,668,"Company Name")
        pdf.drawString(205,668,"Owner Name")
        pdf.drawString(280,668,"PAN")
        pdf.drawString(345,668,"GST")
        pdf.drawString(428,668,"Email-ID")
        pdf.drawString(515,668,"Contact")

        pdf.line(20,662,560,662)
        pdf.line(60,677,60,100)
        pdf.line(200,677,200,100)
        pdf.line(270,677,270,100)
        pdf.line(320,677,320,100)
        pdf.line(400,677,400,100)
        pdf.line(510,677,510,100)
        pdf.line(30,100,550,100)

        ycoordinate=IntVar()
        ycoordinate=650
        for i in Data:
            pdf.setFont("Courier-Bold",7)
            pdf.drawString(10,ycoordinate,i[0])
            pdf.drawString(65,ycoordinate,i[1])
            pdf.drawString(210,ycoordinate,i[2])
            pdf.drawString(275,ycoordinate,i[5])
            pdf.drawString(325,ycoordinate,i[4])
            pdf.drawString(410,ycoordinate,i[7])
            pdf.drawString(515,ycoordinate,i[6])
            ycoordinate = ycoordinate - 15
            
        pdf.save()
        webbrowser.open("F:\\InvoiceGeneration\\Customers\\"+str(Number)+".pdf")
        
    def show(self,obj):
        Data=[]
        frame2=Frame(win,width=1000,height=600,bg="lavender").place(x=0,y=0)
        conn=pymysql.connect(host='localhost',user='root',password='',db='software')
        a=conn.cursor()
        a.execute('select ID,Company,Name,Gender,GST,PAN,Mobile,Email,State from customers')
        result=a.fetchall()
        count=a.rowcount

        frame3=Frame(win,width=960,height=407,bg="black").place(x=10,y=160)
        self.scrollbary = Scrollbar(frame3,orient=VERTICAL)
        self.tree = ttk.Treeview(frame3,columns=(1,2,3,4,5,6,7,8,9),show='headings',height=19, selectmode= EXTENDED, yscrollcommand=self.scrollbary.set)
        Update_data=self.tree.selection()
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill='y')
        self.tree.place(x=10,y=160)

        self.tree.heading(1,text='Customer ID')
        self.tree.heading(2,text='Company Name')
        self.tree.heading(3,text='Owner Name')
        self.tree.heading(4,text='Gender')
        self.tree.heading(5,text='GST Number')
        self.tree.heading(6,text='Pan Number')
        self.tree.heading(7,text='Mobile No.')
        self.tree.heading(8,text='Email-Id')
        self.tree.heading(9,text='State')

        self.tree.column(1,stretch=NO,width=85)
        self.tree.column(2,stretch=NO,width=165)
        self.tree.column(3,stretch=NO,width=97)
        self.tree.column(4,stretch=NO,width=60)
        self.tree.column(5,stretch=NO,width=120)
        self.tree.column(6,stretch=NO,width=90)
        self.tree.column(7,stretch=NO,width=80)
        self.tree.column(8,stretch=NO,width=170)
        self.tree.column(9,stretch=NO,width=90)

        for i in result:
            Data.append(i)
            self.tree.insert('','end',values=i)

        Label(frame2,text='CUSTOMERS',font=('Times New Roman',70),fg='orangered',bg="lavender").place(x=220,y=0)
        self.pho=PhotoImage(file="home.png")
        Button(frame2,image=self.pho,border=0,compound=TOP,bg='lavender',command=obj.home).place(x=10,y=0)
        Button(frame2,text="New",bd=2,width=10,height=1,relief="ridge",bg='purple3',fg='white',font=('Poor Richard',20),command=lambda:obj.New(obj)).place(x=800,y=20)
        Button(frame2,text="Print",bd=2,width=6,height=1,relief="ridge",bg='gray25',fg='white',font=('Poor Richard',15),command=lambda:obj.printCustomers(obj,Data)).place(x=820,y=100)

    def home(self):
        self.front=main(win)   
        
    def New(self,obj):
        frame1=Frame(win,width=1000,height=600,bg="lavender").place(x=0,y=0)
        
        Label(frame1,text="Customer Registraion",font=('Times New Roman',73),fg='orangered',bg="lavender").place(x=100,y=0)
        
        cid=StringVar()
        ci=StringVar()
        cn=StringVar()
        pn=StringVar()
        gen=IntVar()
        gst=StringVar()
        pan=StringVar()
        mob=StringVar()
        plno=StringVar()
        loc=StringVar()
        dist=StringVar()
        email=StringVar()
        sdist=StringVar()
        st=StringVar()
        pinc=StringVar()
        rm=StringVar()
        Address=StringVar()
        now=datetime.datetime.today()
        ci=str('C')+now.strftime('%y')+str('-')+str(now.day)+str(now.microsecond)
        cid.set(ci)
        Label(frame1,text='Customer Id',font=('Arail',15),bg="lavender").place(x=200,y=140)
        Entry(frame1,width=63,textvariable=cid,bg="lavender",border=0).place(x=360,y=146)
        
        Label(frame1,text="Company Name :",font=('Arail',15),bg="lavender").place(x=200,y=180)
        Entry(frame1,width=63,textvariable=cn).place(x=360,y=186)

        Label(frame1,text="Proprietor Name :",font=('Arail',15),bg="lavender").place(x=200,y=214)
        Entry(frame1,width=63,textvariable=pn).place(x=360,y=220)

        Label(frame1,text="Gender:",font=('Arail',15),bg="lavender").place(x=200,y=248)
        r1=tk.Radiobutton(frame1,text="Male",padx=20,value=0,bg="lavender",variable=gen).place(x=360,y=252)  #value can alphanumeric
        r2=tk.Radiobutton(frame1,text='Female',padx=20,value=1,bg="lavender",variable=gen).place(x=450,y=252)
       
        
        Label(frame1,text="GST Number:",font=('Arail',15),bg="lavender").place(x=200,y=282)
        Entry(frame1,width=63,textvariable=gst).place(x=360,y=286)

        Label(frame1,text="PAN Number:",font=('Arail',15),bg="lavender").place(x=200,y=316)
        Entry(frame1,width=63,textvariable=pan).place(x=360,y=320)

        Label(frame1,text="Mobile Number:",font=('Arail',15),bg="lavender").place(x=200,y=350)
        Entry(frame1,width=63,textvariable=mob).place(x=360,y=354)

        Label(frame1,text="Email ID:",font=('Arail',15),bg="lavender").place(x=200,y=384)
        Entry(frame1,width=63,textvariable=email).place(x=360,y=390)

        Label(frame1,text="Plot no:",font=('Arail',15),bg="lavender").place(x=200,y=418)
        Entry(frame1,width=63,textvariable=plno).place(x=360,y=424)


        Label(frame1,text="Locality:",font=('Arail',15),bg="lavender").place(x=200,y=452)
        Entry(frame1,width=63,textvariable=loc).place(x=360,y=456)


        Label(frame1,text="District:",font=('Arail',15),bg="lavender").place(x=200,y=486)
        Entry(frame1,width=20,textvariable=dist).place(x=360,y=492)


        Label(frame1,text="Sub-Division:",font=('Arail',15),bg="lavender").place(x=500,y=486)
        Entry(frame1,width=20,textvariable=sdist).place(x=620,y=492)


        Label(frame1,text="State:",font=('Arail',15),bg="lavender").place(x=200,y=520)
        Entry(frame1,width=20,textvariable=st).place(x=360,y=526)

        
        Label(frame1,text="Pincode:",font=('Arail',15),bg="lavender").place(x=500,y=520)
        Entry(frame1,width=20,textvariable=pinc).place(x=620,y=526)
        

        Label(frame1,text="Remarks:",font=('Arail',15),bg="lavender").place(x=200,y=560)
        Entry(frame1,width=63,textvariable=rm).place(x=360,y=566)

        self.pho=PhotoImage(file="home.png")
        
        Button(frame1,image=self.pho,border=0,font=('Maiandra GD',20),compound=TOP,bg='lavender',command=obj.home).place(x=800,y=150)
        Button(frame1,text="Reload",bd=2,width=12,height=1,relief="ridge",bg='yellow',fg='black',font=('Poor Richard',20),command=lambda:obj.New(obj)).place(x=800,y=340)
        Button(frame1,text="Reset",bd=2,width=12,height=1,relief="ridge",bg='blue',fg='white',font=('Poor Richard',20),command=lambda:obj.rese(cid.set(''),cn.set(''),pn.set(''),gen.set(''),gst.set(''),pan.set(''),mob.set(''),email.set(''),plno.set(''),loc.set(''),dist.set(''),sdist.set(''),st.set(''),pinc.set(''),rm.set(''))).place(x=800,y=420)
        Button(frame1,text="Save",bd=2,width=12,height=1,relief="ridge",bg='Green',fg='white',font=('Poor Richard',20),command=lambda:obj.save(obj,cid.get(),cn.get(),pn.get(),gen.get(),gst.get(),pan.get(),mob.get(),email.get(),plno.get(),loc.get(),dist.get(),sdist.get(),st.get(),pinc.get(),rm.get())).place(x=800,y=500)
        
    def save(self,obj,cid,cn,pn,gen,gst,pan,mob,email,plno,loc,dist,sdist,st,pinc,rm):
        
        self.cid=cid
        self.cn=cn
        self.pn=pn
        self.gen=gen
        self.gst=gst
        self.pan=pan
        self.mob=mob
        self.email=email
        self.plno=plno
        self.loc=loc
        self.dist=dist
        self.sdist=sdist
        self.st=st
        self.pinc=pinc
        self.rm=rm
        gender=StringVar()
        if self.gen == 0:
            gender='Male'
        else:
            gender='Female'
            
        try:
            conn=pymysql.connect(host='localhost',user='root',password='',db='software')
            a=conn.cursor()
            a.execute("insert into customers(ID,Company,Name,Gender,GST,PAN,Mobile,Email,Plot,Locality,District,Division,State,Pincode,Remarks)value('"+cid+"','"+cn+"','"+pn+"','"+gender+"','"+gst+"','"+pan+"','"+mob+"','"+email+"','"+plno+"','"+loc+"','"+dist+"','"+sdist+"','"+st+"','"+pinc+"','"+rm+"')")
            conn.commit()
            messagebox.showinfo("Status","Saved")
        except:
            conn.rollback()
            messagebox.showinfo("Status","Not Saved")
            messagebox.showinfo("Help","Reload and Try again")
        conn.close()

    def update(self,obj,Update_data):
        self.Update_data=Update_data
        
    def rese(self,cid,cn,pn,gen,gst,pan,mob,email,plno,loc,dist,sdist,st,pinc,rm):
        messagebox.showinfo("Status","Reseted")

class Invoice:
    def InvoicePrint(self,InvoiceData,cid,ci,cn,gstn,pan,mob,Address,Email):
        try:
            os.mkdir("F:\\InvoiceGeneration\\Invoice\\")
        except:
            pass
        conn=pymysql.connect(host='localhost',user='root',password='',db='software')
        a=conn.cursor()
        a.execute('select CompanyName,Name,GST,PAN,Mobile,Email,Address,Locality,State from client')
        result=a.fetchall()
        conn.close()
        
        cName=StringVar
        Name=StringVar
        G=StringVar
        P=StringVar
        M=StringVar
        E=StringVar
        Add=StringVar
        Loc=StringVar()
        sts=StringVar()            
        for i in result:
            cName=i[0]
            Name=i[1]
            G=i[2]
            P=i[3]
            M=i[4]
            E=i[5]
            Add=i[6]
            Loc=i[7]
            sts=i[8]
        
        now=datetime.datetime.today()
        Number=str(now.strftime('%y'))+str(now.strftime('%d'))+str(now.microsecond)
        Canvas(width=210,height=293)
        pdf= canvas.Canvas("F:\\InvoiceGeneration\\Invoice\\"+str(Number)+".pdf",pagesize=A4)
        width,height=A4
        Todaydate=str(datetime.date.today())
        
        qr = qrcode.QRCode(version=1,box_size=1,border=1)
        data ='Seller\t'+str(cName)+'\t'+ str(M )+'\t'+str(Number)+'\nTime:'+str(Todaydate)+'\nBuyer\t'+str(cid)+'\t'+str(ci)+'\t'+str(cn)+'\t'+str(gstn)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        pdf.drawInlineImage(img,270,685)
        
        
        pdf.setTitle("Invoice")
        pdf.line(20,815,575,815)
        pdf.line(260,780,330,780)
        pdf.line(260,740,330,740)
        pdf.line(260,815,260,677)
        pdf.line(330,815,330,677)
        pdf.setFont("Courier-Bold",9)
        pdf.drawString(265,795,Number)
        pdf.drawString(265,760,Todaydate)
        pdf.drawString(265,750,str(now.strftime("%H:%M:%S")))
        pdf.setFont("Courier-Bold",10)
        pdf.drawString(263,805,"Invoice No.")
        pdf.drawString(280,770,"Date")
        pdf.setFont("Courier-Bold",15)
        pdf.drawString(265,825,"Invoice")
        pdf.drawString(30,795,cName)
        pdf.setFont("Courier-Bold",12)
        pdf.drawString(30,780,"Gst:"+G)
        pdf.drawString(30,765,"Pan:"+P)
        pdf.drawString(30,750,"Mobile:"+M)
        pdf.drawString(30,735,"Email:"+E)
        pdf.drawString(30,720,Add)
        pdf.drawString(30,690,sts)
        pdf.setFont("Courier-Bold",8)
        pdf.drawString(30,705,Loc)
        
        pdf.setFont("Courier-Bold",15)
        pdf.drawString(340,795,cn)
        pdf.setFont("Courier-Bold",12)
        pdf.drawString(340,780,"Gst:"+gstn)
        pdf.drawString(340,765,"Pan:"+pan)
        pdf.drawString(340,750,"Mobile:"+mob)
        pdf.drawString(340,735,"Email:"+Email)
        pdf.drawString(340,720,str(Address))

        
        pdf.setTitle("Invoice")
        pdf.line(20,815,575,815)
        pdf.line(260,780,330,780)
        pdf.line(260,740,330,740)
        pdf.line(260,815,260,677)
        pdf.line(330,815,330,677)
        pdf.setFont("Courier-Bold",9)
        pdf.drawString(265,795,Number)
        pdf.drawString(265,760,Todaydate)
        pdf.drawString(265,750,str(now.strftime("%H:%M:%S")))
        pdf.setFont("Courier-Bold",10)
        pdf.drawString(263,805,"Invoice No.")
        pdf.drawString(220,805,"Seller")
        pdf.drawString(540,805,"Buyer")
        pdf.drawString(280,770,"Date")
        pdf.setFont("Courier-Bold",15)
        pdf.drawString(265,825,"Invoice")
        pdf.line(20,677,575,677)
        pdf.setFont("Courier-Bold",10)
        pdf.drawString(25,665,"S.N.")
        pdf.drawString(80,665,"Product Detalis")
        pdf.drawString(230,665,"HSN/SAC")
        pdf.drawString(285,665,"Qty.")
        pdf.drawString(320,665,"Rate")
        pdf.drawString(357,665,"Tax")
        pdf.drawString(390,665,"Taxble")
        pdf.drawString(440,665,"Sgst")
        pdf.drawString(485,665,"Cgst")
        pdf.drawString(530,665,"Total")
        pdf.setFont("Courier-Bold",20)
        pdf.drawString(110,185,"Grand Total")
        
        ttaxable=IntVar()
        tsgst =IntVar()
        GrT=IntVar()
        qty=IntVar()
        ftax=IntVar()
        fgst=IntVar()
        ft=IntVar()
        twtax=IntVar()
        twgst=IntVar()
        twt=IntVar()
        etax=IntVar()
        egst=IntVar()
        et=IntVar()
        htax=IntVar()
        hgst=IntVar()
        ht=IntVar()
        qty=0
        ttaxable=0
        tsgst =0
        GrT=0
        ftax=0
        fgst=0
        ft=0
        twtax=0
        twgst=0
        twt=0
        etax=0
        egst=0
        et=0
        htax=0
        hgst=0
        ht=0
        ycoordinate=IntVar()
        ycoordinate=650
        j=IntVar
        j=1
        print(InvoiceData)
        for i in InvoiceData:
            ttaxable= ttaxable + i[5]
            tsgst = tsgst +i[6]
            GrT= GrT + i[8]
            qty= qty + i[2]
            v4=str(i[0])
            v5=str(i[3])
            v7=str(i[4])
            v8=str(i[5])
            v9=str(i[6])
            v10=str(i[6])
            v11=str(i[8])
            pdf.setFont("Courier-Bold",10)
            pdf.drawString(30,ycoordinate,str(j))
            if len(str(i[0])) > 27:
                pdf.setFont("Courier-Bold",7)
                pdf.drawString(55,ycoordinate,str(i[0]))
            else:
                pdf.drawString(55,ycoordinate,str(i[0]))
            pdf.setFont("Courier-Bold",10)
            if len(str(i[1])) > 8 :
                pdf.setFont("Courier-Bold",7)
                pdf.drawString(228,ycoordinate,str(i[1]))
            else:
                pdf.drawString(228,ycoordinate,str(i[1]))
            pdf.setFont("Courier-Bold",10)
            pdf.drawString(290,ycoordinate,str(i[2]))
            pdf.drawString(315,ycoordinate,str(i[3]))
            pdf.drawString(363,ycoordinate,str(i[4]))
            if i[4] == 5:
                ftax = ftax + i[5]
                fgst = fgst + i[6]
            elif i[4] == 12:
                twtax = twtax + i[5]
                twgst = twgst + i[6]
            elif i[4] == 18:
                etax = etax + i[5]
                egst = egst + i[6]
            elif i[4] == 28:
                htax = htax + i[5]
                hgst = hgst + i[6]
            pdf.drawString(387,ycoordinate,str(i[5]))
            pdf.drawString(440,ycoordinate,str(i[6]))
            pdf.drawString(485,ycoordinate,str(i[7]))
            pdf.drawString(530,ycoordinate,str(i[8]))
            hsc=str(i[1])
            qty=i[2]
            conn=pymysql.connect(host='localhost',user='root',password='',db='software')
            a=conn.cursor()
            a.execute("select Quantity from net where HSNorSAC='"+hsc+"'")
            result=a.fetchall()
            for i in result:
                ans =int(i[0])
            ans = ans - qty
            an=str(ans)
            a.execute("update net set Quantity ='"+an+"' where HSNorSAC='"+hsc+"'")
            conn.commit()
            a.execute("insert into invoice(ID,Invoice_Number,HSNorSAC,Goods,Rate_Per_Unit,Quantity,Applied_Tax,Taxable_Amount,Sgst,Cgst,Grand_Total)value('"+cid+"','"+Number+"','"+hsc+"','"+v4+"','"+v5+"','"+an+"','"+v7+"','"+v8+"','"+v9+"','"+v10+"','"+v11+"')")
            conn.commit()
            conn.close()
            j=j+1
            ycoordinate = ycoordinate - 25

        ft = ft + ftax + (2*fgst)
        twt = twt + twtax + (2*twgst)
        et = et + etax + (2*egst)
        ht = ht + htax + (2*hgst)
        finaltotal=StringVar()
        finaltaxable=StringVar()
        finalgst=StringVar()
        finaltaxable=str(ftax + twtax + etax + htax)
        finalgst = str(fgst + twgst + egst + hgst)
        finaltotal =str(ft + twt + et + ht)
        conn=pymysql.connect(host='localhost',user='root',password='',db='software')
        a=conn.cursor()
        a.execute("insert into product(ID,Invoice_Number,Taxable_Amount,Sgst,Cgst,Total)value('"+cid+"','"+Number+"','"+finaltaxable+"','"+finalgst+"','"+finalgst+"','"+finaltotal+"')")
        conn.commit()
        conn.close()
            
            
        pdf.setFont("Courier-Bold",10)
        pdf.drawString(290,190,str(qty))
        pdf.drawString(390,190,str(ttaxable))
        pdf.drawString(440,190,str(tsgst))
        pdf.drawString(485,190,str(tsgst))
        pdf.drawString(530,190,str(GrT))
        
        pdf.line(20,660,575,660)
        pdf.line(20,815,20,20)
        pdf.line(575,815,575,20)

        pdf.line(50,677,50,200)
        pdf.line(225,677,225,200)
        pdf.line(280,677,280,180)
        pdf.line(310,677,310,180)
        pdf.line(355,677,355,200)
        pdf.line(380,677,380,200)
        pdf.line(430,677,430,180)
        pdf.line(475,677,475,180)
        pdf.line(520,677,520,180)
        pdf.line(20,160,420,160)
        pdf.line(20,140,420,140)
        pdf.line(20,120,420,120)
        pdf.line(20,100,420,100)
        pdf.line(20,80,420,80)
        pdf.line(420,180,420,20)
        pdf.line(320,180,320,80)
        pdf.line(220,180,220,80)
        pdf.line(150,160,150,80)
        pdf.line(120,180,120,80)
        pdf.line(250,160,250,80)
        pdf.line(50,180,50,80)
        pdf.setFont("Courier-Bold",10)

        pdf.drawString(25,165,"Tax")
        pdf.drawString(25,145,"5%")
        pdf.drawString(25,125,"12%")
        pdf.drawString(25,105,"18%")
        pdf.drawString(25,85,"28%")
        pdf.drawString(60,165,"Taxable")
        pdf.drawString(60,145,str(ftax))
        pdf.drawString(60,125,str(twtax))
        pdf.drawString(60,105,str(etax))
        pdf.drawString(60,85,str(htax))
        pdf.drawString(150,165,"Cgst")
        pdf.drawString(125,145,"2.5%")
        pdf.drawString(125,125,"6%")
        pdf.drawString(125,105,"9%")
        pdf.drawString(125,85,"14%")
        pdf.drawString(165,145,str(fgst))
        pdf.drawString(165,125,str(twgst))
        pdf.drawString(165,105,str(egst))
        pdf.drawString(165,85,str(hgst))
        
        pdf.drawString(250,165,"Sgst")
        pdf.drawString(225,145,"2.5%")
        pdf.drawString(225,125,"6%")
        pdf.drawString(225,105,"9%")
        pdf.drawString(225,85,"14%")
        pdf.drawString(265,145,str(fgst))
        pdf.drawString(265,125,str(twgst))
        pdf.drawString(265,105,str(egst))
        pdf.drawString(265,85,str(hgst))
        
        pdf.drawString(355,165,"Total")
        pdf.drawString(355,145,str(ft))
        pdf.drawString(355,125,str(twt))
        pdf.drawString(355,105,str(et))
        pdf.drawString(355,85,str(ht))
        
        pdf.line(20,20,575,20)
        pdf.line(20,200,575,200)
        pdf.line(20,180,575,180)
        pdf.line(20,100,575,100)
        pdf.setFont("Courier-Bold",10)
        pdf.drawString(25,70,"Terms & Conditions:")
        pdf.drawString(25,60,"1:Battery, Charger, Mobile warranty is provided by service center.")
        pdf.drawString(25,50,"2:Every dispute will settled in Mau Court.")
        pdf.drawString(25,40,"3:Sold items will not be returned or changed.")
        pdf.drawString(25,30,"THANK YOU")
        pdf.setFont("Courier-Bold",10)
        pdf.drawString(440,80,"for ")
        pdf.drawString(440,30,"Authorised Signatory")
        pdf.drawString(440,110,"Receiver's Signature")
        pdf.save()
        webbrowser.open("F:\\InvoiceGeneration\\Invoice\\"+str(Number)+".pdf")
        
    def home(self):
        self.front=main(win)

    def show(self,obj,cobj):
        global InvoiceData
        InvoiceData = [ ]
        def AddProduct():
            def check(hsc):
                getb=IntVar()
                conn=pymysql.connect(host='localhost',user='root',password='',db='software')
                a=conn.cursor()
                a.execute('select HSNorSAC,Goods,Quantity,Rate_Per_Unit from net')
                result=a.fetchall()
                for i in result:
                    if hsc == i[0]:
                        getb=0
                        avqt.set(i[2])
                        dog.set(i[1])
                        rate.set(i[3])
                        messagebox.showinfo("Status","Available")
                        break
                    else:
                        getb=1
                if getb == 1:
                    messagebox.showinfo("Status","Currently unavailable")
                conn.close()

            def SubmitData(dog,hsc,qty,rate,apt,ta,sgst,cgst,gt):
                prod.append((dog,hsc,qty,rate,apt,ta,sgst,cgst,gt))
                for data in (prod):
                    InvoiceData.append(data)
                    self.tree.insert('', 'end', values=(data))
                prod.clear()
                    
                

            def Caltax(apt,rate,qty,avqt):
                if avqt < qty:
                    messagebox.showinfo('Status',"Insuficient Quantity")
                else:
                    Total=rate*qty
                    val=100+apt
                    t=apt/2
                    a=(Total/val*t)
                    gst=round(a,2)
                    sgst.set(gst)
                    cgst.set(gst)
                    b=Total-gst*2
                    ta.set(b)
                    gt.set(Total)
                
            wi=Toplevel()
            wi.title("Add Product")
            wi.config(bg='lavender')
            wi.resizable(0,0)
            width = 460
            height = 500
            screen_width = win.winfo_screenwidth()
            screen_height = win.winfo_screenheight()
            x = ((screen_width/2) - 455) - (width/2)
            y = ((screen_height/2) + 20) - (height/2)
            wi.geometry("%dx%d+%d+%d"%(width,height,x,y))
            hsc=StringVar()
            dog=StringVar()
            vid=StringVar()
            rate=IntVar()
            qty=IntVar()
            ta=IntVar()
            sgst=IntVar()
            cgst=IntVar()
            gt=IntVar()
            avqt=IntVar()
                    
            Label(wi,text="HSN/SAC code:",font=('Times New Roman',15),fg='midnightblue',bg="lavender").grid(row=0,column=0,padx=10,pady=10)
            Entry(wi,width=20,bd=2,textvariable=hsc).grid(row=0,column=1,padx=10,pady=10)
            Button(wi,text='Check',font=('Maiandra GD',10),fg='yellow',bg='purple',command=lambda:check(hsc.get())).grid(row=0,column=2,padx=10,pady=10)
        
            Label(wi,text="Product Descrption:",font=('Times New Roman',15),fg='midnightblue',bg="lavender").grid(row=1,column=0,padx=10,pady=10)
            Entry(wi,width=20,bd=2,textvariable=dog).grid(row=1,column=1,padx=10,pady=10)
            Label(wi,text="Rate Per Unit:",font=('Times New Roman',15),fg='midnightblue',bg="lavender").grid(row=2,column=0,padx=10,pady=10)
            Entry(wi,width=20,bd=2,textvariable=rate).grid(row=2,column=1,padx=10,pady=10)
            Label(wi,text="Quantity:",font=('Times New Roman',15),fg='midnightblue',bg="lavender").grid(row=3,column=0,padx=10,pady=10)
            Entry(wi,width=20,bd=2,textvariable=qty).grid(row=3,column=1,padx=10,pady=10)
        
            Label(wi,text="Available Quantity",font=('Times New Roman',10),fg='midnightblue',bg="lavender").grid(row=2,column=2,padx=10,pady=10)
            Entry(wi,width=10,bd=2,textvariable=avqt).grid(row=3,column=2,padx=10,pady=10)
            Label(wi,text="Applied Tax:",font=('Times New Roman',15),fg='midnightblue',bg="lavender").grid(row=4,column=0,padx=10,pady=10)
            P = ["-Percentage-","5","12","18","28"]
            apt=IntVar()
            apt.set(P[0])
            OptionMenu(wi,apt,*P).grid(row=4,column=1,padx=10,pady=10)
            Label(wi,text="Taxable Amount:",font=('Times New Roman',15),fg='midnightblue',bg="lavender").grid(row=5,column=0,padx=10,pady=10)
            Entry(wi,width=20,bd=2,textvariable=ta).grid(row=5,column=1,padx=10,pady=10)
            Label(wi,text="Sgst:",font=('Times New Roman',15),fg='midnightblue',bg="lavender").grid(row=6,column=0,padx=10,pady=10)
            Entry(wi,width=20,bd=2,textvariable=sgst).grid(row=6,column=1,padx=10,pady=10)
            Label(wi,text="Cgst:",font=('Times New Roman',15),fg='midnightblue',bg="lavender").grid(row=7,column=0,padx=10,pady=10)
            Entry(wi,width=20,bd=2,textvariable=cgst).grid(row=7,column=1,padx=10,pady=10)
            Label(wi,text="Total:",font=('Times New Roman',15),fg='midnightblue',bg="lavender").grid(row=8,column=0,padx=10,pady=10)
            Entry(wi,width=20,bd=2,textvariable=gt).grid(row=8,column=1,padx=10,pady=10)

            Button(wi,text='Add to Cart',font=('Maiandra GD',15),fg='midnightblue',bg='lawngreen',bd=2,command=lambda:SubmitData(dog.get(),hsc.get(),qty.get(),rate.get(),apt.get(),ta.get(),sgst.get(),cgst.get(),gt.get())).grid(row=9,column=1,padx=10,pady=10)
            Button(wi,text='Calculate',font=('Maiandra GD',10),fg='white',bg='gray25',command=lambda:Caltax(apt.get(),rate.get(),qty.get(),avqt.get())).grid(row=6,column=2,padx=10,pady=10)
            
            
        prod = []
        def DeleteData():
            if not self.tree.selection():
                result = tkMessageBox.showwarning('Alert', 'Please Select Item First!', icon="warning")
            else:
                result = tkMessageBox.askquestion('Alert', 'Are you sure you want to delete this item?', icon="warning")
                if result == 'yes':
                    curItem = self.tree.focus()
                    contents =(self.tree.item(curItem))
                    selecteditem = contents['values']
                    self.tree.delete(curItem)
                    
                    for item in range(len(prod)):
                        if((prod[item])[0] == selecteditem[0]):
                            break
                        del(prod[item])
                        
        def Verify(cid):
            getb=IntVar()
            conn=pymysql.connect(host='localhost',user='root',password='',db='software')
            a=conn.cursor()
            a.execute('select * from 	customers')
            result=a.fetchall()
            
            for i in result:
                if cid == i[0]:
                    getb=0
                    cn.set(i[1])
                    ci.set(i[2])
                    gstn.set(i[4])
                    pan.set(i[5])
                    mob.set(i[6])
                    Email.set(i[7])
                    Address.set(str(i[8])+str(' ')+str(i[9])+str(' ')+str(i[10])+str(' ')+str(i[11])+str(' ')+str(i[12])+str(' ')+str(i[13]))
                    messagebox.showinfo("Status","Already Customer")
                    break
                else:
                    getb=1
            if getb == 1:
                messagebox.showinfo("Status","Register as New Customer")
            conn.close()
        

        iframe1= Frame(win,width=1000,height=600,bg="lavender").place(x=0,y=0)
        cid=StringVar()
        ci=StringVar()
        cn=StringVar()
        gstn=StringVar()
        pan=StringVar()
        mob=StringVar()
        Address=StringVar()
        Email=StringVar()
        Label(iframe1,text="Customer Id:",font=('Arail',10),bg="lavender").place(x=30,y=10)
        Entry(iframe1,width=30,textvariable=cid).place(x=150,y=14)

        Label(iframe1,text="Customer Name:",font=('Arail',10),bg="lavender").place(x=30,y=40)
        Entry(iframe1,width=30,textvariable=ci).place(x=150,y=44)

        Label(iframe1,text="Company Name:",font=('Arail',10),bg="lavender").place(x=400,y=50)
        Entry(iframe1,width=30,textvariable=cn).place(x=500,y=54)

        Label(iframe1,text="GST Number:",font=('Arail',10),bg="lavender").place(x=30,y=70)
        Entry(iframe1,width=30,textvariable=gstn).place(x=150,y=74)

        Label(iframe1,text="PAN Number:",font=('Arail',10),bg="lavender").place(x=30,y=100)
        Entry(iframe1,width=30,textvariable=pan).place(x=150,y=104)

        Label(iframe1,text="Mobile Number:",font=('Arail',10),bg="lavender").place(x=30,y=130)
        Entry(iframe1,width=30,textvariable=mob).place(x=150,y=134)

        Label(iframe1,text="Email:",font=('Arail',10),bg="lavender").place(x=400,y=80)
        Entry(iframe1,width=40,textvariable=Email).place(x=460,y=84)
        
        Label(iframe1,text="Address:",font=('Arail',10),bg="lavender").place(x=400,y=130)
        Entry(iframe1,width=40,textvariable=Address).place(x=460,y=134)
        

        Button(iframe1,text="Verify",bd=2,width=10,height=1,relief="ridge",bg='Yellow',fg='black',font=('Poor Richard',10),command=lambda:Verify(cid.get())).place(x=350,y=10)
        Button(iframe1,text="Save",bd=2,width=10,height=1,relief="ridge",bg='peach puff',fg='black',font=('Poor Richard',18),command=lambda:iobj.InvoicePrint(InvoiceData,cid.get(),ci.get(),cn.get(),gstn.get(),pan.get(),mob.get(),Address.get(),Email.get())).place(x=830,y=120)
        Button(iframe1,text="Add Item",bd=2,width=10,height=1,relief="ridge",bg='green2',fg='black',font=('Poor Richard',18),command=AddProduct).place(x=830,y=200)
        Button(iframe1,text="Remove Item",bd=2,width=10,height=1,relief="ridge",bg='tomato',fg='black',font=('Poor Richard',18),command=DeleteData).place(x=830,y=280)
        Button(iframe1,text="New Customer",bd=2,width=10,height=1,relief="ridge",bg='gold',fg='black',font=('Poor Richard',18),command=lambda:cobj.New(cobj)).place(x=830,y=360)
        self.pho=PhotoImage(file="home.png")
        Button(iframe1,image=self.pho,border=0,compound=TOP,bg='lavender',command=obj.home).place(x=830,y=420)

        self.scrollbary = Scrollbar(iframe1, orient=VERTICAL)

        self.tree = ttk.Treeview(iframe1,columns=(1,2,3,4,5,6,7,8,9),show='headings',height=19, selectmode="extended", yscrollcommand=self.scrollbary.set)

        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill='y')
        
        self.tree.heading(1, text="Product")
        self.tree.heading(2, text="HSN/SAC")
        self.tree.heading(3, text="Quantity")
        self.tree.heading(4, text="Rate")
        self.tree.heading(5,text="Tax")
        self.tree.heading(6, text="Taxable_Amount")
        self.tree.heading(7, text="Sgst")
        self.tree.heading(8, text="cgst")
        self.tree.heading(9, text="Total")

        self.tree.column(1, stretch=NO,width=210)
        self.tree.column(2, stretch=NO,width=80)
        self.tree.column(3, stretch=NO,width=75)
        self.tree.column(4, stretch=NO,width=60)
        self.tree.column(5, stretch=NO,width=40)
        self.tree.column(6, stretch=NO,width=126)
        self.tree.column(7, stretch=NO,width=56)
        self.tree.column(8, stretch=NO,width=56)
        self.tree.column(9, stretch=NO,width=86)
        self.tree.place(x=10,y=170)

        
       
class SalesRecord:
    def home(self,isobj):
        self.front=main(win)

    def Sales_Record(self,Userd):
        try:
            os.mkdir("F:\\InvoiceGeneration\\Sales_Record\\")
        except:
            pass
        conn=pymysql.connect(host='localhost',user='root',password='',db='software')
        a=conn.cursor()
        a.execute('select CompanyName,Name,GST,PAN,Mobile,Email,Address,Locality,State from client')
        result=a.fetchall()
        conn.close()
        cName=StringVar
        Name=StringVar
        G=StringVar
        P=StringVar
        M=StringVar
        E=StringVar
        Add=StringVar
        Loc=StringVar()
        sts=StringVar()            
        for i in result:
            cName=i[0]
            Name=i[1]
            G=i[2]
            P=i[3]
            M=i[4]
            E=i[5]
            Add=i[6]
            Loc=i[7]
            sts=i[8]
        
        now=datetime.datetime.today()
        Number='Sales'+str(now.strftime('%y'))+str(now.strftime('%d'))+str(now.microsecond)
        Canvas(width=210,height=293)
        pdf= canvas.Canvas("F:\\InvoiceGeneration\\Sales_Record\\"+str(Number)+".pdf",pagesize=A4)
        width,height=A4
        
        pdf.setTitle("Sales Report")
        pdf.line(20,815,560,815)
        pdf.setFont("Courier-Bold",15)
        pdf.drawString(220,825,"Sales Record")
        pdf.setFont("Courier-Bold",25)
        pdf.drawString(150,795,cName)
        pdf.setFont("Courier-Bold",10)
        pdf.drawString(245,780,Name)
        pdf.drawString(245,765,"Gst:"+G)
        pdf.drawString(245,750,"Pan:"+P)
        pdf.drawString(150,735,"Mobile:"+M+"  Email:"+E)
        pdf.drawString(250,720,Add)
        pdf.drawString(150,705,Loc)
        pdf.drawString(250,690,sts)
        
        pdf.setFont("Courier-Bold",8)
        pdf.drawString(20,668,"Customer")
        pdf.drawString(30,655,"Id")
        pdf.drawString(68,668,"Invoice")
        pdf.drawString(70,655,"Number")
        pdf.drawString(115,660,"HSN/SAC")
        pdf.drawString(160,660,"Product Detalis")
        pdf.drawString(320,660,"Rate")
        pdf.drawString(355,660,"Qty.")
        pdf.drawString(380,660,"Tax")
        pdf.drawString(405,660,"Taxble")
        pdf.drawString(445,668,"Sgst/")
        pdf.drawString(445,655,"Cgst")
        pdf.drawString(490,660,"Total")
        pdf.drawString(540,660,"Date")
        
        
        ttaxable=IntVar()
        tsgst =IntVar()
        GrT=IntVar()
        ttaxable=0
        tsgst =0
        GrT=0
        extaxable=IntVar()
        extaxable=0
        qty=IntVar()
        ftax=IntVar()
        fgst=IntVar()
        ft=IntVar()
        
        twtax=IntVar()
        twgst=IntVar()
        twt=IntVar()
        
        etax=IntVar()
        egst=IntVar()
        et=IntVar()
        
        htax=IntVar()
        hgst=IntVar()
        ht=IntVar()

        qty=0
        ftax=0
        fgst=0
        ft=0
        twtax=0
        twgst=0
        twt=0
        etax=0
        egst=0
        et=0
        htax=0
        hgst=0
        ht=0
        ycoordinate=IntVar()
        ycoordinate=640
        
        for i in Userd:
            ttaxable= ttaxable + i[7]
            tsgst = tsgst +i[8]
            GrT= GrT + i[10]
            pdf.setFont("Courier-Bold",7)
            qty = qty + i[5]
            pdf.drawString(18,ycoordinate,str(i[0]))
            pdf.drawString(65,ycoordinate,str(i[1]))
            pdf.drawString(115,ycoordinate,str(i[2]))
            pdf.drawString(160,ycoordinate,str(i[3]))
            pdf.drawString(320,ycoordinate,str(i[4]))
            pdf.drawString(355,ycoordinate,str(i[5]))
            pdf.drawString(380,ycoordinate,str(i[6]))
            if i[6] == 0:
                extaxable = extaxable + i[6]
            elif i[6] == 5:
                ftax = ftax + i[7]
                fgst = fgst + i[8]

            elif i[6] == 12:
                twtax = twtax + i[7]
                twgst = twgst + i[8]

            elif i[6] == 18:
                etax = etax + i[7]
                egst = egst + i[8]

            elif i[6] == 28:
                htax = htax + i[7]
                hgst = hgst + i[8]
                
            pdf.drawString(406,ycoordinate,str(i[7]))
            pdf.drawString(448,ycoordinate,"2*"+str(i[9]))
            pdf.drawString(490,ycoordinate,str(i[10]))
            pdf.drawString(533,ycoordinate,str(i[11]))
            ycoordinate = ycoordinate - 25

        Userd.clear()
        pdf.setFont("Courier-Bold",20)
        pdf.drawString(125,185,"Grand Total")
        pdf.setFont("Courier-Bold",10)
    
        pdf.drawString(307,185,str(GrT))
        pdf.drawString(355,185,str(qty))
        pdf.drawString(406,185,str(ttaxable))
        pdf.drawString(448,185,"2*"+str(tsgst))
        pdf.drawString(489,185,str(GrT))
    
        
        

        #Outer border
          #Horizontal
        pdf.line(15,815,580,815)
        pdf.line(15,815,15,15)
           #Vertical
        pdf.line(15,15,580,15)
        pdf.line(580,815,580,15)
        #column Vertical lines
        pdf.line(15,650,580,650)
        pdf.line(15,680,580,680)
        
       
        pdf.line(15,200,580,200)
        pdf.line(15,180,580,180)
        pdf.line(15,150,580,150)
     
        #Internal Horizontal Lines
        pdf.line(62,680,62,200)
        pdf.line(110,680,110,200)
        pdf.line(155,680,155,200)
        pdf.line(305,680,305,180)
        pdf.line(350,680,350,180)
        pdf.line(375,680,375,180)
        pdf.line(400,680,400,180)
        pdf.line(440,680,440,180)
        pdf.line(480,680,480,180)
        pdf.line(530,680,530,180)

        
        pdf.line(15,115,400,115)
        pdf.line(15,95,400,95)
        pdf.line(15,75,400,75)
        pdf.line(15,55,400,55)
        pdf.line(15,35,400,35)

        #Tax Horizontal Lines
        pdf.line(400,150,400,15)
        pdf.line(320,150,320,15)
        pdf.line(250,115,250,15)
        pdf.line(220,150,220,15)
        pdf.line(150,115,150,15)
        pdf.line(120,150,120,15)
        pdf.line(50,150,50,15)
        
        pdf.setFont("Courier-Bold",12)

        pdf.drawString(355,130,"Total")
        pdf.drawString(20,130,"Tax")
        pdf.drawString(60,130,"Taxable")
        pdf.drawString(20,100,"0%")
        pdf.drawString(20,80,"5%")
        pdf.drawString(20,60,"12%")
        pdf.drawString(20,40,"18%")
        pdf.drawString(20,20,"28%")

        pdf.drawString(55,100,str(extaxable))
        pdf.drawString(55,80,str(ftax))
        pdf.drawString(55,60,str(twtax))
        pdf.drawString(55,40,str(etax))
        pdf.drawString(55,20,str(htax))
        
        pdf.drawString(150,130,"Cgst")
        
        pdf.drawString(125,60,"6%")
        pdf.drawString(125,40,"9%")
        pdf.drawString(125,20,"14%")
    
        pdf.drawString(155,80,str(fgst))
        pdf.drawString(155,60,str(twgst))
        pdf.drawString(155,40,str(egst))
        pdf.drawString(155,20,str(hgst))
    
        pdf.drawString(250,130,"Sgst")
        
        pdf.drawString(225,60,"6%")
        pdf.drawString(225,40,"9%")
        pdf.drawString(225,20,"14%")
    
        pdf.drawString(255,80,str(fgst))
        pdf.drawString(255,60,str(twgst))
        pdf.drawString(255,40,str(egst))
        pdf.drawString(255,20,str(hgst))

        ft = ft + ftax + (2*fgst)
        twt = twt + twtax + (2*twgst)
        et = et + etax + (2*egst)
        ht = ht + htax + (2*hgst)

        pdf.drawString(330,100,str(extaxable))
        pdf.drawString(330,80,str(ft))
        pdf.drawString(330,60,str(twt))
        pdf.drawString(330,40,str(et))
        pdf.drawString(330,20,str(ht))
        
        pdf.drawString(420,120,"For "+cName)
        pdf.drawString(420,30,"Authorised Signatory")
        
        pdf.setFont("Courier-Bold",10)
        pdf.drawString(225,80,"2.5%")
        pdf.drawString(125,80,"2.5%")
        Userd.clear()    
        pdf.save()
        webbrowser.open("F:\\InvoiceGeneration\\Sales_Record\\"+str(Number)+".pdf")
        
    def show(self,isobj):
        global flag
        self.flag=IntVar()

        flag=2
        
        pframe3=Frame(win,width=1000,height=600,bg="lavender").place(x=0,y=0)
        
        self.scrollbary = Scrollbar(pframe3, orient=VERTICAL)

        self.tree = ttk.Treeview(pframe3,columns=(1,2,3,4,5,6,7,8,9,10,11,12),show='headings',height=18, selectmode="extended", yscrollcommand=self.scrollbary.set)

        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill='y')

        self.tree.heading(1, text="Customer ID")
        self.tree.heading(2, text="Invoice No.")
        self.tree.heading(3, text="HSN/SAC")
        self.tree.heading(4, text="Product")
        self.tree.heading(5,text="Rate")
        self.tree.heading(6,text="Quantity")
        self.tree.heading(7, text="Tax")
        self.tree.heading(8, text="Taxable")
        self.tree.heading(9, text="Sgst")
        self.tree.heading(10, text="cgst")
        self.tree.heading(11, text="Total")
        self.tree.heading(12, text="Date")
        

        self.tree.column(1, stretch=NO,width=85)
        self.tree.column(2, stretch=NO,width=80)
        self.tree.column(3, stretch=NO,width=80)
        self.tree.column(4, stretch=NO,width=200)
        self.tree.column(5, stretch=NO,width=70)
        self.tree.column(6, stretch=NO,width=65)
        self.tree.column(7, stretch=NO,width=30)
        self.tree.column(8, stretch=NO,width=70)
        self.tree.column(9, stretch=NO,width=70)
        self.tree.column(10, stretch=NO,width=70)
        self.tree.column(11, stretch=NO,width=70)
        self.tree.column(12, stretch=NO,width=80)
        
        self.tree.place(x=5,y=5)

        conn=pymysql.connect(host='localhost',user='root',password='',db='software')
        a=conn.cursor()
        a.execute('select * from invoice')
        result=a.fetchall()
        conn.close()
        Userd = []
        for i in result:
            Userd.append(i)
            self.tree.insert('','end',value=i)

        def showtax(apt,flag):
            if self.flag == 0:
                now=datetime.datetime.today()
                ci=now.strftime('%y')
                conn=pymysql.connect(host='localhost',user='root',password='',db='software')
                a=conn.cursor()
                a.execute('select Time,Applied_Tax,Taxable_Amount,Sgst,Cgst,Grand_Total from invoice')
                result=a.fetchall()
                ttt=int
                Sgst=int
                cgst=int
                tg=int
                ttt=0
                Sgst=0
                cgst=0
                tg=0
                ffff=IntVar()
                fff=IntVar()
                for i in result:
                    cm=i[0].strftime('%y')
                    if cm == ci:
                        if apt == i[1]:
                            ffff=1
                            fff=1
                            ttt= ttt + i[2]
                            Sgst= Sgst + i[3]
                            cgst= cgst + i[4]
                        else:
                            ffff=0
                    else:
                        messagebox.showinfo("Status",'No Record Found')
                        break
                if not((ffff == 1 )or(fff == 1)):
                    messagebox.showinfo("Status",'No Record Found for Selected Tax Range')
                tg=ttt+Sgst+cgst   
                tt.set(ttt)
                tsgst.set(Sgst)
                tcgst.set(cgst)
                tgt.set(tg)

            elif self.flag == 1:
                now=datetime.datetime.today()
                ci=now.strftime('%d')
                conn=pymysql.connect(host='localhost',user='root',password='',db='software')
                a=conn.cursor()
                a.execute('select Time,Applied_Tax,Taxable_Amount,Sgst,Cgst,Grand_Total from invoice')
                result=a.fetchall()
                ttt=int
                Sgst=int
                cgst=int
                tg=int
                ttt=0
                Sgst=0
                cgst=0
                tg=0
                ffff=IntVar()
                fff=IntVar()
                for i in result:
                    cm=i[0].strftime('%d')
                    if cm == ci:
                        if apt == i[1]:
                            ffff=1
                            fff=1
                            ttt= ttt + i[2]
                            Sgst= Sgst + i[3]
                            cgst= cgst + i[4]
                        else:
                            ffff=0
                    else:
                        messagebox.showinfo("Status",'No Record Found')
                        break
                if not((ffff == 1 )or(fff == 1)):
                    messagebox.showinfo("Status",'No Record Found for Selected Tax Range')
                tg=ttt+Sgst+cgst    
                tt.set(ttt)
                tsgst.set(Sgst)
                tcgst.set(cgst)
                tgt.set(tg)
    
            elif self.flag == 2:
                now=datetime.datetime.today()
                ci=now.strftime('%m')
                conn=pymysql.connect(host='localhost',user='root',password='',db='software')
                a=conn.cursor()
                a.execute('select Time,Applied_Tax,Taxable_Amount,Sgst,Cgst,Grand_Total from invoice')
                result=a.fetchall()
                ttt=int
                Sgst=int
                cgst=int
                tg=int
                ttt=0
                Sgst=0
                cgst=0
                tg=0
                ffff=IntVar()
                fff=IntVar()
                for i in result:
                    cm=i[0].strftime('%m')
                    if cm == ci:
                        if apt == i[1]:
                            ffff=1
                            fff=1
                            ttt= ttt + i[2]
                            Sgst= Sgst + i[3]
                            cgst= cgst + i[4]
                        else:
                            ffff=0
                    else:
                        messagebox.showinfo("Status",'No Record Found')
                        break
                if not((ffff == 1 )or(fff == 1)):
                    messagebox.showinfo("Status",'No Record Found for Selected Tax Range')

                tg=ttt+Sgst+cgst
                tt.set(ttt)
                tsgst.set(Sgst)
                tcgst.set(cgst)
                tgt.set(tg)
        
                
        def RToday():
            self.flag=1
            self.tree.destroy()
            self.tree = ttk.Treeview(pframe3,columns=(1,2,3,4,5,6,7,8,9,10,11,12),show='headings',height=18, selectmode="extended", yscrollcommand=self.scrollbary.set)
            self.tree.heading(1, text="Customer ID")
            self.tree.heading(2, text="Invoice No.")
            self.tree.heading(3, text="HSN/SAC")
            self.tree.heading(4, text="Product")
            self.tree.heading(5,text="Rate")
            self.tree.heading(6,text="Quantity")
            self.tree.heading(7, text="Tax")
            self.tree.heading(8, text="Taxable")
            self.tree.heading(9, text="Sgst")
            self.tree.heading(10, text="cgst")
            self.tree.heading(11, text="Total")
            self.tree.heading(12, text="Date")

            self.tree.column(1, stretch=NO,width=85)
            self.tree.column(2, stretch=NO,width=80)
            self.tree.column(3, stretch=NO,width=80)
            self.tree.column(4, stretch=NO,width=200)
            self.tree.column(5, stretch=NO,width=70)
            self.tree.column(6, stretch=NO,width=65)
            self.tree.column(7, stretch=NO,width=30)
            self.tree.column(8, stretch=NO,width=70)
            self.tree.column(9, stretch=NO,width=70)
            self.tree.column(10, stretch=NO,width=70)
            self.tree.column(11, stretch=NO,width=70)
            self.tree.column(12, stretch=NO,width=80)
            self.tree.place(x=5,y=5)
            now=datetime.datetime.today()
            ci=now.strftime('%d')
            conn=pymysql.connect(host='localhost',user='root',password='',db='software')
            a=conn.cursor()
            a.execute('select * from invoice')
            result=a.fetchall()
           
            
            for i in result:
                cm=i[11].strftime('%d')
                if cm == ci:
                    Userd.append(i)
                    self.tree.insert('','end',values=i)
                else:
                    messagebox.showinfo("Status",'No Record Found')
                    break
                        
            
             
        def RMonth():
            self.flag=2
            self.tree.destroy()
            self.tree = ttk.Treeview(pframe3,columns=(1,2,3,4,5,6,7,8,9,10,11,12),show='headings',height=18, selectmode="extended", yscrollcommand=self.scrollbary.set)
            self.tree.heading(1, text="Customer ID")
            self.tree.heading(2, text="Invoice No.")
            self.tree.heading(3, text="HSN/SAC")
            self.tree.heading(4, text="Product")
            self.tree.heading(5,text="Rate")
            self.tree.heading(6,text="Quantity")
            self.tree.heading(7, text="Tax")
            self.tree.heading(8, text="Taxable")
            self.tree.heading(9, text="Sgst")
            self.tree.heading(10, text="cgst")
            self.tree.heading(11, text="Total")
            self.tree.heading(12, text="Date")

            self.tree.column(1, stretch=NO,width=85)
            self.tree.column(2, stretch=NO,width=80)
            self.tree.column(3, stretch=NO,width=80)
            self.tree.column(4, stretch=NO,width=200)
            self.tree.column(5, stretch=NO,width=70)
            self.tree.column(6, stretch=NO,width=65)
            self.tree.column(7, stretch=NO,width=30)
            self.tree.column(8, stretch=NO,width=70)
            self.tree.column(9, stretch=NO,width=70)
            self.tree.column(10, stretch=NO,width=70)
            self.tree.column(11, stretch=NO,width=70)
            self.tree.column(12, stretch=NO,width=80)
            self.tree.place(x=5,y=5)
            
            now=datetime.datetime.today()
            ci=now.strftime('%m')
            conn=pymysql.connect(host='localhost',user='root',password='',db='software')
            a=conn.cursor()
            a.execute('select * from invoice')
            result=a.fetchall()
            
            for i in result:
                cm=i[11].strftime('%m')
                if cm == ci:
                    Userd.append(i)
                    self.tree.insert('','end',values=i)
                else:
                    messagebox.showinfo("Status",'No Record Found')
                    break
            
        def RYear():
            self.flag=0
            self.tree.destroy()
            self.tree = ttk.Treeview(pframe3,columns=(1,2,3,4,5,6,7,8,9,10,11,12),show='headings',height=18, selectmode="extended", yscrollcommand=self.scrollbary.set)
            self.tree.heading(1, text="Customer ID")
            self.tree.heading(2, text="Invoice No.")
            self.tree.heading(3, text="HSN/SAC")
            self.tree.heading(4, text="Product")
            self.tree.heading(5,text="Rate")
            self.tree.heading(6,text="Quantity")
            self.tree.heading(7, text="Tax")
            self.tree.heading(8, text="Taxable")
            self.tree.heading(9, text="Sgst")
            self.tree.heading(10, text="cgst")
            self.tree.heading(11, text="Total")
            self.tree.heading(12, text="Date")

            self.tree.column(1, stretch=NO,width=85)
            self.tree.column(2, stretch=NO,width=80)
            self.tree.column(3, stretch=NO,width=80)
            self.tree.column(4, stretch=NO,width=200)
            self.tree.column(5, stretch=NO,width=70)
            self.tree.column(6, stretch=NO,width=65)
            self.tree.column(7, stretch=NO,width=30)
            self.tree.column(8, stretch=NO,width=70)
            self.tree.column(9, stretch=NO,width=70)
            self.tree.column(10, stretch=NO,width=70)
            self.tree.column(11, stretch=NO,width=70)
            self.tree.column(12, stretch=NO,width=80)
            self.tree.place(x=5,y=5)
            
            now=datetime.datetime.today()
            ci=now.strftime('%y')
            conn=pymysql.connect(host='localhost',user='root',password='',db='software')
            a=conn.cursor()
            a.execute('select * from invoice')
            result=a.fetchall()
            now=datetime.datetime.today()
            ci=now.strftime('%y')
            
            for i in result:
                cm=i[11].strftime('%y')
                if cm == ci:
                    Userd.append(i)
                    self.tree.insert('','end',values=i)
                else:
                    messagebox.showinfo("Status",'No Record Found')
                    break
           
        
        tt=IntVar()
        tsgst=IntVar()
        tcgst=IntVar()
        tgt=IntVar()
    
        Label(pframe3,text="Total Taxable",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=330,y=470)
        Entry(pframe3,width=20,bd=2,textvariable=tt).place(x=325,y=496)

        Label(pframe3,text="+",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=465,y=490)
        Label(pframe3,text="+",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=640,y=490)
        Label(pframe3,text="=",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=820,y=490)

        Label(pframe3,text="Total Sgst",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=510,y=470)
        Entry(pframe3,width=20,bd=2,textvariable=tsgst).place(x=500,y=496)

        Label(pframe3,text="Total Cgst",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=690,y=470)
        Entry(pframe3,width=20,bd=2,textvariable=tcgst).place(x=680,y=496)

        Label(pframe3,text="Total",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=870,y=470)
        Entry(pframe3,width=20,bd=2,textvariable=tgt).place(x=850,y=496)

        Label(pframe3,text="Applied Tax",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=10,y=470)

        P = ["-Percentage-","5","12","18","28"]
        apt=IntVar()
        apt.set(P[0])  
        OptionMenu(pframe3,apt,*P).place(x=190,y=490)

        

        self.pho=PhotoImage(file="home.png")
        Button(pframe3,image=self.pho,border=0,compound=TOP,bg='lavender',command=lambda:isobj.home(isobj)).place(x=20,y=420)
        Button(pframe3,text='Show',bd=2,width=10,height=1,relief="ridge",bg='Yellow',fg='Black',font=('Poor Richard',15),command=lambda:showtax(apt.get(),self.flag)).place(x=450,y=540)
        Button(pframe3,text="Today's",bd=2,width=10,height=1,relief="ridge",bg='blue',fg='white',font=('Poor Richard',15),command=RToday).place(x=250,y=400)
        Button(pframe3,text='Monthly',bd=2,width=10,height=1,relief="ridge",bg='Green',fg='white',font=('Poor Richard',15),command=RMonth).place(x=450,y=400)
        Button(pframe3,text='Yearly',bd=2,width=10,height=1,relief="ridge",bg='gray15',fg='white',font=('Poor Richard',15),command=RYear).place(x=650,y=400)
        Button(pframe3,text='Print',bd=2,width=10,height=1,relief="ridge",bg='gray',fg='white',font=('Poor Richard',15),command=lambda:isobj.Sales_Record(Userd)).place(x=850,y=400)        
    
    
class Purchase:
    def Purchase_Record(self,Userd):
        try:
            os.mkdir("F:\\InvoiceGeneration\\Purchase_Record\\")
        except:
            pass
        conn=pymysql.connect(host='localhost',user='root',password='',db='software')
        a=conn.cursor()
        a.execute('select CompanyName,Name,GST,PAN,Mobile,Email,Address,Locality,State from client')
        result=a.fetchall()
        cName=StringVar
        Name=StringVar
        G=StringVar
        P=StringVar
        M=StringVar
        E=StringVar
        Add=StringVar
        Loc=StringVar()
        sts=StringVar()            
        for i in result:
            cName=i[0]
            Name=i[1]
            G=i[2]
            P=i[3]
            M=i[4]
            E=i[5]
            Add=i[6]
            Loc=i[7]
            sts=i[8]
        
        now=datetime.datetime.today()
        Number='Purchase'+str(now.strftime('%y'))+str(now.strftime('%d'))+str(now.microsecond)
        Canvas(width=210,height=293)
        pdf= canvas.Canvas("F:\\InvoiceGeneration\\Purchase_Record\\"+str(Number)+".pdf",pagesize=A4)
        width,height=A4
        
        pdf.setTitle("Purchase Report")
        
        pdf.setFont("Courier-Bold",15)
        pdf.drawString(220,825,"Purchase Record")
        pdf.setFont("Courier-Bold",25)
        pdf.drawString(150,795,cName)
        pdf.setFont("Courier-Bold",10)
        pdf.drawString(245,780,Name)
        pdf.drawString(245,765,"Gst:"+G)
        pdf.drawString(245,750,"Pan:"+P)
        pdf.drawString(150,735,"Mobile:"+M+"  Email:"+E)
        pdf.drawString(250,720,Add)
        pdf.drawString(150,705,Loc)
        pdf.drawString(250,690,sts)
        
        ttaxable=IntVar()
        tsgst =IntVar()
        GrT=IntVar()
        ttaxable=0
        tsgst =0
        GrT=0
        extaxable=IntVar()
        extaxable=0
        qty=IntVar()
        ftax=IntVar()
        fgst=IntVar()
        ft=IntVar()
        
        twtax=IntVar()
        twgst=IntVar()
        twt=IntVar()
        
        etax=IntVar()
        egst=IntVar()
        et=IntVar()
        
        htax=IntVar()
        hgst=IntVar()
        ht=IntVar()

        qty=0
        ftax=0
        fgst=0
        ft=0
        twtax=0
        twgst=0
        twt=0
        etax=0
        egst=0
        et=0
        htax=0
        hgst=0
        ht=0
        ycoordinate=IntVar()
        ycoordinate=650
        
        for i in Userd:
            ttaxable= ttaxable + i[6]
            tsgst = tsgst +i[7]
            GrT= GrT + i[9]
            pdf.setFont("Courier-Bold",7)
            qty = qty + i[4]
            pdf.drawString(20,ycoordinate,str(i[0]))
            pdf.drawString(75,ycoordinate,str(i[1]))
            pdf.drawString(125,ycoordinate,str(i[2]))
            pdf.drawString(270,ycoordinate,str(i[3]))
            pdf.drawString(305,ycoordinate,str(i[4]))
            pdf.drawString(335,ycoordinate,str(i[5]))
            if i[5] == 0:
                extaxable = extaxable + i[6]
            elif i[5] == 5:
                ftax = ftax + i[6]
                fgst = fgst + i[7]

            elif i[5] == 12:
                twtax = twtax + i[6]
                twgst = twgst + i[7]

            elif i[5] == 18:
                etax = etax + i[6]
                egst = egst + i[7]

            elif i[5] == 28:
                htax = htax + i[6]
                hgst = hgst + i[7]
                
            pdf.drawString(360,ycoordinate,str(i[6]))
            pdf.drawString(410,ycoordinate,str(i[7]))
            pdf.drawString(450,ycoordinate,str(i[8]))
            pdf.drawString(490,ycoordinate,str(i[9]))
            pdf.drawString(533,ycoordinate,str(i[10]))
            ycoordinate = ycoordinate - 25

        Userd.clear()
        pdf.setFont("Courier-Bold",20)
        pdf.drawString(125,185,"Grand Total")
        pdf.setFont("Courier-Bold",10)
        pdf.drawString(300,185,str(qty))
        pdf.drawString(354,185,str(ttaxable))
        pdf.drawString(404,185,str(tsgst))
        pdf.drawString(444,185,str(tsgst))
        pdf.drawString(489,185,str(GrT))
       
        pdf.drawString(40,668,"Id")
        pdf.drawString(80,668,"HSN")
        pdf.drawString(135,668,"Product Detalis")
        pdf.drawString(270,668,"Rate")
        pdf.drawString(300,668,"Qty.")
        pdf.drawString(330,668,"Tax")
        pdf.drawString(355,668,"Taxble")
        pdf.drawString(405,668,"Sgst")
        pdf.drawString(445,668,"Cgst")
        pdf.drawString(485,668,"Total")
        pdf.drawString(535,668,"Date")
        

        #Outer border
          #Horizontal
        pdf.line(15,815,580,815)
        pdf.line(15,815,15,15)
           #Vertical
        pdf.line(15,15,580,15)
        pdf.line(580,815,580,15)
        #column Vertical lines
        pdf.line(15,660,580,660)
        pdf.line(15,680,580,680)
        
       
        pdf.line(15,200,580,200)
        pdf.line(15,180,580,180)
        pdf.line(15,150,580,150)
     
        #Internal Horizontal Lines
        pdf.line(72,680,72,200)
        pdf.line(120,680,120,200)
        pdf.line(265,680,265,180)
        pdf.line(295,680,295,180)
        pdf.line(325,680,325,200)
        pdf.line(350,680,350,200)
        pdf.line(400,680,400,180)
        pdf.line(440,680,440,180)
        pdf.line(480,680,480,180)
        pdf.line(530,680,530,180)

        
        pdf.line(15,115,400,115)
        pdf.line(15,95,400,95)
        pdf.line(15,75,400,75)
        pdf.line(15,55,400,55)
        pdf.line(15,35,400,35)

        #Tax Horizontal Lines
        pdf.line(400,150,400,15)
        pdf.line(320,150,320,15)
        pdf.line(250,115,250,15)
        pdf.line(220,150,220,15)
        pdf.line(150,115,150,15)
        pdf.line(120,150,120,15)
        pdf.line(50,150,50,15)
        
        pdf.setFont("Courier-Bold",12)

        pdf.drawString(355,130,"Total")
        pdf.drawString(20,130,"Tax")
        pdf.drawString(60,120,"Taxable")
        pdf.drawString(20,100,"0%")
        pdf.drawString(20,80,"5%")
        pdf.drawString(20,60,"12%")
        pdf.drawString(20,40,"18%")
        pdf.drawString(20,20,"28%")

        pdf.drawString(50,100,str(extaxable))
        pdf.drawString(50,80,str(ftax))
        pdf.drawString(50,60,str(twtax))
        pdf.drawString(50,40,str(etax))
        pdf.drawString(50,20,str(htax))
        
        pdf.drawString(150,130,"Cgst")
        
        pdf.drawString(125,60,"6%")
        pdf.drawString(125,40,"9%")
        pdf.drawString(125,20,"14%")
    
        pdf.drawString(155,80,str(fgst))
        pdf.drawString(155,60,str(twgst))
        pdf.drawString(155,40,str(egst))
        pdf.drawString(155,20,str(hgst))
    
        pdf.drawString(250,130,"Sgst")
        
        pdf.drawString(225,60,"6%")
        pdf.drawString(225,40,"9%")
        pdf.drawString(225,20,"14%")
    
        pdf.drawString(255,80,str(fgst))
        pdf.drawString(255,60,str(twgst))
        pdf.drawString(255,40,str(egst))
        pdf.drawString(255,20,str(hgst))

        ft = ft + ftax + (2*fgst)
        twt = twt + twtax + (2*twgst)
        et = et + etax + (2*egst)
        ht = ht + htax + (2*hgst)

        pdf.drawString(330,100,str(extaxable))
        pdf.drawString(330,80,str(ft))
        pdf.drawString(330,60,str(twt))
        pdf.drawString(330,40,str(et))
        pdf.drawString(330,20,str(ht))
        
        pdf.drawString(420,120,"For "+cName)
        pdf.drawString(420,30,"Authorised Signatory")
        
        pdf.setFont("Courier-Bold",10)
        pdf.drawString(225,80,"2.5%")
        pdf.drawString(125,80,"2.5%")
        pdf.save()
        webbrowser.open("F:\\InvoiceGeneration\\Purchase_Record\\"+str(Number)+".pdf")
        
        
    def In_Ward(self,pobj):
        hsc=StringVar()
        dog=StringVar()
        vid=StringVar()

        rate=IntVar()
        qty=IntVar()
        ta=IntVar()
        sgst=IntVar()
        cgst=IntVar()
        gt=IntVar()
        sgst.set('')
        cgst.set('')
        gt.set('')
        rate.set('')
        qty.set('')
        ta.set('')
        pframe1=Frame(win,width=1000,height=600,bg="lavender").place(x=0,y=0)

        Label(pframe1,text=" Product Entry ",font=('Times New Roman',70),fg='midnightblue',bg="lavender").place(x=200,y=0)

        Label(pframe1,text="Enter Vendor Id:",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=200,y=170)
        Entry(pframe1,width=20,bd=2,textvariable=vid).place(x=400,y=175)

        Label(pframe1,text="Enter HSN/SAC Code:",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=200,y=200)
        Entry(pframe1,width=20,bd=2,textvariable=hsc).place(x=400,y=205)
        
        Label(pframe1,text="Description of Goods :",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=200,y=230)
        Entry(pframe1,width=50,bd=2,textvariable=dog).place(x=400,y=235)

        Label(pframe1,text="Rate Per Unit:",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=200,y=260)
        Entry(pframe1,width=20,bd=2,textvariable=rate).place(x=400,y=265)
        
        Label(pframe1,text="Quantity:",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=200,y=290)
        Entry(pframe1,width=20,bd=2,textvariable=qty).place(x=400,y=295)

        Label(pframe1,text="Applied Tax:",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=200,y=320)
        P = ["-Percentage-","5","12","18","28"]
        apt=IntVar()
        apt.set(P[0])  
        OptionMenu(pframe1,apt,*P).place(x=400,y=325)

        Label(pframe1,text="Taxable Amount:",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=200,y=400)
        Entry(pframe1,width=20,bd=2,textvariable=ta).place(x=400,y=405)

        Label(pframe1,text="Sgst:",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=200,y=430)
        Entry(pframe1,width=20,bd=2,textvariable=sgst).place(x=400,y=435)

        Label(pframe1,text="Cgst:",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=200,y=460)
        Entry(pframe1,width=20,bd=2,textvariable=cgst).place(x=400,y=465)

        Label(pframe1,text="Grand Total:",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=200,y=490)
        Entry(pframe1,width=20,bd=2,textvariable=gt).place(x=400,y=495)

        global getb
        getb=IntVar()
        pho=PhotoImage(file="home.png")
        Button(pframe1,image=pho,border=0,compound=TOP,bg='lavender',command=lambda:pobj.home).place(x=800,y=420)
        Button(pframe1,text="Reset",bd=2,width=10,height=1,relief="ridge",bg='blue',fg='white',font=('Poor Richard',20),command=lambda:pobj.rese(pobj,hsc.set(''),dog.set(''),rate.set(''),qty.set(''),ta.set(''),vid.set(''),sgst.set(''),cgst.set(''),gt.set(''))).place(x=800,y=350)
        Button(pframe1,text='Verify',font=('Maiandra GD',10),fg='black',bg='Yellow',command=lambda:check(vid.get())).place(x=150,y=170)
        Button(pframe1,text='Calculate',font=('Maiandra GD',15),fg='white',bg='gray25',command=lambda:Caltax(apt.get(),rate.get(),qty.get())).place(x=400,y=360)
        Button(pframe1,text='Save',bd=2,width=10,height=1,relief="ridge",bg='Green',fg='white',font=('Poor Richard',20),command=lambda:pobj.save(pobj,vid.get(),hsc.get(),dog.get(),rate.get(),qty.get(),ta.get(),sgst.get(),cgst.get(),gt.get(),apt.get())).place(x=800,y=250)
        Button(pframe1,text='Report',bd=2,width=10,height=1,relief="ridge",bg='gray15',fg='white',font=('Poor Richard',20),command=lambda:pobj.Report(pobj)).place(x=800,y=150)
        self.pho=PhotoImage(file="home.png")
        Button(pframe1,image=self.pho,border=0,compound=TOP,bg='lavender',command=pobj.home).place(x=800,y=440)

        def Caltax(apt,rate,qty):
            Total=rate*qty
            val=100+apt
            t=apt/2
            a=Total/val*t
            gst=round(a,2)
            sgst.set(gst)
            cgst.set(gst)
            b=Total-gst*2
            ta.set(b)
            gt.set(Total)
            
        def check(vid):
            self.vid=vid
            pframe2=Frame(win,width=250,height=20,bg="lavender").place(x=540,y=175)
            try:
                conn=pymysql.connect(host='localhost',user='root',password='',db='software')
                a=conn.cursor()
                a.execute('select ID,Company from venders')
                result=a.fetchall()
                for i in result:
                    if vid == i[0]:
                        getb=0
                        Label(pframe2,text=i[1],font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=540,y=170)
                        messagebox.showinfo("Status","Verified")
                        
                        break
                    else:
                        getb=1
                if getb == 1:
                    messagebox.showinfo("Status","Not Verified")
            except:
                messagebox.showinfo("Status","Technical Issue")
            conn.close()

    def home(self):
        self.front=main(win)

    def save(self,pobj,vid,hsc,dog,rate,qty,ta,sgst,cgst,gt,apt):
        self.vid=vid
        self.hsc=hsc
        self.dog=dog
        self.rate=str(rate)
        self.qty=str(qty)
        self.ta=str(ta)
        self.sgst=str(sgst)
        self.cgst=str(cgst)
        self.gt=str(gt)
        self.apt=str(apt)
        try:
            conn=pymysql.connect(host='localhost',user='root',password='',db='software')
            a=conn.cursor()
            a.execute("insert into purchase(ID,HSNorSAC,Goods,Rate_Per_Unit,Quantity,Applied_Tax,Taxable_Amount,Sgst,Cgst,Grand_Total)value('"+vid+"','"+hsc+"','"+dog+"','"+self.rate+"','"+self.qty+"','"+self.apt+"','"+self.ta+"','"+self.sgst+"','"+self.cgst+"','"+self.gt+"')")
            a.execute("insert into net(ID,HSNorSAC,Goods,Rate_Per_Unit,Quantity,Applied_Tax,Taxable_Amount,Sgst,Cgst,Grand_Total)value('"+vid+"','"+hsc+"','"+dog+"','"+self.rate+"','"+self.qty+"','"+self.apt+"','"+self.ta+"','"+self.sgst+"','"+self.cgst+"','"+self.gt+"')")
            conn.commit()
            pobj.In_Ward(pobj)
            messagebox.showinfo("Status","Saved")
        except:
            conn.rollback()
            messagebox.showinfo("Status","Not Saved")
        conn.close()
        
    def rese(self,pobj,hsc,dog,rate,qty,ta,vid,sgst,cgst,gt):
        messagebox.showinfo("Status","Reset")

    def Report(self,pobj):
        global Userd
        Userd=[]
        global flag
        self.flag=IntVar()
        self.flag=2
        pframe3=Frame(win,width=1000,height=600,bg="lavender").place(x=0,y=0)
        self.pho=PhotoImage(file="home.png")
        Button(pframe3,image=self.pho,border=0,compound=TOP,bg='lavender',command=pobj.home).place(x=825,y=420)

        self.scrollbary = Scrollbar(pframe3, orient=VERTICAL)
        self.tree = ttk.Treeview(pframe3,columns=(0,1,2,3,4,5,6,7,8,9,10),show='headings',height=20, selectmode="extended", yscrollcommand=self.scrollbary.set)
        self.tree.heading(0, text="Seller Id")
        self.tree.heading(1, text="HSN/SAC")
        self.tree.heading(2, text="Product Name")
        self.tree.heading(3, text="Rate")
        self.tree.heading(4, text="Qty.")
        self.tree.heading(5,text="Tax")
        self.tree.heading(6,text="Taxable Amount")
        self.tree.heading(7, text="Sgst")
        self.tree.heading(8, text="Cgst")
        self.tree.heading(9, text="Total")
        self.tree.heading(10, text="Date")
        self.tree.column(0, stretch=NO,width=78)
        self.tree.column(1, stretch=NO,width=78)
        self.tree.column(2, stretch=NO,width=185)
        self.tree.column(3, stretch=NO,width=55)
        self.tree.column(4, stretch=NO,width=30)
        self.tree.column(5, stretch=NO,width=30)
        self.tree.column(6, stretch=NO,width=100)
        self.tree.column(7, stretch=NO,width=50)
        self.tree.column(8, stretch=NO,width=50)
        self.tree.column(9, stretch=NO,width=80)
        self.tree.column(10, stretch=NO,width=70)
        self.tree.place(x=10,y=10)
        try:
            conn=pymysql.connect(host='localhost',user='root',password='',db='software')
            a=conn.cursor()
            a.execute('select * from purchase')
            result=a.fetchall()
            subdat=datetime.datetime
            for i in result:
                Userd.append(i)
                self.tree.insert('','end',values=i)
        except:
            messagebox.showinfo("Status","Technical Issue")
        conn.close()
        
        def showtax(apt,flag):
            if self.flag == 0:
                now=datetime.datetime.today()
                ci=now.strftime('%y')
                conn=pymysql.connect(host='localhost',user='root',password='',db='software')
                a=conn.cursor()
                a.execute('select Time,Applied_Tax,Taxable_Amount,Sgst,Cgst,Grand_Total from purchase')
                result=a.fetchall()
                ttt=int
                Sgst=int
                cgst=int
                tg=int
                ttt=0
                Sgst=0
                cgst=0
                tg=0
                ffff=IntVar()
                fff=IntVar()
                for i in result:
                    cm=i[0].strftime('%y')
                    if cm == ci:
                        if apt == i[1]:
                            ffff=1
                            fff=1
                            ttt= ttt + i[2]
                            Sgst= Sgst + i[3]
                            cgst= cgst + i[4]
                            tg=ttt+Sgst+cgst
                        else:
                            ffff=0
                    else:
                        messagebox.showinfo("Status",'No Record Found')
                        break
                if not((ffff == 1 )or(fff == 1)):
                    messagebox.showinfo("Status",'No Record Found for Selected Tax Range')
                    
                tt.set(ttt)
                tsgst.set(Sgst)
                tcgst.set(cgst)
                tgt.set(tg)

            elif self.flag == 1:
                now=datetime.datetime.today()
                ci=now.strftime('%d')
                conn=pymysql.connect(host='localhost',user='root',password='',db='software')
                a=conn.cursor()
                a.execute('select Time,Applied_Tax,Taxable_Amount,Sgst,Cgst,Grand_Total from purchase')
                result=a.fetchall()
                ttt=int
                Sgst=int
                cgst=int
                tg=int
                ttt=0
                Sgst=0
                cgst=0
                tg=0
                ffff=IntVar()
                fff=IntVar()
                for i in result:
                    cm=i[0].strftime('%d')
                    if cm == ci:
                        if apt == i[1]:
                            ffff=1
                            fff=1
                            ttt= ttt + i[2]
                            Sgst= Sgst + i[3]
                            cgst= cgst + i[4]
                            tg=ttt+Sgst+cgst
                        else:
                            ffff=0
                    else:
                        messagebox.showinfo("Status",'No Record Found')
                        break
                if not((ffff == 1 )or(fff == 1)):
                    messagebox.showinfo("Status",'No Record Found for Selected Tax Range')
                    
                tt.set(ttt)
                tsgst.set(Sgst)
                tcgst.set(cgst)
                tgt.set(tg)
    
            elif self.flag == 2:
                now=datetime.datetime.today()
                ci=now.strftime('%m')
                conn=pymysql.connect(host='localhost',user='root',password='',db='software')
                a=conn.cursor()
                a.execute('select Time,Applied_Tax,Taxable_Amount,Sgst,Cgst,Grand_Total from purchase')
                result=a.fetchall()
                ttt=int
                Sgst=int
                cgst=int
                tg=int
                ttt=0
                Sgst=0
                cgst=0
                tg=0
                ffff=IntVar()
                fff=IntVar()
                for i in result:
                    cm=i[0].strftime('%m')
                    if cm == ci:
                        if apt == i[1]:
                            ffff=1
                            fff=1
                            ttt= ttt + i[2]
                            Sgst= Sgst + i[3]
                            cgst= cgst + i[4]
                            tg=ttt+Sgst+cgst
                        else:
                            ffff=0
                    else:
                        messagebox.showinfo("Status",'No Record Found')
                        break
                if not((ffff == 1 )or(fff == 1)):
                    messagebox.showinfo("Status",'No Record Found for Selected Tax Range')
                    
                tt.set(ttt)
                tsgst.set(Sgst)
                tcgst.set(cgst)
                tgt.set(tg)
        
                
        def RToday():
            self.flag=1
            self.tree.destroy()
            
            self.tree = ttk.Treeview(pframe3,columns=(0,1,2,3,4,5,6,7,8,9,10),show='headings',height=20, selectmode="extended", yscrollcommand=self.scrollbary.set)
            self.tree.heading(0, text="Seller Id")
            self.tree.heading(1, text="HSN/SAC")
            self.tree.heading(2, text="Product Name")
            self.tree.heading(3, text="Rate")
            self.tree.heading(4, text="Qty.")
            self.tree.heading(5,text="Tax")
            self.tree.heading(6,text="Taxable Amount")
            self.tree.heading(7, text="Sgst")
            self.tree.heading(8, text="Cgst")
            self.tree.heading(9, text="Total")
            self.tree.heading(10, text="Date")
            self.tree.column(0, stretch=NO,width=78)
            self.tree.column(1, stretch=NO,width=78)
            self.tree.column(2, stretch=NO,width=185)
            self.tree.column(3, stretch=NO,width=55)
            self.tree.column(4, stretch=NO,width=30)
            self.tree.column(5, stretch=NO,width=30)
            self.tree.column(6, stretch=NO,width=100)
            self.tree.column(7, stretch=NO,width=50)
            self.tree.column(8, stretch=NO,width=50)
            self.tree.column(9, stretch=NO,width=80)
            self.tree.column(10, stretch=NO,width=70)
            self.tree.place(x=10,y=10)
            
            now=datetime.datetime.today()
            ci=now.strftime('%d')
            conn=pymysql.connect(host='localhost',user='root',password='',db='software')
            a=conn.cursor()
            a.execute('select * from purchase')
            result=a.fetchall()
            now=datetime.datetime.today()
            ci=now.strftime('%d')
            
            for i in result:
                cm=i[10].strftime('%d')
                if cm == ci:
                    Userd.append(i)
                    self.tree.insert('','end',values=i)
                else:
                    messagebox.showinfo("Status",'No Record Found')
                    break
                        
            
             
        def RMonth():
            self.flag=2
            self.tree.destroy()
            
            self.tree = ttk.Treeview(pframe3,columns=(0,1,2,3,4,5,6,7,8,9,10),show='headings',height=20, selectmode="extended", yscrollcommand=self.scrollbary.set)
            self.tree.heading(0, text="Seller Id")
            self.tree.heading(1, text="HSN/SAC")
            self.tree.heading(2, text="Product Name")
            self.tree.heading(3, text="Rate")
            self.tree.heading(4, text="Qty.")
            self.tree.heading(5,text="Tax")
            self.tree.heading(6,text="Taxable Amount")
            self.tree.heading(7, text="Sgst")
            self.tree.heading(8, text="Cgst")
            self.tree.heading(9, text="Total")
            self.tree.heading(10, text="Date")
            self.tree.column(0, stretch=NO,width=78)
            self.tree.column(1, stretch=NO,width=78)
            self.tree.column(2, stretch=NO,width=185)
            self.tree.column(3, stretch=NO,width=55)
            self.tree.column(4, stretch=NO,width=30)
            self.tree.column(5, stretch=NO,width=30)
            self.tree.column(6, stretch=NO,width=100)
            self.tree.column(7, stretch=NO,width=50)
            self.tree.column(8, stretch=NO,width=50)
            self.tree.column(9, stretch=NO,width=80)
            self.tree.column(10, stretch=NO,width=70)
            self.tree.place(x=10,y=10)
            
            now=datetime.datetime.today()
            ci=now.strftime('%m')
            conn=pymysql.connect(host='localhost',user='root',password='',db='software')
            a=conn.cursor()
            a.execute('select * from purchase')
            result=a.fetchall()
            
            for i in result:
                cm=i[10].strftime('%m')
                if cm == ci:
                    Userd.append(i)
                    self.tree.insert('','end',values=i)
                else:
                    messagebox.showinfo("Status",'No Record Found')
                    break
            
        def RYear():
            self.flag=0
            self.tree.destroy()
            
            self.tree = ttk.Treeview(pframe3,columns=(0,1,2,3,4,5,6,7,8,9,10),show='headings',height=20, selectmode="extended", yscrollcommand=self.scrollbary.set)
            self.tree.heading(0, text="Seller Id")
            self.tree.heading(1, text="HSN/SAC")
            self.tree.heading(2, text="Product Name")
            self.tree.heading(3, text="Rate")
            self.tree.heading(4, text="Qty.")
            self.tree.heading(5,text="Tax")
            self.tree.heading(6,text="Taxable Amount")
            self.tree.heading(7, text="Sgst")
            self.tree.heading(8, text="Cgst")
            self.tree.heading(9, text="Total")
            self.tree.heading(10, text="Date")
            self.tree.column(0, stretch=NO,width=78)
            self.tree.column(1, stretch=NO,width=78)
            self.tree.column(2, stretch=NO,width=185)
            self.tree.column(3, stretch=NO,width=55)
            self.tree.column(4, stretch=NO,width=30)
            self.tree.column(5, stretch=NO,width=30)
            self.tree.column(6, stretch=NO,width=100)
            self.tree.column(7, stretch=NO,width=50)
            self.tree.column(8, stretch=NO,width=50)
            self.tree.column(9, stretch=NO,width=80)
            self.tree.column(10, stretch=NO,width=70)
            self.tree.place(x=10,y=10)
            
            now=datetime.datetime.today()
            ci=now.strftime('%y')
            conn=pymysql.connect(host='localhost',user='root',password='',db='software')
            a=conn.cursor()
            a.execute('select * from purchase')
            result=a.fetchall()
            now=datetime.datetime.today()
            ci=now.strftime('%y')
            
            for i in result:
                cm=i[10].strftime('%y')
                if cm == ci:
                    Userd.append(i)
                    self.tree.insert('','end',values=i)
                else:
                    messagebox.showinfo("Status",'No Record Found')
                    break
           
        
        tt=IntVar()
        tsgst=IntVar()
        tcgst=IntVar()
        tgt=IntVar()
    
        Label(pframe3,text="Total Taxable",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=150,y=440)
        Entry(pframe3,width=20,bd=2,textvariable=tt).place(x=145,y=466)

        Label(pframe3,text="+",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=285,y=460)
        Label(pframe3,text="+",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=470,y=460)
        Label(pframe3,text="=",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=640,y=460)

        Label(pframe3,text="Total Sgst",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=330,y=440)
        Entry(pframe3,width=20,bd=2,textvariable=tsgst).place(x=320,y=466)

        Label(pframe3,text="Total Cgst",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=510,y=440)
        Entry(pframe3,width=20,bd=2,textvariable=tcgst).place(x=500,y=466)

        Label(pframe3,text="Total",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=690,y=440)
        Entry(pframe3,width=20,bd=2,textvariable=tgt).place(x=670,y=466)

        Label(pframe3,text="Applied Tax",font=('Times New Roman',15),fg='midnightblue',bg="lavender").place(x=10,y=440)

        P = ["-Percentage-","5","12","18","28"]
        apt=IntVar()
        apt.set(P[0])  
        OptionMenu(pframe3,apt,*P).place(x=10,y=466)
       
        Button(pframe3,text='Show',bd=2,width=10,height=1,relief="ridge",bg='gray20',fg='white',font=('Poor Richard',20),command=lambda:showtax(apt.get(),self.flag)).place(x=350,y=510)
        Button(pframe3,text="Today's",bd=2,width=10,height=1,relief="ridge",bg='blue',fg='white',font=('Poor Richard',20),command=RToday).place(x=825,y=330)
        Button(pframe3,text='Monthly',bd=2,width=10,height=1,relief="ridge",bg='Green',fg='white',font=('Poor Richard',20),command=RMonth).place(x=825,y=230)
        Button(pframe3,text='Yearly',bd=2,width=10,height=1,relief="ridge",bg='gray15',fg='white',font=('Poor Richard',20),command=RYear).place(x=825,y=130)
        Button(pframe3,text='Print',bd=2,width=10,height=1,relief="ridge",bg='gray',fg='white',font=('Poor Richard',20),command=lambda:pobj.Purchase_Record(Userd)).place(x=825,y=30)

        

class Stock:
    def home(self,sobj):
        self.front=main(win)
        
    def Stock_Record(self,Data):
        try:
            os.mkdir("F:\\InvoiceGeneration\\Stock_Record\\")
        except:
            pass
        conn=pymysql.connect(host='localhost',user='root',password='',db='software')
        a=conn.cursor()
        a.execute('select CompanyName,Name,GST,PAN,Mobile,Email,Address,Locality,State from client')
        result=a.fetchall()
        cName=StringVar
        Name=StringVar
        G=StringVar
        P=StringVar
        M=StringVar
        E=StringVar
        Add=StringVar
        Loc=StringVar()
        sts=StringVar()            
        for i in result:
            cName=i[0]
            Name=i[1]
            G=i[2]
            P=i[3]
            M=i[4]
            E=i[5]
            Add=i[6]
            Loc=i[7]
            sts=i[8]
        
        now=datetime.datetime.today()
        Number='Stock'+str(now.strftime('%y'))+str(now.strftime('%d'))+str(now.microsecond)
        Canvas(width=210,height=293)
        pdf= canvas.Canvas("F:\\InvoiceGeneration\\Stock_Record\\"+str(Number)+".pdf",pagesize=A4)
        width,height=A4
        #Header
        pdf.line(20,815,575,815)
        pdf.setTitle("Stock Report")
        pdf.setFont("Courier-Bold",15)
        pdf.drawString(220,825,"Stock Record")
        pdf.setFont("Courier-Bold",25)
        pdf.drawString(150,795,cName)
        pdf.setFont("Courier-Bold",10)
        pdf.drawString(245,780,Name)
        pdf.drawString(245,765,"Gst:"+G)
        pdf.drawString(245,750,"Pan:"+P)
        pdf.drawString(150,735,"Mobile:"+M+"  Email:"+E)
        pdf.drawString(250,720,Add)
        pdf.drawString(150,705,Loc)
        pdf.drawString(250,690,sts)
        #Head Column
        pdf.setFont("Courier-Bold",9)
        pdf.drawString(25,670,"S.N.")
        pdf.drawString(65,670,"Product Detalis")
        pdf.drawString(248,670,"HSN/SAC")
        pdf.drawString(300,670,"Rate")
        pdf.drawString(342,675,"Inward")
        pdf.drawString(345,665,"Qty.")
        pdf.drawString(380,675,"OutWard")
        pdf.drawString(390,665,"Qty.")
        pdf.drawString(425,675,"Net")
        pdf.drawString(424,665,"Qty.")
        pdf.drawString(455,675,"Inventory")
        pdf.drawString(460,665,"Value")
        pdf.drawString(530,675,"Sales")
        pdf.drawString(530,665,"Value")

        #Internal lines

        pdf.line(50,685,50,20)
        pdf.line(240,685,240,20)
        pdf.line(290,685,290,20)
        pdf.line(340,685,340,20)
        pdf.line(378,685,378,20)
        pdf.line(420,685,420,20)
        pdf.line(450,685,450,20)
        pdf.line(513,685,513,20)

        #Border
        pdf.line(20,20,575,20)
        pdf.line(20,815,20,20)
        pdf.line(575,815,575,20)
        pdf.line(20,815,575,815)

        pdf.line(20,685,575,685)
        pdf.line(20,660,575,660)

        J=IntVar()
        J=1
        ycoordinate=IntVar()
        ycoordinate=640
        for i in Data:
            pdf.drawString(30,ycoordinate,str(J))
            pdf.drawString(55,ycoordinate,str(i[0]))
            if len(i[1]) > 8:
                pdf.setFont("Courier-Bold",7)
                pdf.drawString(243,ycoordinate,str(i[1]))
            else:
                pdf.setFont("Courier-Bold",9)
                pdf.drawString(243,ycoordinate,str(i[1]))
            pdf.setFont("Courier-Bold",9)
            pdf.drawString(295,ycoordinate,str(i[2]))
            pdf.drawString(355,ycoordinate,str(i[3]))
            pdf.drawString(395,ycoordinate,str(i[4]))
            pdf.drawString(430,ycoordinate,str(i[5]))
            pdf.drawString(460,ycoordinate,str(i[6]))
            pdf.drawString(530,ycoordinate,str(i[7]))
            J=J+1
            ycoordinate = ycoordinate - 25
        pdf.save()
        webbrowser.open("F:\\InvoiceGeneration\\Stock_Record\\"+str(Number)+".pdf")
    
    def show(self,sobj):
        sframe1=Frame(win,width=1000,height=600,bg="lavender").place(x=0,y=0)
        
        self.scrollbary = Scrollbar(sframe1, orient=VERTICAL)
        self.tree = ttk.Treeview(sframe1,columns=(1,2,3,4,5,6,7,8),show='headings',height=20, selectmode="extended", yscrollcommand=self.scrollbary.set)

        self.tree.heading(1, text="Product Name")
        self.tree.heading(2, text="HSN/SAC")
        self.tree.heading(3, text="Unit Price")
        self.tree.heading(4, text="Inward Quantity")
        self.tree.heading(5, text="Outward Quantity")
        self.tree.heading(6, text="Net Quantity")
        self.tree.heading(7, text="Inventory Value")
        self.tree.heading(8, text="Sales Value")
        
        self.tree.column(1, stretch=NO,width=250)
        self.tree.column(2, stretch=NO,width=100)
        self.tree.column(3, stretch=NO,width=100)
        self.tree.column(4, stretch=NO,width=100)
        self.tree.column(5, stretch=NO,width=110)
        self.tree.column(6, stretch=NO,width=90)
        self.tree.column(7, stretch=NO,width=100)
        self.tree.column(8, stretch=NO,width=100)
        self.tree.place(x=10,y=10)
            
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill='y')

        Data = []
        conn=pymysql.connect(host='localhost',user='root',password='',db='software')
        a=conn.cursor()
        a.execute('select * from purchase')
        result=a.fetchall()
        a.execute('select * from invoice')
        result1=a.fetchall()
        a.execute('select * from net')
        result2=a.fetchall()
        a.execute('delete from stock')
        Outward=IntVar()
        iv=IntVar()
        sv=IntVar()
        Net=IntVar()
        iv=0
        sv=0
        Net=0
        Outward=0
        for i in result:
            hsn=i[1]
            for k in result2:
                for j in result1:
                    if (hsn == j[2]) and (hsn == k[1]):
                        iv = i[3]*i[4]
                        sv = i[3]*j[5]
                        Outward = j[5]
                        Net=k[4]
                        a.execute("insert into stock(Product_Name,HSNorSAC,Rate,Inward,Outward,Net,Inventory_Value,Sales_Value,Time)value('"+str(i[2])+"','"+str(i[1])+"','"+str(i[3])+"','"+str(i[4])+"','"+str(Outward)+"','"+str(Net)+"','"+str(iv)+"','"+str(sv)+"','"+str(k[10])+"')")
                        conn.commit()
                    elif (hsn == k[1]):
                        iv = i[3]*i[4]
                        sv = i[3]*0
                        Outward=0
                        Net=k[4]
                        a.execute("insert into stock(Product_Name,HSNorSAC,Rate,Inward,Outward,Net,Inventory_Value,Sales_Value,Time)value('"+str(i[2])+"','"+str(i[1])+"','"+str(i[3])+"','"+str(i[4])+"','"+str(Outward)+"','"+str(Net)+"','"+str(iv)+"','"+str(sv)+"','"+str(k[10])+"')")
                        conn.commit()
        a.execute('select * from stock')
        Data=a.fetchall()
        conn.close()
        for i in Data:
            self.tree.insert('','end',value=i)

        self.pho=PhotoImage(file="home.png")
        Button(sframe1,image=self.pho,border=0,compound=TOP,bg='lavender',command=lambda:sobj.home(sobj)).place(x=10,y=445)
        Button(sframe1,text="Print",bd=2,width=10,height=1,relief="ridge",bg='Blue',fg='white',font=('Poor Richard',18),command=lambda:sobj.Stock_Record(Data)).place(x=500,y=500)
        

class  stat:
    def graph(self):
        def graphs():
            conn=pymysql.connect(host='localhost',user='root',password='',db='software')
            a=conn.cursor()
            a.execute('select Applied_Tax from invoice')
            result=a.fetchall()
            conn.close()
            p=IntVar()
            q=IntVar()
            r=IntVar()
            s=IntVar()
            p=0
            q=0
            r=0
            s=0
            for i in result:
                if i[0] == 5:
                    p = p +1
                elif i[0] == 12:
                    q = q + 1
                elif i[0] == 18:
                    r = r +1
                elif i[0] == 28:
                    s = s + 1
            textprops={"fontsize":20}
            activites=['5% Gst','12% Gst','18% Gst','28% Gst']
            slices=[p,q,r,s]
            colors=['r','g','m','b']
            plt.pie(slices,labels=activites,colors=colors,textprops=textprops,startangle=90,explode=(0.1,0.1,0.1,0.1),autopct='%1.f%%')
            plt.legend(loc=(1.0,0.0))
            plt.show()
   
        def graphp():
            conn=pymysql.connect(host='localhost',user='root',password='',db='software')
            a=conn.cursor()
            a.execute('select Applied_Tax from purchase')
            result=a.fetchall()
            conn.close()
            p=IntVar()
            q=IntVar()
            r=IntVar()
            s=IntVar()
            p=0
            q=0
            r=0
            s=0
            for i in result:
                if i[0] == 5:
                    p = p +1
                elif i[0] == 12:
                    q = q + 1
                elif i[0] == 18:
                    r = r +1
                elif i[0] == 28:
                    s = s + 1
            textprops={"fontsize":15}
            activites=['5% Gst','12% Gst','18% Gst','28% Gst']
            slices=[p,q,r,s]
            colors=['r','g','m','b']
            plt.pie(slices,labels=activites,colors=colors,textprops=textprops,startangle=180,explode=(0.1,0.1,0.1,0.1),autopct='%1.f%%')
            plt.legend(loc='lower right')
            plt.show()
        
        def graphd():
            conn=pymysql.connect(host='localhost',user='root',password='',db='software')
            a=conn.cursor()
            a.execute('select Applied_Tax from invoice')
            result=a.fetchall()
        
            p=IntVar()
            q=IntVar()
            r=IntVar()
            s=IntVar()
            p=0
            q=0
            r=0
            s=0
            for i in result:
                if i[0] == 5:
                    p = p +1
                elif i[0] == 12:
                    q = q + 1
                elif i[0] == 18:
                    r = r +1
                elif i[0] == 28:
                    s = s + 1
           
            x=[5,10,15,20]
            y=[p,q,r,s]
            tick_label=['5%','12%','18%','28%']
            plt.bar(x,y,width=0.4,tick_label=tick_label,color='red')
            plt.xlabel('Tax Range',color='green')
            plt.ylabel('y-axis',color='red')
            plt.title('Bar Graph',color='black')
            plt.show()
        
        def graphpro():
            conn=pymysql.connect(host='localhost',user='root',password='',db='software')
            a=conn.cursor()
            a.execute('select Applied_Tax,Grand_Total from purchase')
            result=a.fetchall()
            a.execute('select Applied_Tax,Grand_Total from invoice')
            result1=a.fetchall()
            conn.close()
            ptwtotal=IntVar()
            pfitotal=IntVar()
            peitotal=IntVar()
            ptwetotal=IntVar()
            ptwtotal=0
            pfitotal=0
            peitotal=0
            ptwetotal=0
            for i in result:
                if i[0] == 5:
                    pfitotal = pfitotal + i[1]
                elif i[0] == 12:
                    ptwtotal = ptwtotal + i[1]
                elif i[0] == 18:
                    peitotal = peitotal + i[1]
                elif i[0] == 28:
                    ptwetotal = ptwetotal + i[1]
            stwtotal=IntVar()
            sfitotal=IntVar()
            seitotal=IntVar()
            stwetotal=IntVar()
            stwtotal=0
            sfitotal=0
            seitotal=0
            stwetotal=0
            for i in result1:
                if i[0] == 5:
                    sfitotal = sfitotal + i[1]
                elif i[0] == 12:
                    stwtotal = stwtotal + i[1]
                elif i[0] == 18:
                    seitotal = seitotal + i[1]
                elif i[0] == 28:
                    stwetotal = stwetotal + i[1]
            select = StringVar()
            
            p = sfitotal- pfitotal
            q = stwtotal- ptwtotal
            r = seitotal- peitotal
            s = stwetotal- ptwetotal

            if (p<0)or(q<0)or(r<0)or(s<0):
                select = 'red'
            else:
                select = 'green'
                            
            x=[1,2,3,4]
            y=[p,q,r,s]
            tick_label=['5%','12%','18%','28%']
            plt.bar(x,y,width=0.3,tick_label=tick_label,color=select)
            plt.xlabel('Tax Range',color='green')
            plt.ylabel('y-axis',color='red')
            plt.title('Bar Graph',color='black')
            plt.show()
        
        frame1=Frame(win,width=1000,height=600,bg="lavender").place(x=0,y=0)
        self.pho=PhotoImage(file="home.png")
        Button(frame1,image=self.pho,border=0,compound=TOP,bg='lavender',command=lambda:sobj.home(sobj)).place(x=450,y=200)
        Button(frame1,text="Sales PieChart",bd=2,width=13,height=1,relief="ridge",bg='Blue',fg='white',font=('Poor Richard',30),command=graphs).place(x=100,y=100)
        Button(frame1,text="Purchase PieChart",bd=2,width=13,height=1,relief="ridge",bg='Blue',fg='white',font=('Poor Richard',30),command=graphp).place(x=650,y=100)
        Button(frame1,text="Profit/Loss Graph",bd=2,width=13,height=1,relief="ridge",bg='Blue',fg='white',font=('Poor Richard',30),command=graphpro).place(x=100,y=400)
        Button(frame1,text="Demand",bd=2,width=13,height=1,relief="ridge",bg='Blue',fg='white',font=('Poor Richard',30),command=graphd).place(x=650,y=400)
    

class main:
    def __init__(self,master):
        frame=Frame(win,width=1000,height=600,bg="lavender").place(x=0,y=0)
        self.photo=PhotoImage(file="invoic.png")
        self.photo1=PhotoImage(file="CLOSE.png")
        self.photo2=PhotoImage(file="ve.png")
        self.photo3=PhotoImage(file="customer.png")
        self.photo4=PhotoImage(file="Stock.png")
        self.photo5=PhotoImage(file="stat.png")
        self.photo6=PhotoImage(file="sale.png")
        self.photo7=PhotoImage(file="pur.png")

        Label(win,text="Inventoy Management System",width=47,height=2,font=('Times New Roman',28),fg="yellow",bg='purple',bd=6,relief="ridge").place(x=0,y=0)

        Button(frame,image=self.photo,border=0,text='Invoice',font=('Maiandra GD',20),fg='orange red',compound=TOP,bg='lavender',command=lambda:iobj.show(iobj,cobj)).place(x=40,y=150)

        Button(frame,image=self.photo2,border=0,text='Vendors',font=('Maiandra GD',20),fg='orange red',compound=TOP,bg='lavender',command=lambda:vobj.show(vobj)).place(x=290,y=150)

        Button(frame,image=self.photo3,border=0,text='Customers',font=('Maiandra GD',20),fg='orange red',compound=TOP,bg='lavender',command=lambda:cobj.show(cobj)).place(x=540,y=150)

        Button(frame,image=self.photo4,border=0,text='Stock',font=('Maiandra GD',20),fg='orange red',compound=TOP,bg='lavender',command=lambda:sobj.show(sobj)).place(x=790,y=150)

        Button(frame,image=self.photo6,border=0,text='Sales',font=('Maiandra GD',20),fg='orange red',compound=TOP,bg='lavender',command=lambda:isobj.show(isobj)).place(x=40,y=380)

        Button(frame,image=self.photo7,border=0,text='Purchase',font=('Maiandra GD',20),fg='orange red',compound=TOP,bg='lavender',command=lambda:pobj.In_Ward(pobj)).place(x=290,y=380)

        Button(frame,image=self.photo5,border=0,text='Statistics',font=('Maiandra GD',20),fg='orange red',compound=TOP,bg='lavender').place(x=540,y=380)
    
        Button(frame,image=self.photo1,border=0,text='Exit',font=('Maiandra GD',20),fg='orange red',compound=TOP,bg='lavender',command=quit).place(x=790,y=380)
        
        Button(frame,image=self.photo5,border=0,text='Statistics',font=('Maiandra GD',20),fg='orange red',compound=TOP,bg='lavender',command=daobj.graph).place(x=540,y=380)

vobj=Vendor()
cobj=Customers()
iobj=Invoice()
pobj=Purchase()
sobj=Stock()
isobj=SalesRecord()
daobj=stat()

class regi:
    def __init__(self,master):
        try:
            conn=pymysql.connect(host='localhost',user='root',password='',db='software')
            a=conn.cursor()
            a.execute("select * from client")
            res=a.fetchall()
            c=a.rowcount
            if(c>0):
                messagebox.showinfo("Status","Software for this device already Registered")
            else:
                frame=Frame(win,width=500,height=450,bg="yellow").place(x=250,y=110)
                Label(frame,text="Registration",width=26,height=1,font=('Times New Roman',26),bg="gold",fg='midnightblue',bd=2,relief="ridge").place(x=250,y=100)

                Label(frame,text="Company Name :",font=('Times New Roman',15),bg="yellow",fg='midnightblue').place(x=350,y=160)
                cn=StringVar()
                Entry(frame,width=30,textvariable=cn).place(x=500,y=164)
    
                Label(frame,text="User Name :",font=('Times New Roman',15),bg="yellow",fg='midnightblue').place(x=385,y=190)
                un=StringVar()
                Entry(frame,textvariable=un).place(x=500,y=194)

                Label(frame,text="Password :",font=('Times New Roman',15),bg="yellow",fg='midnightblue').place(x=395,y=220)
                pas=StringVar()
                Entry(frame,textvariable=pas).place(x=500,y=224)

                Label(frame,text="Name :",font=('Times New Roman',15),bg="yellow",fg='midnightblue').place(x=426,y=250)
                n=StringVar()
                Entry(frame,textvariable=n).place(x=500,y=254)


                Label(frame,text="GST :",font=('Times New Roman',15),bg="yellow",fg='midnightblue').place(x=435,y=280)
                gst=StringVar()
                Entry(frame,textvariable=gst).place(x=500,y=284)

                Label(frame,text="PAN :",font=('Times New Roman',15),bg="yellow",fg='midnightblue').place(x=435,y=310)
                pan=StringVar()
                Entry(frame,textvariable=pan).place(x=500,y=314)

                Label(frame,text="Mobile No :",font=('Times New Roman',15),bg="yellow",fg='midnightblue').place(x=388,y=340)
                m=StringVar()
                Entry(frame,textvariable=m).place(x=500,y=344)

                Label(frame,text="Email ID :",font=('Times New Roman',15),bg="yellow",fg='midnightblue').place(x=399,y=370)
                em=StringVar()
                Entry(frame,textvariable=em).place(x=500,y=374)

                Label(frame,text="Address :",font=('Times New Roman',15),bg="yellow",fg='midnightblue').place(x=410,y=400)
                Add=StringVar()
                Entry(frame,width=30,textvariable=Add).place(x=500,y=404)

                Label(frame,text="State :",font=('Times New Roman',15),bg="yellow",fg='midnightblue').place(x=410,y=430)
                st=StringVar()
                Entry(frame,width=20,textvariable=st).place(x=500,y=434)

                Label(frame,text="Pincode :",font=('Times New Roman',15),bg="yellow",fg='midnightblue').place(x=410,y=460)
                pin=StringVar()
                Entry(frame,width=15,textvariable=pin).place(x=500,y=464)

                Label(frame,text="Product Key :",font=('Times New Roman',15),bg="yellow",fg='midnightblue').place(x=380,y=490)
                prokey=StringVar()
                Entry(frame,textvariable=prokey).place(x=500,y=494)
                
                def save():
                    a=cn.get()
                    b=un.get()
                    c=pas.get()
                    d=n.get()
                    e=gst.get()
                    f=pan.get()
                    g=m.get()
                    h=em.get()
                    i=Add.get()
                    j=prokey.get()
                    k=st.get()
                    l=pin.get()
                    add=str(i)+str(k)+str(l)

                    if j == '8010052860':
                        try:
                            conn=pymysql.connect(host='localhost',user='root',password='',db='software')
                            connection=conn.cursor()
                            connection.execute("insert into client(PRODUCTKEY,Username,password,CompanyName,Name,Mobile,Email,GST,PAN,Address)value('"+j+"','"+b+"','"+c+"','"+a+"','"+d+"','"+g+"','"+h+"','"+e+"','"+f+"','"+add+"')")
                            conn.commit()
                            messagebox.showinfo("Status","Saved")
                        except:
                            conn.rollback()
                            messagebox.showinfo("Status","Not Saved")
                            conn.close()
                    else:
                        messagebox.showinfo("Status","Enter Valid Product Key")
                Button(frame,text="SUBMIT",width=35,font=('Times New Roman',19),bd=3,bg="Green",fg='white',command=save).place(x=249,y=536)    

       
        except:
            conn.rollback()
            messagebox.showinfo("Status","Login Failed Technical Issue")
        conn.close()
    

def newregi():
    obj=regi(win)
class C:
    def check(self):
        uname=Eun.get()
        pas=Epas.get()
        try:
            conn=pymysql.connect(host='localhost',user='root',password='',db='software')
            a=conn.cursor()
            a.execute("select CompanyName from client where Username='"+uname+"' and password='"+pas+"' ")
            res=a.fetchall()
            c=a.rowcount
            if(c>0):
                self.front=main(win)
            else:
                messagebox.showinfo("Status","Username or Password Incorrect")
        except:
            conn.rollback()
            messagebox.showinfo("Status","Login Failed Technical Issue")
        conn.close()
obj=C()
Label(win,text="Inventory Management System",width=47,height=2,font=('Times New Roman',28),bg="yellow",bd=6,relief="ridge").place(x=0,y=0)
Label(win,text="Enter Username :",font=('Times New Roman',20),bg="lavender",fg='midnightblue').place(x=300,y=200)
Eun=StringVar()
Entry(win,width=30,textvariable=Eun).place(x=500,y=205)
Label(win,text="Password :",font=('Times New Roman',20),bg="lavender",fg='midnightblue').place(x=370,y=300)
Epas=StringVar()
Entry(win,width=30,textvariable=Epas).place(x=500,y=305)
Button(win,text="SUBMIT",width=10,font=('Times New Roman',19),bd=3,bg="Green",fg='white',command=obj.check).place(x=530,y=400)
Button(win,text="New Registration",width=13,font=('Times New Roman',19),bd=3,bg="Blue",fg='white',command=newregi).place(x=300,y=400)
    
win.mainloop()