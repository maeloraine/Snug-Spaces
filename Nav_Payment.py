import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
from datetime import datetime
from AddRentals_Db import fetch_payment, payment_sum
from AddPayment import Add_Payment

class Payment(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='#3A98CC')
        self.create_widgets()
        self.selected_item = None
        self.populate_tree()

    def create_widgets(self):
        # Payment label
        payment_label = tk.Label(self, text="Payments", bg='#3A98CC', font=('Times New Roman', 30, 'bold'))
        payment_label.place(x=100, y=20)

        # Search Entry
        self.search_entry = tk.Entry(self, background="white", width=50, borderwidth=2, font=("Times New Roman", 13), relief='raised')
        self.search_entry.place(x=350, y=112)

        # Search Button
        search_img = Image.open("Rental Management images/search.png")
        resized_search_img = search_img.resize((30, 30), Image.LANCZOS)
        search_img_tk = ImageTk.PhotoImage(resized_search_img)
        search_button = tk.Button(self, image=search_img_tk, borderwidth=0, bg='#3A98CC', relief='raised', command=self.search_payments)
        search_button.image = search_img_tk
        search_button.place(x=790, y=108)

        # Payment list
        frame_width = 1000
        frame_height = 500

        payment_frame = tk.Frame(self, width=frame_width, height=frame_height, relief="raised", borderwidth=5)
        payment_frame.pack_propagate(False)
        payment_frame.place(x=110, y=170)

        scrollbar = ttk.Scrollbar(payment_frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        # Treeview (Table) for Payments
        self.tree = ttk.Treeview(payment_frame, columns=("Tenant Name", "Amount", "Payment Date", "Total Rent Due","Balance"),
                                 show="headings")
        self.tree.place(relwidth=1, relheight=1)
        self.tree.bind('<<TreeviewSelect>>', self.on_selected_user)  # copy
        # Configure Treeview Columns and Headings
        column_headings = ["Tenant Name", "Amount", "Payment Date", "Total Rent Due", "Balance"]

        for col, heading in zip(self.tree['columns'], column_headings):
            self.tree.heading(col, text=heading)
            self.tree.column(col, width=150, anchor='center', stretch=True)

        # Edit Payment Button
        edit_button = tk.Button(self, text="Edit Payment", font=("times new roman", 12, "bold"), pady=5, padx=20,
                                bg="#2C6FBC", width=10, command=self.open_add_payment_window)
        edit_button.place(x=820, y=710)

        # Generate Invoice Button (Placeholder, add functionality as needed)
        generate_invoice_button = tk.Button(self, text="Generate Invoice", font=("times new roman", 12, "bold"),
                                            pady=5, padx=20, bg="#2C6FBC", width=10)
        generate_invoice_button.place(x=970, y=710)

    def populate_tree(self):
        print("Populating Treeview...")
        # Clear existing data from Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch updated data from database
        payments = fetch_payment()


        # Insert updated data into Treeview
        for payment in payments:
            last_name, first_name, middle_name, amount, payment_date = payment
            full_name = f"{last_name}, {first_name} {middle_name if middle_name else ''}"
            values = [full_name, amount, payment_date]
            print(f"Inserting payments: {values}")
            self.tree.insert('', 'end', values=values)

    def on_selected_user(self, event):
        self.selected_item = self.tree.selection()[0] if self.tree.selection() else None

    # def compute_months_between_dates(self, start_date_str, end_date_str):
    #     # Function to compute the number of months between two dates (not used in searching)
    #     start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
    #     end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
    #     start_month = start_date.year * 12 + start_date.month
    #     end_month = end_date.year * 12 + end_date.month
    #     total_months = end_month - start_month + 1
    #     return total_months

    def open_add_payment_window(self):
        if self.selected_item:
            # Retrieve selected item data
            item_data = self.tree.item(self.selected_item)['values']
            tenant_name, amount, payment_date = item_data

            # Open Add_Payment window with selected item data
            new_window = tk.Toplevel(self)
            Add_Payment(new_window, tenant_name, amount, payment_date, self.tree)
        else:
            messagebox.showerror('Error', 'No Payment Information Selected!')

    def search_payments(self):
        search_text = self.search_entry.get().strip().lower()

        # Clear existing data from Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch updated data from database (replace with your actual fetch function)
        payments = fetch_payment()  # Replace with your actual fetch function

        # Filter payments based on search_text
        filtered_payments = [payment for payment in payments if search_text in str(payment).lower()]

        # Insert filtered data into Treeview
        for payment in filtered_payments:
            last_name, first_name, middle_name, amount, payment_date = payment
            full_name = f"{last_name}, {first_name} {middle_name if middle_name else ''}"
            values = [full_name, amount, payment_date]
            print(f"Inserting payments: {values}")
            self.tree.insert('', 'end', values=values)

    def get_search_text(self):
        return self.search_entry.get()