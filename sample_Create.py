import tkinter as tk
from tkinter import ttk
import sqlite3

# Database setup
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT
    )
''')

# Sample data insertion
cursor.execute('INSERT INTO users (first_name, last_name) VALUES (?, ?)', ('John', 'Doe'))
cursor.execute('INSERT INTO users (first_name, last_name) VALUES (?, ?)', ('Jane', 'Smith'))
conn.commit()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Treeview Example")
        self.geometry("400x300")

        # Treeview setup
        self.tree = ttk.Treeview(self, columns=("first_name", "last_name"), show="headings")
        self.tree.heading("first_name", text="First Name")
        self.tree.heading("last_name", text="Last Name")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.populate_treeview()

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.update_button = tk.Button(self, text="Update Selected", command=self.open_update_window)
        self.update_button.pack(pady=10)

        self.selected_item = None

    def populate_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        cursor.execute("SELECT * FROM users")
        for row in cursor.fetchall():
            self.tree.insert("", tk.END, values=(row[1], row[2]), iid=row[0])

    def on_tree_select(self, event):
        selected_item = self.tree.selection()[0]
        self.selected_item = self.tree.item(selected_item, "values")
        self.selected_item_id = selected_item

    def open_update_window(self):
        if self.selected_item:
            self.update_window = tk.Toplevel(self)
            self.update_window.title("Update User")
            self.update_window.geometry("300x200")

            tk.Label(self.update_window, text="First Name").pack(pady=5)
            self.first_name_entry = tk.Entry(self.update_window)
            self.first_name_entry.pack(pady=5)
            self.first_name_entry.insert(0, self.selected_item[0])

            tk.Label(self.update_window, text="Last Name").pack(pady=5)
            self.last_name_entry = tk.Entry(self.update_window)
            self.last_name_entry.pack(pady=5)
            self.last_name_entry.insert(0, self.selected_item[1])

            tk.Button(self.update_window, text="Submit", command=self.update_user).pack(pady=20)

    def update_user(self):
        new_first_name = self.first_name_entry.get()
        new_last_name = self.last_name_entry.get()

        cursor.execute('''
            UPDATE users
            SET first_name = ?, last_name = ?
            WHERE id = ?
        ''', (new_first_name, new_last_name, self.selected_item_id))
        conn.commit()

        self.populate_treeview()
        self.update_window.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()

# Close the database connection when done
conn.close()
