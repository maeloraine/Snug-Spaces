import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font
from tkcalendar import DateEntry
from tkinter import messagebox
from datetime import datetime
from AddRentals_Db import update_rental, fetch_all_rental, delete_rental

def Update_Rental (parent, item_data, treeview):
    rental_id,  room_no, name, start_lease, end_lease = item_data

    def center_window(root, width, height):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    parent.title("Snugspaces: Add Remtal")
    parent.geometry('1290x815')
    center_window(parent, 1290, 815)
    parent.resizable(0, 0)
    parent.configure(background='white')
    #     root.configure(background='white')
    name_parts = name.split(' ')  # splits full name based on spaces
    first_name = name_parts[0] if len(name_parts) > 0 else ''
    last_name = name_parts[-1] if len(name_parts) > 1 else ''
    middle_name = ' '.join(name_parts[1:-1]) if len(name_parts) > 2 else ''
    # Outputs
    print("First Name:", first_name)
    print("Middle Name(s):", middle_name)
    print("Last Name:", last_name)

    def Submit_Update_Rentals():
        lease_start = strt_entry.get_date()
        lease_end = end_entry.get_date()

        # Update rental information in the database
        update_rental(rental_id, room_no,  lease_end)

        # Clear the Treeview
        treeview.delete(*treeview.get_children())
        # Fetch all rental data and repopulate the Treeview
        rental_data = fetch_all_rental()
        print("Current Rental in Database:")
        for rental in rental_data:
            fullName = f"{rental[2]}, {rental[3]} {rental[4]}"
            values = [rental[0] , rental[1], fullName, rental[5], rental[6]]
            treeview.insert('', 'end', values=values)

        # Show a success message
        messagebox.showinfo("Update", "Rental updated successfully!")
        parent.destroy()
        # Print the current rentals in the database to the console
        print("Current Rentals in Database:")
        for rental in rental_data:
            print(rental)

    def confirm_delete():
        if messagebox.askyesno("Delete Rental", "Are you sure you want to delete this rental information?"):
            # Delete rental from database
            delete_rental(rental_id)

            # Refresh Treeview in parent window
            treeview.delete(*treeview.get_children())
            rental_data = fetch_all_rental()
            print("Current Rental in Database:")
            for rental in rental_data:
                fullName = f"{rental[2]}, {rental[3]} {rental[4]}"
                values = [rental[0], fullName, rental[5], rental[6], rental[1]]
                treeview.insert('', 'end', values=values)

            messagebox.showinfo("Delete", "Rental deleted successfully!")
            parent.destroy()

    # add frame para d gumalaw
    add_frame = tk.Frame(parent, bg="white")
    add_frame.place(x=100, y=50)

    # Add a New Rental label
    add_label = tk.Label(add_frame, text="Add a New Rental", bg='white', font=('times new roman', 25, 'bold'))
    add_label.pack()

    # Tenant details label
    details_frame = tk.Frame(parent, bg="white")
    details_frame.place(x=120, y=110)
    details_label = tk.Label(details_frame, text="Tenant Details", bg='white', font=('times new roman', 22, 'bold'))
    details_label.pack()  # Main frame for scrollbar
    main_frame = tk.Frame(parent, bg='white', borderwidth=0)
    main_frame.place(x=0, y=150, height=1000, width=1290)

    # Create a canvas
    my_canvas = tk.Canvas(main_frame, bg='white', borderwidth=0)
    my_canvas.place(height=700, width=1650)

    # Create a scrollbar
    scrollbar_y = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    scrollbar_y.pack(side='right', fill='y')

    # Configure the canvas
    my_canvas.configure(yscrollcommand=scrollbar_y.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    # Create another frame inside the canvas
    det_frame = tk.Frame(my_canvas, bg='white', borderwidth=0)
    det_frame.pack()

    # Add that new frame to a window in the canvas
    my_canvas.create_window((0, 0), window=det_frame, anchor="ne", height=1000, width=1650)

    # First name label
    first_frame = tk.Frame(det_frame, bg="white")
    first_frame.place(x=120, y=20)
    first_label = tk.Label(first_frame, text="First Name", bg='white', font=('times new roman', 15, 'bold'))
    first_label.pack(padx=(0, 150))

    # First Name picture para soft edges
    first_pic = Image.open("Rental Management images/long rectangle.png")
    resized = first_pic.resize((250, 35), Image.Resampling.LANCZOS)
    first_pic = ImageTk.PhotoImage(resized)
    first_label = tk.Label(first_frame, image=first_pic, borderwidth=0, bg="white")
    first_label.pack(pady=(15, 0))

    # First name entry
    firstentry_frame = tk.Frame(det_frame, bg="white")
    firstentry_frame.place(x=135, y=70)
    first = tk.Entry(firstentry_frame, background="#D9D9D9", width=20, borderwidth=0, font=("helvica", 13))
    first.pack()
    first.insert(0, first_name)
    first.config(state='readonly')
    # first.insert(0, first_name)
    # first.config(state='readonly')

    # Middle name label
    middle_frame = tk.Frame(det_frame, bg="white")
    middle_frame.place(x=420, y=20)
    middle_label = tk.Label(middle_frame, text="Middle Name", bg='white', font=('times new roman', 15, 'bold'))
    middle_label.pack(padx=(0, 130))

    # Middle Name picture para soft edges
    middle_pic = Image.open("Rental Management images/long rectangle.png")
    resized = middle_pic.resize((250, 35), Image.Resampling.LANCZOS)
    middle_pic = ImageTk.PhotoImage(resized)
    middle_label = tk.Label(middle_frame, image=middle_pic, borderwidth=0, bg="white")
    middle_label.pack(pady=(15, 0))

    # Middle name entry
    middleentry_frame = tk.Frame(det_frame, bg="white")
    middleentry_frame.place(x=435, y=70)
    middle = tk.Entry(middleentry_frame, background="#D9D9D9", width=20, borderwidth=0, font=("helvica", 13))
    middle.pack()
    middle.insert(0, middle_name)
    middle.config(state='readonly')

    # Last name label
    last_frame = tk.Frame(det_frame, bg="white")
    last_frame.place(x=720, y=20)
    last_label = tk.Label(last_frame, text="Last Name", bg='white', font=('times new roman', 15, 'bold'))
    last_label.pack(padx=(0, 140))

    # Last Name picture para soft edges
    last_pic = Image.open("Rental Management images/long rectangle.png")
    resized = last_pic.resize((250, 35), Image.Resampling.LANCZOS)
    last_pic = ImageTk.PhotoImage(resized)
    last_label = tk.Label(last_frame, image=last_pic, borderwidth=0, bg="white")
    last_label.pack(pady=(15, 0))

    # Last name entry
    lastentry_frame = tk.Frame(det_frame, bg="white")
    lastentry_frame.place(x=735, y=70)
    last = tk.Entry(lastentry_frame, background="#D9D9D9", width=20, borderwidth=0, font=("helvica", 13))
    last.pack()
    last.insert(0,last_name)
    last.config(state='readonly')

    # Lease Agreement Label
    lease_agreement_frame = tk.Frame(det_frame, bg="white")
    lease_agreement_frame.place(x=120, y=356)
    lease_agreement_label = tk.Label(lease_agreement_frame, text="Lease Agreement", bg='white',
                                    font=('times new roman', 17, 'bold'))
    lease_agreement_label.pack(padx=(0, 280))

    # Lease Term Start date label
    strt_frame = tk.Frame(det_frame, bg="white")
    strt_frame.place(x=130, y=400)
    strt_label = tk.Label(strt_frame, text="Lease Term Start Date", bg='white', font=('times new roman', 15, 'bold'))
    strt_label.pack(padx=(0, 280))

    # Lease Term Start Date entry
    strt_entry_frame = tk.Frame(det_frame, height=10, width=500, bg="white", borderwidth=0)
    strt_entry_frame.place(x=140, y=445)

    strt_entry = DateEntry(strt_entry_frame, font=('helvica', 12))
    strt_entry.pack()
    strt_entry.configure(state='disabled')

    # Lease Term End Date label
    end_frame = tk.Frame(det_frame, bg="white")
    end_frame.place(x=355, y=400)

    end_label = tk.Label(end_frame, text="Lease Term End Date", bg='white', font=('times new roman', 15, 'bold'))
    end_label.pack(padx=(0, 280))

    # Lease Term End Date entry
    end_entry_frame = tk.Frame(det_frame, height=10, width=500, bg="white", borderwidth=0)
    end_entry_frame.place(x=365, y=445)
    end_entry = DateEntry(end_entry_frame, font=('helvica', 12))
    end_entry.pack()
    end_date = datetime.strptime(end_lease, '%Y-%m-%d').date()
    end_entry.set_date(end_date)

    # Add New Rental frame
    add_frame = tk.Frame(det_frame, bg="white")
    add_frame.place(x=945, y=590)

    add = tk.Button(add_frame, text="Add", font=("times new roman", 14, "bold"), pady=5, padx=15, background="#2C6FBC",
                    width=10, command=Submit_Update_Rentals)
    add.pack()

    # del_frame = tk.Frame(det_frame, bg="white")
    # del_frame.place(x=750, y=590)
    #
    # delete_btn = tk.Button(del_frame, text="Delete", font=("times new roman", 14, "bold"), pady=5, padx=15, background="#2C6FBC",
    #                 width=10, command=confirm_delete)
    # delete_btn.pack()

    #
    return

