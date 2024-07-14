import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk

def create_room(parent, controller):
    frame = tk.Frame(parent)
    frame.grid(row=0, column=0, sticky="nsew")
    frame.configure(background='#3A98CC')

    room_frame = tk.Frame(frame, height=10, width=500)
    room_frame.place(x=400, y=60)

    room_label = tk.Label(room_frame, text="Rooms", bg='#3A98CC', font=('times new roman', 20, 'bold'))
    room_label.pack()

    return frame
