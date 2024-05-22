from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
from PIL import Image,ImagerTk

db_connection=pymysql.connect(
    host='localhost',
    user='root',
    password='Ashik',
    database='crmm'
)
my_database=db_connection.cursor()
print("connected successfully")

root=Tk()
root.title('CRM')
root.geometry("1530x800+0+0")
root.resizable(True,True)
root.configure(background='#1A5276')



def admin_signin():
    global a2,ebb_8,ebb_9
    a2=Frame(a1,bg='#1A5276',height=1000,width=950) 
    a2.place(x=600,y=0)
    a22=Frame(a11,bg='white',height=1000,width=600)
    a22.place(x=0,y=0)

    img=Image.open('vas2.jpeg')
    img=img.resize((650,800))
    img2=ImageTk.PhotoImage(img)
    imglabel=Label(a22,image=img2,bg="#1A5276")
    imglabel.image=img2
    imglabel.place(x=0,y=0)

    label=Label(a2,text="A d m i n  S i g n i n",
           font=('century gothic', 35, 'bold'),fg="white",bg='#1A5276')
    label.place(x=300,y=100)


    label=Label(a2,text="Name ",
           font=('century gothic', 25, 'bold'),fg="white",bg='#1A5276')
    label.place(x=250,y=318)
    ety1=Entry(a2)
    ety1.place(x=475,y=330,width=220,height=35)

    label=Label(a2,text="Mobile No ",
           font=('century gothic', 25, 'bold'),fg="white",bg='#1A5276')
    label.place(x=250,y=408)
    ety2=Entry(a2)
    ety2.place(x=475,y=420,width=220,height=35)

    label=Label(a2,text="Password ",
           font=('century gothic', 25, 'bold'),fg="white",bg='#1A5276')
    label.place(x=250,y=498)
    ety3=Entry(a2)
    ety3.place(x=475,y=500,width=220,height=35)
    

    def save():
        if (ety1.get()=="" or ety2.get()=="" or ety3.get()==""  ): 
            messagebox.showerror("Error", "Enter all details")
        elif (ety1.get()and ety2.get() and ety3.get()): 
            op = messagebox.askyesno("Save", "Do you really want to save?")
            if op > 0:
                sql_statement="INSERT INTO admin_register (name,mobile,password) values(%s,%s,%s)"
                values=(ety1.get(),ety2.get(),ety3.get())
                my_database.execute(sql_statement,values)
                db_connection.commit()
                messagebox.showinfo("Done","Successfully ID Created")
                a2.destroy()
                a22.destroy()

    b6 = Button(a2,text='Register',bg="#EE8309",fg="white",command=save,font=("century gothic", 13, "bold"),
                     height="1",width="20",bd=0,highlightthickness=2,padx=10,pady=5)
    b6.place(x=370, y=600)
    def rem():
        a2.destroy()
        a22.destroy()
    b6 = Button(a2,text='Back',bg="white",fg="black",command=rem,font=("century gothic", 13, "bold"),
                     height="1",width="15",bd=0,highlightthickness=2,padx=10,pady=5)
    b6.place(x=680, y=720)
    
