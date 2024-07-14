import tkinter as tk
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from data import sales_data, inventory_data, product_data, sales_year_data, inventory_month_data
from tkinter import ttk


root = tk.Tk()
root.title("Snugspaces")
root.geometry("1290x832")
root.state('zoomed')
root.configure(background='#3A98CC')

#frame para d gumalaw
side_frame = tk.Frame(root, bg="white")
side_frame.pack(side="left", fill="y")

# Load and resize logo
snugspacelogo = Image.open("Rental Management images/snugspaceheading.png")
resized_logo = snugspacelogo.resize((302,100), Image.LANCZOS)
logo_img = ImageTk.PhotoImage(resized_logo)
logo_label = tk.Label(side_frame, image=logo_img,borderwidth=0,bg='white')
logo_label.pack()

#Dashboard button
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

#Rental button
rent_img = Image.open("Rental Management images/Rental.png")
resized_rent = rent_img.resize((300, 100), Image.LANCZOS)
rent_img_tk = ImageTk.PhotoImage(resized_rent)
rent_button = tk.Button(side_frame, image=rent_img_tk,borderwidth=0,bg='white')
rent_button.pack()

# payment button
payment_img = Image.open("Rental Management images/Payment.png")
resized_payment = payment_img.resize((300, 100), Image.LANCZOS)
payment_img_tk = ImageTk.PhotoImage(resized_payment)
payment_button = tk.Button(side_frame, image=payment_img_tk,borderwidth=0,bg='white')
payment_button.pack()

# analytics button
analytics_img = Image.open("Rental Management images/analytics.png")
resized_analytics = analytics_img.resize((300, 100), Image.LANCZOS)
analytics_img_tk = ImageTk.PhotoImage(resized_analytics)
analytics_button = tk.Button(side_frame, image=analytics_img_tk,borderwidth=0,bg='white')
analytics_button.pack()

# accounts button
acc_img = Image.open("Rental Management images/Account.png")
resized_acc = acc_img.resize((300, 100), Image.LANCZOS)
acc_img_tk = ImageTk.PhotoImage(resized_acc)
acc_button = tk.Button(side_frame, image=acc_img_tk,borderwidth=0,bg='white')
acc_button.pack()

##base background
#base frame
base_frame = tk.Frame(root,bg='#3A98CC',pady=20, height = 1234, width=2000)
base_frame.pack()

##portfolio frame
#porfolio frame
port_frame = tk.Frame(root,pady=20,borderwidth=0, background='white')
port_frame.place(x=400,y=120)
#portfolio frame
prt_label = tk.Label(port_frame, width=150, height =13,borderwidth=0,bg="white")
prt_label.pack()


#dashboard label
base_frame = tk.Frame(root,height=10,width=500)
base_frame.place(x=400,y=20)
dashboard_label=tk.Label(base_frame,text="Dashboard",bg='#3A98CC',font=('Impact',30,'bold'))
dashboard_label.pack()


#welome statement label
base_frame = tk.Frame(root,height=10,width=500)
base_frame.place(x=400,y=80)
statement_label=tk.Label(base_frame,text="Welcome to snugspaces a place where you can manage your room rental in a convenient way!",bg='#3A98CC',font=('Times New Roman',14,))
statement_label.pack()


#portfolio statement
base_frame = tk.Frame(root,height=10,width=500)
base_frame.place(x=420,y=130)
portStatement_label=tk.Label(base_frame,text="This is your property portfolio summary.",bg='white',font=('Times New Roman',14,))
portStatement_label.pack()

#total rooms
totalRooms_img = Image.open("Rental Management images/roomsDash.png")
resized_totalRooms = totalRooms_img.resize((70, 70), Image.LANCZOS)
totalRooms_img_tk = ImageTk.PhotoImage(resized_totalRooms)
analytics_button = tk.Button(image=totalRooms_img_tk,borderwidth=0,bg='white')
analytics_button.place(x=510,y=200)

base_frame = tk.Frame(root,height=10,width=500)
base_frame.place(x=520,y=280)
totalRooms_label=tk.Label(base_frame,text="Total Rooms",bg='white',font=('Times New Roman',14,))
totalRooms_label.pack()

