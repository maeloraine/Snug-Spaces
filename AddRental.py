import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font
from tkcalendar import DateEntry

# Root properties
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Snugspaces")

    # Window dimensions
    w = 1290
    h = 815

    # Get the screen resolution of computer
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    # Get window x & y position
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # Center the window
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # this removes the maximize button
    root.resizable(0,0)
    root.configure(background='white')

#add frame para d gumalaw
add_frame = tk.Frame(root, bg="white")
add_frame.place(x=100,y=50)

# Add a New Rental label
add_label=tk.Label(add_frame,text="Add a New Rental",bg='white',font=('times new roman',25,'bold'))
add_label.pack()

# Tenant details label
details_frame = tk.Frame(root, bg="white")
details_frame.place(x=120,y=110)
details_label=tk.Label(details_frame,text="Tenant Details",bg='white',font=('times new roman',22,'bold'))
details_label.pack()# Main frame for scrollbar
main_frame = tk.Frame(root,bg='white',borderwidth=0)
main_frame.place(x=0,y=150,height=1000,width=1290)

# Create a canvas
my_canvas = tk.Canvas(main_frame,bg='white',borderwidth=0)
my_canvas.place(height=700,width=1650)

# Create a scrollbar
scrollbar_y = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
scrollbar_y.pack(side='right', fill='y')

