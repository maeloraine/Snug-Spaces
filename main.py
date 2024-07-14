import tkinter as tk
from PIL import ImageTk, Image
from Nav_Dashboard import Dashboard
from Nav_Room import Room
from Nav_Tenants import TenantManagement
from Nav_Payment import Payment

from Nav_Rentals import RentalManagement

# Define pages with their creation functions
pages = [
    (Dashboard, "Nav_Dashboard"),
    (Room, "Nav_Room"),
    (TenantManagement, "Nav_Tenants"),
    (Payment, "Nav_Payment"),
    #(create_analytics, "Nav_Analytics"),
    (RentalManagement, "Nav_Rentals")
]

class LoginWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Snugspaces")
        self.geometry("800x600")
        self.resizable(0, 0)
        self.configure(background='#4b7cdc')
        self.center_window()
        self.init_ui()
        self.master = master

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def init_ui(self):
        logo_pic = Image.open("Rental Management images/SnugSpaceslogo.png")
        resized = logo_pic.resize((300, 300), Image.LANCZOS)
        logo_pic = ImageTk.PhotoImage(resized)

        login_frame = tk.Frame(self, bg="white")
        login_frame.place(relwidth=1, relheight=1)

        login_label = tk.Label(login_frame, image=logo_pic, borderwidth=0)
        login_label.image = logo_pic
        login_label.pack(pady=(15, 0))

        username_label = tk.Label(login_frame, text="Username", font=("Arial", 12, 'bold'), background="white")
        username_label.pack(anchor=tk.W, padx=(280, 0), pady=(0, 0))

        UUser_frame = tk.Frame(self, bg='white')
        UUser_frame.place(x=280, y=350)
        # user picture para soft edges
        User_pic = Image.open("Rental Management images/long rectangle.png")
        resized = User_pic.resize((250, 35), Image.Resampling.LANCZOS)
        User_pic = ImageTk.PhotoImage(resized)
        User_label = tk.Label(UUser_frame, image=User_pic, borderwidth=0, bg="white")
        User_label.image = User_pic
        User_label.pack()

        username_frame = tk.Frame(self,bg='white')
        username_frame.place(x=290,y=355)
        self.username_entry = tk.Entry(username_frame, background="#D9D9D9", width=25, font=("Arial", 12), borderwidth=0)
        self.username_entry.pack()

        password_label = tk.Label(login_frame, text="Password", font=("Arial", 12, 'bold'), background="white")
        password_label.pack(anchor=tk.W, padx=(280, 0), pady=(55, 0))

        PASS_frame = tk.Frame(self, bg='white')
        PASS_frame.place(x=280, y=430)
        # user picture para soft edges
        PASS_pic = Image.open("Rental Management images/long rectangle.png")
        resized = PASS_pic.resize((250, 35), Image.Resampling.LANCZOS)
        PASS_pic = ImageTk.PhotoImage(resized)
        PASS_label = tk.Label(PASS_frame, image=PASS_pic, borderwidth=0, bg="white")
        PASS_label.image = PASS_pic
        PASS_label.pack()

        PASSENT_frame = tk.Frame(self, bg='white')
        PASSENT_frame.place(x=290, y=435)

        self.password_entry = tk.Entry(PASSENT_frame, background="#D9D9D9", width=25, font=("Arial", 12), borderwidth=0, show="*")
        self.password_entry.pack()

        self.no_acc_error_label = tk.Label(login_frame, text="You have entered invalid username or password.", bg='white',
                                           fg='red', font=('times new roman', 12))
        self.no_acc_error_label.pack(pady=(15, 0))
        self.no_acc_error_label.pack_forget()

        login_button = tk.Button(login_frame, text="Log in", pady=5, padx=20, background="#2C6FBC", command=self.on_button_click)
        login_button.pack(pady=(65, 0))

        # Terms and Conditions Label
        Termsandco_label = tk.Label(login_frame,
                                    text="By logging into our system, you acknowledge that you have read and understood the Terms of Use and Privacy statement\nto our"
                                         " collection, use, and sharing of your personal information as described.",
                                    background="white")
        Termsandco_label.pack(pady=(10, 0))

    def on_button_click(self):
        if self.username_entry.get() != "owner" or self.password_entry.get() != "123":
            self.no_acc_error_label.pack()
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
        else:
            self.no_acc_error_label.pack_forget()
            self.master.show_app()
            self.destroy()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw()
        self.login_window = LoginWindow(self)
        self.login_window.grab_set()

    def show_app(self):
        self.login_window.grab_release()
        self.login_window.destroy()
        self.deiconify()
        self.title("Snugspaces")
        self.state('zoomed')
        self.geometry("1290x832")
        self.init_ui()

    def init_ui(self):
        side_frame = tk.Frame(self, bg="white")
        side_frame.pack(side="left", fill="y")

        logo_canvas = tk.Canvas(side_frame, bg="white", width=300, height=90, bd=0, highlightthickness=0)
        logo_canvas.pack(side="top", anchor="nw", pady=5)

        snugspacelogo = Image.open("Rental Management images/snugspaceheading.png")
        resized_logo = snugspacelogo.resize((300, 100), Image.LANCZOS)
        logo_img = ImageTk.PhotoImage(resized_logo)
        logo_canvas.image = logo_img
        logo_canvas.create_image(0, 0, anchor="nw", image=logo_img)

        self.images = {
            "Nav_Dashboard": self.load_and_resize_image("Rental Management images/Dashboard.png", (300, 95)),
            "Nav_Room": self.load_and_resize_image("Rental Management images/Rooms.png", (300, 95)),
            "Nav_Tenants": self.load_and_resize_image("Rental Management images/Tenants.png", (300, 95)),
            "Nav_Rentals": self.load_and_resize_image("Rental Management images/Rental.png", (300, 95)),
            "Nav_Payment": self.load_and_resize_image("Rental Management images/Payment.png", (300, 95)),
            #"Nav_Analytics": self.load_and_resize_image("Rental Management images/analytics.png", (300, 95)),
        }

        self.create_nav_buttons(side_frame)

        self.container = tk.Frame(self, bg='#3A98CC')
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        for create_page, page_name in pages:
            frame = create_page(self.container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Nav_Dashboard")

    def create_nav_buttons(self, side_frame):
        for page_name in self.images:
            button = tk.Button(side_frame, image=self.images[page_name],
                               command=lambda name=page_name: self.show_frame(name))
            button.config(width=300, height=90, borderwidth=0, bg='white')
            button.pack(side="top", anchor="nw", padx=10, pady=0)

    def load_and_resize_image(self, path, size):
        original_image = Image.open(path)
        resized_image = original_image.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(resized_image)

    def show_frame(self, page_name):
        # Destroy existing frame if it exists
        for frame_name, frame in self.frames.items():
            if frame_name == page_name:
                frame.destroy()
                break

        # Create new instance of the frame
        for create_page, name in pages:
            if name == page_name:
                frame = create_page(self.container, self)
                self.frames[page_name] = frame
                frame.grid(row=0, column=0, sticky="nsew")
                break

        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
