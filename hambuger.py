import tkinter as tk
from tkinter import messagebox

# Function to simulate opening different pages
def open_account_page():
    messagebox.showinfo("User Account", "Opening User Account Page")

def open_settings_page():
    messagebox.showinfo("Settings", "Opening Application Settings Page")

def open_report_bug_page():
    messagebox.showinfo("Report Bug", "Opening Report Bug Page")

def logout():
    messagebox.showinfo("Logout", "Logging out...")

def toggle_menu():
    # Toggle the visibility of the menu inside the hamburger button
    if menu_frame.winfo_ismapped():
        menu_frame.pack_forget()
    else:
        menu_frame.pack(side="top", fill="x", padx=10, pady=10)

# Main window setup
root = tk.Tk()
root.title("Hamburger Button UI")
root.geometry("300x400")

# Create a smaller hamburger button
hamburger_button = tk.Button(root, text="☰", font=("Arial", 20), width=4, height=2, command=toggle_menu)
hamburger_button.pack(padx=20, pady=20)

# Frame for the menu options (to be displayed inside the hamburger button)
menu_frame = tk.Frame(root)

# Create menu buttons inside the menu frame
user_account_button = tk.Button(menu_frame, text="User Account Page", command=open_account_page)
user_account_button.pack(fill="x", pady=5)

settings_button = tk.Button(menu_frame, text="Application Settings", command=open_settings_page)
settings_button.pack(fill="x", pady=5)

report_bug_button = tk.Button(menu_frame, text="Report Bug", command=open_report_bug_page)
report_bug_button.pack(fill="x", pady=5)

logout_button = tk.Button(menu_frame, text="Logout", command=logout)
logout_button.pack(fill="x", pady=5)

# Application version label (placed at the bottom)
version_label = tk.Label(root, text="App Version: 1.0.0", font=("Arial", 10))
version_label.pack(side="bottom", padx=10, pady=10)

# Run the application
root.mainloop()
