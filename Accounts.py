import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import font
import AddPayment
import AddRental
import Analytics
import Breakdown
import CreateAccount
import Dashboard
import EditAccount
import Login
import Payment
import Rentals
import Room
import Tenant


root = tk.Tk()
root.title("Snugspaces")
root.geometry("1290x832")
root.state('zoomed')
root.configure(background='#3A98CC')

# NavBar Frame
side_frame = tk.Frame(root, bg="white")
side_frame.pack(side="left", fill="y")

# Load and resize logo
snugspacelogo = Image.open("Rental Management images/snugspaceheading.png")
resized_logo = snugspacelogo.resize((302,100), Image.LANCZOS)
logo_img = ImageTk.PhotoImage(resized_logo)
logo_label = tk.Label(side_frame, image=logo_img,borderwidth=0,bg='white')
logo_label.pack()


# Dashboard button
dashboard_img = Image.open("Rental Management images/Dashboard.png")
resized_dashboard = dashboard_img.resize((300, 100), Image.LANCZOS)
dashboard_img_tk = ImageTk.PhotoImage(resized_dashboard)
dashboard_button = tk.Button(side_frame, image=dashboard_img_tk,borderwidth=0,bg='white')
dashboard_button.pack()

# Room button
room_img = Image.open("Rental Management images/Rooms.png")
resized_room = room_img.resize((300, 100), Image.LANCZOS)
room_img_tk = ImageTk.PhotoImage(resized_room)
room_button = tk.Button(side_frame, image=room_img_tk,borderwidth=0,bg='white')
room_button.pack()

# Tenant button
tenant_img = Image.open("Rental Management images/Tenants.png")
resized_tenant = tenant_img.resize((300, 100), Image.LANCZOS)
tenant_img_tk = ImageTk.PhotoImage(resized_tenant)
tenant_button = tk.Button(side_frame, image=tenant_img_tk,borderwidth=0,bg='white')
tenant_button.pack()

# Rental button
rent_img = Image.open("Rental Management images/Rental.png")
resized_rent = rent_img.resize((300, 100), Image.LANCZOS)
rent_img_tk = ImageTk.PhotoImage(resized_rent)
rent_button = tk.Button(side_frame, image=rent_img_tk,borderwidth=0,bg='white')
rent_button.pack()

# Payment button
payment_img = Image.open("Rental Management images/Payment.png")
resized_payment = payment_img.resize((300, 100), Image.LANCZOS)
payment_img_tk = ImageTk.PhotoImage(resized_payment)
payment_button = tk.Button(side_frame, image=payment_img_tk,borderwidth=0,bg='white')
payment_button.pack()

# Analytics button
analytics_img = Image.open("Rental Management images/analytics.png")
resized_payment = analytics_img.resize((300, 100), Image.LANCZOS)
analytics_img_tk = ImageTk.PhotoImage(resized_payment)
analytics_button = tk.Button(side_frame, image=analytics_img_tk,borderwidth=0,bg='white')
analytics_button.pack()

# Accounts button
acc_img = Image.open("Rental Management images/Account.png")
resized_acc = acc_img.resize((300, 100), Image.LANCZOS)
acc_img_tk = ImageTk.PhotoImage(resized_acc)
acc_button = tk.Button(side_frame, image=acc_img_tk,borderwidth=0,bg='white')
acc_button.pack()

# Accounts label
tenant_frame = tk.Frame(root,height=10,width=500)
tenant_frame.place(x=325,y=60)

tenant_label=tk.Label(tenant_frame,text="Accounts",bg='#3A98CC', font=('times new roman',22,'bold'))
tenant_label.pack()

# Search payment entry
searchPaymentEntry_frame = tk.Frame(root, bg="white")
searchPaymentEntry_frame.place(x=600,y=110)
searchPaymentEntry=tk.Entry(searchPaymentEntry_frame,background="#D9D9D9",width=50,borderwidth=2,font=("helvica",13),relief='raised')
searchPaymentEntry.pack()


# Search button
buttonSearch_frame= tk.Frame(root,bg='#3A98CC')
buttonSearch_frame.place(x=1060,y=105)

searchPayment_img = Image.open("Rental Management images/search.png")
resized_searchPayment = searchPayment_img.resize((30,30), Image.LANCZOS)
searchPayment_img_tk = ImageTk.PhotoImage(resized_searchPayment)
searchPayment_button = tk.Button(buttonSearch_frame, image=searchPayment_img_tk,borderwidth=0,bg='#3A98CC',relief='raised')
searchPayment_button.pack(padx = (5,0))

# Account list
frame_width =1160
frame_height = 575
bg_color='pink'

# Create a frame to hold the listbox
frame = tk.Frame(root, width=frame_width, height=frame_height,relief="raised",borderwidth=5)
frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
frame.place(x=340,y=150)

# Create a scrollbar
scrollbar = ttk.Scrollbar(frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

# Create the Treeview (multi-column listbox)
columns = ("User ID", "Username", "Password")
tree = ttk.Treeview(frame, columns=columns, show="headings", yscrollcommand=scrollbar.set)
tree.pack(fill="both", expand=True)

# Configure the scrollbar
scrollbar.config(command=tree.yview)

# Define the column headings with specified background and foreground colors
style = ttk.Style()
style.configure("Treeview.Heading", foreground="black", font=("Times new roman", 15, "bold"),relief="raised",borderwidth=5,bd=1)
style.configure("Treeview", foreground="black", fieldbackground="blue", font=("Helvetica", 10))

# Define row stripe colors
style.map("Treeview", background=[("selected", "#2C6FBC")], foreground=[("selected", "black")])

# Define the column headings
tree.heading("User ID", text="User ID")
tree.heading("Username", text="Username")
tree.heading("Password", text="Password")

# Define the column widths
tree.column("User ID", width=100,anchor='n')
tree.column("Username", width=150,anchor='n')
tree.column("Password", width=150,anchor='n')


# Insert some sample data
sample_data = [
    (1, "Owner", "123"),
    (2, "Assistant", "456"),
    (3, "Secretary", "789"),
]

for item in sample_data:
    tree.insert("", "end", values=item)


# Add Account button
addAcc_frame = tk.Frame(root)
addAcc_frame.place(x=1350,y=760)

addAcc_button = tk.Button(addAcc_frame,text="Add Account",font=("times new roman",12,"bold"), pady= 5, padx= 20,
                             bg= "#2C6FBC", width=10)
addAcc_button.pack()

# Edit Account button
editAcc_frame = tk.Frame(root)
editAcc_frame.place(x=1200,y=760)

editAcc_button = tk.Button(editAcc_frame,text="Edit Account",font=("times new roman",12,"bold"), pady= 5, padx= 20,
                             bg= "#2C6FBC", width=10)
editAcc_button.pack()

root.mainloop()