import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from New_AddRental import AddRentalApp
from Edit_Rental import Update_Rental
from AddRentals_Db import fetch_all_rental
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from AddRentals_Db import fetch_all_rental
from New_AddRental import AddRentalApp
from Edit_Rental import Update_Rental

class RentalManagement(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='#3A98CC', pady=45)
        self.controller = controller
        self.selected_item = None

        # Rentals Frame
        rentals_frm = tk.Frame(self, bg='#3A98CC', padx=30)
        rentals_frm.grid(row=0, column=0, sticky=tk.NW, padx=20)  # NW (Northwest) anchors to top-left

        # Rentals label
        rental_lbl = tk.Label(rentals_frm, text="Rentals", bg='#3A98CC', font=('times new roman', 30, 'bold'))
        rental_lbl.pack(anchor=tk.W, padx=0, pady=10)  # Adjust padding here if needed

        # Frame for search entry
        searchRentalEntry_frame = tk.Frame(self, bg='#3A98CC')
        searchRentalEntry_frame.grid(row=1, column=0, padx=25, pady=10, sticky=tk.W)  # Adjust row and column position

        # Search entry widget
        self.searchRentalEntry = tk.Entry(searchRentalEntry_frame, width=50, borderwidth=2, font=("helvetica", 13),
                                         relief='raised')
        self.searchRentalEntry.pack(side=tk.LEFT, padx=(300, 25))  # Adjust other options if needed

        # Search button
        searchRental_img = Image.open("Rental Management images/search.png")  # Adjust path as needed
        resized_searchRental = searchRental_img.resize((30, 30), Image.LANCZOS)
        searchRental_img_tk = ImageTk.PhotoImage(resized_searchRental)
        searchRental_button = tk.Button(searchRentalEntry_frame, image=searchRental_img_tk, borderwidth=0, bg='#3A98CC',
                                        relief='raised', command=self.search_rentals)
        searchRental_button.image = searchRental_img_tk  # Keep a reference to the image to prevent garbage collection
        searchRental_button.pack(side=tk.LEFT)

        frame_width = 1000
        frame_height = 550

        # Listbox Frame
        listbox_frame = tk.Frame(self, bg='#3A98CC', width=frame_width, height=frame_height)
        listbox_frame.pack_propagate(False)
        listbox_frame.grid(row=2, column=0, padx=110, pady=0, sticky=tk.W)

        self.tree = ttk.Treeview(listbox_frame, columns=("Rental ID","Room No.", "Tenant Name", "Lease Start", "Lease End"),
                                 show="headings")
        self.tree.place(relwidth=1, relheight=1)

        # Configure Treeview Columns and Headings
        column_headings = ["Rental ID", "Room No.","Tenant Name", "Lease Start", "Lease End"]

        for col, heading in zip(self.tree['columns'], column_headings):
            self.tree.heading(col, text=heading)
            if heading == "Tenant ID" and heading == "Rental ID":
                self.tree.column(col, width=0, anchor='center', stretch=False)
            else:
                self.tree.column(col, width=100, anchor='center', stretch=True)

        # Create a scrollbar
        scrollbar = ttk.Scrollbar(listbox_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")

        # Pack the Treeview and configure scrollbar
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Bind selection event to on_selected_user
        self.tree.bind('<<TreeviewSelect>>', self.on_selected_user)

        # Edit Rental button
        editRent_button = tk.Button(self, text="Edit Rental", font=("times new roman", 12, "bold"), pady=5,
                                    padx=20, bg="#2C6FBC", width=10, command=self.open_update_room_window)
        editRent_button.grid(row=3, column=0, padx=825, pady=10)

        # Add Rental button
        addRent_button = tk.Button(self, text="Add Rental", font=("times new roman", 12, "bold"), pady=5,
                                   padx=20, bg="#2C6FBC", width=10, command=self.open_add_rental_window)
        addRent_button.grid(row=3, column=0, padx=(320, 20), pady=10)

        # Insert sample data into the Treeview
        self.populate_tree()

    def populate_tree(self):
        print("Populating Treeview...")
        # Clear existing data from Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Fetch updated data from database
        rentals = fetch_all_rental()

        # Insert updated data into Treeview
        for rental in rentals:
            fullName = f"{rental[2]}, {rental[3]} {rental[4]}"
            values = [rental[0], rental[1], fullName, rental[5], rental[6]]
            print(f"Inserting rentals: {rental}")
            self.tree.insert('', 'end', values=values)

    def on_selected_user(self, event):
        self.selected_item = self.tree.selection()[0] if self.tree.selection() else None

    def open_add_rental_window(self):
        new_window = tk.Toplevel(self)
        add_rental_view = AddRentalApp(new_window, self.tree)

    def open_update_room_window(self):
        if self.selected_item:
            item_data = self.tree.item(self.selected_item)['values']
            new_window = tk.Toplevel(self)
            Update_Rental(new_window, item_data, self.tree)
        else:
            messagebox.showerror('Error', 'No Rental Information Selected!')

    def search_rentals(self):
        search_text = self.searchRentalEntry.get().strip().lower()

        # Clear existing data from Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch updated data from database
        rentals = fetch_all_rental()  # Replace with your actual fetch function

        if not search_text:
            # If search text is empty, populate Treeview with all data
            for rental in rentals:
                fullName = f"{rental[2]}, {rental[3]} {rental[4]}"
                values = [rental[0], rental[1], fullName, rental[5], rental[6]]
                self.tree.insert('', 'end', values=values)
        else:
            # Filter data based on search_text
            filtered_rentals = [rental for rental in rentals if search_text in str(rental).lower()]

            # Insert filtered data into Treeview
            for rental in filtered_rentals:
                fullName = f"{rental[2]}, {rental[3]} {rental[4]}"
                values = [rental[0], rental[1], fullName, rental[5], rental[6]]
                self.tree.insert('', 'end', values=values)

    def open_rental_management_view(self):
        self.controller.show_frame("RentalManagement")  # Assuming you have a method to switch frames in your controller