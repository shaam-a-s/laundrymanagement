from tkinter import *
from customer_login import C_Login
# from customer_page import Customer_Page
from login import User_login

class Front_Page:
    def __init__(self):
       pass

    def create(self):
            self.root=Tk()
            self.root.geometry("612x333")
            self.canvas=Canvas(width=612,height=333)
            self.image_path=PhotoImage(file="pic-4.png")
            self.canvas.create_image(306,166,image=self.image_path)
            self.canvas.place(x=0,y=0)
            self.w=Label(self.root,text="LAUNDRY SERVICE",width=30,height=2,font=("Arial",24))
            self.w.pack()

            self.root.title("LOG IN ")
            self.button2 = Button(text="USER", width=30, height=3, command=self.user_page)
            self.button3 = Button(text="CUSTOMER", width=30, height=3, command=self.c_page)

            self.button2.config(background="white")
            self.button3.config(background="white")

            self.button2.place(x=200, y=100)
            self.button3.place(x=200, y=180)

            self.root.mainloop()

    def c_page(self):
        if self.root.winfo_exists():
            self.root.destroy()
            cl=C_Login()
            cl.create()
    def user_page(self):

        if self.root.winfo_exists():
            self.root.destroy()
        ul=User_login()
        ul.create_w()

fp=Front_Page()
fp.create()
