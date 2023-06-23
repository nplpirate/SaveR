import tkinter as tk
from tkinter import messagebox
from login_gui import LoginGUI
from register_gui import RegisterGUI
from session import Session
from PIL import Image, ImageTk

def print_menu():
    menu_text = """
    Welcome to SaveR, your Personal Savings App!
    Please choose an option:
    """
    return menu_text


def handle_login():
    session = Session()
    login = LoginGUI(session)
    root.withdraw()  # Hide the main menu GUI
    login.start()


def handle_register():
    session = Session()
    register = RegisterGUI(session, root)
    root.withdraw()  # Hide the main menu GUI
    register.start()


def handle_exit():
    messagebox.showinfo("Exit", "Thank you for using SaveR, hope to see you again!")
    root.destroy()


root = tk.Tk()
root.title("SaveR")

# Load and display the image
image = Image.open("/Users/alextebeica/Desktop/SaveR.png")  # Replace "path/to/your/image.png" with the actual path to your image file
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo)
image_label.pack()

menu_label = tk.Label(root, text=print_menu())
menu_label.pack()

login_button = tk.Button(root, text="Login", command=handle_login)
login_button.pack()

register_button = tk.Button(root, text="Register", command=handle_register)
register_button.pack()

exit_button = tk.Button(root, text="Exit", command=handle_exit)
exit_button.pack()

root.mainloop()
