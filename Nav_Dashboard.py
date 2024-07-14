import tkinter as tk
from PIL import ImageTk, Image
from AddRentals_Db import fetch_available_rooms, fetch_total_rooms, fetch_occupied_rooms, fetch_total_tenants
from New_AddRental import AddRentalApp
from Nav_Rentals import RentalManagement

def open_add_rental_window(room_no):
    new_window = tk.Toplevel()
    add_rental_view = AddRentalApp(new_window, room_no)

def Dashboard(parent, controller):
    frame = tk.Frame(parent)
    frame.grid(row=0, column=0, sticky="nsew")
    frame.configure(background='#3A98CC')

    # Base frame
    base_frame = tk.Frame(frame, bg='#3A98CC', pady=20, height=1234, width=2000)
    base_frame.pack()

    # Dashboard label
    base_frame = tk.Frame(frame, height=10, width=500)
    base_frame.place(x=100, y=20)
    dashboard_label = tk.Label(base_frame, text="Dashboard", bg='#3A98CC', font=('times new roman', 30, 'bold'))
    dashboard_label.pack()

    # Welcome statement label
    base_frame = tk.Frame(frame, height=10, width=500)
    base_frame.place(x=100, y=80)
    statement_label = tk.Label(base_frame, text="Welcome to snugspaces a place where you can manage your room rental in a convenient way!", bg='#3A98CC', font=('Times New Roman', 14,))
    statement_label.pack()

    # Summary frame
    base_frame = tk.Frame(frame, pady=20, borderwidth=0, background='white')
    base_frame.place(x=100, y=120)
    summaryBG = tk.Label(base_frame, width=150, height=13, borderwidth=0, bg="white")
    summaryBG.pack()

    # Summary statement
    base_frame = tk.Frame(frame, height=10, width=500)
    base_frame.place(x=120, y=130)
    summaryStatement_label = tk.Label(base_frame, text="This is your property portfolio summary.", bg='white', font=('Times New Roman', 14,))
    summaryStatement_label.pack()

    # Fetch data for labels
    total_rooms = fetch_total_rooms()
    available_rooms = fetch_available_rooms()
    occupied_rooms = fetch_occupied_rooms()
    total_tenants = fetch_total_tenants()

    # Total rooms
    base_frame = tk.Frame(frame, height=70, width=70, bg='white')
    base_frame.place(x=190, y=200)
    totalRooms_img = Image.open("Rental Management images/roomsDash.png")
    resized_totalRooms = totalRooms_img.resize((70, 70), Image.LANCZOS)
    totalRooms_img_tk = ImageTk.PhotoImage(resized_totalRooms)
    totalRoomsBG = tk.Button(base_frame, image=totalRooms_img_tk, borderwidth=0, bg='white')
    totalRoomsBG.image = totalRooms_img_tk
    totalRoomsBG.pack()

    base_frame = tk.Frame(frame, height=10, width=500)
    base_frame.place(x=190, y=280)
    totalRooms_label = tk.Label(base_frame, text="Total Rooms", bg='white', font=('Times New Roman', 14,))
    totalRooms_label.pack()

    base_frame = tk.Frame(frame, height=10, width=500)
    base_frame.place(x=270, y=220)
    totalRooms_count_label = tk.Label(base_frame, text=str(total_rooms), bg='white', font=('Times New Roman', 30,))
    totalRooms_count_label.pack()

    # Available rooms
    base_frame = tk.Frame(frame, height=70, width=70, bg='white')
    base_frame.place(x=420, y=200)
    availRooms_img = Image.open("Rental Management images/availableRooms.png")
    resized_availRooms = availRooms_img.resize((70, 70), Image.LANCZOS)
    availRooms_img_tk = ImageTk.PhotoImage(resized_availRooms)
    availRooms_button = tk.Button(base_frame, image=availRooms_img_tk, borderwidth=0, bg='white')
    availRooms_button.image = availRooms_img_tk
    availRooms_button.pack()

    base_frame = tk.Frame(frame, height=10, width=500)
    base_frame.place(x=420, y=280)
    availRooms_label = tk.Label(base_frame, text="Available Rooms", bg='white', font=('Times New Roman', 14,))
    availRooms_label.pack()

    base_frame = tk.Frame(frame, height=10, width=500)
    base_frame.place(x=500, y=220)
    availRooms_count_label = tk.Label(base_frame, text=str(len(available_rooms)), bg='white', font=('Times New Roman', 30,))
    availRooms_count_label.pack()

    # Occupied rooms
    base_frame = tk.Frame(frame, height=70, width=70, bg='white')
    base_frame.place(x=660, y=200)
    occupiedRooms_img = Image.open("Rental Management images/occupiedRooms.png")
    resized_occupiedRooms = occupiedRooms_img.resize((70, 70), Image.LANCZOS)
    occupiedRooms_img_tk = ImageTk.PhotoImage(resized_occupiedRooms)
    occupiedRooms_button = tk.Button(base_frame, image=occupiedRooms_img_tk, borderwidth=0, bg='white')
    occupiedRooms_button.image = occupiedRooms_img_tk
    occupiedRooms_button.pack()

    base_frame = tk.Frame(frame, height=10, width=500)
    base_frame.place(x=670, y=280)
    occupiedRooms_label = tk.Label(base_frame, text="Occupied Rooms", bg='white', font=('Times New Roman', 14,))
    occupiedRooms_label.pack()

    base_frame = tk.Frame(frame, height=10, width=500)
    base_frame.place(x=750, y=220)
    occupiedRooms_count_label = tk.Label(base_frame, text=str(occupied_rooms), bg='white', font=('Times New Roman', 30,))
    occupiedRooms_count_label.pack()

    # Total Tenants
    base_frame = tk.Frame(frame, height=70, width=70, bg='white')
    base_frame.place(x=910, y=200)
    tenants_img = Image.open("Rental Management images/tenants1.png")  # Update with an appropriate image
    resized_tenants = tenants_img.resize((70, 70), Image.LANCZOS)
    tenants_img_tk = ImageTk.PhotoImage(resized_tenants)
    tenants_button = tk.Button(base_frame, image=tenants_img_tk, borderwidth=0, bg='white')
    tenants_button.image = tenants_img_tk
    tenants_button.pack()

    base_frame = tk.Frame(frame, height=10, width=500)
    base_frame.place(x=900, y=280)
    tenants_label = tk.Label(base_frame, text="Total Tenants", bg='white', font=('Times New Roman', 14,))
    tenants_label.pack()

    base_frame = tk.Frame(frame, height=10, width=500)
    base_frame.place(x=1000, y=220)
    tenants_count_label = tk.Label(base_frame, text=str(total_tenants), bg='white', font=('Times New Roman', 30,))
    tenants_count_label.pack()

    # Available rooms panels
    base_frame = tk.Frame(frame, height=10, width=500)
    base_frame.place(x=100, y=380)
    statement_label = tk.Label(base_frame, text="Available Rooms", bg='#3A98CC', font=('Times New Roman', 18, 'bold'))
    statement_label.pack()

    # Fetch available rooms
    available_rooms = fetch_available_rooms()

    # Create a canvas and a horizontal scrollbar
    canvas = tk.Canvas(frame, bg='#3A98CC', width=1040, height=275,
                       highlightthickness=0)  # Set highlightthickness to 0 to remove the outline
    h_scrollbar = tk.Scrollbar(frame, orient='horizontal', command=canvas.xview)
    canvas.configure(xscrollcommand=h_scrollbar.set)

    canvas.place(x=100, y=420)
    h_scrollbar.place(x=100, y=690, width=1045)

    # Adjust the scrollable frame's background color to match the canvas background
    scroll_frame = tk.Frame(canvas, bg='#3A98CC')  # Set the background color to match the canvas
    canvas.create_window((0, 0), window=scroll_frame, anchor='nw')

    # Display available rooms
    for room in available_rooms:
        room_frame = tk.Frame(scroll_frame, bg='white', pady=10)
        room_frame.pack(side='left', padx=20, pady=(0, 20))
        room1_img = Image.open("Rental Management images/room1.jpg")
        resized_room1 = room1_img.resize((230, 150), Image.LANCZOS)
        room1_img_tk = ImageTk.PhotoImage(resized_room1)
        room1 = tk.Label(room_frame, image=room1_img_tk, borderwidth=0, bg='white')
        room1.image = room1_img_tk
        room1.pack()

        # Display room information
        room_label = tk.Label(room_frame, text=f"Room #{room[1]}", bg='white', font=('Times New Roman', 12,))
        room_label.pack()

        Rent_button = tk.Button(room_frame, text="Rent", font=("times new roman", 12, "bold"), pady=5, padx=10,
                                bg="#2C6FBC", width=10,
                                command=lambda room_no=room[1]: open_add_rental_window(room_no))
        Rent_button.pack(pady=(5, 0))

    # Update the scroll region
    scroll_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    # View Room Rental button
    base_frame = tk.Frame(frame)
    base_frame.place(x=920, y=730)
    VRoomRental_button = tk.Button(base_frame, text="View Room Rental", font=("times new roman", 12, "bold"), pady=5,
                                   padx=20, bg="#2C6FBC", width=20, command=lambda: controller.show_frame( "RentalManagement"))
    VRoomRental_button.pack()

    return frame
