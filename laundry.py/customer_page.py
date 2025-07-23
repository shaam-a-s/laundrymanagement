from tkinter import *
import json
from tkinter import ttk,messagebox
# from front_page import Front_Page

class Customer_Page:
    def __init__(self):
        self.u_id=None
        self.name=""
        self.cont=None
        self.order_id=None
        self.type=None
        self.delivery_date=''
        self.order_date=''
        self.payment_st=""
        self.delivery_st=''
        self.total_cost=0
        self.c_cost=0
        self.c_wds= False
    def get_info(self):
        with open("data.json","r") as file:
            content=json.load(file)
        if self.u_id in content.keys():
            self.name=content[self.u_id]['name']
            self.cont = content[self.u_id]['contact']
            self.order_id=content[self.u_id]['order_id']
            self.type=content[self.u_id]['type']
            self.total_cost=content[self.u_id]['Total']
            self.payment_st=content[self.u_id]['payment']
            self.delivery_st=content[self.u_id]['delivery']
            self.delivery_date=content[self.u_id]['Delivary_Date']
            self.order_date = content[self.u_id]['Date']
            print(self.name)

        else:
            messagebox.showerror("Error", "Unique ID not found")



    def create(self,uid):
        self.u_id=uid
        self.get_info()
        self.wds=Tk()
        self.c_wds=True
        self.wds.title(f"WELCOME {self.name}")
        self.wds.geometry("800x600")
        self.canvas = Canvas(width=800, height=600)
        self.img_2=PhotoImage(file="picture-2.png")
        self.canvas.create_image(400,300,image=self.img_2)
        self.canvas2=Canvas(width=500, height=550)
        self.canvas2.config(background="#0ABAB5")
        self.canvas2.create_text(250,30,text=f"Welcome {self.name.title()} to Bharathi laundry services",font=("bold",15),fill="white")
        self.canvas2.create_text(250,60,text="Address : 45,Venkatramana street,pollachi,642001",font=("bold",14),fill="white")
        self.canvas2.create_text(230,90,text="G-Mail : sekarlaundry1234@gmail.com",font=("bold",15),fill="white")
        self.canvas2.create_text(230,120,text="Contact no :6546535425",font=("bold",15),fill="white")
        self.canvas.place(x=0, y=0)
        self.canvas2.place(x=150,y=20)
        self.canvas2.create_text(100,180,text="Your order Details :",font=("Bebas Neue",17),fill="white")
        self.canvas2.create_text(120,220,text="CLICK HERE TO VIEW →",font=("Arial",15),fill="white")

        self.view_button=Button(text="VIEW",width=10,command=self.view,font=("Bold",10))
        self.view_button.config(bg="white",foreground="#0ABAB5")
        self.view_button.place(x=405,y=230)

        self.back_button=Button(text="Log out",width=10,command=self.log_out,font=("Bold",10))
        self.back_button.config(bg="white",foreground="#0ABAB5")
        self.back_button.place(x=170,y=530)







        self.wds.mainloop()
    def view(self):
        self.v_window=Toplevel()
        self.v_window.geometry("400x565")
        self.v_window.title("__ YOUR ORDER __")
        self.v_window.config(background="white")
        self.odate=Label(self.v_window,text=f" Order Date : {self.order_date}",padx=2,background="white",font=("Bold",14))
        self.odate.place(x=10,y=0)
        self.ddate=Label(self.v_window,text=f" Delivery Date : {self.delivery_date}",padx=2,background="white",font=("Bold",14))
        self.ddate.place(x=10,y=30)
        self.ord_id=Label(self.v_window,text=f" Order ID : {self.order_id}",padx=2,background="white",font=("Bold",14))
        self.ord_id.place(x=10,y=120)

        self.un_id=Label(self.v_window,text=f" Unique ID : {self.u_id}",padx=2,background="white",font=("Bold",14))
        self.un_id.place(x=10,y=90)
        self.cm_name=Label(self.v_window,text=f" Name : {self.name}",padx=2,background="white",font=("Bold",14))
        self.cm_name.place(x=10,y=60)
        self.ord_id=Label(self.v_window,text=f" Order ID : {self.order_id}",padx=2,background="white",font=("Bold",14))
        self.ord_id.place(x=10,y=120)
        self.ord_tot=Label(self.v_window,text=f" Total : {self.total_cost}",padx=2,background="white",font=("Bold",14))
        self.ord_tot.place(x=10,y=380)
        self.ord_tot=Label(self.v_window,text=f" Payment : {self.payment_st}",padx=2,background="white",font=("Bold",14))
        self.ord_tot.place(x=10,y=410)
        self.ord_tot=Label(self.v_window,text=f" Delivery : {self.delivery_st}",padx=2,background="white",font=("Bold",14))
        self.ord_tot.place(x=10,y=440)




        trv = ttk.Treeview(self.v_window, selectmode='browse')
        trv.place(x=40, y=150)

        # number of columns
        trv["columns"] = ("1", "2", "3", "4")

        # Defining heading
        trv['show'] = 'headings'
        self.v_window.config(background="white")
        trv.column("1", width=80, anchor='c')
        trv.column("2", width=80, anchor='c')
        trv.column("3", width=80, anchor='c')
        trv.column("4", width=80, anchor='c')

        trv.heading("1", text="Type")
        trv.heading("2", text="Laundary Type")
        trv.heading("3", text="Quantity")
        trv.heading("4", text="Cost")
        for dt in self.type:
            trv.insert("", 'end',
                       values=(dt[0], dt[2], dt[1], dt[3]))
    def log_out(self):
        if self.c_wds:
            self.wds.destroy()
        from front_page import Front_Page

        fp=Front_Page()
        fp.create()












# c=Customer_Page("4787d6f6")
# c.get_info()
# c.create()