def leadd():
    a15=Frame(a3,bg='white',height=1000,width=1225) #1A5276
    a15.place(x=0,y=0)
    
    label = Label(a15, text="L e a d  D e t a i l s",
                  font=('century gothic', 35, 'bold'), fg="#1A5276", bg='white')
    label.place(x=400, y=60)


    
    def add_leadd(name, email, mobile, lead_source, lead_owner, status, followup_date, next_followup_date):
        tree.insert("", "end", values=(name, email, mobile, lead_source, lead_owner, status, followup_date, next_followup_date))

    tree = ttk.Treeview(a15, columns=("Name", "Email", "Mobile", "LeadSource","LeadOwner","Status","Followup_date","next_followup_date"), show="headings")
    tree.heading("Name", text="Name")
    tree.heading("Email", text="Email")
    tree.heading("Mobile", text="Mobile")
    tree.heading("LeadSource", text="LeadSource")
    tree.heading("LeadOwner", text="LeadOwner")
    tree.heading("Status", text="Status")
    tree.heading("Followup_date", text="Followup_date")
    tree.heading("next_followup_date", text="next_followup_date")
    tree.place(x=50, y=200, width=1000, height=450)

    xscrollbar = ttk.Scrollbar(a15, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=xscrollbar.set)

 
    tree.place(x=50, y=200, width=1000, height=450)
    xscrollbar.place(x=50, y=650, width=1000)

    sql="SELECT name, email, mobile, leadsource, leadowner, statuss, followup_dates, nextfollowup_date from leadd"
    my_database.execute(sql)
    res=my_database.fetchall()

    for lead in res:
        add_leadd(*lead)

    def add_lead():
        a20=Frame(a15,bg='white',height=1000,width=1225) #1A5276
        a20.place(x=0,y=0)
        label = Label(a20, text=" A d d  L e a d  D e t a i l s",
                      font=('century gothic', 35, 'bold'), fg="#1A5276", bg='white')
        label.place(x=300, y=60)

        label=Label(a20,text="Username",
           font=('century gothic', 17, 'bold'),fg='#1A5276',bg='white')
        label.place(x=100,y=220)
        ebb1=Entry(a20,font=('century gothic', 17, 'bold'),bd=1,relief="solid")
        ebb1.place(x=300,y=220,width=200,height=35)
        
        label=Label(a20,text="Email",
           font=('century gothic', 17, 'bold'),fg='#1A5276',bg='white')
        label.place(x=550,y=220)
        ebb2=Entry(a20,font=('century gothic', 17, 'bold'),bd=1,relief="solid")
        ebb2.place(x=750,y=220,width=200,height=35)

        
        label=Label(a20,text="Mobile",
           font=('century gothic', 17, 'bold'),fg='#1A5276',bg='white')
        label.place(x=100,y=320)
        ebb3=Entry(a20,font=('century gothic', 17, 'bold'),bd=1,relief="solid")
        ebb3.place(x=300,y=320,width=200,height=35)
        
        label=Label(a20,text="lead Source ",
           font=('century gothic', 17, 'bold'),fg='#1A5276',bg='white')
        label.place(x=550,y=320)
        data1=StringVar()
        ebb4=ttk.Combobox(a20,textvariable = data1)
        ebb4["values"]=("Website",
                        "Social Media",
                        "Reference")
        ebb4['state']="readonly"
        ebb4.place(x=750,y=320,width=200,height=35)

        label=Label(a20,text="lead owner",
           font=('century gothic', 17, 'bold'),fg='#1A5276',bg='white')
        label.place(x=100,y=420)
        data2=StringVar()
        ebb5=ttk.Combobox(a20,textvariable = data2)
        ebb5["values"]=("Admin1",
                        "Admin2",
                        "Admin3")
        ebb5['state']="readonly"
        ebb5.place(x=300,y=420,width=200,height=35)
        
        label=Label(a20,text="Status ",
           font=('century gothic', 17, 'bold'),fg='#1A5276',bg='white')
        label.place(x=550,y=420)
        data3=StringVar()
        ebb6=ttk.Combobox(a20,textvariable = data3)
        ebb6["values"]=("Registered",
                        "Follow Up",
                        "Not Interest")
        ebb6['state']="readonly"
        ebb6.place(x=750,y=420,width=200,height=35)
        
        label=Label(a20,text="follow up date",
           font=('century gothic', 17, 'bold'),fg='#1A5276',bg='white')
        label.place(x=100,y=520)
        ebb7=Entry(a20,font=('century gothic', 17, 'bold'),bd=1,relief="solid")
        ebb7.place(x=300,y=520,width=200,height=35)
        
        label=Label(a20,text="next followup",
           font=('century gothic', 17, 'bold'),fg='#1A5276',bg='white')
        label.place(x=550,y=520)
        ebb8=Entry(a20,font=('century gothic', 17, 'bold'),bd=1,relief="solid")
        ebb8.place(x=750,y=520,width=200,height=35)

        def lead_store():
           
            if (ebb1.get()=="" or ebb2.get()=="" or ebb3.get()=="" or ebb4.get()=="" or ebb5.get()=="" or ebb6.get()=="" or ebb7.get()=="" or ebb8.get()==""):
                messagebox.showerror("Error", "Enter all details")
            elif (ebb1.get()and ebb2.get() and ebb3.get() and ebb4.get() and ebb5.get() and ebb6.get() and ebb7.get() and ebb8.get()):
                op = messagebox.askyesno("Save", "Do you really want to save?")
                if op > 0:
                    sql_statement="INSERT INTO leadd (name,email,mobile,leadsource, leadowner,statuss,followup_dates,nextfollowup_date) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                    values=(ebb1.get(),ebb2.get(),ebb3.get(),ebb4.get(),ebb5.get(),ebb6.get(),ebb7.get(),ebb8.get())
                    my_database.execute(sql_statement,values)
                    db_connection.commit()
                    messagebox.showinfo("DONE", "Stored Successfully")
 
        b5 = Button(a20,text='Submit',command=lead_store,bg="#1A5276",fg="white",font=("century gothic", 13, "bold"),
                         height="1",width="17",bd=0,highlightthickness=2,padx=10,pady=5)
        b5.place(x=300, y=680)
        b5 = Button(a20,text='back',bg="#1A5276",fg="white",command=a20.destroy,font=("century gothic", 13, "bold"),
                         height="1",width="17",bd=0,highlightthickness=2,padx=10,pady=5)
        b5.place(x=600, y=680)

    def update_lead():
        a21=Frame(a15,bg='white',height=1000,width=1225) #1A5276
        a21.place(x=0,y=0)
        label = Label(a21, text="  U p d a t e  L e a d  D e t a i l s",
                      font=('century gothic', 35, 'bold'), fg="#1A5276", bg='white')
        label.place(x=200, y=60)

        label=Label(a21,text="Username",
        font=('century gothic', 17, 'bold'),fg='#1A5276',bg='white')
        label.place(x=350,y=240)
        ebbb1=Entry(a21,font=('century gothic', 17, 'bold'),bd=1,relief="solid")
        ebbb1.place(x=550,y=240,width=200,height=35)

        label=Label(a21,text="Status ",
        font=('century gothic', 17, 'bold'),fg='#1A5276',bg='white')
        label.place(x=350,y=340)
        data3=StringVar()
        ebbb2=ttk.Combobox(a21,textvariable = data3)
        ebbb2["values"]=("Registered",
                        "Follow Up",
                        "Not Interest")
        ebbb2['state']="readonly"
        ebbb2.place(x=550,y=340,width=200,height=35)
        
        label=Label(a21,text="follow up date",
        font=('century gothic', 17, 'bold'),fg='#1A5276',bg='white')
        label.place(x=350,y=440)
        ebbb3=Entry(a21,font=('century gothic', 17, 'bold'),bd=1,relief="solid")
        ebbb3.place(x=550,y=440,width=200,height=35)
        
        label=Label(a21,text="next followup",
        font=('century gothic', 17, 'bold'),fg='#1A5276',bg='white')
        label.place(x=350,y=540)
        ebbb4=Entry(a21,font=('century gothic', 17, 'bold'),bd=1,relief="solid")
        ebbb4.place(x=550,y=540,width=200,height=35)

        def up_lead():
            if (ebbb1.get()=="" or ebbb2.get()=="" or ebbb3.get()=="" or ebbb4.get()==""):
                messagebox.showerror("Error", "Enter all details")
            elif (ebbb1.get()and ebbb2.get() and ebbb3.get() and ebbb4.get()):
                op = messagebox.askyesno("Save", "Do you really want to save?")
                if op > 0:
                    sql_statement = "UPDATE leadd SET   statuss=%s, followup_dates=%s, nextfollowup_date=%s WHERE name=%s"
                    values=(ebbb2.get(),ebbb3.get(),ebbb4.get(),ebbb1.get())
                    my_database.execute(sql_statement,values)
                    db_connection.commit()
                    messagebox.showinfo("DONE", "Stored Successfully")
        
        b5 = Button(a21,text='Submit',bg="#1A5276",command=up_lead,fg="white",font=("century gothic", 13, "bold"),
                         height="1",width="17",bd=0,highlightthickness=2,padx=10,pady=5)
        b5.place(x=300, y=680)
        b5 = Button(a21,text='back',bg="#1A5276",fg="white",command=a21.destroy,font=("century gothic", 13, "bold"),
                         height="1",width="17",bd=0,highlightthickness=2,padx=10,pady=5)
        b5.place(x=600, y=680)
            
    b5 = Button(a15,text='Add',bg="#1A5276",fg="white",command=add_lead,font=("century gothic", 13, "bold"),
                     height="1",width="17",bd=0,highlightthickness=2,padx=10,pady=5)
    b5.place(x=20, y=690)
    b5 = Button(a15,text='Update',bg="#1A5276",fg="white",command=update_lead,font=("century gothic", 13, "bold"),
                     height="1",width="17",bd=0,highlightthickness=2,padx=10,pady=5)
    b5.place(x=320, y=690)
    b5 = Button(a15,text='Refresh',bg="#1A5276",fg="white",command=leadd,font=("century gothic", 13, "bold"),
                     height="1",width="17",bd=0,highlightthickness=2,padx=10,pady=5)
    b5.place(x=620, y=690)

    b5 = Button(a15,text='Close',bg="#1A5276",fg="white",command=a15.destroy,font=("century gothic", 13, "bold"),
                     height="1",width="17",bd=0,highlightthickness=2,padx=10,pady=5)
    b5.place(x=920, y=690)

    
