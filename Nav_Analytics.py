import tkinter as tk
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from data import sales_data, inventory_data, product_data, sales_year_data, inventory_month_data
from tkinter import ttk

def create_analytics(parent, controller):
    frame = tk.Frame(parent, bg='#3A98CC')

    # Monthly Details label
    monthDeets_label = tk.Label(frame, text='Monthly Details for ', bg='#3A98CC', font=('times new roman', 30, 'bold'))
    monthDeets_label.place(x=100, y=40)

    # Month Label
    month_label = tk.Label(frame, text='[December]', bg='#3A98CC', font=('times new roman', 30, 'bold'))
    month_label.place(x=445, y=40)

    # Total Rooms button and image
    totPic_img = Image.open("Rental Management images/Interior.png")
    resized_room3 = totPic_img.resize((100, 100), Image.LANCZOS)
    totPic_img_tk = ImageTk.PhotoImage(resized_room3)
    totPic = tk.Button(frame, image=totPic_img_tk, borderwidth=0, bg='white')
    totPic.image = totPic_img_tk
    totPic.place(x=180, y=145)

    totNoRooom_label = tk.Label(frame, text='22', font=('helvetica', 14, 'bold'), bg='white')
    totNoRooom_label.place(x=217, y=250)

    totRoom_label = tk.Label(frame, text='Total No. of Room', font=('times new roman', 14, 'bold'), bg='white')
    totRoom_label.place(x=150, y=300)

    # Total Rentals button and image
    totBooking_img = Image.open("Rental Management images/Booking.png")
    resized_room3 = totBooking_img.resize((100, 100), Image.LANCZOS)
    totBooking_img_tk = ImageTk.PhotoImage(resized_room3)
    totBooking = tk.Button(frame, image=totBooking_img_tk, borderwidth=0, bg='white')
    totBooking.image = totBooking_img_tk
    totBooking.place(x=395, y=145)

    totNoBooking_label = tk.Label(frame, text='22', font=('helvetica', 14, 'bold'), bg='white')
    totNoBooking_label.place(x=433, y=250)

    totBooking_label = tk.Label(frame, text='Total Rentals', font=('times new roman', 14, 'bold'), bg='white')
    totBooking_label.place(x=390, y=300)

    # Occupied Rooms button and image
    totOccRooms_img = Image.open("Rental Management images/Hotel Room Key.png")
    resized_room3 = totOccRooms_img.resize((100, 100), Image.LANCZOS)
    totOccRooms_img_tk = ImageTk.PhotoImage(resized_room3)
    totOccRooms = tk.Button(frame, image=totOccRooms_img_tk, borderwidth=0, bg='white')
    totOccRooms.image = totOccRooms_img_tk
    totOccRooms.place(x=605, y=145)

    NoOccRooms_label = tk.Label(frame, text='22', font=('helvetica', 14, 'bold'), bg='white')
    NoOccRooms_label.place(x=635, y=250)

    OccRooms_label = tk.Label(frame, text='Occupied Rooms', font=('times new roman', 14, 'bold'), bg='white')
    OccRooms_label.place(x=580, y=300)

    # Available Rooms button and image
    totAvailRooms_img = Image.open("Rental Management images/Room.png")
    resized_room3 = totAvailRooms_img.resize((100, 100), Image.LANCZOS)
    totAvailRooms_img_tk = ImageTk.PhotoImage(resized_room3)
    totAvailRooms = tk.Button(frame, image=totAvailRooms_img_tk, borderwidth=0, bg='white')
    totAvailRooms.image = totAvailRooms_img_tk
    totAvailRooms.place(x=805, y=145)

    NoAvailRooms_label = tk.Label(frame, text='22', font=('helvetica', 14, 'bold'), bg='white')
    NoAvailRooms_label.place(x=835, y=250)

    AvailRooms_label = tk.Label(frame, text='Available Rooms', font=('times new roman', 14, 'bold'), bg='white')
    AvailRooms_label.place(x=780, y=300)

    # Occupancy Rate button and image
    OccRate_img = Image.open("Rental Management images/Reducing Churn.png")
    resized_room3 = OccRate_img.resize((100, 100), Image.LANCZOS)
    OccRate_img_tk = ImageTk.PhotoImage(resized_room3)
    OccRate = tk.Button(frame, image=OccRate_img_tk, borderwidth=0, bg='white')
    OccRate.image = OccRate_img_tk
    OccRate.place(x=1005, y=145)

    OccRatePercent_label = tk.Label(frame, text='22%', font=('helvetica', 14, 'bold'), bg='white')
    OccRatePercent_label.place(x=1030, y=250)

    OccRate_label = tk.Label(frame, text='Occupancy Rate', font=('times new roman', 14, 'bold'), bg='white')
    OccRate_label.place(x=975, y=300)

    # Graphs
    plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["#2C6FBC"])

    # Chart 1: Bar chart of inventory data
    fig1, ax1 = plt.subplots()
    ax1.bar(list(inventory_data.keys()), inventory_data.values())
    ax1.set_title("Occupancy Rate")
    ax1.set_ylabel("")
    canvas1 = FigureCanvasTkAgg(fig1, master=frame)
    canvas1.draw()
    canvas1.get_tk_widget().place(x=100, y=400)

    # Chart 2: Bar chart of sales data
    fig2, ax2 = plt.subplots()
    ax2.bar(list(sales_data.keys()), sales_data.values())
    ax2.set_title("Monthly Revenue")
    ax2.set_ylabel("")
    canvas2 = FigureCanvasTkAgg(fig2, master=frame)
    canvas2.draw()
    canvas2.get_tk_widget().place(x=600, y=400)

    return frame