base_frame = tk.Frame(root,height=10,width=500)
base_frame.place(x=590,y=220)
totalRooms_label=tk.Label(base_frame,text="7",bg='white',font=('Times New Roman',30,))
totalRooms_label.pack()

#available rooms
availRooms_img = Image.open("Rental Management images/availableRooms.png")
resized_availRooms = availRooms_img.resize((70, 70), Image.LANCZOS)
availRooms_img_tk = ImageTk.PhotoImage(resized_availRooms)
availRooms_button = tk.Button(image=availRooms_img_tk,borderwidth=0,bg='white')
availRooms_button.place(x=740,y=200)

base_frame = tk.Frame(root,height=10,width=500)
base_frame.place(x=740,y=280)
availRooms_label=tk.Label(base_frame,text="Available Rooms",bg='white',font=('Times New Roman',14,))
availRooms_label.pack()

base_frame = tk.Frame(root,height=10,width=500)
base_frame.place(x=820,y=220)
availRooms_label=tk.Label(base_frame,text="10",bg='white',font=('Times New Roman',30,))
availRooms_label.pack()

#occupied rooms
occupiedRooms_img = Image.open("Rental Management images/occupiedRooms.png")
resized_occupiedRooms = occupiedRooms_img.resize((70, 70), Image.LANCZOS)
occupiedRooms_img_tk = ImageTk.PhotoImage(resized_occupiedRooms)
occupiedRooms_button = tk.Button(image=occupiedRooms_img_tk,borderwidth=0,bg='white')
occupiedRooms_button.place(x=990,y=200)

base_frame = tk.Frame(root,height=10,width=500)
base_frame.place(x=990,y=280)
occupiedRooms_label=tk.Label(base_frame,text="Occupied Rooms",bg='white',font=('Times New Roman',14,))
occupiedRooms_label.pack()

base_frame = tk.Frame(root,height=10,width=500)
base_frame.place(x=1080,y=220)
occupiedRooms_label=tk.Label(base_frame,text="13",bg='white',font=('Times New Roman',30,))
occupiedRooms_label.pack()

#pending payments
paymentDash_img = Image.open("Rental Management images/paymentDash.png")
resized_paymentDash = paymentDash_img.resize((70, 70), Image.LANCZOS)
paymentDash_img_tk = ImageTk.PhotoImage(resized_paymentDash)
paymentDash_button = tk.Button(image=paymentDash_img_tk,borderwidth=0,bg='white')
paymentDash_button.place(x=1230,y=200)

base_frame = tk.Frame(root,height=10,width=500)
base_frame.place(x=1230,y=280)
paymentDash_label=tk.Label(base_frame,text="Pending Payments",bg='white',font=('Times New Roman',14,))
paymentDash_label.pack()

base_frame = tk.Frame(root,height=10,width=500)
base_frame.place(x=1320,y=220)
paymentDash_label=tk.Label(base_frame,text="4",bg='white',font=('Times New Roman',30,))
paymentDash_label.pack()


##box frame
#box frame
bx_frame = tk.Frame(root,pady=20,borderwidth=0, background='white')
bx_frame.place(x=400,y=420)
#b0x frame
bx_label = tk.Label(bx_frame, width=40, height=17,borderwidth=0,bg="white")
bx_label.pack()

room1_img = Image.open("Rental Management images/room1.jpg")
resized_room1 = room1_img.resize((230, 150), Image.LANCZOS)
room1_img_tk = ImageTk.PhotoImage(resized_room1)
room1_button = tk.Button(image=room1_img_tk,borderwidth=0,bg='white')
room1_button.place(x=425,y=450)

base_frame = tk.Frame(root,height=10,width=500)
base_frame.place(x=425,y=610)
room1_label=tk.Label(base_frame,text="Room #1",bg='white',font=('Times New Roman',12,))
room1_label.pack()

Rent_frame = tk.Frame(root)
Rent_frame.place(x=480,y=655)
Rent_button = tk.Button(Rent_frame,text="Rent",font=("times new roman",12,"bold"), pady=5, padx=10,
                             bg= "#2C6FBC", width=10)