def admin():
    global a1,a11
    a1=Frame(root,bg='#1A5276',height=1000,width=950) #1A5276
    a1.pack(fill=X)
    a11=Frame(root,bg='white',height=1000,width=600)
    a11.place(x=0,y=0)
    
    img=Image.open('vas2.jpeg')
    img=img.resize((650,800))
    img2=ImageTk.PhotoImage(img)
    imglabel=Label(a11,image=img2,bg="#1A5276")
    imglabel.image=img2
    imglabel.place(x=0,y=0)

    label=Label(a1,text="A d m i n  D a s h b o a r d",
           font=('century gothic', 35, 'bold'),fg="white",bg='#1A5276')
    label.place(x=750,y=60)

    label=Label(a1,text="Login To Access ",
           font=('century gothic', 25, 'bold'),fg="white",bg='#1A5276')
    label.place(x=900,y=200)

    label=Label(a1,text="Username ",
           font=('century gothic', 25, 'bold'),fg="white",bg='#1A5276')
    label.place(x=800,y=318)
    eb1=Entry(a1,font=('century gothic', 17, 'bold'))
    eb1.place(x=1050,y=330,width=220,height=35)

    label=Label(a1,text="Password ",
           font=('century gothic', 25, 'bold'),fg="white",bg='#1A5276')
    label.place(x=800,y=418)
    eb2=Entry(a1,show="*",font=('century gothic', 17, 'bold'))
    eb2.place(x=1050,y=430,width=220,height=35)

    def admin_details():
        user=eb1.get()
        passs=eb2.get()   
        sql="SELECT * from admin_register where name=%s and password=%s"
        my_database.execute(sql,[(user),(passs)])
        result=my_database.fetchall()
        print(result)
        def welcomee():
            custom_message.destroy()
            a11.destroy()
            global a3,a33
            a33=Frame(a1,bg='#1A5276',height=1000,width=325)
            a33.place(x=0,y=0)
            a3=Frame(a1,bg='white',height=1000,width=1225) #1A5276
            a3.place(x=400,y=0)


            img=Image.open('imagee.png')
            img=img.resize((150,150))
            img2=ImageTk.PhotoImage(img)
            imglabel=Label(a33,image=img2,bg="#1A5276")
            imglabel.image=img2
            imglabel.place(x=110,y=20)
            b5 = Button(a33,text='Lead',bg="white",fg="black",command=leadd,font=("century gothic", 13, "bold"),
                     height="1",width="17",bd=0,highlightthickness=2,padx=10,pady=5)
            b5.place(x=90, y=230)
            b5 = Button(a33,text='Students',bg="white",fg="black",font=("century gothic", 13, "bold"),
                     height="1",width="17",bd=0,highlightthickness=2,padx=10,pady=5)
            b5.place(x=90, y=300)
            b5 = Button(a33,text='Faculty',bg="white",fg="black",font=("century gothic", 13, "bold"),
                     height="1",width="17",bd=0,highlightthickness=2,padx=10,pady=5)
            b5.place(x=90, y=370)
            b5 = Button(a33,text='Course',bg="white",fg="black",font=("century gothic", 13, "bold"),
                     height="1",width="17",bd=0,highlightthickness=2,padx=10,pady=5)
            b5.place(x=90, y=440)
            b5 = Button(a33,text='Finance',bg="white",fg="black",font=("century gothic", 13, "bold"),
                     height="1",width="17",bd=0,highlightthickness=2,padx=10,pady=5)
            b5.place(x=90, y=510)
            b5 = Button(a33,text='Placement',bg="white",fg="black",font=("century gothic", 13, "bold"),
                         height="1",width="17",bd=0,highlightthickness=2,padx=10,pady=5)
            b5.place(x=90, y=580)
            b6 = Button(a33,text='Email',bg="#EE8309",fg="white",font=("century gothic", 13, "bold"),
                             height="1",width="12",bd=0,highlightthickness=2,padx=10,pady=5)
            b6.place(x=25, y=700)
            def rem():
                a3.destroy()
                a33.destroy()
            b6 = Button(a33,text='Back',bg="#EE8309",fg="white",command=rem,font=("century gothic", 13, "bold"),
                             height="1",width="12",bd=0,highlightthickness=2,padx=10,pady=5)
            b6.place(x=200, y=700)
        if (eb1.get()=="" or eb2.get()==""):
            messagebox.showerror("Error", "Enter all details")  
        elif(result):

            global custom_message
            custom_message = Toplevel()
            custom_message.title("Greetings")
            custom_message.config(bg="white")
            custom_message_width = 300
            custom_message_height = 200
            screen_width = custom_message.winfo_screenwidth()
            screen_height = custom_message.winfo_screenheight()
            x = (screen_width - custom_message_width) // 2
            y = (screen_height - custom_message_height) // 2
            custom_message.geometry(f"{custom_message_width}x{custom_message_height}+{x}+{y}")
            b5 = Button(custom_message,text='Welcome',command=welcomee,bg="#1A5276",fg="white",font=("century gothic", 11, "bold"),
                     height="1",width="14",bd=0,highlightthickness=2,padx=10,pady=5)
            b5.place(x=80, y=100)
    b5 = Button(a1,text='Login',bg="#26B3E8",fg="white",command=admin_details,font=("century gothic", 13, "bold"),
                     height="1",width="20",bd=0,highlightthickness=2,padx=10,pady=5)
    b5.place(x=900, y=525)

    label=Label(a1,text="Don't Have Account ? ",
           font=('century gothic', 15, 'bold'),fg="white",bg='#1A5276')
    label.place(x=800,y=630)

    b6 = Button(a1,text='Sign In',bg="#EE8309",fg="white",command=admin_signin,font=("century gothic", 13, "bold"),
                     height="1",width="20",bd=0,highlightthickness=2,padx=10,pady=5)
    b6.place(x=1040, y=620)
    def rem():
        a1.destroy()
        a11.destroy()
    b6 = Button(a1,text='Back',bg="white",fg="black",command=rem,font=("century gothic", 13, "bold"),
                     height="1",width="15",bd=0,highlightthickness=2,padx=10,pady=5)
    b6.place(x=1250, y=720)


img=Image.open('imagee.png')
img=img.resize((150,150))
img2=ImageTk.PhotoImage(img)
imglabel=Label(root,image=img2,bg="#1A5276")
imglabel.image=img2
imglabel.place(x=700,y=100)
label=Label(root,text="C R M   S O F T W A R E ",
           font=('century gothic', 45, 'bold'),fg="white",bg='#1A5276')
label.place(x=480,y=280)
label=Label(root,text="P o w e r e d    B y  I m a g e c o n",
           font=('century gothic',25, 'bold'),fg="white",bg='#1A5276')
label.place(x=530,y=370)
btn_next = Button(root, text='GET STARTED', bg="white", fg="#1A5276", command=admin, font=("Times New Roman", 20, "bold"),
       height="2", width="25", bd=2, highlightthickness=5, padx=10, pady=5, highlightbackground="#1CA8D6")
btn_next.place(x=550, y=550)

root.mainloop()
