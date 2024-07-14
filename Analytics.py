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
root.configure(background='white')

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

#analytics frame
charts_frame = tk.Frame(root,bg='white',pady=20)
charts_frame.pack()

#monthly details label
Mot_frame = tk.Frame(root, bg='white')
Mot_frame.place(x=450,y=40)
mot_label= tk.Label(Mot_frame,text='Monthly Details for ',bg='white',font=('times new roman',20,'bold'))
mot_label.pack()

#what month label
month_frame = tk.Frame(root, bg='white')
month_frame.place(x=694,y=40)
month_label= tk.Label(month_frame,text='December',bg='white',font=('times new roman',20,'bold'))
month_label.pack()



# total room label and images
tot_frame = tk.Frame(root,bg='white')
tot_frame.place(x=555,y=80)
#total pics
tot_pic = Image.open ("Rental Management images/Interior.png")
resized = tot_pic.resize((100,100),Image.Resampling.LANCZOS)
tot_pic = ImageTk.PhotoImage(resized)
tot_label = tk.Label(tot_frame, image=tot_pic,borderwidth=0,bg="white")
tot_label.pack()

# Total No of Rooms label
totper_frame = tk.Frame(root,bg='white')
totper_frame.place(x=585,y=180)
totper_label = tk.Label(totper_frame,text='22',font=('helvica',20,'bold'),bg='white')
totper_label.pack()

# Total of rooms label
totroom_frame = tk.Frame(root,bg='white')
totroom_frame.place(x=495,y=240)
totroom_label = tk.Label(totroom_frame,text='Total No. of Room',font=('times new roman',20,'bold'),bg='white')
totroom_label.pack()

# Occupied rooms label  and images
bok_frame = tk.Frame(root,bg='white')
bok_frame.place(x=825,y=80)

bok_pic = Image.open ("Rental Management images/Booking.png")
resized = bok_pic.resize((100,100),Image.Resampling.LANCZOS)
bok_pic = ImageTk.PhotoImage(resized)
bok_label = tk.Label(bok_frame, image=bok_pic,borderwidth=0,bg="white")
bok_label.pack()

# No of Occupied Rooms label
bokper_frame = tk.Frame(root,bg='white')
bokper_frame.place(x=855,y=180)
bokper_label = tk.Label(bokper_frame,text='22',font=('helvica',20,'bold'),bg='white')
bokper_label.pack()

# Occupied Rooms label
totbok_frame = tk.Frame(root,bg='white')
totbok_frame.place(x=780,y=240)
totbok_label = tk.Label(totbok_frame,text='Total Bookings',font=('times new roman',20,'bold'),bg='white')
totbok_label.pack()


#occupied rooms label  and images
occ_frame = tk.Frame(root,bg='white')
occ_frame.place(x=1055,y=80)

#occupied rooms pics
occ_pic = Image.open ("Rental Management images/Hotel Room Key.png")
resized = occ_pic.resize((100,100),Image.Resampling.LANCZOS)
occ_pic = ImageTk.PhotoImage(resized)
occ_label = tk.Label(occ_frame, image=occ_pic,borderwidth=0,bg="white")
occ_label.pack()

#percent label
occper_frame = tk.Frame(root,bg='white')
occper_frame.place(x=1090,y=180)
occper_label = tk.Label(occper_frame,text='22',font=('helvica',20,'bold'),bg='white')
occper_label.pack()

#occupied rooms label
occrom_frame = tk.Frame(root,bg='white')
occrom_frame.place(x=1010,y=240)
occrom_label = tk.Label(occrom_frame,text='Occupied Rooms',font=('times new roman',20,'bold'),bg='white')
occrom_label.pack()


#occupancy rate label  and images
or_frame = tk.Frame(root,bg='white')
or_frame.place(x=1305,y=80)

#occupancy rate  pics
or_pic = Image.open ("Rental Management images/Reducing Churn.png")
resized = or_pic.resize((100,100),Image.Resampling.LANCZOS)
or_pic = ImageTk.PhotoImage(resized)
or_label = tk.Label(or_frame, image=or_pic,borderwidth=0,bg="white")
or_label.pack()

#percent label
ocrate_frame = tk.Frame(root,bg='white')
ocrate_frame.place(x=1335,y=180)
ocrate_label = tk.Label(ocrate_frame,text='22',font=('helvica',20,'bold'),bg='white')
ocrate_label.pack()

#occupancy rate label
OR_frame = tk.Frame(root,bg='white')
OR_frame.place(x=1260,y=240)
OR_label = tk.Label(OR_frame,text='Occupancy Rate',font=('times new roman',20,'bold'),bg='white')
OR_label.pack()



#available rooms label  and images
availroom_frame = tk.Frame(root,bg='white')
availroom_frame.place(x=1555,y=80)

#available room pics
availroom_pic = Image.open ("Rental Management images/Room.png")
resized = availroom_pic.resize((100,100),Image.Resampling.LANCZOS)
availroom_pic = ImageTk.PhotoImage(resized)
availroom_label = tk.Label(availroom_frame, image=availroom_pic,borderwidth=0,bg="white")
availroom_label.pack()

#percent label
availrate_frame = tk.Frame(root,bg='white')
availrate_frame.place(x=1585,y=180)
availrate_label = tk.Label(availrate_frame,text='22',font=('helvica',20,'bold'),bg='white')
availrate_label.pack()

#occupancy rate label
avrom_frame = tk.Frame(root,bg='white')
avrom_frame.place(x=1510,y=240)
avrom_label = tk.Label(avrom_frame,text='Available Rooms',font=('times new roman',20,'bold'),bg='white')
avrom_label.pack()




#background ng numerical analytics
backk_pic = Image.open ("Rental Management images/backkground.png")
resized = backk_pic.resize((1400,300),Image.Resampling.LANCZOS)
backk_pic = ImageTk.PhotoImage(resized)
backk_label = tk.Label(charts_frame, image=backk_pic,borderwidth=0,bg="white")
backk_label.pack()

#mga graph
plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#2C6FBC"])

# Chart 2: Horizontal bar chart of inventory data
fig1, ax1 = plt.subplots()
ax1.bar(list(inventory_data.keys()), inventory_data.values())
ax1.set_title("Occupancy Rate")
ax1.set_ylabel("")
# plt.show()

# Chart 3: Pie chart of product data
fig2, ax2 = plt.subplots()
ax2.bar(list(inventory_data.keys()), inventory_data.values())
ax2.set_title("Monthly Revenue")
ax2.set_ylabel("")
# plt.show()

upper_frame = tk.Frame(charts_frame,bg='white')
upper_frame.pack(fill="both", expand=True)

canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)


root.mainloop()