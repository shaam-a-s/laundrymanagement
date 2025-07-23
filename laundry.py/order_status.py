import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime, date

class OrderStatus(tk.Tk):
    def __init__(self):
        self.orders = []
        super().__init__()
        self.title("Order Status")
        self.geometry("1200x600")

        self.orders = []
        with open('data.json', 'r') as file:
            json_data = json.load(file)

        for key in json_data:
            self.orders.append(json_data[key])

        self.create_widgets()
        self.populate_table()

    def create_widgets(self):
        heading = tk.Label(self, text="Order Status", fg="#785E3B", bg="#EFE6DD", font=("times roman", 24, "bold"))
        heading.place(x=550, y=10)

        input_frame = tk.Frame(self, bg="#EFE6DD", padx=10, pady=10)
        input_frame.place(x=230, y=70, width=800, height=120)

        tk.Label(input_frame, text="Order ID:", fg="#785E3B", bg="#EFE6DD", font=("times roman", 13, "bold")).grid(
            row=0, column=0, padx=5, pady=5)
        self.order_id_entry = tk.Entry(input_frame, font=("times roman", 13))
        self.order_id_entry.grid(row=0, column=1, padx=6, pady=5)

        tk.Label(input_frame, text="Payment Status:", fg="#785E3B", bg="#EFE6DD",
                 font=("times roman", 13, "bold")).grid(row=1, column=0, padx=5, pady=5)
        self.payment_var = tk.StringVar()
        self.payment_combo = ttk.Combobox(input_frame, textvariable=self.payment_var, values=["Paid", "Pending"],
                                          font=("times roman", 13))
        self.payment_combo.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Delivery Status:", fg="#785E3B", bg="#EFE6DD",
                 font=("times roman", 13, "bold")).grid(row=0, column=2, padx=5, pady=5)
        self.delivery_var = tk.StringVar()
        self.delivery_combo = ttk.Combobox(input_frame, textvariable=self.delivery_var, values=["Completed", "Pending"],
                                           font=("times roman", 13))
        self.delivery_combo.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(input_frame, text="Priority:", fg="#785E3B", bg="#EFE6DD", font=("times roman", 13, "bold")).grid(
            row=1, column=2, padx=5, pady=5)
        self.priority_var = tk.StringVar()
        self.priority_combo = ttk.Combobox(input_frame, textvariable=self.priority_var,
                                           values=["High", "Medium", "Low"], font=("times roman", 13))
        self.priority_combo.grid(row=1, column=3, padx=5, pady=5)

        update_button = tk.Button(input_frame, text="Update", fg="#EFE6DD", bg="#785E3B", font=("times roman", 12),
                                  command=self.update_order)
        update_button.grid(row=2, column=2, padx=5, pady=5)

        table_frame = tk.Frame(self, bg="#EFE6DD")
        table_frame.place(x=150, y=210, width=960, height=380)

        columns = ("order_date", "order_id", "customer_name", "payment", "delivery", "priority")

        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=8)
        self.tree.heading("order_date", text="Order Date")
        self.tree.heading("order_id", text="Order ID")
        self.tree.heading("customer_name", text="Customer Name")
        self.tree.heading("payment", text="Payment Status")
        self.tree.heading("delivery", text="Delivery Status")
        self.tree.heading("priority", text="Priority")

        self.tree.column("order_date", anchor="center", width=100)
        self.tree.column("order_id", anchor="center")
        self.tree.column("customer_name", anchor="center")
        self.tree.column("payment", anchor="center", width=100)
        self.tree.column("delivery", anchor="center", width=100)
        self.tree.column("priority", anchor="center", width=100)
        delete_button = tk.Button(self, text="Delete", fg="#EFE6DD", bg="#785E3B", font=("times roman", 12),
                                  command=self.delete_order)
        delete_button.place(x=980, y=600, width=80, height=39)
        back_button = tk.Button(self, text="Home", fg="#EFE6DD", bg="#785E3B", font=("times roman", 12),
                                  command=self.home)
        back_button.place(x=80, y=600, width=80, height=39)

        self.populate_table()

        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

    def populate_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for order in self.orders:
            with open("orders.txt", "r") as f:
                cont = f.readlines()
                od=[]
                for i in cont:
                    sp = i.split(" ")
                    od.append(sp[1])
            if order["order_id"] in od :
                pass
            else:
                self.orders.sort(key=lambda x: (self.priority_to_number(x["priority"]), datetime.strptime(x["Date"], "%Y-%m-%d")))
                self.tree.insert("", "end", values=(
                    order["Date"], order["order_id"], order["name"], order["payment"], order["delivery"],
                    order["priority"]))

    def priority_to_number(self, priority):
        priority_map = {"High": 1, "Medium": 2, "Low": 3}
        return priority_map[priority]

    def update_order(self):
        order_id = self.order_id_entry.get()
        new_payment = self.payment_var.get()
        new_delivery = self.delivery_var.get()
        new_priority = self.priority_var.get()

        if not order_id:
            messagebox.showerror("Error", "Enter a valid Order ID")
            return

        if new_payment not in ["Paid", "Pending"]:
            messagebox.showerror("Error", "Payment status must be 'Paid' or 'Pending'")
            return

        if new_delivery not in ["Completed", "Pending"]:
            messagebox.showerror("Error", "Delivery status must be 'Completed' or 'Pending'")
            return

        if new_priority not in ["High", "Medium", "Low"]:
            messagebox.showerror("Error", "Priority must be 'High', 'Medium', or 'Low'")
            return

        order_found = False
        for order in self.orders:
            if order["order_id"] == order_id:
                order_found = True
                if new_payment:
                    order["payment"] = new_payment
                if new_delivery:
                    order["delivery"] = new_delivery
                if new_priority:
                    # if order["Delivary_Date"] == str(date.today()):
                    #     order["priority"] = "High"
                    order["priority"] = new_priority
                with open('data.json', 'r') as file:
                    json_data = json.load(file)

                # Update the order details in the JSON data
                for key in json_data:
                    if json_data[key]["order_id"] == order_id:
                        json_data[key]["payment"] = order["payment"]
                        json_data[key]["delivery"] = order["delivery"]
                        json_data[key]["priority"] = order["priority"]

                with open('data.json', 'w') as file:
                    json.dump(json_data, file, indent=4)

        if not order_found:
            messagebox.showerror("Error", "Order ID not found")
            return

        self.populate_table()

        self.order_id_entry.delete(0, tk.END)
        self.payment_var.set("")
        self.delivery_var.set("")
        self.priority_var.set("")
    def delete_order(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select an order to delete")
            return

        order_data = self.tree.item(selected_item, "values")
        order_id = order_data[1]

        with open('data.json', 'r') as file:
            json_data = json.load(file)

        # Remove the order from the orders list
        for order in self.orders:
            if order["order_id"] == order_id:
                self.orders.remove(order)
                for key in json_data:
                    if json_data[key]["order_id"] == order_id:
                        json_data[key]["type"]=[]
                with open('data.json', 'w') as file:
                    json.dump(json_data, file, indent=4)

                break
        with open("orders.txt", "a") as file:
            file.write(" ".join(order_data) + "\n")

        self.tree.delete(selected_item)

    def home(self):
        from admin import Admin
        ad = Admin()
        if self.winfo_exists():
            self.destroy()
        ad.admin_page()
