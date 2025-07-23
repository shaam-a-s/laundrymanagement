import smtplib
gmail="sekarlaundry1234@gmail.com"
password="vrwbnkwrkztgrgda"

t="sarveash17@gmail.com"
def mail(u,o,dd,Tol):
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=gmail,password=password)
        connection.sendmail(from_addr=gmail,to_addrs=t,
                            msg=f"Subject:Bharathi Laundry Service\n\nThank YOU for choosing our laundry\nYour Unique ID : {u}\nYour Order ID : {o}\nDelivery Date : {dd}\nTotal : {Tol}")