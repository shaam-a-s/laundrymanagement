from tkinter import *
# from PIL import ImageTk, Image
from tkinter import messagebox
from transaction import TransactionSlip

from customer_module import *
from order_status import OrderStatus
from report import *
# from front_page import Front_Page

class Admin(TransactionSlip):
    def __init__(self):
        self.a_window=False
        super().__init__()

    def cm_module(self):
        if self.w.winfo_exists():
            self.w.destroy()
        customer_manager = CustomerManager()
        root = tk.Tk()
        app = CustomerApp(root, customer_manager)
        root.mainloop()

    def admin_page(self):
        self.w = Tk()
        self.a_window=True
        self.w.title("Admin page")
        self.w.geometry("1320x800")


        #window.resizable(False,False)

         # Load and display the image
        # image = Image.open("machine.jpg")
        # image = image.resize((800, 650))
        # image_tk = ImageTk.PhotoImage(image)

        # label = Label(window, image=image_tk)
        # label.image = image_tk  # Keep a reference to the image to prevent garbage collection
        # label.place(x=0, y=0)

        # Right Frame
        self.right_frame = Frame(self.w,bg="#785E3B")
        self.right_frame.place(x=750, y=0, width=600, height=900)

        #Welcome label
        self.welcome_label=Label(self.right_frame,text="Welcome!",fg="#EFE6DD", bg="#785E3B", font=("times roman",31,"bold"))
        self.welcome_label.place(x=90, y=50)
        # Shop Name Label
        self.shop_name_label = Label(self.right_frame, text="Bharathi Laundry", fg="#EFE6DD", bg="#785E3B", font=("times roman",31,"bold"))
        self.shop_name_label.place(x=120, y=110)

        # Adding buttons to the right frame
        self.button1 = Button(self.right_frame, text="Customer",bg="#EFE6DD", fg="#785E3B", font=("times roman",20),command=self.cm_module)
        self.button2 = Button(self.right_frame, text="Transaction",bg="#EFE6DD", fg="#785E3B", font=("times roman",20),command=self.exist_1)
        self.button3 = Button(self.right_frame, text="Order Status",bg="#EFE6DD", fg="#785E3B", font=("times roman",20),command=self.exist_2)
        self.button4 = Button(self.right_frame, text="Report",bg="#EFE6DD", fg="#785E3B", font=("times roman",20),command=self.exist_3)
        self.button_l=Button(self.right_frame, text="Log Out",bg="#EFE6DD", fg="#785E3B", font=("times roman",20),command=self.log_out)
        self.button1.place(x=140, y=210, width=250,height=55)
        self.button2.place(x=140, y=290, width=250,height=55)
        self.button3.place(x=140, y=370, width=250,height=55)
        self.button4.place(x=140, y=450, width=250,height=55)
        self.button_l.place(x=140, y=550, width=250, height=55)
        self.w.mainloop()
    def exist_1(self):
        if self.w.winfo_exists():
            self.w.destroy()
            super().ts_slip()
    def exist_2(self):
        if self.w.winfo_exists():
            self.w.destroy()
            ord=OrderStatus()
            return ord
    def exist_3(self):
        if self.w.winfo_exists():
            self.w.destroy()
            root = Tk()
            gui=GUI(root)
            return gui
    def log_out(self):
        if self.a_window == True:
            self.w.destroy()
            self.a_window=False
        from front_page import Front_Page
        # front = Front_Page()
        # front.create()

# ad=Admin()
# ad.admin_page()

