import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import font


# Root properties
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Snugspaces")

    # Window dimensions
    w = 650
    h = 450

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
    root.configure(background='#4b7cdc')

# Back button
back_frame = tk.Frame(root, bg = 'white')
back_frame.place(x = "10", y = "10")

back_label = tk.Label(back_frame, text = " Back", bg = '#4b7cdc', fg = 'white', font = ('times new roman', 12, 'bold'))
back_label.pack()

# Create Account label
add_frame = tk.Frame(root, bg="white")
add_frame.place(x="210", y = "60")

add_label = tk.Label(add_frame, text = "Create Account", bg = '#4b7cdc', fg = 'white', font = ('times new roman', 24, 'bold'))
add_label.pack()

# Username label
un_frame = tk.Frame(root, bg="#4b7cdc")
un_frame.place(x=90,y=130)
un_label=tk.Label(un_frame,text="Username", bg = '#4b7cdc', fg = 'white' , font=('times new roman',14,'bold'))
un_label.pack()

# Username picture para soft edges
un_pic = Image.open ("Rental Management images/long rectangle.png")
resized = un_pic.resize((220,25),Image.Resampling.LANCZOS)
un_pic = ImageTk.PhotoImage(resized)
un_label = tk.Label(un_frame, image=un_pic,borderwidth=0,bg="#4b7cdc")
un_label.pack(padx = (120, 0))

# Username entry
unEntry_frame = tk.Frame(root, bg="#4b7cdc")
unEntry_frame.place(x=220,y=160)
userName = tk.Entry(unEntry_frame,background="#D9D9D9",width=20,borderwidth=0,font=("helvica",13))
userName.pack()

# Password label
pass_frame = tk.Frame(root, bg="#4b7cdc")
pass_frame.place(x=90,y=200)
pass_label=tk.Label(pass_frame,text="Password", bg = '#4b7cdc', fg = 'white' , font=('times new roman',14,'bold'))
pass_label.pack()

# Password picture para soft edges
pass_pic = Image.open ("Rental Management images/long rectangle.png")
resized = pass_pic.resize((220,25),Image.Resampling.LANCZOS)
pass_pic = ImageTk.PhotoImage(resized)
pass_label = tk.Label(pass_frame, image=pass_pic,borderwidth=0,bg="#4b7cdc")
pass_label.pack(padx = (120, 0))

# Password entry
passEntry_frame = tk.Frame(root, bg="#4b7cdc")
passEntry_frame.place(x=220,y=230)
password = tk.Entry(passEntry_frame,background="#D9D9D9",width=20,borderwidth=0,font=("helvica",13))
password.pack()

# Confirm Password label
confirmPass_frame = tk.Frame(root, bg="#4b7cdc")
confirmPass_frame.place(x=166,y=270)
confirmPass_label=tk.Label(confirmPass_frame,text="Confirm Password", bg = '#4b7cdc', fg = 'white' , font=('times new roman',14,'bold'))
confirmPass_label.pack()

# Confirm Password picture para soft edges
confirmPass_pic = Image.open ("Rental Management images/long rectangle.png")
resized = confirmPass_pic.resize((220,25),Image.Resampling.LANCZOS)
confirmPass_pic = ImageTk.PhotoImage(resized)
confirmPass_label = tk.Label(confirmPass_frame, image=confirmPass_pic,borderwidth=0,bg="#4b7cdc")
confirmPass_label.pack(padx = (45, 0))

# Confirm Password entry
confirmPassEntry_frame = tk.Frame(root, bg="#4b7cdc")
confirmPassEntry_frame.place(x=220,y=300)
confirmPassword = tk.Entry(confirmPassEntry_frame,background="#D9D9D9",width=20,borderwidth=0,font=("helvica",13))
confirmPassword.pack()

# Credentials error
passError_frame = tk.Frame(root, bg="#4b7cdc")
passError_frame.place(x=210, y=335)
passError_label = tk.Label(passError_frame, text="You have entered invalid credentials.",
                                  bg='#4b7cdc', fg='red', font=('times new roman', 12))
passError_label.pack_forget()  # Initially hide the error label

# Duplicate username error
usernameError_frame = tk.Frame(root, bg="#4b7cdc")
usernameError_frame.place(x=210, y=335)
usernameError_label = tk.Label(usernameError_frame, text="You have entered invalid credentials.",
                                  bg='#4b7cdc', fg='red', font=('times new roman', 12))
usernameError_label.pack_forget()  # Initially hide the error label

# Existing Account error
accountExistError_frame = tk.Frame(root, bg="#4b7cdc")
accountExistError_frame.place(x=210, y=335)
accountExistError_label = tk.Label(accountExistError_frame, text="Account already exist",
                                  bg='#4b7cdc', fg='red', font=('times new roman', 12))
accountExistError_label.pack_forget()  # Initially hide the error label

# Create Account button
def on_button_click():
    # Condition when entered username is already in the database

    # Condition when all credentials are already in the system

    # Condition when entered password does not match
    if password.get() != confirmPassword.get():
        passError_label.pack()  # Show the error label
        password.delete(0, tk.END)  # Clear the password field
        confirmPassword.delete(0, tk.END)  # Clear the confirm password field
    else:
        passError_label.pack_forget()  # Hide the error label if passwords match
        # Add further logic for account creation here

# Create Account button
buttonCreate_frame = tk.Frame(root)
buttonCreate_frame.place(x=275, y=375)
createAcc_button = tk.Button(buttonCreate_frame, text='Create', fg='white', bg='#2c6fbc',
                             font=(("Times New Roman"), 14), width=8, command=on_button_click)
createAcc_button.pack()

root.mainloop()