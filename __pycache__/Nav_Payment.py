import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk

def create_payment(parent, controller):
    frame = tk.Frame(parent)
    frame.grid(row=0, column=0, sticky="nsew")
    frame.configure(background='#3A98CC')

    return frame