import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import datetime
from tkcalendar import DateEntry
from datetime import datetime
from AddRentals_Db import update_tenant, fetch_all_tenants

def UD_Tenant(parent, item_data, treeview):
    tenant_id, name, birthday, email, contact_no, gender, full_address, zip_code = item_data
    # Function to center the window
    def center_window(root, width, height):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    parent.title("Snugspaces: Update Tenant")
    parent.geometry('1290x815')
    center_window(parent, 1290, 815)
    parent.resizable(0, 0)
    parent.configure(background='white')

    # Function to handle submission of updated tenant information
    def submit_update():
        first_name = first.get()
        last_name = last.get()
        middle_name = middle.get()
        birthday = bdaydate.get_date()
        email_add = email_entry.get()
        contact_nbr = contact_number.get()
        selected_gender = selected_option.get()
        street = street_entry.get()
        barangay = brgy_entry.get()
        city = city_entry.get()
        province = prov_entry.get()
        zip_code = zip_entry.get()

        # Update tenant information in the database
        update_tenant(tenant_id, first_name, middle_name, last_name, birthday, email_add, contact_nbr,
                         selected_gender, street, barangay, city, province, zip_code)

        # Refresh Treeview in parent window
        treeview.delete(*treeview.get_children())
        tenant_data = fetch_all_tenants()
        for tenant in tenant_data:
            full_name = f"{tenant[3]}, {tenant[2]} {tenant[1]}"
            full_address = f"{tenant[8]} street, Brgy. {tenant[9]}, {tenant[10]} City, {tenant[11]}"
            values = (tenant[0], full_name, tenant[4], tenant[5], tenant[6], tenant[7], full_address, tenant[12])
            treeview.insert('', 'end', values=values)
        messagebox.showinfo("Update", "Tenant updated successfully!")

        parent.destroy()

        tenants = fetch_all_tenants()
        print("Current Tenants in Database:")
        for tenant in tenants:
            print(tenant)

    # def confirm_delete():
    #     messagebox.askyesno("Delete Tenant", "Are you sure you want to delete this tenant?")
    #     # Delete tenant from database
    #     delete_tenant(tenant_id)
    #
    #     # Refresh Treeview in parent window
    #     treeview.delete(*treeview.get_children())
    #     tenant_data = fetch_all_tenants()
    #     for tenant in tenant_data:
    #         full_name = f"{tenant[3]}, {tenant[1]} {tenant[2]}"
    #         full_address = f"{tenant[8]} street, Brgy. {tenant[9]}, {tenant[10]} City, {tenant[11]}"
    #         values = (tenant[0], full_name, tenant[4], tenant[5], tenant[6], tenant[7], full_address, tenant[12])
    #         treeview.insert('', 'end', values=values)
    #     messagebox.showinfo("Delete", "Tenant deleted successfully!")
    #     parent.destroy()

    # example full name:  [0]Danga, [1]Crystalyn [2]Rubio
    name_parts = name.split(' ') # splits full name based on spaces
    first_name = name_parts[1] # retrieves the first index (Crystalyn)
    last_name = name_parts[0] # retrieves the index zero (Danga)
    middle_name = ' '.join(name_parts[2:]) if len(name_parts) > 2 else ''

    #_______________________________________________________
    address_parts = full_address.split(', ')
    street_part = address_parts[0]
    barangay_part = address_parts[1].split(' ')[1]
    city_part = address_parts[2].split(' ')[0]
    province_part = address_parts[2].split(' ')[1]

    # Extract the province, which is the last element
    province_part = address_parts[-1]

    # add frame para d gumalaw
    add_frame = tk.Frame(parent, bg="white")
    add_frame.place(x=100, y=50)

    # Add a New Rental label
    add_label = tk.Label(add_frame, text="Edit Tenant's Information", bg='white', font=('times new roman', 25, 'bold'))
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
    first_label.image = first_pic
    first_label.pack(pady=(15, 0))

    # First name entry
    first_entry_frame = tk.Frame(det_frame, bg="white")
    first_entry_frame.place(x=135, y=70)
    first = tk.Entry(first_entry_frame, background="#D9D9D9", width=20, borderwidth=0, font=("helvica", 13))
    first.pack()
    first.insert(0, first_name)

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
    middle_label.iamge = middle_pic
    middle_label.pack(pady=(15, 0))

    # Middle name entry
    middleentry_frame = tk.Frame(det_frame, bg="white")
    middleentry_frame.place(x=435, y=70)
    middle = tk.Entry(middleentry_frame, background="#D9D9D9", width=20, borderwidth=0, font=("helvica", 13))
    middle.pack()
    middle.insert(0, middle_name)


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
    last_label.image = last_pic
    last_label.pack(pady=(15, 0))

    # Last name entry
    lastentry_frame = tk.Frame(det_frame, bg="white")
    lastentry_frame.place(x=735, y=70)
    last = tk.Entry(lastentry_frame, background="#D9D9D9", width=20, borderwidth=0, font=("helvica", 13))
    last.pack()
    last.insert(0, last_name.strip(','))

    # Birthday label
    bday_frame = tk.Frame(det_frame, bg="white")
    bday_frame.place(x=1020, y=20)
    bday_label = tk.Label(bday_frame, text="Birthday", bg='white', font=('times new roman', 15, 'bold'))
    bday_label.pack(padx=(0, 160))

    # Bday entry
    bdayentry_frame = tk.Frame(det_frame, height=10, width=500, bg="white", borderwidth=0)
    bdayentry_frame.place(x=1020, y=70)

    bdaydate = DateEntry(bdayentry_frame, font=('helvica', 12))
    bdaydate.pack()
    bday_date = datetime.strptime(birthday, '%Y-%m-%d').date()
    bdaydate.set_date(bday_date)

    # email label
    email_frame = tk.Frame(det_frame, bg="white")
    email_frame.place(x=120, y=120)
    email_label = tk.Label(email_frame, text="Email", bg='white', font=('times new roman', 15, 'bold'))
    email_label.pack(padx=(0, 280))

    # email picture para soft edges
    email_pic = Image.open("Rental Management images/long rectangle.png")
    resized = email_pic.resize((250, 35), Image.Resampling.LANCZOS)
    email_pic = ImageTk.PhotoImage(resized)
    email_label = tk.Label(email_frame, image=email_pic, borderwidth=0, bg="white")
    email_label.image = email_pic
    email_label.pack(pady=(15, 0), padx=(0, 100))

    # email entry
    email_entry_frame = tk.Frame(det_frame, bg="white")
    email_entry_frame.place(x=135, y=170)
    email_entry = tk.Entry(email_entry_frame, background="#D9D9D9", width=23, borderwidth=0, font=("helvica", 13))
    email_entry.pack()
    email_entry.insert(0, email)

    # contact number label
    contact_frame = tk.Frame(det_frame, bg="white")
    contact_frame.place(x=420, y=120)
    contact_label = tk.Label(contact_frame, text="Contact Number", bg='white', font=('times new roman', 15, 'bold'))
    contact_label.pack(padx=(0, 170))

    # Contact number picture para soft edges
    contact_pic = Image.open("Rental Management images/long rectangle.png")
    resized = contact_pic.resize((250, 35), Image.Resampling.LANCZOS)
    contact_pic = ImageTk.PhotoImage(resized)
    contact_label = tk.Label(contact_frame, image=contact_pic, borderwidth=0, bg="white")
    contact_label.image = contact_pic
    contact_label.pack(pady=(15, 0), padx=(0, 60))

    # contact entry
    contac_tentry_frame = tk.Frame(det_frame, bg="white")
    contac_tentry_frame.place(x=435, y=170)
    contact_number = tk.Entry(contac_tentry_frame, background="#D9D9D9", width=20, borderwidth=0, font=("helvica", 13))
    contact_number.pack()
    contact_number.insert(0, contact_no)


    # gender label
    gender_frame = tk.Frame(parent, height=10, width=500, bg='white', borderwidth=0)
    gender_frame.place(x=720, y=270)
    gender_label = tk.Label(gender_frame, text="Gender", bg='white', font=('times new roman', 15, 'bold'))
    gender_label.pack()


    # gender pic frame
    gindir_frame = tk.Frame(parent, height=10, width=500, bg='white', borderwidth=0)
    gindir_frame.place(x=720, y=315)

    # gender drop down frame
    genmenu_frame = tk.Frame(parent, height=10, width=500, bg='#D9D9D9', borderwidth=0)
    genmenu_frame.place(x=730, y=317)

    # Gender menu
    selected_option = tk.StringVar()
    selected_option.set("Male")
    options = ["Male", "Female", "Prefer Not to say"]
    option_menu = tk.OptionMenu(genmenu_frame, selected_option, *options)
    option_menu.configure(borderwidth=0, width=13, font=('Helvica', 12), bg='#D9D9D9', highlightbackground='#D9D9D9', )
    option_menu.pack()
    selected_option.set(gender)

    # Gender picture para soft edges
    gender_pic = Image.open("Rental Management images/long rectangle.png")
    resized = gender_pic.resize((170, 35), Image.Resampling.LANCZOS)
    gender_pic = ImageTk.PhotoImage(resized)
    gender_label = tk.Label(gindir_frame, image=gender_pic, borderwidth=0, bg="white")
    gender_label.image = gender_pic
    gender_label.pack(pady=(0, 0))

    # Address label
    address_frame = tk.Frame(det_frame, bg="white")
    address_frame.place(x=120, y=225)
    address_label = tk.Label(address_frame, text="Address", bg='white', font=('times new roman', 17, 'bold'))
    address_label.pack(padx=(0, 280))

    # streetlabel
    street_label = tk.Label(address_frame, text="Street", bg='white', font=('times new roman', 15, 'bold'))
    street_label.pack(padx=(0, 280))

    # street picture para soft edges
    street_pic = Image.open("Rental Management images/long rectangle.png")
    resized = street_pic.resize((180, 35), Image.Resampling.LANCZOS)
    street_pic = ImageTk.PhotoImage(resized)
    street_label = tk.Label(address_frame, image=street_pic, borderwidth=0, bg="white")
    street_label.image = street_pic
    street_label.pack(pady=(15, 0), padx=(0, 159))

    # street entry
    streetentry_frame = tk.Frame(det_frame, bg="white")
    streetentry_frame.place(x=145, y=307)

    street_entry = tk.Entry(streetentry_frame, bg="#D9D9D9", borderwidth=0, font=('helvica', 12), width=10)
    street_entry.pack()
    street_entry.insert(0, street_part.strip('street'))

    # Barangay frame
    brgy_frame = tk.Frame(det_frame, bg="white")
    brgy_frame.place(x=350, y=256)

    # Barangay label
    brgy_label = tk.Label(brgy_frame, text="Barangay", bg='white', font=('times new roman', 15, 'bold'))
    brgy_label.pack(padx=(0, 285))

    # Barangay picture para soft edges
    brgy_pic = Image.open("Rental Management images/long rectangle.png")
    resized = brgy_pic.resize((180, 35), Image.Resampling.LANCZOS)
    brgy_pic = ImageTk.PhotoImage(resized)
    brgy_label = tk.Label(brgy_frame, image=brgy_pic, borderwidth=0, bg="white")
    brgy_label.image = brgy_pic
    brgy_label.pack(pady=(15, 0), padx=(0, 199))

    # Barangay entry
    brgyentry_frame = tk.Frame(det_frame, bg="white")
    brgyentry_frame.place(x=360, y=307)

    brgy_entry = tk.Entry(brgyentry_frame, bg="#D9D9D9", borderwidth=0, font=('helvica', 12), width=10)
    brgy_entry.pack()
    brgy_entry.insert(0, barangay_part)

    # City frame
    city_frame = tk.Frame(det_frame, bg="white")
    city_frame.place(x=560, y=256)

    # City label
    city_label = tk.Label(city_frame, text="City", bg='white', font=('times new roman', 15, 'bold'))
    city_label.pack(padx=(0, 335))

    # City picture para soft edges
    city_pic = Image.open("Rental Management images/long rectangle.png")
    resized = city_pic.resize((180, 35), Image.Resampling.LANCZOS)
    city_pic = ImageTk.PhotoImage(resized)
    city_label = tk.Label(city_frame, image=city_pic, borderwidth=0, bg="white")
    city_label.image = city_pic
    city_label.pack(pady=(15, 0), padx=(0, 199))

    # city entry
    cityentry_frame = tk.Frame(det_frame, bg="white")
    cityentry_frame.place(x=570, y=307)

    city_entry = tk.Entry(cityentry_frame, bg="#D9D9D9", borderwidth=0, font=('helvica', 12), width=10)
    city_entry.pack()
    city_entry.insert(0, city_part)

    # Province frame
    prov_frame = tk.Frame(det_frame, bg="white")
    prov_frame.place(x=780, y=256)

    # Province label
    prov_label = tk.Label(prov_frame, text="Province", bg='white', font=('times new roman', 15, 'bold'))
    prov_label.pack(padx=(0, 302))

    # Province picture para soft edges
    prov_pic = Image.open("Rental Management images/long rectangle.png")
    resized = prov_pic.resize((180, 35), Image.Resampling.LANCZOS)
    prov_pic = ImageTk.PhotoImage(resized)
    prov_label = tk.Label(prov_frame, image=prov_pic, borderwidth=0, bg="white")
    prov_label.image = prov_pic
    prov_label.pack(pady=(15, 0), padx=(0, 199))

    # Province entry
    proventry_frame = tk.Frame(det_frame, bg="white")
    proventry_frame.place(x=790, y=307)

    prov_entry = tk.Entry(proventry_frame, bg="#D9D9D9", borderwidth=0, font=('helvica', 12), width=10)
    prov_entry.pack()
    prov_entry.insert(0, province_part)

    # Zip code frame
    zip_frame = tk.Frame(det_frame, bg="white")
    zip_frame.place(x=1000, y=256)

    # Zip code label
    zip_label = tk.Label(zip_frame, text="Zip Code", bg='white', font=('times new roman', 15, 'bold'))
    zip_label.pack(padx=(0, 240))

    # Zip code picture para soft edges
    zip_pic = Image.open("Rental Management images/small rectangle.png")
    resized = zip_pic.resize((100, 35), Image.Resampling.LANCZOS)
    zip_pic = ImageTk.PhotoImage(resized)
    zip_label = tk.Label(zip_frame, image=zip_pic, borderwidth=0, bg="white")
    zip_label.image = zip_pic
    zip_label.pack(pady=(15, 0), padx=(0, 220))

    # Zip code  entry
    zip_entry_frame = tk.Frame(det_frame, bg="white")
    zip_entry_frame.place(x=1010, y=307)

    zip_entry = tk.Entry(zip_entry_frame, background="#D9D9D9", width=6, borderwidth=0, font=("helvica", 13))
    zip_entry.pack()
    zip_entry.insert(0, zip_code)

    add_frame = tk.Frame(det_frame, bg="white")
    add_frame.place(x=945, y=545)

    add = tk.Button(add_frame, text="Update Tenant", font=("times new roman", 14, "bold"), pady=5, padx=15,
                    background="#2C6FBC",
                    width=10, command=submit_update)
    add.pack()

    # delete_frame = tk.Frame(det_frame, bg="white")
    # delete_frame.place(x=750, y=545)
    #
    # delete_btn = tk.Button(delete_frame, text="Delete Tenant", font=("times new roman", 14, "bold"), pady=5, padx=15,
    #                        background="#2C6FBC",
    #                        width=10, command=confirm_delete)
    # delete_btn.pack()

    add_frame = tk.Frame(det_frame, bg="white")
    add_frame.place(x=945, y=545)

    add = tk.Button(add_frame, text="Update Tenant", font=("times new roman", 14, "bold"), pady=5, padx=15,
                    background="#2C6FBC",
                    width=10, command=submit_update)
    add.pack()
    # delete_frame = tk.Frame(det_frame, bg="white")
    # delete_frame.place(x=750, y=545)
    #
    # delete_btn = tk.Button(delete_frame, text="Delete Tenant", font=("times new roman", 14, "bold"), pady=5, padx=15,
    #                        background="#2C6FBC",
    #                        width=10, command=confirm_delete)
    # delete_btn.pack()



    return
