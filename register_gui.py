import tkinter as tk
from tkinter import messagebox
import json
from session import Session
from myprofile_gui import MyProfileGUI


class RegisterGUI:
    def __init__(self, session: Session, main_menu_window: tk.Tk):
        self.session = session
        self.main_menu_window = main_menu_window

        self.register_window = tk.Toplevel(self.main_menu_window)
        self.register_window.title("SaveR - Register")

        self.username_label = tk.Label(self.register_window, text="Username:")
        self.username_entry = tk.Entry(self.register_window)
        self.password_label = tk.Label(self.register_window, text="Password:")
        self.password_entry = tk.Entry(self.register_window, show="*")
        self.email_label = tk.Label(self.register_window, text="Email Address:")
        self.email_entry = tk.Entry(self.register_window)
        self.register_button = tk.Button(self.register_window, text="Register", command=self.register_user)
        self.back_button = tk.Button(self.register_window, text="Back", command=self.back_to_main_menu)

        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.email_label.pack()
        self.email_entry.pack()
        self.register_button.pack()
        self.back_button.pack()

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()

        if self.validate_input(username, password, email):
            if self.is_username_available(username):
                self.save_user_details(username, password, email)
                self.session.set_current_user(username)
                self.register_window.destroy()
                myprofile = MyProfileGUI(self.session)
                myprofile.start()
            else:
                messagebox.showerror("Registration Failed", "Username is already taken.")
        else:
            messagebox.showerror("Registration Failed", "Please fill in all the fields.")

    def validate_input(self, username, password, email):
        return username.strip() and password.strip() and email.strip()

    def is_username_available(self, username):
        try:
            with open("users.json", encoding="utf-8") as file:
                users = json.load(file)

            return username not in users
        except FileNotFoundError:
            return True

    def save_user_details(self, username, password, email):
        user_data = {
            "password": password,
            "email": email
        }

        try:
            with open("users.json", "r", encoding="utf-8") as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}

        users[username] = user_data

        with open("users.json", "w", encoding="utf-8") as file:
            json.dump(users, file)

    def back_to_main_menu(self):
        self.register_window.destroy()
        self.main_menu_window.deiconify()

    def start(self):
        self.register_window.mainloop()