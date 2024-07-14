import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import font

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

# Rentals label
rental_frame = tk.Frame(root,height=10,width=500)
rental_frame.place(x=325,y=60)

rental_label=tk.Label(rental_frame,text="Rentals",bg='#3A98CC', font=('times new roman',22,'bold'))
rental_label.pack()

# Search Rental entry
searchRentalEntry_frame = tk.Frame(root, bg="white")
searchRentalEntry_frame.place(x=600,y=110)
searchRentalEntry=tk.Entry(searchRentalEntry_frame,background="#D9D9D9",width=50,borderwidth=2,font=("helvica",13),relief='raised')
searchRentalEntry.pack()


# Search button
searchRental_frame= tk.Frame(root,bg='#3A98CC')
searchRental_frame.place(x=1060,y=105)

searchRental_img = Image.open("Rental Management images/search.png")
resized_searchRental = searchRental_img.resize((30,30), Image.LANCZOS)
searchRental_img_tk = ImageTk.PhotoImage(resized_searchRental)
searchRental_button = tk.Button(searchRental_frame, image=searchRental_img_tk,borderwidth=0,bg='#3A98CC',relief='raised')
searchRental_button.pack(padx = (5,0))

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
columns = ("Tenant Name", "Room No", "Lease Start Date", "Lease End Date", "Lease Duration", "Payment Status")
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
tree.heading("Tenant Name", text="Tenant Name")
tree.heading("Room No", text="Room No")
tree.heading("Lease Start Date", text="Lease End Date")
tree.heading("Lease End Date", text="Lease End Date")
tree.heading("Lease Duration", text="Lease Duration")
tree.heading("Payment Status", text="Payment Status")

# Define the column widths
tree.column("Tenant Name", width=150,anchor='n')
tree.column("Room No", width=80,anchor='n')
tree.column("Lease Start Date", width=100,anchor='n')
tree.column("Lease End Date", width=100,anchor='n')
tree.column("Lease Duration", width=80,anchor='n')
tree.column("Payment Status", width=80,anchor='n')

# Insert some sample data
sample_data = [
    ("Clarisse Irish", "101", "06/01/2024", "06/30/2024", "1 month", "Paid"),
    ("Crystalyn", "102", "06/27/2024", "06/30/2024", "3 days", "Pending"),
    ("Mae Loraine", "103", "09/19/2023", "09/25/2023", "6 days", "Pending"),
]

for item in sample_data:
    tree.insert("", "end", values=item)


# Add Account button
addRent_frame = tk.Frame(root)
addRent_frame.place(x=1350,y=760)

addRent_button = tk.Button(addRent_frame,text="Add Rental",font=("times new roman",12,"bold"), pady= 5, padx= 20,
                             bg= "#2C6FBC", width=10)
addRent_button.pack()

# Edit Account button
editRent_frame = tk.Frame(root)
editRent_frame.place(x=1200,y=760)

editRent_button = tk.Button(editRent_frame,text="Edit Rental",font=("times new roman",12,"bold"), pady= 5, padx= 20,
                             bg= "#2C6FBC", width=10)
editRent_button.pack()

root.mainloop()