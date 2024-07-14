import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import font
from AddRentals_Db import add_room, fetch_all_rooms

def AddRoomApp(parent, treeview):

    def center_window(root, width, height):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    parent.title("Snugspaces: Add Room")
    parent.geometry('650x450')
    center_window(parent, 650, 450)
    parent.resizable(0, 0)
    parent.configure(background='#4b7cdc')

    def Submit_Rooms():
        roomNbr = roomNo.get()
        room_rate = roomRateEntry.get()
        room_status = selectedRoomStatus_option.get()

        try:
            # Attempt to add the room
            add_room(roomNbr, room_rate, room_status)
        except ValueError as e:
            # Display an error message if room number already exists
            if "already exists" in str(e):
                messagebox.showinfo("Error", "Cannot add room. Room already exists.")
            else:
                messagebox.showinfo("Error", str(e))
            return
        except Exception as e:
            # Handle any other exceptions that might occur
            messagebox.showinfo("Error", f"An unexpected error occurred: {str(e)}")
            return

        roomRateEntry.delete(0, tk.END)
        room_data = fetch_all_rooms()
        print("Current Rooms in Database:")
        for rooms_data in room_data:
            print(rooms_data)

        treeview.delete(*treeview.get_children())
        room_data = fetch_all_rooms()
        for room in room_data:
            values = (room[0], room[1], room[2], room[3])
            treeview.insert('', 'end', values=values)

        parent.destroy()

    # Back button
    back_frame = tk.Frame(parent, bg = 'white')
    back_frame.place(x = "10", y = "10")

    back_label = tk.Label(back_frame, text = " Back", bg = '#4b7cdc', fg = 'white', font = ('times new roman', 12, 'bold'))
    back_label.pack()

    # Add Room label
    addRoomLabel_frame = tk.Frame(parent, bg="white")
    addRoomLabel_frame.place(x="210", y = "60")

    addRoomLabel = tk.Label(addRoomLabel_frame, text = "Add a Room", bg = '#4b7cdc', fg = 'white', font = ('times new roman', 24, 'bold'))
    addRoomLabel.pack()

    # Room No label
    roomNo_frame = tk.Frame(parent, bg="#4b7cdc")
    roomNo_frame.place(x=90,y=130)
    roomNo_label=tk.Label(roomNo_frame,text="Room No", bg = '#4b7cdc', fg = 'white' , font=('times new roman',14,'bold'))
    roomNo_label.pack()

    # Room No picture para soft edges
    roomNo_pic = Image.open ("Rental Management images/long rectangle.png")
    resized = roomNo_pic.resize((220,25),Image.Resampling.LANCZOS)
    roomNo_pic = ImageTk.PhotoImage(resized)
    roomNoPic_label = tk.Label(roomNo_frame, image=roomNo_pic,borderwidth=0,bg="#4b7cdc")
    roomNoPic_label.pack(padx = (120, 0))

    # Room No entry
    roomNoEntry_frame = tk.Frame(parent, bg="#4b7cdc")
    roomNoEntry_frame.place(x=220,y=160)
    roomNo = tk.Entry(roomNoEntry_frame,background="#D9D9D9",width=20,borderwidth=0,font=("helvica",13))
    roomNo.pack()

    # Room Rate label
    roomRate_frame = tk.Frame(parent, bg="#4b7cdc")
    roomRate_frame.place(x=90,y=200)
    roomRate_label=tk.Label(roomRate_frame,text="Room Rate", bg = '#4b7cdc', fg = 'white' , font=('times new roman',14,'bold'))
    roomRate_label.pack()

    # Password picture para soft edges
    roomRate_pic = Image.open ("Rental Management images/long rectangle.png")
    resized = roomRate_pic.resize((220,25),Image.Resampling.LANCZOS)
    roomRate_pic = ImageTk.PhotoImage(resized)
    roomRatePic_label = tk.Label(roomRate_frame, image=roomRate_pic,borderwidth=0,bg="#4b7cdc")
    roomRatePic_label.pack(padx = (120, 0))

    # Room Rate entry
    roomRateEntry_frame = tk.Frame(parent, bg="#4b7cdc")
    roomRateEntry_frame.place(x=220,y=230)
    roomRateEntry = tk.Entry(roomRateEntry_frame,background="#D9D9D9",width=20,borderwidth=0,font=("helvica",13))
    roomRateEntry.pack()

    # Room Status label
    roomStatus_frame = tk.Frame(parent, bg="#4b7cdc")
    roomStatus_frame.place(x=166,y=270)
    roomStatus_label=tk.Label(roomStatus_frame,text="Room Status", bg = '#4b7cdc', fg = 'white' , font=('times new roman',14,'bold'))
    roomStatus_label.pack()

    # Room Status picture para soft edges
    roomStatus_pic = Image.open ("Rental Management images/long rectangle.png")
    resized = roomStatus_pic.resize((220,25),Image.Resampling.LANCZOS)
    roomStatus_pic = ImageTk.PhotoImage(resized)
    roomStatusPic_label = tk.Label(roomStatus_frame, image=roomStatus_pic,borderwidth=0,bg="#4b7cdc")
    roomStatusPic_label.pack(padx = (45, 0))

    # Room Status menu
    roomStatusMenu_frame = tk.Frame(parent, bg="#4b7cdc")
    roomStatusMenu_frame.place(x=220, y=300)

    selectedRoomStatus_option = tk.StringVar()
    selectedRoomStatus_option.set("Available")
    roomStatus = ["Available", "Occupied"]
    roomStatus_menu = tk.OptionMenu(roomStatusMenu_frame, selectedRoomStatus_option, *roomStatus)
    roomStatus_menu.configure(borderwidth=0, width=13, font=('Helvica', 12), bg='#D9D9D9', highlightbackground='#D9D9D9', )
    roomStatus_menu.pack()

    # Existing Room error
    roomExistError_frame = tk.Frame(parent, bg="#4b7cdc")
    roomExistError_frame.place(x=210, y=335)
    roomExistError_label = tk.Label(roomExistError_frame, text="Room already exist",
                            bg='#4b7cdc', fg='red', font=('times new roman', 12))
    roomExistError_label.pack_forget()  # Initially hide the error label

    # Error handling
    def on_button_click():
        # Condition when room is already in the system
        # if roomNo.get() == confirmPassword.get():
        #     roomExistError_label.pack()  # Show the error label
        #     roomRateEntry.delete(0, tk.END)  # Clear the room rate field
        #     roomStatus.delete(0, tk.END)  # Clear the room status field
        # else:
             pass




    # Add Room button
    addRoom_frame = tk.Frame(parent)
    addRoom_frame.place(x=275, y=375)
    addRoom_button = tk.Button(addRoom_frame, text="Confirm", font=("times new roman", 14, "bold"), pady=5, padx=15, background="#2C6FBC",
                    width=10, command=Submit_Rooms)
    addRoom_button.pack()

    return