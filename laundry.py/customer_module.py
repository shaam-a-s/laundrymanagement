import tkinter as tk
from tkinter import ttk, messagebox
#from PIL import Image, ImageTk
import csv
import uuid

# Define Customer classes
class Customer:
    def __init__(self, name, phone, address, item=None, id=None):
        self.id = id if id else str(uuid.uuid4())[:8]
        self.name = name
        self.phone = phone
        self.address = address
        self.item = item if item is not None else []

class CustomerNode:
    def __init__(self, customer):
        self.customer = customer
        self.next = None

class CustomerManager:
    def __init__(self, csv_file='customers.csv'):
        self.head = None
        self.csv_file = csv_file
        self.load_customers()

    def add_customer(self, name, phone, address):
        customer = Customer(name, phone, address)
        new_node = CustomerNode(customer)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.save_customers()
        return customer

    def view_customers(self):
        customers = []
        current = self.head
        while current:
            customers.append({
                "id": current.customer.id,
                "name": current.customer.name,
                "phone": current.customer.phone,
                "address": current.customer.address,

            })
            current = current.next
        return customers

    def get_customer_by_name(self, customer_name):
        current = self.head
        while current:
            if current.customer.name == customer_name:
                return current.customer
            current = current.next
        return None

    def update_customer(self, customer_name, new_phone=None, new_address=None):
        current = self.head
        while current:
            if current.customer.name == customer_name:
                if new_phone:
                    current.customer.phone = new_phone
                if new_address:
                    current.customer.address = new_address
                self.save_customers()
                return True
            current = current.next
        return False

    def remove_customer(self, customer_name):
        if not self.head:
            return False
        if self.head.customer.name == customer_name:
            self.head = self.head.next
            self.save_customers()
            return True
        prev = self.head
        current = self.head.next
        while current:
            if current.customer.name == customer_name:
                prev.next = current.next
                self.save_customers()
                return True
            prev = current
            current = current.next
        return False

    def save_customers(self):
        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["id", "name", "phone", "address", ])
            current = self.head
            while current:
                writer.writerow([
                    current.customer.id,
                    current.customer.name,
                    current.customer.phone,
                    current.customer.address,

                ])
                current = current.next

    def load_customers(self):
        try:
            with open(self.csv_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    customer = Customer(
                        name=row['name'],
                        phone=row['phone'],
                        address=row['address'],
                        id=row['id']
                    )
                    new_node = CustomerNode(customer)
                    if not self.head:
                        self.head = new_node
                    else:
                        current = self.head
                        while current.next:
                            current = current.next
                        current.next = new_node
        except FileNotFoundError:
            pass

# Define the main application
class CustomerApp:
    def __init__(self, root, customer_manager):
        self.root = root
        self.customer_manager = customer_manager
        self.root.title("Customer Management System")
        self.root.geometry("1560x850")
    
        
        # Set the background image
        # self.bg_image = Image.open("background.jpg")
        # self.bg_image = self.bg_image.resize((1540, 840))
        # self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        # self.bg_label = tk.Label(root, image=self.bg_photo)
        # self.bg_label.place(relwidth=1, relheight=1)
        #
        # self.frames = {}

        self.create_main_menu()
    def exist_1(self):
        from admin import Admin
        if self.root.winfo_exists():
            self.root.destroy()

            ad = Admin()
            ad.admin_page()

    def create_main_menu(self):
        self.main_menu_frame = tk.Frame(self.root, bg="#785E3B", bd=5)
        self.main_menu_frame.place(relx=0.5, y=180, width=700, height=500, anchor="n")

        heading = tk.Label(self.main_menu_frame, text='Customer Management System', bg="#785E3B",fg='#EFE6DD', font=("times roman", 20, "bold"))
        heading.place(relx=0.15, y=70, width=500, height=100)

        self.add_customer_button = tk.Button(self.main_menu_frame, text="Add Customer",bg="#EFE6DD",fg='#785E3B', font=("times roman", 14, "bold"), command=self.show_add_customer_frame)
        self.add_customer_button.place(relx=0.3, y=210, width=280, height=50)

        self.view_customer_button = tk.Button(self.main_menu_frame, text="View Customers",bg="#EFE6DD",fg='#785E3B', font=("times roman", 14, "bold"), command=self.show_view_customer_frame)
        self.view_customer_button.place(relx=0.3, y=280, width=280, height=50)

        self.update_customer_button = tk.Button(self.main_menu_frame, text="Update Customer",bg="#EFE6DD",fg='#785E3B', font=("times roman", 14, "bold"), command=self.show_update_customer_frame)
        self.update_customer_button.place(relx=0.3, y=350, width=280, height=50)

        self.home_button = tk.Button(self.main_menu_frame, text="Back",bg="#EFE6DD",fg='#785E3B', font=("times roman", 14, "bold"), command=self.exist_1)
        self.home_button.place(relx=0.3, y=400, width=280, height=50)

    def show_add_customer_frame(self):
        self.hide_main_menu()
        self.add_customer_frame = AddCustomerFrame(self.root, self, self.customer_manager)
        self.add_customer_frame.place(relx=0.5, y=180, width=700, height=500, anchor="n")
        
    def show_view_customer_frame(self):
        self.hide_main_menu()
        self.view_customer_frame = ViewCustomerFrame(self.root, self, self.customer_manager)
        self.view_customer_frame.place(relx=0.5, y=180, width=900, height=500, anchor="n")

    def show_update_customer_frame(self):
        self.hide_main_menu()
        self.update_customer_frame = UpdateCustomerFrame(self.root, self, self.customer_manager)
        self.update_customer_frame.place(relx=0.5, y=180, width=700, height=500, anchor="n")

    def hide_main_menu(self):
        self.main_menu_frame.place_forget()

    def show_main_menu(self):
        self.main_menu_frame.place(relx=0.5, y=180, width=700, height=500, anchor="n")

# Define Frames for different functionalities
class AddCustomerFrame(tk.Frame):
    def __init__(self, parent, controller, customer_manager):
        tk.Frame.__init__(self, parent, bg="#785E3B")
        self.controller = controller
        self.customer_manager = customer_manager

        tk.Label(self, text="Add Customer", bg="#785E3B",fg='#EFE6DD', font=("times roman", 18, "bold")).place(relx=0.3, y=50, width=280, height=50)

        self.name_label = tk.Label(self, text="Name", bg="#785E3B",fg='#EFE6DD', font=("times roman", 14, "bold"))
        self.name_label.place(relx=0.2, y=150, width=200, height=30)
        self.name_entry = tk.Entry(self)
        self.name_entry.place(relx=0.4, y=150, width=280, height=30)

        self.phone_label = tk.Label(self, text="Phone", bg="#785E3B",fg='#EFE6DD', font=("times roman", 14, "bold"))
        self.phone_label.place(relx=0.185, y=220, width=200, height=30)
        self.phone_entry = tk.Entry(self)
        self.phone_entry.place(relx=0.4, y=220, width=280, height=30)

        self.address_label = tk.Label(self, text="Address", bg="#785E3B",fg='#EFE6DD', font=("times roman", 14, "bold"))
        self.address_label.place(relx=0.180, y=290, width=200, height=30)
        self.address_entry = tk.Entry(self)
        self.address_entry.place(relx=0.4, y=290, width=280, height=30)

        self.add_button = tk.Button(self, text="Add Customer", bg="#EFE6DD", fg='#785E3B', font=("times roman", 14, "bold"), command=self.add_customer)
        self.add_button.place(relx=0.4, y=380, width=200, height=40)

        self.back_button = tk.Button(self, text="◁", bg="#785E3B", fg='#EFE6DD' , font=("times roman", 14, "bold"), command=self.show_main_menu)
        self.back_button.place(x=20, y=30, width=40, height=40)

    def add_customer(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        if name and phone and address:
            self.customer_manager.add_customer(name, phone, address)
            messagebox.showinfo("Success", "Customer added successfully!")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Enter the details!")

    def show_main_menu(self):
        self.controller.show_main_menu()
        self.place_forget()

class ViewCustomerFrame(tk.Frame):
    def __init__(self, parent, controller, customer_manager):
        tk.Frame.__init__(self, parent, bg='#785E3B')
        self.controller = controller
        self.customer_manager = customer_manager

        tk.Label(self, text="View Customers", font=("times roman", 18, "bold"), bg="#785E3B", fg='#EFE6DD' ).place(relx=0.3, y=30, width=390, height=50)

        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Phone", "Address"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Address", text="Address")

        self.tree.place(x=20, y=120, width=850, height=320 )
        self.view_customers()

        self.back_button = tk.Button(self, text="◁", bg="#785E3B",fg='#EFE6DD', font=("times roman", 14, "bold"), command=self.show_main_menu)
        self.back_button.place(x=20, y=30, width=40, height=40)


    def view_customers(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        customers = self.customer_manager.view_customers()
        for customer in customers:
            self.tree.insert("", "end", values=(customer['id'], customer['name'], customer['phone'], customer['address']))

    def show_main_menu(self):
        self.controller.show_main_menu()
        self.place_forget()




class UpdateCustomerFrame(tk.Frame):
    def __init__(self, parent, controller, customer_manager):
        tk.Frame.__init__(self, parent, bg="#785E3B")
        self.controller = controller
        self.customer_manager = customer_manager

        tk.Label(self, text="Update Customer", font=("times roman", 18, "bold"), bg="#785E3B" ).place(relx=0.3, y=50, width=280, height=50)

        self.name_label = tk.Label(self, text="Name", bg="#785E3B", font=("times roman", 14, "bold"))
        self.name_label.place(relx=0.2, y=150, width=200, height=30)
        self.name_entry = tk.Entry(self)
        self.name_entry.place(relx=0.4, y=150, width=280, height=30)

        self.new_phone_label = tk.Label(self, text="New Phone", bg="#785E3B", font=("times roman", 14, "bold"))
        self.new_phone_label.place(relx=0.165, y=220, width=200, height=30)
        self.new_phone_entry = tk.Entry(self)
        self.new_phone_entry.place(relx=0.4, y=220, width=280, height=30)


        self.new_address_label = tk.Label(self, text="New Address", bg="#785E3B", font=("times roman", 14, "bold"))
        self.new_address_label.place(relx=0.150, y=290, width=200, height=30)
        self.new_address_entry = tk.Entry(self)
        self.new_address_entry.place(relx=0.4, y=290, width=280, height=30)

        self.update_button = tk.Button(self, text="Update Customer", bg='#EFE6DD', fg="#785E3B", font=("times roman", 14, "bold"), command=self.update_customer)
        self.update_button.place(relx=0.4, y=380, width=200, height=40)

        self.back_button = tk.Button(self, text="◁",bg="#785E3B",fg='#EFE6DD', font=("times roman", 14, "bold"), command=self.show_main_menu)
        self.back_button.place(x=20, y=30, width=40, height=40)

    def update_customer(self):
        name = self.name_entry.get()
        new_phone = self.new_phone_entry.get()
        new_address = self.new_address_entry.get()
        if name:
            if self.customer_manager.update_customer(name, new_phone, new_address):
                messagebox.showinfo("Success", "Customer updated successfully!")
            else:
                messagebox.showerror("Error", "Customer not found!")
        else:
            messagebox.showerror("Error", "Name is required!")

    def show_main_menu(self):
        self.controller.show_main_menu()
        self.place_forget()

# Main code to run the application

# if __name__ == "__main__":
#
#     customer_manager = CustomerManager()
#     root = tk.Tk()
#     app = CustomerApp(root, customer_manager)
#     root.mainloop()
