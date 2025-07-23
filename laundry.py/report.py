from tkinter import *
import json
from datetime import datetime, timedelta
from collections import defaultdict

class LaundryReport:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def check(self,or_id):
        cp_order = []
        with open("orders.txt", "r") as file:
            cont = file.readlines()
            for i in cont:
                s = i.split(" ")
                cp_order.append(s[1])
        if or_id in cp_order:
            return True
        else:
            return False


    def get_start_of_week(self, date):
        start_of_week = date - timedelta(days=date.weekday())
        return start_of_week.strftime('%Y-%W')

    def generate_weekly_report(self):
        weekly_totals = defaultdict(lambda: {'total_revenue': 0, 'members': 0})
        for entry in self.data.values():
            if self.check(entry["order_id"]):
                total = entry['Total']
                date_str = entry['Date']
                date = datetime.strptime(date_str, '%Y-%m-%d')
                week_key = self.get_start_of_week(date)
                weekly_totals[week_key]['total_revenue'] += total
                weekly_totals[week_key]['members'] += 1

        for week, totals in sorted(weekly_totals.items()):
            print(f"Week {week}: {totals['members']} members, Total Revenue: ${totals['total_revenue']}")
            return totals['members'],totals['total_revenue']

    def generate_monthly_report(self):
        monthly_totals = defaultdict(lambda: {'total_revenue': 0, 'members': 0})
        for entry in self.data.values():
            if self.check(entry["order_id"]):
                total = entry['Total']
                date_str = entry['Date']
                date = datetime.strptime(date_str, '%Y-%m-%d')
                month_key = date.strftime('%Y-%m')
                monthly_totals[month_key]['total_revenue'] += total
                monthly_totals[month_key]['members'] += 1

        print("\nMonthly Totals:")
        for month, totals in sorted(monthly_totals.items()):
            print(f"Month {month}: {totals['members']} members, Total Revenue: ${totals['total_revenue']}")
            return totals['members'],totals['total_revenue']

    def generate_yearly_report(self):
        yearly_totals = defaultdict(lambda: {'total_revenue': 0, 'members': 0})
        for entry in self.data.values():
            if self.check(entry["order_id"]):
                total = entry['Total']
                date_str = entry['Date']
                date = datetime.strptime(date_str, '%Y-%m-%d')
                year_key = date.strftime('%Y')
                yearly_totals[year_key]['total_revenue'] += total
                yearly_totals[year_key]['members'] += 1

        print("\nYearly Totals:")
        for year, totals in sorted(yearly_totals.items()):
            print(f"Year {year}: {totals['members']} members, Total Revenue: ${totals['total_revenue']}")
            return totals['members'],totals['total_revenue']



# File path
file_path = 'data.json'




class GUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Laundry Service Management")

        self.canvas = Canvas(width=800, height=600)
        self.image_path = PhotoImage(file="pic-3.png")
        self.canvas.create_image(400, 300, image=self.image_path)
        self.canvas.place(x=0, y=0)

        self.label_title = Label(root, text="REPORT MANAGEMENT", width=30, height=2, font=("Arial", 24))
        self.label_title.pack()

        self.button_weekly = Button(root, text="WEEKLY REPORT", width=30, height=3, command=self.show_weekly_report)
        self.button_monthly = Button(root, text="MONTHLY REPORT", width=30, height=3, command=self.show_monthly_report)
        self.button_yearly = Button(root, text="YEARLY REPORT", width=30, height=3, command=self.show_yearly_report)
        self.button_back=Button(root, text="Home", width=30, height=3, command=self.home)
        self.button_weekly.config(background="light blue")
        self.button_monthly.config(background="light blue")
        self.button_yearly.config(background="light blue")
        self.button_back.config(background="light blue")

        self.button_weekly.place(x=310, y=200)
        self.button_monthly.place(x=310, y=300)
        self.button_yearly.place(x=310, y=400)
        self.button_back.place(x=310, y=500)


        self.report = LaundryReport(file_path)

    def show_weekly_report(self):
        total_transactions, total_income = self.report.generate_weekly_report()
        self.show_report_window("Weekly Report", total_transactions, total_income)

    def show_monthly_report(self):
        total_transactions, total_income = self.report.generate_monthly_report()
        self.show_report_window("Monthly Report", total_transactions, total_income)

    def show_yearly_report(self):
        total_transactions, total_income = self.report.generate_yearly_report()
        self.show_report_window("Yearly Report", total_transactions, total_income)

    def show_report_window(self, title, total_transactions, total_income):
        report_window = Toplevel(self.root)
        report_window.geometry("400x300")
        report_window.title(title)
        report_window.config(bg="light blue")

        label_transactions = Label(report_window, text=f"Total Transactions: {total_transactions}", font=("Arial", 18), bg="light blue")
        label_transactions.pack(pady=10)

        label_income = Label(report_window, text=f"Total Income: {total_income}", font=("Arial", 18), bg="light blue")
        label_income.pack(pady=10)

    def home(self):
        from admin import Admin
        ad=Admin()
        if Tk.winfo_exists(self.root):
            Tk.destroy(self.root)
        ad.admin_page()


