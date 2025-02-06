import tkinter as tk
from tkinter import messagebox

# Temporary accounts
accounts = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username in accounts and accounts[username] == password:
        messagebox.showinfo("Login", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def create_account():
    # Add your create account logic here
    messagebox.showinfo("Create Account", "Redirecting to create account page...")

def cant_sign_in():
    # Add your can't sign in logic here
    messagebox.showinfo("Can't Sign In", "Redirecting to can't sign in page...")

root = tk.Tk()
root.title("Tiny Tech Login")
root.geometry("450x450")
root.configure(bg="white")

# Tiny Tech logo
logo = tk.Label(root, text="TINY TECH", font=("Arial", 24, "bold"), bg="white")
logo.pack(pady=10)

# Frame for the login form
form_frame = tk.Frame(root, bg="white")
form_frame.pack(pady=10)

# Username
username_label = tk.Label(form_frame, text="Username", font=("Arial", 12), bg="white", anchor="w")
username_label.grid(row=0, column=0, pady=(0, 5), sticky="w")
username_entry = tk.Entry(form_frame, font=("Arial", 12), width=40, highlightthickness=1, bd=0, relief="solid")
username_entry.grid(row=1, column=0, pady=5, ipady=10)

# Password
password_label = tk.Label(form_frame, text="Password", font=("Arial", 12), bg="white", anchor="w")
password_label.grid(row=2, column=0, pady=(10, 5), sticky="w")
password_entry = tk.Entry(form_frame, font=("Arial", 12), show="*", width=40, highlightthickness=1, bd=0, relief="solid")
password_entry.grid(row=3, column=0, pady=5, ipady=10)

# Login button
login_button = tk.Button(form_frame, text="Sign In", font=("Arial", 12), command=login, width=20)
login_button.grid(row=4, column=0, pady=10)

# Social media login buttons
social_frame = tk.Frame(root, bg="white")
social_frame.pack(pady=10)

fb_button = tk.Button(social_frame, text="Sign in with Facebook", font=("Arial", 12), width=20)
fb_button.pack(side=tk.LEFT, padx=5)

google_button = tk.Button(social_frame, text="Sign in with Google", font=("Arial", 12), width=20)
google_button.pack(side=tk.LEFT, padx=5)

apple_button = tk.Button(social_frame, text="Sign in with Apple", font=("Arial", 12), width=20)
apple_button.pack(side=tk.LEFT, padx=5)

# Stay signed in checkbox
stay_signed_in = tk.Checkbutton(root, text="Stay signed in", font=("Arial", 12), bg="white")
stay_signed_in.pack(pady=5)

# Can't sign in and create account links
link_frame = tk.Frame(root, bg="white")
link_frame.pack(pady=5)

cant_sign_in_link = tk.Button(link_frame, text="CAN'T SIGN IN?", font=("Arial", 12), command=cant_sign_in, bd=0, highlightthickness=0)
cant_sign_in_link.pack(side=tk.LEFT, padx=5)

create_account_link = tk.Button(link_frame, text="CREATE ACCOUNT", font=("Arial", 12), command=create_account, bd=0, highlightthickness=0)
create_account_link.pack(side=tk.LEFT, padx=5)

root.mainloop()
