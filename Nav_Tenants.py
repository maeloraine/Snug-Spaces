import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
from AddRentals_Db import fetch_all_tenants
from UD_Tenant_Data import UD_Tenant

class TenantManagement(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='#3A98CC')
        self.controller = controller
        self.selected_item = None

        # Tenant Label
        self.tenant_label = tk.Label(self, text="Tenants", bg='#3A98CC', font=('Times New Roman', 30, 'bold'))
        self.tenant_label.place(x=100, y=20)

        # Search Tenant Entry
        self.search_entry = tk.Entry(self, background="white", width=50, borderwidth=2, font=("Times New Roman", 13))
        self.search_entry.place(x=290, y=112)

        # Search Button
        search_img = Image.open("Rental Management images/search.png")
        resized_search = search_img.resize((30, 30), Image.LANCZOS)
        self.search_img_tk = ImageTk.PhotoImage(resized_search)
        self.search_button = tk.Button(self, image=self.search_img_tk, borderwidth=0, bg='#3A98CC', relief='raised', command=self.search_tenants)
        self.search_button.image = self.search_img_tk
        self.search_button.place(x=760, y=108)

        # Listbox Frame
        listbox_frame = tk.Frame(self, bg='#3A98CC')
        listbox_frame.place(x=10, y=170, width=1180, height=500)

        # Tenant Table (Treeview)
        self.tree = ttk.Treeview(listbox_frame, columns=("Tenant_ID", "Name", "Birthday", "Email", "Contact No", "Gender",
                                                        "Full Address", "Zip Code"),
                                 show="headings")
        self.tree.place(relwidth=1, relheight=1)

        # Configure Treeview Columns and Headings
        column_headings = ["Tenant_ID", "Name", "Birthday", "Email", "Contact No", "Gender",
                           "Full Address", "Zip Code"]

        for col, heading in zip(self.tree['columns'], column_headings):
            self.tree.heading(col, text=heading)
            if heading == "Tenant_ID":
                self.tree.column(col, width=0, anchor='center', stretch=False)
            else:
                self.tree.column(col, width=100, anchor='center', stretch=True)

        # Add scrollbar to the Treeview
        scrollbar = ttk.Scrollbar(listbox_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

        # Populate Treeview with data from database
        self.populate_tree()

        # Bind selection event to on_selected_user
        self.tree.bind('<<TreeviewSelect>>', self.on_selected_user)

        # Edit Tenant Button
        self.edit_button = tk.Button(self, text="Edit Tenant", font=("Times New Roman", 12, "bold"), pady=5, padx=20,
                                     bg="#2C6FBC", width=10, command=self.open_update_tenant_window)
        self.edit_button.place(x=1000, y=735)

    def populate_tree(self):
        print("Populating Treeview...")
        # Clear existing data from Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Fetch updated data from database
        tenant_data = fetch_all_tenants()

        # Insert updated data into Treeview
        for tenant in tenant_data:
            full_name = f"{tenant[3]}, {tenant[1]} {tenant[2]}"
            full_address = (f"{tenant[8]} street, Brgy. {tenant[9]}, {tenant[10]} City, "
                            f"{tenant[11]}")  # Street, Barangay, City, Province
            values = (tenant[0], full_name, tenant[4], tenant[5], tenant[6], tenant[7], full_address, tenant[12])
            # for verification in terminal
            print(f"Inserting tenant: {values}")
            self.tree.insert('', 'end', values=values)

    def on_selected_user(self, event):
        self.selected_item = self.tree.selection()[0] if self.tree.selection() else None

    def open_update_tenant_window(self):
        if self.selected_item:
            # Retrieve selected item data
            item_data = self.tree.item(self.selected_item)['values']
            new_window = tk.Toplevel(self)
            UD_Tenant(new_window, item_data, self.tree)
        else:
           messagebox.showerror('Error', 'No Tenant Selected!')

    def search_tenants(self):
        search_text = self.search_entry.get().strip().lower()

        # Clear existing data from Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch updated data from database (or wherever your data source is)
        tenant_data = fetch_all_tenants()  # Replace with your actual fetch function

        if not search_text:
            # If search text is empty, populate Treeview with all data
            for tenant in tenant_data:
                full_name = f"{tenant[3]}, {tenant[1]} {tenant[2]}"
                full_address = (f"{tenant[8]} street, Brgy. {tenant[9]}, {tenant[10]} City, "
                                f"{tenant[11]}")  # Street, Barangay, City, Province
                values = (tenant[0], full_name, tenant[4], tenant[5], tenant[6], tenant[7], full_address, tenant[12])
                self.tree.insert('', 'end', values=values)
        else:
            # Filter data based on search_text
            filtered_tenants = [tenant for tenant in tenant_data if search_text in str(tenant).lower()]

            # Insert filtered data into Treeview
            for tenant in filtered_tenants:
                full_name = f"{tenant[3]}, {tenant[1]} {tenant[2]}"
                full_address = (f"{tenant[8]} street, Brgy. {tenant[9]}, {tenant[10]} City, "
                                f"{tenant[11]}")  # Street, Barangay, City, Province
                values = (tenant[0], full_name, tenant[4], tenant[5], tenant[6], tenant[7], full_address, tenant[12])
                self.tree.insert('', 'end', values=values)
