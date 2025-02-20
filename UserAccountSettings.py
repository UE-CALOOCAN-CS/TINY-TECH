import tkinter as tk
from tkinter import messagebox

# Temporary database (list) with username and password
user_data = ["current_user", "password123"]  # [Username, Password]

def on_entry_click(entry, default_text):
    """Clear the entry field when clicked"""
    if entry.get() == default_text:
        entry.delete(0, tk.END)
        entry.config(fg="black", font=("Calibre", 12, "normal"))
        if entry in (oldpassentry, newpassentry, confpassentry):  # Hide password when clicked
            entry.config(show="*")

def on_focus_out(entry, default_text):
    """Restore placeholder text if empty"""
    if entry.get() == "":
        entry.insert(0, default_text)
        entry.config(fg="gray", font=("Calibre", 12, "normal"), show="")

def reset_fields():
    """Reset all fields to default states"""
    entryusern.delete(0, tk.END)
    entryusern.insert(0, deftextusern)
    entryusern.config(fg="gray", font=font_style)

    oldpassentry.delete(0, tk.END)
    oldpassentry.insert(0, deftextoldpass)
    oldpassentry.config(fg="gray", font=font_style, show="")

    newpassentry.delete(0, tk.END)
    newpassentry.insert(0, deftextnewpass)
    newpassentry.config(fg="gray", font=font_style, show="")

    confpassentry.delete(0, tk.END)
    confpassentry.insert(0, deftextconfpass)
    confpassentry.config(fg="gray", font=font_style, show="")

def save_username():
    """Update the username only"""
    entered_username = entryusern.get().strip()

    if entered_username != deftextusern and entered_username:  # Ensure it's not placeholder or empty
        if entered_username != user_data[0]:  # Ensure it's different from the current username
            user_data[0] = entered_username
            messagebox.showinfo("Success", "Username is updated")  # Show success message
        else:
            messagebox.showerror("Error", "Invalid. New and Current username is the same")

    reset_fields()  # Reset fields after operation

def save_password():
    """Update the password only"""
    entered_old_password = oldpassentry.get().strip()
    entered_new_password = newpassentry.get().strip()
    entered_confirm_password = confpassentry.get().strip()

    if entered_new_password != deftextnewpass and entered_new_password:  # Ensure input isn't placeholder
        if entered_old_password == user_data[1]:  # Ensure old password is correct
            if entered_new_password == entered_confirm_password:  # Ensure new passwords match
                user_data[1] = entered_new_password
                messagebox.showinfo("Success", "Password is updated")  # Show success message
            else:
                messagebox.showerror("Error", "New and Confirm password do not match")
        else:
            messagebox.showerror("Error", "Invalid. Current password is incorrect")

    reset_fields()  # Reset fields after operation

# Create the GUI window
win = tk.Tk()
win.title("User Account Settings")
win.geometry("450x500")

font_style = ("Calibre", 12, "normal")  # Set font for consistency

# Create Labels and Input Fields
labelusern = tk.Label(win, text="Change Username", font=("Glacial Indifference", 16))
labelusern.place(x=50, y=50)

def create_entry(default_text, y_position, is_password=False):
    entry = tk.Entry(win, fg="gray", font=font_style, width=32)
    entry.insert(0, default_text)
    entry.bind("<FocusIn>", lambda event: on_entry_click(entry, default_text))
    entry.bind("<FocusOut>", lambda event: on_focus_out(entry, default_text))
    entry.place(x=50, y=y_position, height=45)
    return entry

# Username Entry
deftextusern = "   ENTER NEW USERNAME"
entryusern = create_entry(deftextusern, 90)

# Change Password Section
labelpassw = tk.Label(win, text="Change Password", font=("Glacial Indifference", 16))
labelpassw.place(x=50, y=145)

# Password Fields
deftextoldpass = "   CURRENT PASSWORD"
oldpassentry = create_entry(deftextoldpass, 185, is_password=True)

deftextnewpass = "   NEW PASSWORD"
newpassentry = create_entry(deftextnewpass, 243, is_password=True)

deftextconfpass = "   CONFIRM NEW PASSWORD"
confpassentry = create_entry(deftextconfpass, 303, is_password=True)

# Buttons
cancelbt = tk.Button(win, text="Cancel", command=reset_fields)
cancelbt.place(x=50, y=365)

save_user_bt = tk.Button(win, text="Save Username", command=save_username)
save_user_bt.place(x=115, y=365)

save_pass_bt = tk.Button(win, text="Save Password", command=save_password)
save_pass_bt.place(x=220, y=365)

win.mainloop()
