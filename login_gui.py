import tkinter as tk
from tkinter import messagebox
import json
from session import Session
from myprofile_gui import MyProfileGUI


class LoginGUI:
    def __init__(self, session: Session):
        self.session = session
        self.login_window = tk.Tk()
        self.login_window.title("SaveR - Login")

        self.username_label = tk.Label(self.login_window, text="Username:")
        self.username_entry = tk.Entry(self.login_window)
        self.password_label = tk.Label(self.login_window, text="Password:")
        self.password_entry = tk.Entry(self.login_window, show="*")
        self.login_button = tk.Button(self.login_window, text="Login", command=self.login_user)
        self.back_button = tk.Button(self.login_window, text="Back", command=self.back_to_main_menu)

        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack()
        self.back_button.pack()

    def login_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.verify_credentials(username, password):
            self.session.set_current_user(username)
            self.login_window.destroy()
            myprofile = MyProfileGUI(self.session)
            myprofile.start()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password.")

    def verify_credentials(self, username, password):
        try:
            with open("users.json", encoding="utf-8") as file:
                users = json.load(file)

            if username in users:
                user_data = users[username]
                return user_data["password"] == password

            return False
        except FileNotFoundError:
            return False

    def back_to_main_menu(self):
        self.login_window.destroy()

    def start(self):
        self.login_window.mainloop()


