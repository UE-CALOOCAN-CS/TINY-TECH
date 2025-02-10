import tkinter as tk
import webbrowser
from PIL import Image, ImageTk  # Import Pillow for image handling

def toggle_menu():
    """Toggle between the two menu frames."""
    if main_menu.winfo_ismapped():
        main_menu.place_forget()
        module_menu.place(x=0, y=40, width=150, height=765)
    else:
        module_menu.place_forget()
        main_menu.place(x=0, y=40, width=150, height=765)

def open_module_1():
    """Open the TikTok link for Module 1."""
    webbrowser.open("https://www.tiktok.com/@parenghayb")

def show_message():
    """Display 'Hello student!!' in the white space."""
    content_label.config(text="Hello student!!")

# Create main window
root = tk.Tk()
root.title("Module")
root.geometry("500x400")

# Hamburger button
menu_button = tk.Button(root, text="☰", font=("Arial", 14), command=toggle_menu)
menu_button.place(x=5, y=5)

# Sidebar menus (initially showing main_menu)
main_menu = tk.Frame(root, bg="lightgray", relief="raised")
module_menu = tk.Frame(root, bg="lightgray", relief="raised")

# Load and display logo image with error handling
try:
    image_path = "logo.png"  # Change this to your image file path
    logo_image = Image.open("logo.png")
    logo_image = logo_image.resize((100, 100))  # Resize image
    logo_photo = ImageTk.PhotoImage(logo_image)

    logo_label = tk.Label(main_menu, image=logo_photo, bg="lightgray")
    logo_label.image = logo_photo  # Keep reference to avoid garbage collection
    logo_label.pack(pady=20)
except Exception as e:
    print("Error loading image:", e)  # Print error message for debugging
    logo_label = tk.Label(main_menu, text="LOGO", font=("Arial", 14, "bold"), bg="lightgray")
    logo_label.pack(pady=20)

# Main menu items centered
main_items = ["Home", "Profile", "Settings"]
button_frame = tk.Frame(main_menu, bg="lightgray")
button_frame.pack(expand=True)

for item in main_items:
    btn = tk.Button(button_frame, text=item, font=("Arial", 12), width=15, relief="flat", bg="white")
    btn.pack(pady=5, padx=5, fill="x")

# Logout button placed at the bottom of main menu
logout_button = tk.Button(main_menu, text="Logout", font=("Arial", 12), width=15, relief="flat", bg="white", command=root.quit)
logout_button.pack(side="bottom", pady=10)

# Module menu items
top_buttons = [
    ("Module 1", open_module_1),
    ("Module 2", show_message),
    ("Module 3", lambda: print("Module 3 Clicked"))
]

for text, command in top_buttons:
    btn = tk.Button(module_menu, text=text, font=("Arial", 12), width=15, relief="flat", bg="white", command=command)
    btn.pack(pady=2, padx=5, fill="x")

# Content area (white space) - menu will overlap this
content_label = tk.Label(root, text="", font=("Arial", 16), bg="white", width=100, height=20, relief="solid")
content_label.place(x=150, y=80)

# Initially show the main menu
main_menu.place(x=0, y=40, width=150, height=765)

root.mainloop()