Rent_button.pack()

##box2 frame
#box2 frame
bx_frame = tk.Frame(root,pady=20,borderwidth=0, background='white')
bx_frame.place(x=710,y=420)
#b0x frame
bx2_label = tk.Label(bx_frame, width=40, height=17,borderwidth=0,bg="white")
bx2_label.pack()

room2_img = Image.open("Rental Management images/room2.png")
resized_room2 = room2_img.resize((230, 150), Image.LANCZOS)
room2_img_tk = ImageTk.PhotoImage(resized_room2)
room2_button = tk.Button(image=room2_img_tk,borderwidth=0,bg='white')
room2_button.place(x=735,y=450)

base_frame = tk.Frame(root,height=10,width=500)
base_frame.place(x=735,y=610)
room2_label=tk.Label(base_frame,text="Room #2",bg='white',font=('Times New Roman',12,))
room2_label.pack()

Rent_frame = tk.Frame(root)
Rent_frame.place(x=790,y=655)
Rent_button = tk.Button(Rent_frame,text="Rent",font=("times new roman",12,"bold"), pady=5, padx=10,
                             bg= "#2C6FBC", width=10)
Rent_button.pack()

##box3 frame
#box3 frame
bx_frame = tk.Frame(root,pady=20,borderwidth=0, background='white')
bx_frame.place(x=1020,y=420)
#b0x frame
bx3_label = tk.Label(bx_frame, width=40, height=17,borderwidth=0,bg="white")
bx3_label.pack()

room3_img = Image.open("Rental Management images/room3.jpg")
resized_room3 = room3_img.resize((230, 150), Image.LANCZOS)
room3_img_tk = ImageTk.PhotoImage(resized_room3)
room3_button = tk.Button(image=room3_img_tk,borderwidth=0,bg='white')
room3_button.place(x=1045,y=450)

base_frame = tk.Frame(root,height=10,width=500)
base_frame.place(x=1045,y=610)
room3_label=tk.Label(base_frame,text="Room #3",bg='white',font=('Times New Roman',12,))
room3_label.pack()

Rent_frame = tk.Frame(root)
Rent_frame.place(x=1100,y=655)
Rent_button = tk.Button(Rent_frame,text="Rent",font=("times new roman",12,"bold"), pady=5, padx=10,
                             bg= "#2C6FBC", width=10)
Rent_button.pack()

##box4 frame
#box4 frame
bx_frame = tk.Frame(root,pady=20,borderwidth=0, background='white')
bx_frame.place(x=1330,y=420)
#b0x frame
bx4_label = tk.Label(bx_frame, width=40, height=17,borderwidth=0,bg="white")
bx4_label.pack()

room4_img = Image.open("Rental Management images/room4.jpg")
resized_room4 = room4_img.resize((230, 150), Image.LANCZOS)
room4_img_tk = ImageTk.PhotoImage(resized_room4)
room4_button = tk.Button(image=room4_img_tk,borderwidth=0,bg='white')
room4_button.place(x=1355,y=450)

base_frame = tk.Frame(root,height=10,width=500)
base_frame.place(x=1353,y=610)
room4_label=tk.Label(base_frame,text="Room #4",bg='white',font=('Times New Roman',12,))
room4_label.pack()

Rent_frame = tk.Frame(root)
Rent_frame.place(x=1400,y=655)
Rent_button = tk.Button(Rent_frame,text="Rent",font=("times new roman",12,"bold"), pady=5, padx=10,
                             bg= "#2C6FBC", width=10)
Rent_button.pack()

#available rooms panels
base_frame = tk.Frame(root,height=10,width=500)
base_frame.place(x=400,y=380)
statement_label=tk.Label(base_frame,text="Available Rooms",bg='#3A98CC',font=('Times New Roman',18,'bold'))
statement_label.pack()

# Add Account button
addRent_frame = tk.Frame(root)
addRent_frame.place(x=800,y=760)
addRent_button = tk.Button(addRent_frame,text="View Room Rental",font=("times new roman",12,"bold"), pady= 5, padx= 20,
                             bg= "#2C6FBC", width=20)
addRent_button.pack()



root.mainloop()