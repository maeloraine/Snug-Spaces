import tkinter as tk
from PIL import ImageTk, Image

# Root properties
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Snugspaces")

    # Window dimensions
    w = 800
    h = 600

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

# Logo picture
Logo_pic = Image.open ("Rental Management images/SnugSpaceslogo.png")
resized = Logo_pic.resize((300,300),Image.Resampling.LANCZOS)
Logo_pic = ImageTk.PhotoImage(resized)

Login_frame = tk.Frame(root,bg="white")
Login_frame.place(relwidth=1, relheight=1)
Login_label = tk.Label(Login_frame, image=Logo_pic,borderwidth=0)
Login_label.pack(pady=(25,0), padx = (0,0))

# Username Label
Username_label= tk.Label (text="Username",background="white")
Username_label.pack(pady=(280,0),padx=(0,193))

# User picture para soft edges
Username_pic = Image.open ("Rental Management images/long rectangle.png")
resized = Username_pic.resize((250,35),Image.Resampling.LANCZOS)
Username_pic = ImageTk.PhotoImage(resized)
Username_label = tk.Label(Login_frame, image=Username_pic,borderwidth=0,bg="white")
Username_label.place(x=270, y= 313)

# User Entry
usernameEntry=tk.Entry(background="#D9D9D9",width=40,borderwidth=0)
usernameEntry.pack(pady=(20,0))

# Password Label
password_label= tk.Label (text="Password",background="white")
password_label.pack(pady=(20,0), padx=(0,193))

# Password picture para soft edges
password_pic = Image.open ("Rental Management images/long rectangle.png")
resized = password_pic.resize((250,35),Image.Resampling.LANCZOS)
password_pic = ImageTk.PhotoImage(resized)
password_label = tk.Label(Login_frame, image=password_pic,borderwidth=0,bg="white")
password_label.place(x=270, y= 385)

# Password Entry
passwordEntry=tk.Entry(background="#D9D9D9",width=40,borderwidth=0)
passwordEntry.pack(pady=(15,0))

# Existing Account error
noAccError_frame = tk.Frame(root, bg='white')
noAccError_frame.place(x=250, y=427)
noAccError_label = tk.Label(noAccError_frame, text="You have entered invalid username or password.", bg = 'white',
                            fg='red', font=('times new roman', 12))
noAccError_label.pack_forget()  # Initially hide the error label

# Login button
def on_button_click():
    # Condition when account does not exist/ invalid input
    if usernameEntry.get() != "owner" or passwordEntry.get() != "123":
        noAccError_label.pack()  # Show the error label
        usernameEntry.delete(0, tk.END)  # Clear the username field
        passwordEntry.delete(0, tk.END)  # Clear the password field
    else:
        noAccError_label.pack_forget()  # Hide the error label if credentials match

        # Add further logic for successful login here


# Bind the button click to the function
Login_button = tk.Button(Login_frame, text="Log in", pady=5, padx=20, background="#2C6FBC", command=on_button_click)
Login_button.pack(pady=(135, 0))

# Terms and Conditions Label
Termsandco_label = tk.Label (Login_frame,text= "By logging into our system, you acknowledge that you have read and understood the Terms of Use and Privacy statement\nto our"
                      " collection, use, and sharing of your personal information as described.", background="white")
Termsandco_label.pack(pady=(10,0))


root.mainloop()