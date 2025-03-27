import customtkinter as ctk
from tkinter import messagebox, font
from PIL import Image, ImageTk
import re
import os

class LoginUI:
    def __init__(self, login_system):
        self.login_system = login_system
        self.root = ctk.CTk()
        self.root.title("Tiny Tech")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        
        # Set the appearance mode and color theme
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        # Start with login page
        self.show_login_page()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def load_login_components(self):
        # Create main container that splits the window into two parts
        main_container = ctk.CTkFrame(self.root)
        main_container.pack(fill="both", expand=True)
        
        # Right container for login (1/3 width) - NOW ON THE LEFT
        right_container = ctk.CTkFrame(main_container, fg_color="#ffffff")
        right_container.pack(side="left", fill="both", expand=False)
        right_container.configure(width=400)
        right_container.pack_propagate(False)
        
        # Left container for video/image (2/3 width) - NOW ON THE RIGHT
        left_container = ctk.CTkFrame(main_container, fg_color="gray75")
        left_container.pack(side="right", fill="both", expand=True, padx=0, pady=0)
        left_container.pack_propagate(False)

        right_image=ctk.CTkImage(light_image=Image.open("images/tiny-tech-bg.png"), size=(1280, 1080))
        image_label=ctk.CTkLabel(left_container, image=right_image, text="")
        image_label.pack(expand=True)

        # For entries, create a frame to center them
        entry_frame = ctk.CTkFrame(right_container, fg_color="transparent")
        entry_frame.pack(pady=10)

        # Add login components...
        username_label = ctk.CTkLabel(entry_frame, text="USERNAME", font=("Calibri", 18, "bold"))
        username_label.pack(anchor="w", pady=(100,5))
        self.username_entry = ctk.CTkEntry(entry_frame, width=240)
        self.username_entry.configure(border_width=5)
        self.username_entry.pack(pady=(0, 20))

        password_label = ctk.CTkLabel(entry_frame, text="PASSWORD", font=("Calibri", 18, "bold"))
        password_label.pack(anchor="w")
        self.password_entry = ctk.CTkEntry(entry_frame, show="*", width=240)
        self.password_entry.configure(border_width=5)
        self.password_entry.pack(pady=(0, 5))

        forgot_password = ctk.CTkButton(entry_frame, text="FORGOT PASSWORD", 
                                      font=("Calibri", 10), command=self.cant_sign_in,
                                      fg_color="transparent", text_color=("gray10", "gray90"))
        forgot_password.pack(anchor="e", padx=(40, 0), pady=(0, 20))

        # Button container
        button_container = ctk.CTkFrame(right_container, fg_color="transparent")
        button_container.pack(pady=10)

        signup_button = ctk.CTkButton(button_container, text="SIGN UP", font=("Calibri", 14, "bold"), 
                                    text_color="#ffffff", command=self.show_signup_page, width=120)
        signup_button.pack(side="left", padx=10)
        
        login_button = ctk.CTkButton(button_container, text="LOGIN", font=("Calibri", 14, "bold"), 
                                    text_color="#ffffff", command=self.handle_login, width=120)
        login_button.pack(side="left", padx=10)

        # Add social media buttons and other components...
        social_container = ctk.CTkFrame(right_container, fg_color="transparent")
        social_container.pack(pady=20)
        
        google_icon = ctk.CTkImage(light_image=Image.open("images/google-logo.png"), size=(24, 24))
        google_button = ctk.CTkButton(social_container, text="Sign in with Google",
                                    width=180, fg_color="#DB4437", hover_color="#C1351D",
                                    image=google_icon, compound="left")
        google_button.pack(pady=5)

        stay_signed_in = ctk.CTkCheckBox(right_container, text="Stay signed in", font=("Calibri", 14, "bold"))
        stay_signed_in.pack(pady=20)

        version_label = ctk.CTkLabel(right_container, text="Copyright \u00A9 2025",
                                     font=("Calibri", 14, "bold"))
        version_label.pack(side="bottom", pady=(0, 50))
        
        logo_label = ctk.CTkLabel(right_container, text="TINY TECH",
                             font=("Calibri", 36, "bold"))
        logo_label.pack(side="bottom", pady=(0, 5))

    def load_signup_components(self): #insert design
        # Create main container that splits the window into two parts
        main_container = ctk.CTkFrame(self.root)
        main_container.pack(fill="both", expand=True)
        
        # Right container for signup (1/3 width) 
        right_container = ctk.CTkFrame(main_container, fg_color="#ffffff")
        right_container.pack(side="right", fill="both", expand=False)
        right_container.configure(width=400)  # 1/3 of 1920
        right_container.pack_propagate(False)
        
        # Left container for video/image (2/3 width)
        left_container = ctk.CTkFrame(main_container, fg_color="gray75")  # Placeholder color
        left_container.pack(side="left", fill="both", expand=True)

        left_image=ctk.CTkImage(light_image=Image.open("images/tiny-tech-bg.png"), size=(1280, 1080))
        image_label=ctk.CTkLabel(left_container, image=left_image, text="")
        image_label.pack(expand=True)

        # Title
        title = ctk.CTkLabel(right_container, text="Sign Up", font=("Arial", 24, "bold"))
        title.pack(pady=(40,10))

        # Form container
        form_container = ctk.CTkFrame(right_container, fg_color="#ffffff")
        form_container.pack(pady=0, padx=60)
        form_container.configure(width=300, height=480)
        form_container.pack_propagate(False)

        # First Name
        ctk.CTkLabel(form_container, text="FIRST NAME", font=("Calibri", 14, "bold"), anchor="w").pack(fill="x", pady=(10, 0))
        self.firstname_entry = ctk.CTkEntry(form_container, width=240)
        self.firstname_entry.pack(fill="x")

        # Last Name
        ctk.CTkLabel(form_container, text="LAST NAME", font=("Calibri", 14, "bold"), anchor="w").pack(fill="x", pady=(10, 0))
        self.lastname_entry = ctk.CTkEntry(form_container, width=240)
        self.lastname_entry.pack(fill="x")

        # Email
        ctk.CTkLabel(form_container, text="EMAIL", font=("Calibri", 14, "bold"), anchor="w").pack(fill="x", pady=(10, 0))
        self.email_entry = ctk.CTkEntry(form_container, width=240)
        self.email_entry.pack(fill="x")

        # Username
        ctk.CTkLabel(form_container, text="USERNAME", font=("Calibri", 14, "bold"), anchor="w").pack(fill="x", pady=(10, 0))
        self.new_username_entry = ctk.CTkEntry(form_container, width=240)
        self.new_username_entry.pack(fill="x")

        # Password
        ctk.CTkLabel(form_container, text="PASSWORD", font=("Calibri", 14, "bold"), anchor="w").pack(fill="x", pady=(10, 0))
        self.new_password_entry = ctk.CTkEntry(form_container, show="*", width=240)
        self.new_password_entry.pack(fill="x")

        # Confirm Password
        ctk.CTkLabel(form_container, text="CONFIRM PASSWORD", font=("Calibri", 14, "bold"), anchor="w").pack(fill="x", pady=(10, 0))
        self.confirm_password_entry = ctk.CTkEntry(form_container, show="*", width=240)
        self.confirm_password_entry.pack(fill="x")

        # Show password checkbox
        self.show_password_var = ctk.BooleanVar()
        show_password_checkbox = ctk.CTkCheckBox(form_container, text="Show Password",
                                               variable=self.show_password_var,
                                               command=self.toggle_password)
        show_password_checkbox.pack(pady=25)

        # Buttons container
        button_container = ctk.CTkFrame(right_container, fg_color="transparent")
        button_container.pack(pady=5)

        # Submit and Back buttons
        back_button = ctk.CTkButton(button_container, text="BACK TO LOGIN", font=("Calibri", 14, "bold"),
                                  command=self.show_login_page, width=120)
        back_button.pack(side="left", padx=10)

        submit_button = ctk.CTkButton(button_container, text="SIGN UP", font=("Calibri", 14, "bold"),
                                    command=self.handle_signup, width=120)
        submit_button.pack(side="left", padx=10)

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
        self.new_password_entry.configure(show="" if show else "*")
        self.confirm_password_entry.configure(show="" if show else "*")

    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        success, message = self.login_system.login(username, password)
        if success:
            messagebox.showinfo("Login Successful", message)
            self.clear_window()
        else:
            messagebox.showerror("Login Failed", message)

    def handle_signup(self):
        user_data = {
            "email": self.email_entry.get(),
            "username": self.new_username_entry.get(),
            "password": self.new_password_entry.get(),
            "first_name": self.firstname_entry.get(),
            "last_name": self.lastname_entry.get()
        }

        if not all(user_data.values()):
            messagebox.showerror("Error", "All fields are required!")
            return

        password_error = self.validate_password(user_data["password"])
        if password_error:
            messagebox.showerror("Password Error", password_error)
            return

        if user_data["password"] != self.confirm_password_entry.get():
            messagebox.showerror("Password Error", "Passwords do not match!")
            return

        success, message = self.login_system.signup(user_data)
        if success:
            messagebox.showinfo("Success", message)
            self.show_login_page()
        else:
            messagebox.showerror("Error", message)

    def cant_sign_in(self):
        messagebox.showinfo("Can't Sign In", "Password recovery feature coming soon...")

    def run(self):
        self.root.mainloop()