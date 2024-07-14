# Import the tkinter module, which provides a way to create graphical user interfaces (GUIs) in Python.
import tkinter as tk

# Import Image and ImageTk classes from the PIL (Python Imaging Library) module.
# These classes are used for opening, manipulating, and displaying image files in the GUI.
from PIL import Image, ImageTk

# Import the create_dashboard function from the Nav_Dashboard module.
# This function is responsible for creating the dashboard page layout.
from Nav_Dashboard import create_dashboard
from Nav_Room import create_room
from Nav_Tenants import create_tenants
from Nav_Payment import create_payment
from Nav_Analytics import create_analytics
from Nav_Accounts import create_accounts
from Nav_Rentals import create_rentals

# Define a list named 'pages', where each element is a tuple containing a page creation function and a page name.
# In this case, there is only one page, the dashboard page, represented by the create_dashboard function and the "Nav_Dashboard" name.
pages = [
    (create_dashboard, "Nav_Dashboard"),
    (create_room, "Nav_Room"),
    (create_tenants, "Nav_Tenants"),
    (create_payment, "Nav_Payment"),
    (create_analytics, "Nav_Analytics"),
    (create_accounts, "Nav_Accounts"),
    (create_rentals, "Nav_Rentals")

]

# Define a class named App that inherits from tk.Tk, which is the main application window class in tkinter.
class App(tk.Tk):
    def __init__(self):
        # Call the __init__ method of the parent class (tk.Tk) to initialize the application window.
        super().__init__()

        # Set the title of the application window.
        self.title("Snugspaces")

        # Set the initial state of the application window to 'zoomed', making it occupy the entire screen.
        self.state('zoomed')

        # Set the initial size of the application window to 1290x832 pixels.
        self.geometry("1290x832")

        # Create a Frame widget named 'side_frame' to hold the navigation buttons and logo.
        # The background color of the frame is set to white.
        side_frame = tk.Frame(self, bg="white")
        # Pack the 'side_frame' to the left side of the application window and make it fill the entire vertical space.
        side_frame.pack(side="left", fill="y")

        # Create a Canvas widget named 'logo_canvas' to display the logo image.
        # The canvas is placed inside 'side_frame', with a white background and dimensions 302x100 pixels.
        # The border width and highlight thickness are set to 0 to remove any border around the canvas.
        logo_canvas = tk.Canvas(side_frame, bg="white", width=300, height=90, bd=0, highlightthickness=0)
        # Pack the 'logo_canvas' at the top of the 'side_frame', anchoring it to the northwest corner (top-left) with a vertical padding of 5 pixels.
        logo_canvas.pack(side="top", anchor="nw", pady=5)

        # Load the logo image file from the specified path using PIL's Image.open method.
        snugspacelogo = Image.open("Rental Management images/snugspaceheading.png")
        # Resize the logo image to 302x100 pixels using the LANCZOS resampling filter, which provides high-quality results.
        resized_logo = snugspacelogo.resize((300, 100), Image.LANCZOS)
        # Convert the resized image to a format that can be used in tkinter (PhotoImage).
        logo_img = ImageTk.PhotoImage(resized_logo)
        # Keep a reference to the image object in the 'logo_canvas' to prevent it from being garbage collected.
        logo_canvas.image = logo_img
        # Display the image on the 'logo_canvas', placing it at the top-left corner (0, 0).
        logo_canvas.create_image(0, 0, anchor="nw", image=logo_img)

        # Create a dictionary named 'self.images' to store the images used in the navigation buttons.
        self.images = {
            # Load and resize the dashboard button image to 302x100 pixels using the 'load_and_resize_image' method.
            "Nav_Dashboard": self.load_and_resize_image("Rental Management images/Dashboard.png", (300, 95)),
            "Nav_Room": self.load_and_resize_image("Rental Management images/Rooms.png", (300, 95)),
            "Nav_Tenants": self.load_and_resize_image("Rental Management images/Tenants.png", (300, 95)),
            "Nav_Payment": self.load_and_resize_image("Rental Management images/Payment.png", (300, 95)),
            "Nav_Analytics": self.load_and_resize_image("Rental Management images/analytics.png", (300, 95)),
            "Nav_Accounts": self.load_and_resize_image("Rental Management images/Account.png", (300, 95)),
            "Nav_Rentals": self.load_and_resize_image("Rental Management images/Rental.png", (300, 95))
        }

        # Create a Button widget named 'btn' to represent the navigation button for the dashboard page.
        # The button is placed inside 'side_frame' and uses the dashboard image from 'self.images'.
        dashboard_btn = tk.Button(side_frame, image=self.images["Nav_Dashboard"],
                        # Set the command option of the button to a lambda function that calls the 'show_frame' method with the page name "Nav_Dashboard".
                        # This means that when the button is clicked, the dashboard page will be displayed.
                        command=lambda page="Nav_Dashboard": self.show_frame(page))
        # Configure the size of the button to be 302x100 pixels.
        dashboard_btn.config(width=300, height=90, borderwidth=0, bg='white')
        # Pack the button at the top of the 'side_frame', anchoring it to the northwest corner (top-left) with horizontal padding of 10 pixels and vertical padding of 5 pixels.
        dashboard_btn.pack(side="top", anchor="nw", padx=10, pady=0)

        # Room Button
        room_btn = tk.Button(side_frame, image=self.images["Nav_Room"],
                             command=lambda page="Nav_Room": self.show_frame(page))
        room_btn.config(width=300, height=90, borderwidth=0, bg='white')
        room_btn.pack(side="top", anchor="nw", padx=10, pady=0)  # Pack button at the top left

        # Tenants Button
        tenants_btn = tk.Button(side_frame, image=self.images["Nav_Tenants"],
                                command=lambda page="Nav_Tenants": self.show_frame(page))
        tenants_btn.config(width=300, height=90, borderwidth=0, bg='white')
        tenants_btn.pack(side="top", anchor="nw", padx=10, pady=0)

        payments_btn = tk.Button(side_frame, image=self.images["Nav_Payment"],
                                 command=lambda page="Nav_Payment": self.show_frame(page))
        payments_btn.config(width=300, height=90, borderwidth=0, bg='white')
        payments_btn.pack(side="top", anchor="nw", padx=10, pady=0)

        analytics_btn = tk.Button(side_frame, image=self.images["Nav_Analytics"],
                                  command=lambda page="Nav_Analytics": self.show_frame(page))
        analytics_btn.config(width=300, height=90, borderwidth=0, bg='white')
        analytics_btn.pack(side="top", anchor="nw", padx=10, pady=0)

        accounts_btn = tk.Button(side_frame, image=self.images["Nav_Accounts"],
                                 command=lambda page="Nav_Accounts": self.show_frame(page))
        accounts_btn.config(width=300, height=90, borderwidth=0, bg='white')
        accounts_btn.pack(side="top", anchor="nw", padx=10, pady=0)

        rentals_btn = tk.Button(side_frame, image=self.images["Nav_Rentals"],
                                command=lambda page="Nav_Rentals": self.show_frame(page))
        rentals_btn.config(width=300, height=90, borderwidth=0, bg='white')
        rentals_btn.pack(side="top", anchor="nw", padx=10, pady=0)

        # Create a Frame widget named 'container' to hold the different pages of the application.
        container = tk.Frame(self)
        # Pack the 'container' frame to fill both the horizontal and vertical space of the application window.
        container.pack(side="top", fill="both", expand=True)


        # Create a dictionary named 'self.frames' to store the different page frames.
        self.frames = {}

        # Iterate over the list of pages to create and store each page frame.
        for create_page, page_name in pages:
            # Create the page frame by calling the page creation function (create_page) with 'container' and 'self' as arguments.
            frame = create_page(container, self)
            # Store the created page frame in 'self.frames' dictionary with the page name as the key.
            self.frames[page_name] = frame
            # Place the page frame inside the 'container' using grid layout, positioning it at row 0, column 0, and making it expand to fill all available space.
            frame.grid(row=0, column=0, sticky="nsew")

        # Display the dashboard page by default by calling the 'show_frame' method with "Nav_Dashboard" as the argument.
        self.show_frame("Nav_Dashboard")

    # Define a method named 'load_and_resize_image' to load an image from a file and resize it to the specified dimensions.
    def load_and_resize_image(self, path, size):
        # Open the image file from the given path using PIL's Image.open method.
        original_image = Image.open(path)
        # Resize the image to the specified size using the LANCZOS resampling filter for high-quality results.
        resized_image = original_image.resize(size, Image.LANCZOS)
        # Convert the resized image to a format that can be used in tkinter (PhotoImage).
        return ImageTk.PhotoImage(resized_image)

    # Define a method named 'show_frame' to display a specific page frame.
    def show_frame(self, page_name):
        # Retrieve the page frame from 'self.frames' dictionary using the page name as the key.
        frame = self.frames[page_name]
        # Raise the retrieved frame to the top of the stacking order, making it visible above all other frames.
        frame.tkraise()

# Check if the script is being run directly (i.e., not imported as a module).
if __name__ == "__main__":
    # Create an instance of the App class, which initializes and configures the application window.
    app = App()
    # Start the main event loop of the application, which waits for events (such as button clicks) and updates the GUI.
    app.mainloop()
