from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
import mysql.connector
import keys

mydb = mysql.connector.connect(host="localhost", user="root", password="Putznslqc4", database = "fasttag")

mycursor = mydb.cursor()







class FastTag_Generator:
    mydb = mysql.connector.connect(host="localhost", user="root", password="Putznslqc4", database="fasttag")

    mycursor = mydb.cursor()
    def __init__(self, root):

         self.root=root
         self.root.geometry("900x600+200+50")
         self.root.title("Fast Tag Generator")
         self.root.resizable(False,False)

         title = Label(self.root,text='   FastTagGenerator',font=('times new roman',40), bg="#053246",fg='white',anchor='w').place(x=0,y=0,relwidth=1)

         self.var_Owner=StringVar()
         self.var_VehicleNo = StringVar()
         self.var_Mobile = IntVar()
         self.var_VehicleType = StringVar()

         vehicle_frame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
         vehicle_frame.place(x=50,y=100,width=500,height=380)
         title = Label(vehicle_frame, text='   Vehicle Details', font=('goudy old style', 20), bg="#053246", fg='white' ).place(x=0, y=0, relwidth=1)

         Vehicle_Owner = Label(vehicle_frame, text=' Owner  Name', font=('goudy old style', 15,'bold'), bg="white",
                       ).place(x=10, y=60)
         Vehicle_No = Label(vehicle_frame, text=' Vehicle No', font=('goudy old style', 15, 'bold'), bg="white",
                               ).place(x=10, y=100)
         Mobile_No = Label(vehicle_frame, text=' Mobile  No', font=('goudy old style', 15, 'bold'), bg="white",
                               ).place(x=10, y=140)
         Vehicle_Type = Label(vehicle_frame, text=' Vehicle Type', font=('goudy old style', 15, 'bold'), bg="white",
                           ).place(x=10, y=200)

         Entry_Vehicle_Owner = Entry(vehicle_frame, font=('goudy old style', 15 ),textvariable=self.var_Owner, bg="lightyellow",
                               ).place(x=200, y=60)
         Entry_Vehicle_No = Entry(vehicle_frame,textvariable=self.var_VehicleNo, font=('goudy old style', 15), bg="lightyellow",
                            ).place(x=200, y=100)
         Entry_Mobile_No = Entry(vehicle_frame, font=('goudy old style', 15),textvariable=self.var_Mobile, bg="lightyellow",
                           ).place(x=200, y=140)
         Entry_Vehicle_Type = Entry(vehicle_frame, font=('goudy old style', 15), textvariable=self.var_VehicleType,bg="lightyellow",
                                 ).place(x=200, y=200)

         btn_generate = Button(vehicle_frame,text='GENERATE',command=self.generate,font=('time new roman',18,'bold'),bg='#2196f3',fg='white').place(x=90,y=250,width=180,height=30)
         btn_clear = Button(vehicle_frame, text='CLEAR',command=self.clear, font=('time new roman', 18, 'bold'), bg='#607d8b',
                               fg='white').place(x=280, y=250, width=120, height=30)

         self.msg=''
         self.lbl_msg=Label(vehicle_frame, text=self.msg, font=('times new roman', 20), bg="white",fg='green'
                               )
         self.lbl_msg.place(x=0, y=310,relwidth=1)

         FastTag_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
         FastTag_frame.place(x=600, y=100, width=250, height=380)
         title = Label(FastTag_frame, text='   FastTagCode', font=('goudy old style', 20), bg="#053246",
                       fg='white').place(x=0, y=0, relwidth=1)


         self.fasttag = Label(FastTag_frame,text='FastTag\n Not Generated',font=('times new roman',15),bg='#3f51b5',fg='white')
         self.fasttag.place(x=35,y=100,width=180,height=180)

    def clear(self):
        self.var_Owner.set('')
        self.var_VehicleNo.set('')
        self.var_Mobile.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.fasttag.config(image='')
        self.var_VehicleType.set('')


    def generate(self):




         if self.var_Mobile.get()=='' or self.var_Owner.get()== ''or self.var_VehicleNo.get()=='':
             self.msg='All Fields are Required'
             self.lbl_msg.config(text=self.msg,fg='red')


         else:

             mydb = mysql.connector.connect(host="localhost", user="root", password="Putznslqc4", database="fasttag")

             mycursor = mydb.cursor()




             fasttag_data=(f'{self.var_Owner.get()}%{self.var_VehicleNo.get()}%{self.var_Mobile.get()}%{self.var_VehicleType.get()}')
             fasttag_code=qrcode.make(fasttag_data)
             #print(qr_code)
             fasttag_code=resizeimage.resize_cover(fasttag_code,[180,180])
             fasttag_code.save("FastTags/fasttag_"+str(self.var_VehicleNo.get())+' .png')
             #location = "C:/Users/strud/PycharmProjects/pythonProject/FastTags/fasttag_"+str(self.var_VehicleNo.get())+' .png'
             load_file = f"load_file('C:/Users/strud/PycharmProjects/pythonProject/FastTags/fasttag_{self.var_VehicleNo.get()}.png')"

             mycursor.execute("insert into vehicle values (%s,%s,%s,%s);",(int(self.var_Mobile.get()),self.var_Owner.get(),self.var_VehicleType.get(),self.var_VehicleNo.get()))
             mydb.commit()
             mycursor.execute("insert into fasttag (vehicleno,FastTagCode) values (%s,%s);",(self.var_VehicleNo.get(),load_file))
             mydb.commit()





             self.im=ImageTk.PhotoImage(file="FastTags/fasttag_"+str(self.var_VehicleNo.get())+' .png')
             self.fasttag.config(image=self.im)


             self.msg = 'FastTag Generated'
             self.lbl_msg.config(text=self.msg, fg='green')




root = Tk()
obj = FastTag_Generator(root)
root.mainloop()
