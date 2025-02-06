import tkinter as tk
from tkinter import messagebox
import re  # Import the regular expression module

def validate_password(password):
    """Check password strength requirements."""
    if len(password) < 6:
        return "Password must be at least 6 characters long."
    if not re.search("[a-z]", password):  # Check for lowercase letter
        return "Password must contain at least one lowercase letter."
    if not re.search("[A-Z]", password):  # Check for uppercase letter
        return "Password must contain at least one uppercase letter."
    if not re.search("[0-9]", password):  # Check for a number
        return "Password must contain at least one number."
    return None  # Return None if all conditions are met

def submit_signup():
    """Handle signup process."""
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    # Validate password
    password_error = validate_password(password)
    if password_error:
        messagebox.showerror("Password Error", password_error)
        return

    # Check if passwords match
    if password != confirm_password:
        messagebox.showerror("Password Error", "Passwords do not match!")
        return

    # You can process the signup data here
    messagebox.showinfo("Sign Up Successful", "Thank you for signing up!")

def toggle_password():
    """Show or hide the password based on the checkbox."""
    if show_password_var.get():
        password_entry.config(show="")
        confirm_password_entry.config(show="")
    else:
        password_entry.config(show="*")
        confirm_password_entry.config(show="*")

# Create the main window
root = tk.Tk()
root.title("Sign Up")

# Set a larger size for the window
root.geometry("500x400")

# Create and place the labels and text boxes with increased width and padding
tk.Label(root, text="Username:", font=("Arial", 12)).grid(row=0, column=0, padx=20, pady=10, sticky=tk.W)
username_entry = tk.Entry(root, font=("Arial", 12), width=30)
username_entry.grid(row=0, column=1, padx=20, pady=10)

tk.Label(root, text="Email:", font=("Arial", 12)).grid(row=1, column=0, padx=20, pady=10, sticky=tk.W)
email_entry = tk.Entry(root, font=("Arial", 12), width=30)
email_entry.grid(row=1, column=1, padx=20, pady=10)

tk.Label(root, text="Password:", font=("Arial", 12)).grid(row=2, column=0, padx=20, pady=10, sticky=tk.W)
password_entry = tk.Entry(root, font=("Arial", 12), show="*", width=30)
password_entry.grid(row=2, column=1, padx=20, pady=10)

tk.Label(root, text="Confirm Password:", font=("Arial", 12)).grid(row=3, column=0, padx=20, pady=10, sticky=tk.W)
confirm_password_entry = tk.Entry(root, font=("Arial", 12), show="*", width=30)
confirm_password_entry.grid(row=3, column=1, padx=20, pady=10)

# Checkbox to show/hide password
show_password_var = tk.BooleanVar()
show_password_checkbox = tk.Checkbutton(root, text="Show Password", font=("Arial", 10), variable=show_password_var, command=toggle_password)
show_password_checkbox.grid(row=4, column=1, padx=20, pady=5, sticky=tk.W)

# Create and place the Submit button with increased size
submit_button = tk.Button(root, text="Sign Up", font=("Arial", 12), command=submit_signup, width=20)
submit_button.grid(row=5, column=1, padx=20, pady=20, sticky=tk.E)

# Run the main loop
root.mainloop()
