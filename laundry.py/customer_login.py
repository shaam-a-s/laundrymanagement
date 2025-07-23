from tkinter import *
#from PIL import ImageTk, Image
from tkinter import messagebox
from subprocess import call
import json

# from front_page import *


class C_Login:
    def __init__(self):
        self.root1 = Tk()
        self.root1.title("Login")
        self.root1.geometry("1000x600")
    def create(self):
 # Set a default size for the window

        # Setting background image for window
        # img = Image.open("loginimage.jpg")
        # img = img.resize((1280, 650))  # Resize the image to fit the window
        # photo = ImageTk.PhotoImage(img)
        # background_label = Label(root, image=photo)
        # background_label.image = photo
        # background_label.pack(fill=BOTH, expand=YES)

        # Centre frame
        self.centreframe = Frame(self.root1, bg="#0ABAB5")
        self.centreframe.place(relx=.5, rely=.5, anchor=CENTER, width=350, height=450)

        # Logo image
        # img_1 = Image.open("file.png")
        # img_1 = img_1.resize((80, 80))
        # photo_1 = ImageTk.PhotoImage(img_1)
        # logo_label = Label(centreframe, image=photo_1)
        # logo_label.image = photo_1
        # logo_label.place(x=135, y=30)

        # Username label
        self.username_label = Label(self.centreframe, text="UNIQUE ID", fg="#EFE6DD", bg="#0ABAB5", font=("times roman", 12, "bold"))
        self.username_label.place(x=30, y=130)

        # Username entry
        self.username_entry = Entry(self.centreframe, width=25, fg="#EFE6DD", border=0, bg="#0ABAB5", font=("times roman", 13))
        self.username_entry.place(x=30, y=170)

        # Line under username entry
        self.username_canvas = Canvas(self.centreframe, width=280, height=2, bg="white", highlightthickness=0)
        self.username_canvas.place(x=30, y=190)

        # # Password label
        # password_label = Label(centreframe, text="Password", fg="#EFE6DD", bg="#785E3B", font=("times roman", 12,"bold"))
        # password_label.place(x=30, y=230)
        #
        # # Password entry
        # password_entry = Entry(centreframe, width=25, fg="#EFE6DD", border=0, bg="#785E3B", font=("times roman", 13), show="*")
        # password_entry.place(x=30, y=270)

        # # Line under password entry
        # password_canvas = Canvas(centreframe, width=280, height=2, bg="#EFE6DD", highlightthickness=0)
        # password_canvas.place(x=30, y=290)

        # Submit button
        self.submit_button = Button(self.centreframe, text="Login", fg="#785E3B", bg="#EFE6DD", font=("times roman", 12), width=15,
                               command=self.validate_login)
        self.submit_button.place(x=100, y=330)

        self.root1.mainloop()



    def validate_login(self):
        userid = self.username_entry.get()
        #password = password_entry.get()
        ids=[]
        with open("data.json","r") as file:
            json_data = json.load(file)
        for i in json_data.keys():
            ids.append(i)
        # You can add your own validation logic here
        if userid in ids :
            self.customer_p(userid)

        else:
            messagebox.showerror("Login Failed","Invalid username or password")
    def customer_p(self,ud):
        from customer_page import Customer_Page
        cp = Customer_Page()
        self.root1.destroy()
        cp.create(ud)

# c=C_Login()
# c.create()