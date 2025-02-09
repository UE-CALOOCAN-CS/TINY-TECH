import tkinter as tk
from tkinter import messagebox
import json
import re
import os

class LoginSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tiny Tech")
        self.root.geometry("500x600")
        self.root.configure(bg="white")
        
        # Initialize the JSON database if it doesn't exist
        self.db_file = "user_accounts.json"
        self.initialize_database()
        
        # Start with login page
        self.show_login_page()
        
    def initialize_database(self):
        if not os.path.exists(self.db_file):
            initial_data = {
                "users": [
                    {
                        "email": "test@example.com",
                        "username": "test_user",
                        "password": "Test123",
                        "first_name": "Test",
                        "last_name": "User"
                    }
                ]
            }
            with open(self.db_file, 'w') as f:
                json.dump(initial_data, f, indent=4)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def load_login_components(self):
        # Tiny Tech logo
        logo = tk.Label(self.root, text="TINY TECH", font=("Arial", 24, "bold"), bg="white")
        logo.pack(pady=10)

        # Frame for the login form
        form_frame = tk.Frame(self.root, bg="white")
        form_frame.pack(pady=10)

        # Username
        username_label = tk.Label(form_frame, text="Username", font=("Arial", 12), bg="white", anchor="w")
        username_label.grid(row=0, column=0, pady=(0, 5), sticky="w")
        self.username_entry = tk.Entry(form_frame, font=("Arial", 12), width=40, highlightthickness=1, bd=0, relief="solid")
        self.username_entry.grid(row=1, column=0, pady=5, ipady=10)

        # Password
        password_label = tk.Label(form_frame, text="Password", font=("Arial", 12), bg="white", anchor="w")
        password_label.grid(row=2, column=0, pady=(10, 5), sticky="w")
        self.password_entry = tk.Entry(form_frame, font=("Arial", 12), show="*", width=40, highlightthickness=1, bd=0, relief="solid")
        self.password_entry.grid(row=3, column=0, pady=5, ipady=10)

        # Login button
        login_button = tk.Button(form_frame, text="Sign In", font=("Arial", 12), command=self.login, width=20)
        login_button.grid(row=4, column=0, pady=10)

        # Social media login buttons
        social_frame = tk.Frame(self.root, bg="white")
        social_frame.pack(pady=10)

        fb_button = tk.Button(social_frame, text="Sign in with Facebook", font=("Arial", 12), width=20)
        fb_button.pack(side=tk.LEFT, padx=5)

        google_button = tk.Button(social_frame, text="Sign in with Google", font=("Arial", 12), width=20)
        google_button.pack(side=tk.LEFT, padx=5)

        apple_button = tk.Button(social_frame, text="Sign in with Apple", font=("Arial", 12), width=20)
        apple_button.pack(side=tk.LEFT, padx=5)

        # Stay signed in checkbox
        stay_signed_in = tk.Checkbutton(self.root, text="Stay signed in", font=("Arial", 12), bg="white")
        stay_signed_in.pack(pady=5)

        # Can't sign in and create account links
        link_frame = tk.Frame(self.root, bg="white")
        link_frame.pack(pady=5)

        cant_sign_in_link = tk.Button(link_frame, text="CAN'T SIGN IN?", font=("Arial", 12), command=self.cant_sign_in, bd=0, highlightthickness=0)
        cant_sign_in_link.pack(side=tk.LEFT, padx=5)

        create_account_link = tk.Button(link_frame, text="CREATE ACCOUNT", font=("Arial", 12), command=self.show_signup_page, bd=0, highlightthickness=0)
        create_account_link.pack(side=tk.LEFT, padx=5)

    def load_signup_components(self):
        # Title
        title = tk.Label(self.root, text="Sign Up", font=("Arial", 24, "bold"), bg="white")
        title.pack(pady=20)

        # Main frame
        form_frame = tk.Frame(self.root, bg="white")
        form_frame.pack(pady=10)

        # First Name
        tk.Label(form_frame, text="First Name:", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=20, pady=10, sticky=tk.W)
        self.firstname_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.firstname_entry.grid(row=0, column=1, padx=20, pady=10)

        # Last Name
        tk.Label(form_frame, text="Last Name:", font=("Arial", 12), bg="white").grid(row=1, column=0, padx=20, pady=10, sticky=tk.W)
        self.lastname_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.lastname_entry.grid(row=1, column=1, padx=20, pady=10)

        # Email
        tk.Label(form_frame, text="Email:", font=("Arial", 12), bg="white").grid(row=2, column=0, padx=20, pady=10, sticky=tk.W)
        self.email_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.email_entry.grid(row=2, column=1, padx=20, pady=10)

        # Username
        tk.Label(form_frame, text="Username:", font=("Arial", 12), bg="white").grid(row=3, column=0, padx=20, pady=10, sticky=tk.W)
        self.new_username_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.new_username_entry.grid(row=3, column=1, padx=20, pady=10)

        # Password
        tk.Label(form_frame, text="Password:", font=("Arial", 12), bg="white").grid(row=4, column=0, padx=20, pady=10, sticky=tk.W)
        self.new_password_entry = tk.Entry(form_frame, font=("Arial", 12), show="*", width=30)
        self.new_password_entry.grid(row=4, column=1, padx=20, pady=10)

        # Confirm Password
        tk.Label(form_frame, text="Confirm Password:", font=("Arial", 12), bg="white").grid(row=5, column=0, padx=20, pady=10, sticky=tk.W)
        self.confirm_password_entry = tk.Entry(form_frame, font=("Arial", 12), show="*", width=30)
        self.confirm_password_entry.grid(row=5, column=1, padx=20, pady=10)

        # Show password checkbox
        self.show_password_var = tk.BooleanVar()
        show_password_checkbox = tk.Checkbutton(form_frame, text="Show Password", font=("Arial", 10), 
                                              variable=self.show_password_var, command=self.toggle_password,
                                              bg="white")
        show_password_checkbox.grid(row=6, column=1, padx=20, pady=5, sticky=tk.W)

        # Buttons frame
        button_frame = tk.Frame(self.root, bg="white")
        button_frame.pack(pady=20)

        # Submit button
        submit_button = tk.Button(button_frame, text="Sign Up", font=("Arial", 12), command=self.signup, width=20)
        submit_button.pack(side=tk.LEFT, padx=10)

        # Back to login button
        back_button = tk.Button(button_frame, text="Back to Login", font=("Arial", 12), command=self.show_login_page, width=20)
        back_button.pack(side=tk.LEFT, padx=10)

    def show_login_page(self):
        self.clear_window()
        self.load_login_components()

    def show_signup_page(self):
        self.clear_window()
        self.load_signup_components()

    def validate_password(self, password):
        if len(password) < 6:
            return "Password must be at least 6 characters long."
        if not re.search("[a-z]", password):
            return "Password must contain at least one lowercase letter."
        if not re.search("[A-Z]", password):
            return "Password must contain at least one uppercase letter."
        if not re.search("[0-9]", password):
            return "Password must contain at least one number."
        return None

    def toggle_password(self):
        show = self.show_password_var.get()
        self.new_password_entry.config(show="" if show else "*")
        self.confirm_password_entry.config(show="" if show else "*")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        with open(self.db_file, 'r') as f:
            data = json.load(f)
            
        for user in data['users']:
            if user['username'] == username and user['password'] == password:
                messagebox.showinfo("Login Successful", f"Welcome, {user['first_name']}!")
                self.clear_window()
                return
                
        messagebox.showerror("Login Failed", "Invalid username or password.")

    def signup(self):
        email = self.email_entry.get()
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        first_name = self.firstname_entry.get()
        last_name = self.lastname_entry.get()

        # Validate all fields are filled
        if not all([email, username, password, confirm_password, first_name, last_name]):
            messagebox.showerror("Error", "All fields are required!")
            return

        # Validate password
        password_error = self.validate_password(password)
        if password_error:
            messagebox.showerror("Password Error", password_error)
            return

        # Check if passwords match
        if password != confirm_password:
            messagebox.showerror("Password Error", "Passwords do not match!")
            return

        # Check if username already exists
        with open(self.db_file, 'r') as f:
            data = json.load(f)
            
        if any(user['username'] == username for user in data['users']):
            messagebox.showerror("Error", "Username already exists!")
            return

        # Add new user
        new_user = {
            "email": email,
            "username": username,
            "password": password,
            "first_name": first_name,
            "last_name": last_name
        }
        
        data['users'].append(new_user)
        
        with open(self.db_file, 'w') as f:
            json.dump(data, f, indent=4)

        messagebox.showinfo("Success", "Account created successfully!")
        self.show_login_page()

    def cant_sign_in(self):
        messagebox.showinfo("Can't Sign In", "Password recovery feature coming soon...")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = LoginSystem()
    app.run()