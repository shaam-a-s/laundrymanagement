import random
from tkinter import *
from tkinter import ttk
from datetime import date,timedelta
import csv
import json
from mail import *




class TransactionSlip:
    def __init__(self):

        self.date =date.today()
        self.dd=self.date+timedelta(days=2)
        self.data={}
        self.unique_id=0
        self.name=""
        self.contact=0
        self.l_type=None
        self.quantity=0
        self.q_total=0
        self.cost=0
        self.total=0
        self.order_id=self.Orderid()
        self.material=[]
        self.w=False
        self.gmail=''

    def Orderid(self):
        rd=""
        for i in range(4):
            rd+=str(random.randint(0,9))
        return rd

    def store_data(self):
        self.coutomer_data={self.unique_id:{"name":self.name,"contact no":self.contact,}}

        return print(self.coutomer_data)

    def next(self):
        # self.coutomer_data[self.unique_id]["type"] = self.material
        # self.coutomer_data[self.unique_id]["Total"] = self.total
        # self.coutomer_data[self.unique_id]["Total Cloths"] = self.q_total
        # self.coutomer_data[self.unique_id]["Date"] = self.date
        # self.coutomer_data[self.unique_id]["order id"] = self.order_id
        # self.coutomer_data[self.unique_id][" Delivary Date"] = self.dd

        try:
            with open("data.json", "r") as file:
                content = json.load(file)
        except json.decoder.JSONDecodeError:
            content = {}

        if self.unique_id in content:
            content[self.unique_id]["type"]=self.material
            content[self.unique_id]["name"]=self.name
            content[self.unique_id]["contact"] = self.contact
            content[self.unique_id]["order_id"] = self.order_id
            content[self.unique_id]["Total Cloths"] = self.q_total
            content[self.unique_id]["Total"] = self.total
            content[self.unique_id]["Date"] = str(self.date)
            content[self.unique_id]["Delivary_Date"] = str(self.dd)
            content[self.unique_id]["payment"] = "pending"
            content[self.unique_id]["delivery"] = "pending"
            content[self.unique_id]["priority"] = "Low"



        else:
            content[self.unique_id] = {
                "name": self.name,
                "contact": self.contact,
                "order_id": self.order_id,
                "type": self.material,
                "Total Cloths":self.q_total,
                "Total": self.total,
                "Date":str(self.date),
                "Delivary_Date" : str(self.dd),
                "payment":"pending",
                "delivery":"pending",
                "priority": "Low"

            }

        with open("data.json", "w") as file:
            json.dump(content, file)

        print(self.data)
        mail(self.unique_id,self.order_id,self.dd,self.total)
        self.slip()

    def price(self):
        if self.l_type in ["only wash","dry wash","iron"]:
            self.cost=7*int(self.quantity)
            self.total+=self.cost
            return self.cost
        elif self.l_type in ["wash and dry"]:
            self.cost=10*int(self.quantity)
            self.total+=self.cost
            return self.cost
        elif self.l_type in ["wash,dry and iron"]:
            self.cost=15*int(self.quantity)
            self.total += self.cost
            return self.cost
    def view_id(self):
        self.id_window=Tk()
        self.id_window.geometry("200x200")

        with open("customers.csv","r") as file:
            content=file.readlines()
        trv = ttk.Treeview(self.id_window, selectmode='browse')
        trv.pack()

        # number of columns
        trv["columns"] = ("1", "2")

        # Defining heading
        trv['show'] = 'headings'
        self.id_window.config(background="white")
        trv.column("1", width=80, anchor='c')
        trv.column("2", width=80, anchor='c')

        trv.heading("1", text="id")
        trv.heading("2", text="Name")
        for i in content:
            s = i.split(",")
            if s[0]=="id":
                pass
            else:
                trv.insert("", 'end',
                       values=(s[0], s[1]))
        self.id_window.mainloop()








    def ts_slip(self):
        if self.w==True:
            self.q_total=0
            self.total=0
            self.ws.destroy()

        self.window=Tk()
        #t=Table()
        self.window.title("__TRANSACTION__")
        self.window.geometry("800x600")
        self.canvas = Canvas(width=800,height=600)
        self.img_2=PhotoImage(file="picture-2.png")
        self.canvas.create_image(400,300,image=self.img_2)
        self.canvas.create_text(380,48,text="Transaction Slip",font=("Arial",24),fill="coral")
        self.canvas.create_text(200,90,text="UNIQUE ID :",font=("Arial",18,"bold"),fill="black")
        self.canvas.create_text(200,123,text="NAME :",font=("Arial",18,"bold"),fill="black")
        self.canvas.create_text(200,153,text="G mail :",font=("Arial",18,"bold"),fill="black")
        self.canvas.config(bg="cyan")
        self.canvas.place(x=0,y=0)


        self.entry_1=Entry(width=35)
        self.entry_1.place(x=300,y=83)
        # n = StringVar()
        self.entry_2=Entry(width=35)
        self.entry_2.place(x=300,y=116)
        self.entry_3=Entry(width=35)
        self.entry_3.place(x=300,y=149)


        self.button=Button(text="NEXT",width=10,command=self.next)
        self.button.config(background="coral")
        self.button.place(x=700,y=550)

        self.view_b=Button(text="View",width=7,command=self.view_id)
        self.view_b.config(background="coral")
        self.view_b.place(x=520,y=80)

        # ws = Tk()
        # ws.geometry('800x600')
        # ws['bg'] = '#AC99F2'
        self.scroll_bar = Frame(self.window)
        self.scroll_bar.place(x=120,y=200)
        # scrollbar
        self.scroll = Scrollbar(self.scroll_bar)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.set = ttk.Treeview(self.scroll_bar, yscrollcommand=self.scroll.set)

        self.set.pack(side="bottom")

        self.scroll.config(command=self.set.yview)
        # scroll.config(command=set.xview)

        self.set['columns'] = ('S.no', 'Type', 'Laundary Type','Quantity', 'Cost')
        self.set.column("#0", width=0, stretch=NO)
        self.set.column("S.no", anchor=CENTER, width=100)
        self.set.column("Type", anchor=CENTER, width=100)
        self.set.column("Laundary Type", anchor=CENTER, width=100)
        self.set.column("Quantity", anchor=CENTER, width=100)
        self.set.column("Cost", anchor=CENTER, width=100)
        #self.set.column("Delivery Date", anchor=CENTER, width=100)

        self.set.heading("#0", text="", anchor=CENTER)
        self.set.heading("S.no", text="S.No", anchor=CENTER)
        self.set.heading("Type", text="Type", anchor=CENTER)
        self.set.heading("Laundary Type", text="Laundary Type", anchor=CENTER)
        self.set.heading("Quantity", text="Quantity", anchor=CENTER)
        self.set.heading("Cost", text="Cost", anchor=CENTER)

        self.Input_frame = Frame(self.window)
        self.Input_frame.place(x=130,y=450)

        self.s_no = Label(self.Input_frame, text="S.No")
        self.s_no.grid(row=0, column=0)

        self.Type = Label(self.Input_frame, text="Type")
        self.Type.grid(row=0, column=1)

        self.Laundary_Type = Label(self.Input_frame, text="Laundary Type")
        self.Laundary_Type.grid(row=0, column=2)

        self.quantity = Label(self.Input_frame, text="Quantity")
        self.quantity.grid(row=0, column=3)


        self.s_no_entry = Entry(self.Input_frame)
        self.s_no_entry.grid(row=1, column=0)


        self.Type_entry =  Entry(self.Input_frame)
        self.Type_entry.grid(row=1, column=1)

        n = StringVar()
        self.Laundary_Type_entry =  ttk.Combobox(self.Input_frame, width=15, textvariable=n,background="white")
        self.Laundary_Type_entry['values'] = ("only wash","dry wash","iron","wash and dry", "wash,dry and iron")
        self.Laundary_Type_entry.grid(row=1, column=2)

        self.quantity_entry = Entry(self.Input_frame)
        self.quantity_entry.grid(row=1, column=3)

        # Delivery_entry = Entry(Input_frame)
        # Delivery_entry.grid(row=1, column=4)
        # button
        self.Input_button = Button(self.window, width=10, text="add", command=self.input_record)
        self.Input_button.config(background="coral")
        self.Input_button.place(x=10, y=550)
        self.window.mainloop()



    def input_record(self):
        # global count
        s_no_inp = self.s_no_entry.get()
        matl = self.Type_entry.get()

        Laundary_Type_inp = self.Laundary_Type_entry.get()
        self.l_type=Laundary_Type_inp

        quantity_inp=self.quantity_entry.get()
        self.quantity=quantity_inp
        self.q_total+=int(self.quantity)

        inp1 = self.entry_1.get()
        with open("customers.csv", newline='') as csvfile:
            # Create a CSV reader
            reader = csv.DictReader(csvfile)

            # Iterate over each row in the CSV file
            for row in reader:
                # Check if the 'id' column matches the target ID
                if str(row['id']) == inp1:
                    # Return the name associated with the target ID
                    self.name=str(row['name'])
                    self.contact=str(row['phone'])

        self.unique_id = inp1

        inp3 = self.entry_3.get()
        self.gmail = inp3


        self.set.insert(parent='', index='end', text='', values=(s_no_inp, matl,
                                                                 Laundary_Type_inp,quantity_inp,self.price()))
        self.material.append([matl,self.quantity,self.l_type,self.cost])
        self.store_data()
        self.s_no_entry.delete(0, END)
        self.Type_entry.delete(0, END)
        self.Laundary_Type_entry.delete(0, END)
        self.Type_entry.delete(0, END)
        self.quantity_entry.delete(0, END)
        # Delivery_entry.delete(0, END)
    def slip(self):
        self.window.destroy()
        self.w=True
        self.ws=Tk()
        self.ws.title("__TRANSACTION Slip__")
        self.ws.geometry("400x565")
        self.canvas=Canvas(width=400,height=565)
        self.img_1=PhotoImage(file="pic-1.png")
        self.canvas.create_image(200,280,image=self.img_1)
        g=f"{self.name}@gmail.com"

        self.shop_name=Label(text="Bharathi laundry services",padx=2,background="white",fg="black",font=("Bernard MT Condensed",18))
        self.shop_name.place(x=80,y=40)
        self.s_address=Label(text="Address : 45,Venkatramana street,pollachi,642001",padx=2,background="white",fg="black",font=("Ariel",10))
        self.s_address.place(x=45,y=80)
        self.s_gmail=Label(text="G-Mail : sekarlaundry1234@gmail.com",padx=2,background="white",fg="black",font=("Ariel",10))
        self.s_gmail.place(x=45,y=100)
        self.s_phone=Label(text="Contact no : 6546535425",padx=5,background="white",fg="black",font=("Ariel",10))
        self.s_phone.place(x=44,y=120)


        self.tdate=Label(text=f"Date : {self.date}",padx=2,background="white",fg="black",font=("Ariel",10))
        self.tdate.place(x=240,y=200)
        self.c_detial=Label(text="Client Details :",padx=2,background="white",fg="black",font=("Bernard MT Condensed",20))
        self.c_detial.place(x=120,y=160)
        self.c_name=Label(text=f" Name : {self.name}",padx=2,background="white",fg="black",font=("Ariel",10))
        self.c_name.place(x=43,y=200)
        self.c_id=Label(text=f" Unique ID : {self.unique_id}",padx=2,background="white",fg="black",font=("Ariel",10))
        self.c_id.place(x=43,y=220)
        self.c_phone=Label(text=f"Phone no: {self.contact}",padx=2,background="white",fg="black",font=("Ariel",10))
        self.c_phone.place(x=45,y=240)
        self.c_gmail=Label(text=f"G-mail: {self.gmail}",padx=2,background="white",fg="black",font=("Ariel",10))
        self.c_gmail.place(x=45,y=260)

        self.orderid=Label(text=f"order No : {self.order_id}",padx=2,background="white",fg="black",font=("Ariel",10))
        self.orderid.place(x=45,y=280)

        self.c_total_items=Label(text=f"Total Items : {self.q_total}",padx=2,background="white",fg="black",font=("Ariel",10))
        self.c_total_items.place(x=45,y=300)
        self.c_total=Label(text=f"Total : ₹ {self.total}",padx=2,background="white",fg="black",font=("Ariel",10))
        self.c_total.place(x=45,y=320)
        # today = date.today()
        self.d_date=Label(text=f" Delivary Date : ₹ {self.dd}",padx=2,background="white",fg="black",font=("Ariel",10))
        self.d_date.place(x=42,y=340)
        self.button1=Button(text="NEXT",width=10,command=self.home)
        self.button1.config(background="black",fg="white")
        self.button1.place(x=240,y=450)
        self.button2 = Button(text="NEXT", width=10, command=self.ts_slip)
        self.button2.config(background="black", fg="white")






        self.canvas.place(x=0,y=0)
        self.canvas.config(background="grey")
        self.ws.mainloop()
    def home(self):
        self.ws.destroy()
        from admin import Admin
        ad=Admin()
        ad.admin_page()



#
# ts=TransactionSlip()
# # ts.view_id()
#
#
# ts.ts_slip()