# Configure the canvas
my_canvas.configure(yscrollcommand=scrollbar_y.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

# Create another frame inside the canvas
det_frame = tk.Frame(my_canvas,bg='white',borderwidth=0)
det_frame.pack()

# Add that new frame to a window in the canvas
my_canvas.create_window((0, 0), window=det_frame, anchor="ne",height=1000,width=1650)


# First name label
first_frame = tk.Frame(det_frame, bg="white")
first_frame.place(x=120,y=20)
first_label=tk.Label(first_frame,text="First Name",bg='white',font=('times new roman',15,'bold'))
first_label.pack(padx=(0,150))

# First Name picture para soft edges
first_pic = Image.open ("Rental Management images/long rectangle.png")
resized = first_pic.resize((250,35),Image.Resampling.LANCZOS)
first_pic = ImageTk.PhotoImage(resized)
first_label = tk.Label(first_frame, image=first_pic,borderwidth=0,bg="white")
first_label.pack(pady=(15,0))

# First name entry
firstentry_frame = tk.Frame(det_frame, bg="white")
firstentry_frame.place(x=135,y=70)
first=tk.Entry(firstentry_frame,background="#D9D9D9",width=20,borderwidth=0,font=("helvica",13))
first.pack()


# Middle name label
middle_frame = tk.Frame(det_frame, bg="white")
middle_frame.place(x=420,y=20)
middle_label=tk.Label(middle_frame,text="Middle Name",bg='white',font=('times new roman',15,'bold'))
middle_label.pack(padx=(0,130))

# Middle Name picture para soft edges
middle_pic = Image.open ("Rental Management images/long rectangle.png")
resized = middle_pic.resize((250,35),Image.Resampling.LANCZOS)
middle_pic = ImageTk.PhotoImage(resized)
middle_label = tk.Label(middle_frame, image=middle_pic,borderwidth=0,bg="white")
middle_label.pack(pady=(15,0))

# Middle name entry
middleentry_frame = tk.Frame(det_frame, bg="white")
middleentry_frame.place(x=435,y=70)
middle=tk.Entry(middleentry_frame,background="#D9D9D9",width=20,borderwidth=0,font=("helvica",13))
middle.pack()


# Last name label
last_frame = tk.Frame(det_frame, bg="white")
last_frame.place(x=720,y=20)
last_label=tk.Label(last_frame,text="Last Name",bg='white',font=('times new roman',15,'bold'))
last_label.pack(padx=(0,140))

# Last Name picture para soft edges
last_pic = Image.open ("Rental Management images/long rectangle.png")
resized = last_pic.resize((250,35),Image.Resampling.LANCZOS)
last_pic = ImageTk.PhotoImage(resized)
last_label = tk.Label(last_frame, image=last_pic,borderwidth=0,bg="white")
last_label.pack(pady=(15,0))

# Last name entry
lastentry_frame = tk.Frame(det_frame, bg="white")
lastentry_frame.place(x=735,y=70)
last=tk.Entry(lastentry_frame,background="#D9D9D9",width=20,borderwidth=0,font=("helvica",13))
last.pack()

#Birthday label
bday_frame = tk.Frame(det_frame, bg="white")
bday_frame.place(x=1020,y=20)
bday_label=tk.Label(bday_frame,text="Birthday",bg='white',font=('times new roman',15,'bold'))
bday_label.pack(padx=(0,160))

#Bday entry
bdayentry_frame = tk.Frame(det_frame, height=10, width=500,bg="white",borderwidth=0)
bdayentry_frame.place(x=1020,y=70)

bdaydate= DateEntry(bdayentry_frame, font=('helvica',12))
bdaydate.pack()

#gender label
gender_frame = tk.Frame(root,height=10,width=500,bg='white',borderwidth=0)
gender_frame.place(x=720,y=270)
gender_label=tk.Label(gender_frame,text="Gender",bg='white',font=('times new roman',15,'bold'))
gender_label.pack()

#gender pic frame
gindir_frame= tk.Frame(root,height=10,width=500,bg='white',borderwidth=0)
gindir_frame.place(x=720,y=315)

# gender drop down frame
genmenu_frame= tk.Frame(root, height=10, width=500,bg='#D9D9D9',borderwidth=0)
genmenu_frame.place(x=730,y=317)

# Gender menu
selected_option = tk.StringVar()
selected_option.set("Male")
options = ["Male", "Female", "Others", "Prefer Not to say"]
option_menu = tk.OptionMenu(genmenu_frame, selected_option, *options)
option_menu.configure(borderwidth=0,width=13,font=('Helvica',12),bg='#D9D9D9',highlightbackground='#D9D9D9',)
option_menu.pack()

#Gender picture para soft edges
gender_pic = Image.open ("Rental Management images/long rectangle.png")
resized = gender_pic.resize((170,35),Image.Resampling.LANCZOS)
gender_pic = ImageTk.PhotoImage(resized)
gender_label = tk.Label(gindir_frame, image=gender_pic,borderwidth=0,bg="white")
gender_label.pack(pady=(0,0))

#email label
email_frame = tk.Frame(det_frame, bg="white")
email_frame.place(x=120,y=120)
email_label=tk.Label(email_frame,text="Email",bg='white',font=('times new roman',15,'bold'))
email_label.pack(padx=(0,280))

#email picture para soft edges
email_pic = Image.open ("Rental Management images/long rectangle.png")
resized = email_pic.resize((250,35),Image.Resampling.LANCZOS)
email_pic = ImageTk.PhotoImage(resized)
email_label = tk.Label(email_frame, image=email_pic,borderwidth=0,bg="white")
email_label.pack(pady=(15,0),padx=(0,100))

#email entry
emailentry_frame = tk.Frame(det_frame, bg="white")
emailentry_frame.place(x=135,y=170)
email=tk.Entry(emailentry_frame,background="#D9D9D9",width=23,borderwidth=0,font=("helvica",13))
email.pack()

#contact number label
contact_frame = tk.Frame(det_frame, bg="white")
contact_frame.place(x=420,y=120)
contact_label=tk.Label(contact_frame,text="Contact Number",bg='white',font=('times new roman',15,'bold'))
contact_label.pack(padx=(0,170))

#Contact number picture para soft edges
contact_pic = Image.open ("Rental Management images/long rectangle.png")
resized = contact_pic.resize((250,35),Image.Resampling.LANCZOS)
contact_pic = ImageTk.PhotoImage(resized)
contact_label = tk.Label(contact_frame, image=contact_pic,borderwidth=0,bg="white")
contact_label.pack(pady=(15,0),padx=(0,60))

#contact entry
contactentry_frame = tk.Frame(det_frame, bg="white")
contactentry_frame.place(x=435,y=170)
contact=tk.Entry(contactentry_frame,background="#D9D9D9",width=20,borderwidth=0,font=("helvica",13))
contact.pack()

#Address label
address_frame = tk.Frame(det_frame, bg="white")
address_frame.place(x=120,y=225)
address_label=tk.Label(address_frame,text="Address",bg='white',font=('times new roman',17,'bold'))
address_label.pack(padx=(0,280))

#streetlabel
street_label=tk.Label(address_frame,text="Street",bg='white',font=('times new roman',15,'bold'))
street_label.pack(padx=(0,280))

#street picture para soft edges
street_pic = Image.open ("Rental Management images/long rectangle.png")
resized = street_pic.resize((180,35),Image.Resampling.LANCZOS)
street_pic = ImageTk.PhotoImage(resized)
street_label = tk.Label(address_frame, image=street_pic,borderwidth=0,bg="white")
street_label.pack(pady=(15,0),padx=(0,159))

#street entry
streetentry_frame = tk.Frame(det_frame, bg="white")
streetentry_frame.place(x=145,y=307)
def on_entry_click1(event, entry, placeholder):
    """Function that gets called whenever entry is clicked."""
    if entry.get() == placeholder:
        entry.delete(0, "end")  # delete all the text in the entry
        entry.insert(0, '')  # Insert blank for user input
        entry.config(fg='black')

def on_focusout1(event, entry, placeholder):
    if entry.get() == '':
        entry.insert(0, placeholder)
        entry.config(fg='grey')

street_entry = tk.Entry(streetentry_frame, fg='gray',bg="#D9D9D9",borderwidth=0,font=('helvica',12),width=10)
street_entry.insert(0, 'Street')
street_entry.bind('<FocusIn>', lambda event: on_entry_click1(event, street_entry, 'Street'))
street_entry.bind('<FocusOut>', lambda event: on_focusout1(event, street_entry, 'Street'))
street_entry.pack()

#Barangay frame
brgy_frame = tk.Frame(det_frame, bg="white")
brgy_frame.place(x=350,y=256)

#Barangay label
brgy_label=tk.Label(brgy_frame,text="Barangay",bg='white',font=('times new roman',15,'bold'))
brgy_label.pack(padx=(0,285))

#Barangay picture para soft edges
brgy_pic = Image.open ("Rental Management images/long rectangle.png")
resized = brgy_pic.resize((180,35),Image.Resampling.LANCZOS)
brgy_pic = ImageTk.PhotoImage(resized)
brgy_label = tk.Label(brgy_frame, image=brgy_pic,borderwidth=0,bg="white")
brgy_label.pack(pady=(15,0),padx=(0,199))

#Barangay entry
brgyentry_frame = tk.Frame(det_frame, bg="white")
brgyentry_frame.place(x=360,y=307)

def on_entry_click2(event, entry, placeholder):
    """Function that gets called whenever entry is clicked."""
    if entry.get() == placeholder:
        entry.delete(0, "end")  # delete all the text in the entry
        entry.insert(0, '')  # Insert blank for user input
        entry.config(fg='black')

def on_focusout2(event, entry, placeholder):
    if entry.get() == '':
        entry.insert(0, placeholder)
        entry.config(fg='grey')

brgy_entry = tk.Entry(brgyentry_frame, fg='gray',bg="#D9D9D9",borderwidth=0,font=('helvica',12),width=10)
brgy_entry.insert(0, 'Barangay')
brgy_entry.bind('<FocusIn>', lambda event: on_entry_click2(event, brgy_entry, 'Barangay'))
brgy_entry.bind('<FocusOut>', lambda event: on_focusout2(event, brgy_entry, 'Barangay'))
brgy_entry.pack()


#City frame
city_frame = tk.Frame(det_frame, bg="white")
city_frame.place(x=560,y=256)

#City label
city_label=tk.Label(city_frame,text="City",bg='white',font=('times new roman',15,'bold'))
city_label.pack(padx=(0,335))

#City picture para soft edges
city_pic = Image.open ("Rental Management images/long rectangle.png")
resized = city_pic.resize((180,35),Image.Resampling.LANCZOS)
city_pic = ImageTk.PhotoImage(resized)
city_label = tk.Label(city_frame, image=city_pic,borderwidth=0,bg="white")
city_label.pack(pady=(15,0),padx=(0,199))

#city entry
cityentry_frame = tk.Frame(det_frame, bg="white")
cityentry_frame.place(x=570,y=307)

def on_entry_click3(event, entry, placeholder):
    """Function that gets called whenever entry is clicked."""
    if entry.get() == placeholder:
        entry.delete(0, "end")  # delete all the text in the entry
        entry.insert(0, '')  # Insert blank for user input
        entry.config(fg='black')

def on_focusout3(event, entry, placeholder):
    if entry.get() == '':
        entry.insert(0, placeholder)
        entry.config(fg='grey')

city_entry = tk.Entry(cityentry_frame, fg='gray',bg="#D9D9D9",borderwidth=0,font=('helvica',12),width=10)
city_entry.insert(0, 'City')
city_entry.bind('<FocusIn>', lambda event: on_entry_click3(event, city_entry, 'City'))
city_entry.bind('<FocusOut>', lambda event: on_focusout3(event, city_entry, 'City'))
city_entry.pack()

#Province frame
prov_frame = tk.Frame(det_frame, bg="white")
prov_frame.place(x=780,y=256)

#Province label
prov_label=tk.Label(prov_frame,text="Province",bg='white',font=('times new roman',15,'bold'))
prov_label.pack(padx=(0,302))

#Province picture para soft edges
prov_pic = Image.open ("Rental Management images/long rectangle.png")
resized = prov_pic.resize((180,35),Image.Resampling.LANCZOS)
prov_pic = ImageTk.PhotoImage(resized)
prov_label = tk.Label(prov_frame, image=prov_pic,borderwidth=0,bg="white")
prov_label.pack(pady=(15,0),padx=(0,199))

#Province entry
proventry_frame = tk.Frame(det_frame, bg="white")
proventry_frame.place(x=790,y=307)

def on_entry_click4(event, entry, placeholder):
    """Function that gets called whenever entry is clicked."""
    if entry.get() == placeholder:
        entry.delete(0, "end")  # delete all the text in the entry
        entry.insert(0, '')  # Insert blank for user input
        entry.config(fg='black')

def on_focusout4(event, entry, placeholder):
    if entry.get() == '':
        entry.insert(0, placeholder)
        entry.config(fg='grey')

prov_entry = tk.Entry(proventry_frame, fg='gray',bg="#D9D9D9",borderwidth=0,font=('helvica',12),width=10)
prov_entry.insert(0, 'Province')
prov_entry.bind('<FocusIn>', lambda event: on_entry_click4(event, prov_entry, 'Province'))
prov_entry.bind('<FocusOut>', lambda event: on_focusout4(event, prov_entry, 'Province'))
prov_entry.pack()

#Zip code frame
zip_frame = tk.Frame(det_frame, bg="white")
zip_frame.place(x=1000,y=256)

#Zip code label
zip_label=tk.Label(zip_frame,text="Zip Code",bg='white',font=('times new roman',15,'bold'))
zip_label.pack(padx=(0,240))

#Zip code picture para soft edges
zip_pic = Image.open ("Rental Management images/small rectangle.png")
resized = zip_pic.resize((100,35),Image.Resampling.LANCZOS)
zip_pic = ImageTk.PhotoImage(resized)
zip_label = tk.Label(zip_frame, image=zip_pic,borderwidth=0,bg="white")
zip_label.pack(pady=(15,0),padx=(0,220))

#Zip code  entry
zipentry_frame = tk.Frame(det_frame, bg="white")
zipentry_frame.place(x=1010,y=307)
def on_entry_click5(event, entry):
    """Function that gets called whenever entry is clicked."""
    if entry.get() == 'Zip Code':
        entry.delete(0, "end")  # delete all the text in the entry
        entry.insert(0, '')  # Insert blank for user input
        entry.config(fg='black')
def on_focusout5(event, entry):
    if entry.get() == '':
        entry.insert(0, 'Zip Code')
        entry.config(fg='grey')

zip_entry = tk.Entry(zipentry_frame, fg='gray',bg="#D9D9D9",borderwidth=0,font=('helvica',12),width=10)
zip_entry.insert(0, 'Zip Code')
zip_entry.bind('<FocusIn>', lambda event: on_entry_click4(event, zip_entry, 'Zip Code'))
zip_entry.bind('<FocusOut>', lambda event: on_focusout4(event, zip_entry, 'Zip Code'))
zip_entry.pack()

# Lease Agreement Label
leaseAgreement_frame = tk.Frame(det_frame, bg="white")
leaseAgreement_frame.place(x=120,y=356)
leaseAgreement_label=tk.Label(leaseAgreement_frame,text="Lease Agreement",bg='white',font=('times new roman',17,'bold'))
leaseAgreement_label.pack(padx=(0,280))

# Lease Term Start date label
strt_frame = tk.Frame(det_frame, bg="white")
strt_frame.place(x=130,y=400)
strt_label=tk.Label(strt_frame,text="Lease Term Start Date",bg='white',font=('times new roman',15,'bold'))
strt_label.pack(padx=(0,280))

#Lease Term Start Date entry
strtEntry_frame = tk.Frame(det_frame, height=10, width=500,bg="white",borderwidth=0)
strtEntry_frame.place(x=140,y=445)

strtEntry= DateEntry(strtEntry_frame, font=('helvica',12))
strtEntry.pack()

#Lease Term End Date label
end_frame = tk.Frame(det_frame, bg="white")
end_frame.place(x=355,y=400)

end_label=tk.Label(end_frame,text="Lease Term End Date",bg='white',font=('times new roman',15,'bold'))
end_label.pack(padx=(0,280))

#Lease Term End Date entry
endEntry_frame = tk.Frame(det_frame, height=10, width=500,bg="white",borderwidth=0)
endEntry_frame.place(x=365,y=445)

endEntry= DateEntry(endEntry_frame, font=('helvica',12))
endEntry.pack()

#Downpayment label
down_frame = tk.Frame(det_frame, bg="white")
down_frame.place(x=570,y=400)
down_label=tk.Label(down_frame,text="Down Payment",bg='white',font=('times new roman',15,'bold'))
down_label.pack(padx=(0,340))

#Downpayment picture para soft edges
down_pic = Image.open ("Rental Management images/long rectangle.png")
resized = down_pic.resize((180,35),Image.Resampling.LANCZOS)
down_pic = ImageTk.PhotoImage(resized)
down_label = tk.Label(down_frame, image=down_pic,borderwidth=0,bg="white")
down_label.pack(pady=(15,0),padx=(0,298))

#Downpayment entry
downentry_frame = tk.Frame(det_frame, bg="white")
downentry_frame.place(x=590,y=450)
down=tk.Entry(downentry_frame,background="#D9D9D9",width=10,borderwidth=0,font=("helvica",15))
down.pack()

#1 month advance label
mnth_frame = tk.Frame(det_frame, bg="white")
mnth_frame.place(x=130,y=500)
mnth_label=tk.Label(mnth_frame,text="1 Month Advance",bg='white',font=('times new roman',15,'bold'))
mnth_label.pack(padx=(0,320))

#1 Month advance picture para soft edges
mnth_pic = Image.open ("Rental Management images/long rectangle.png")
resized = mnth_pic.resize((180,35),Image.Resampling.LANCZOS)
mnth_pic = ImageTk.PhotoImage(resized)
mnth_label = tk.Label(mnth_frame, image=mnth_pic,borderwidth=0,bg="white")
mnth_label.pack(pady=(15,0),padx=(0,298))

#1 month advance entry
mnthentry_frame = tk.Frame(det_frame, bg="white")
mnthentry_frame.place(x=140,y=550)
mnth=tk.Entry(mnthentry_frame,background="#D9D9D9",width=10,borderwidth=0,font=("helvica",15))
mnth.pack()


#1 month deposite advance label
depo_frame = tk.Frame(det_frame, bg="white")
depo_frame.place(x=355,y=500)
depo_label=tk.Label(depo_frame,text="1 Month Deposite",bg='white',font=('times new roman',15,'bold'))
depo_label.pack(padx=(0,320))

#1 Month deposite picture para soft edges
depo_pic = Image.open ("Rental Management images/long rectangle.png")
resized = depo_pic.resize((180,35),Image.Resampling.LANCZOS)
depo_pic = ImageTk.PhotoImage(resized)
depo_label = tk.Label(depo_frame, image=depo_pic,borderwidth=0,bg="white")
depo_label.pack(pady=(15,0),padx=(0,298))

#1 month deposite entry
depoentry_frame = tk.Frame(det_frame, bg="white")
depoentry_frame.place(x=365,y=550)
depo=tk.Entry(depoentry_frame,background="#D9D9D9",width=10,borderwidth=0,font=("helvica",15))
depo.pack()

# Payment Status label
paymentStatus_frame = tk.Frame(root,height=10,width=500,bg='white',borderwidth=0)
paymentStatus_frame.place(x=790,y=550)
paymentStatus_label=tk.Label(paymentStatus_frame,text="Payment Status",bg='white',font=('times new roman',15,'bold'))
paymentStatus_label.pack()

# Payment Status frame
payStat_frame= tk.Frame(root,height=5,width=500,bg='white',borderwidth=0)
payStat_frame.place(x=790,y=595)

# Payment Status frame
payStatMenu_frame= tk.Frame(root, height=10, width=500,bg='#D9D9D9',borderwidth=0)
payStatMenu_frame.place(x=800,y=597)

# Payment Status menu
selected_option = tk.StringVar()
selected_option.set(" ")
options = ["Paid", "Pending"]
option_menu = tk.OptionMenu(payStatMenu_frame, selected_option, *options)
option_menu.configure(borderwidth=0,width=13,font=('Helvica',12),bg='#D9D9D9',highlightbackground='#D9D9D9',)
option_menu.pack()

# Payment Status picture para soft edges
payStat_pic = Image.open ("Rental Management images/long rectangle.png")
resized = payStat_pic.resize((180,35),Image.Resampling.LANCZOS)
payStat_pic = ImageTk.PhotoImage(resized)
payStat_label = tk.Label(payStat_frame, image=payStat_pic,borderwidth=0,bg="white")
payStat_label.pack(padx=(0,298))

#Total label
totalPay_frame = tk.Frame(det_frame, bg="white")
totalPay_frame.place(x=900,y=536)
totalPay = tk.Label(totalPay_frame,text="Total: ",font=("times new roman",20,"bold"), pady= 5, padx= 15,background= "white",borderwidth=0)
totalPay.pack()

# Total Price label
totalPrice_frame = tk.Frame(det_frame, bg="white")
totalPrice_frame.place(x=990,y=530)
totalPrice = tk.Button(totalPrice_frame,text="₱123,456",font=("times new roman",20,"bold", "underline"),background= "white",borderwidth=0)
totalPrice.pack()

#Add New Rental frame
add_frame = tk.Frame(det_frame, bg="white")
add_frame.place(x=945,y=590)

add = tk.Button(add_frame,text="Add",font=("times new roman",14,"bold"), pady= 5, padx= 15,background= "#2C6FBC",width=10)
add.pack()



root.mainloop()