import tkinter as tk


# Root properties
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Snugspaces")

    # Window dimensions
    w = 400
    h = 350

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

# Breakdown label
brkdwn_frame = tk.Frame(root)
brkdwn_frame.place(x=100,y=20)
brkdwn_label = tk.Label(brkdwn_frame, text='List of Payments',font=('Times New Roman',20,'bold'),bg='white')
brkdwn_label.pack()

# Down Payment Label
dp_frame = tk.Frame(root)
dp_frame.place(x=40,y=80)
dp_label = tk.Label(dp_frame,text='Down Payment',font=('Times New Roman',15,'bold'),bg='white')
dp_label.pack()

# Down Payment Price
dpnum_frame = tk.Frame(root)
dpnum_frame.place(x=280,y=80)
dpnum_label = tk.Label(dpnum_frame,text='123,456',font=('Times New Roman',15,'bold'),bg='white')
dpnum_label.pack()

# 1 month advance Label
onead_frame = tk.Frame(root)
onead_frame.place(x=40,y=108)
onead_label = tk.Label(onead_frame,text='1 Month Advance',font=('Times New Roman',15,'bold'),bg='white')
onead_label.pack()

# 1 month advance price
adnum_frame = tk.Frame(root)
adnum_frame.place(x=280,y=108)
adnum_label = tk.Label(adnum_frame,text='123,456',font=('Times New Roman',15,'bold'),bg='white')
adnum_label.pack()

# 1 month deposit label
onedep_frame = tk.Frame(root)
onedep_frame.place(x=40,y=120)
onedep_label = tk.Label(onead_frame,text='1 Month Deposite',font=('Times New Roman',15,'bold'),bg='white')
onedep_label.pack()

# 1 month deposit price
depnum_frame = tk.Frame(root)
depnum_frame.place(x=280,y=140)
depnum_label = tk.Label(depnum_frame,text='123,456',font=('Times New Roman',15,'bold', 'underline'),bg='white')
depnum_label.pack()

# total label
tal_frame = tk.Frame(root)
tal_frame.place(x=40,y=180)
tal_label = tk.Label(tal_frame,text='TOTAL',font=('Times New Roman',15,'bold'),bg='white')
tal_label.pack()

# total price
talnum_frame = tk.Frame(root)
talnum_frame.place(x=263,y=180)
talnum_label = tk.Label(talnum_frame,text='₱ 123,456',font=('Times New Roman',15,'bold'),bg='white')
talnum_label.pack()


root.mainloop()