import tkinter as tk
from PIL import ImageTk, Image

def create_dashboard(parent, controller):
    frame = tk.Frame(parent)
    frame.grid(row=0, column=0, sticky="nsew")
    frame.configure(background='#3A98CC')


    return frame