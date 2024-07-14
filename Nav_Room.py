import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
from AddRoom import AddRoomApp  # Assuming you have these modules defined
from AddRentals_Db import fetch_all_rooms, update_room_status, delete_room
from EditRoom import EditRoomApp

class Room(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='#3A98CC')
        self.create_widgets()
        self.selected_item = None
        self.radio_var = None  # Initialize the radio buttons as unclicked

    def create_widgets(self):
        # Room label
        room_label = tk.Label(self, text="Room", bg='#3A98CC', font=('Times New Roman', 30, 'bold'))
        room_label.place(x=100, y=20)

        # Search Room Entry
        self.search_entry = tk.Entry(self, background="white", width=50, borderwidth=2, font=("Times New Roman", 13), relief='raised')
        self.search_entry.place(x=290, y=112)

        # Search button
        search_img = Image.open("Rental Management images/search.png")
        resized_search_img = search_img.resize((30, 30), Image.LANCZOS)
        search_img_tk = ImageTk.PhotoImage(resized_search_img)
        self.search_button = tk.Button(self, image=search_img_tk, borderwidth=0, bg='#3A98CC', relief='raised', command=self.search_rooms)
        self.search_button.image = search_img_tk
        self.search_button.place(x=760, y=108)

        # Room table
        frame_width = 1000
        frame_height = 550

        room_frame = tk.Frame(self, width=frame_width, height=frame_height, relief="raised", borderwidth=5, bg='white')
        room_frame.pack_propagate(False)
        room_frame.place(x=100, y=170)

        # Listbox Frame
        listbox_frame = tk.Frame(room_frame, bg='#3A98CC')
        listbox_frame.pack(fill='both', expand=True)

        # Room Table (Treeview)
        self.tree = ttk.Treeview(listbox_frame, columns=("Room ID", "Room No", "Room Rate", "Room Status"),
                                 show="headings", selectmode="browse")
        self.tree.pack(side='left', fill='both', expand=True)

        # Configure Treeview Columns and Headings
        column_headings = ["Room ID", "Room No", "Room Rate", "Room Status"]

        for col, heading in zip(self.tree['columns'], column_headings):
            self.tree.heading(col, text=heading)
            if heading == "Room ID":
                self.tree.column(col, width=0, anchor='center', stretch=False)
            else:
                self.tree.column(col, width=200, anchor='center', stretch=True)

        # Add scrollbar to the Treeview
        scrollbar = ttk.Scrollbar(listbox_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Populate Treeview with data from database
        self.populate_tree()

        # Bind selection event to on_selected_user
        self.tree.bind('<<TreeviewSelect>>', self.on_selected_user)

        # Edit Room Button
        edit_button = tk.Button(self, text="Edit Room", font=("Times New Roman", 12, "bold"), pady=5, padx=20,
                                bg="#2C6FBC", width=10, command=self.open_update_room_window)
        edit_button.place(x=810, y=735)

        # Add Room button
        addRoom_button = tk.Button(self, text="Add Room", font=("times new roman", 12, "bold"), pady=5, padx=20,
                                   bg="#2C6FBC", width=10, command=self.open_add_room_window)
        addRoom_button.place(x=960, y=735)

        # Delete Room Button
        deleteRoom_button = tk.Button(self, text="Delete Room", font=("Times New Roman", 12, "bold"), pady=5, padx=20,
                                bg="#2C6FBC", width=10, command=self.delete_record)
        deleteRoom_button.place(x=660, y=735)

    def delete_record(self):
        selected_item = self.tree.focus()  # Get the selected item in the treeview
        if not selected_item:
            messagebox.showerror("Error", "Please select a record to delete.")
            return

        confirmation = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this record?")

        if confirmation:
            # User clicked "Yes"
            item_values = self.tree.item(selected_item, "values")
            room_id = item_values[0]  # Assuming room ID is the first column in your treeview
            # Perform deletion in database
            delete_room(room_id)  # Example function to delete room from database

            # Update the treeview after deletion
            self.tree.delete(selected_item)
            messagebox.showinfo("Deleted", "Record deleted successfully.")
        else:
            # User clicked "No"
            messagebox.showinfo("Delete", "Deletion cancelled.")

    def populate_tree(self):
        print("Populating Treeview...")
        # Clear existing data from Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Fetch updated data from database
        room_data = fetch_all_rooms()

        # Insert data into Treeview
        for room in room_data:
            values = (room[0], room[1], room[2], room[3])
            print(f"Inserting room: {values}")
            self.tree.insert('', 'end', values=values)

    def on_selected_user(self, event):
        self.selected_item = self.tree.selection()[0] if self.tree.selection() else None

    def open_update_room_window(self):
        if self.selected_item:
            # Retrieve selected item data
            item_data = self.tree.item(self.selected_item)['values']
            new_window = tk.Toplevel(self)
            EditRoomApp(new_window, item_data, self.tree)
        else:
            messagebox.showerror('Error', 'No Room Selected!')

    def open_add_room_window(self):
        new_window = tk.Toplevel(self)
        add_room_view = AddRoomApp(new_window, self.tree)

    def search_rooms(self):
        search_text = self.search_entry.get().strip().lower()

        # Clear existing data from Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch updated data from database (or wherever your data source is)
        room_data = fetch_all_rooms()  # Replace with your actual fetch function

        if not search_text:
            # If search text is empty, populate Treeview with all data
            for room in room_data:
                values = (room[0], room[1], room[2], room[3])
                self.tree.insert('', 'end', values=values)
        else:
            # Filter data based on search_text
            filtered_rooms = [room for room in room_data if search_text in str(room).lower()]

            # Insert filtered data into Treeview
            for room in filtered_rooms:
                values = (room[0], room[1], room[2], room[3])
                self.tree.insert('', 'end', values=values)

    def update_room_status(self, room_no, status):
        update_room_status(room_no, status)
        self.populate_tree()
