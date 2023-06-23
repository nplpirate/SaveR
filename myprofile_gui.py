import tkinter as tk
from tkinter import messagebox
import json
from session import Session
from upload_grocery_bill import UploadGroceryBillGUI

class MyProfileGUI:
    def __init__(self, session: Session):
        self.session = session
        self.file = 'users.json'
        try:
            with open(self.file, encoding='utf-8') as file:
                self.users = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.users = {}

        # Create the MyProfile window
        self.myprofile_window = tk.Tk()
        self.myprofile_window.title("SaveR - My Profile")

        # Create the Postcode and Budget entry fields
        self.postcode_label = tk.Label(self.myprofile_window, text="Postcode:")
        self.postcode_entry = tk.Entry(self.myprofile_window)
        self.budget_label = tk.Label(self.myprofile_window, text="Budget (EUR per month):")
        self.budget_entry = tk.Entry(self.myprofile_window)

        # Create the Next button
        self.next_button = tk.Button(self.myprofile_window, text="Next", command=self.open_dietary_requirements)

        # Pack the widgets
        self.postcode_label.pack()
        self.postcode_entry.pack()
        self.budget_label.pack()
        self.budget_entry.pack()
        self.next_button.pack()

    def open_dietary_requirements(self):
        # Get the values from the entry fields
        postcode = self.postcode_entry.get()
        budget = self.budget_entry.get()

        # Check if the values are not empty
        if postcode.strip() and budget.strip():
            # Save the values to the user's profile
            current_user = self.session.get_current_user()
            self.users[current_user]['postcode'] = postcode
            self.users[current_user]['budget'] = budget

            # Save the updated user data to the JSON file
            self.save_users()

            # Open the Dietary Requirements window
            self.open_dietary_requirements_window()
        else:
            self.show_error_message("Postcode and Budget fields cannot be empty.")

    def open_dietary_requirements_window(self):
        # Create the Dietary Requirements window
        dietary_requirements_window = tk.Toplevel(self.myprofile_window)
        dietary_requirements_window.title("SaveR - Dietary Requirements")

        # Create the dietary requirements checkboxes
        dietary_requirements_label = tk.Label(dietary_requirements_window, text="Dietary Requirements:")
        dietary_requirements_label.pack()

        dietary_requirements_options = [
            "Vegetarian",
            "Vegan",
            "Gluten-Free",
            "Dairy-Free",
            "Organic",
            "Sustainable",
            "Diabetic",
            "Nut-free"
        ]

        dietary_requirements_vars = []
        for option in dietary_requirements_options:
            var = tk.BooleanVar()
            check_button = tk.Checkbutton(dietary_requirements_window, text=option, variable=var)
            check_button.pack()
            dietary_requirements_vars.append(var)

        # Create the Next button
        next_button = tk.Button(dietary_requirements_window, text="Next", command=self.open_risk_appetite_window)
        next_button.pack()

    def open_risk_appetite_window(self):
        # Create the Risk Appetite window
        risk_appetite_window = tk.Toplevel(self.myprofile_window)
        risk_appetite_window.title("SaveR - Risk Appetite")

        # Create the risk appetite options
        risk_appetite_label = tk.Label(risk_appetite_window, text="Risk Appetite:")
        risk_appetite_label.pack()

        risk_appetite_options = [
            "Low (2-3% returns)",
            "Medium (4-5% returns)",
            "Aggressive (5-7% returns)"
        ]

        var = tk.StringVar()
        for option in risk_appetite_options:
            radio_button = tk.Radiobutton(risk_appetite_window, text=option, variable=var, value=option)
            radio_button.pack()

        # Create the disclaimer label
        disclaimer_label = tk.Label(risk_appetite_window,
                                    text="A more aggressive portfolio involves a higher risk of capital loss.\n"
                                         "A Low to Medium risk appetite is therefore recommended.")
        disclaimer_label.pack()

        # Create the Submit button
        submit_button = tk.Button(risk_appetite_window, text="Submit", command=lambda: self.save_risk_appetite(var.get()))
        submit_button.pack()

    def save_risk_appetite(self, risk_appetite):
        # Save the risk appetite to the user's profile
        current_user = self.session.get_current_user()
        self.users[current_user]['risk_appetite'] = risk_appetite

        # Save the updated user data to the JSON file
        self.save_users()

        self.show_success_message("Profile successfully updated.")
        
        # Open the Upload Grocery Bill window
        upload_grocery_bill = UploadGroceryBillGUI()
        upload_grocery_bill.upload_grocery_bill()

    def save_users(self):
        """
        Save the updated user data to the JSON file.
        """
        with open(self.file, 'w', encoding='utf-8') as file:
            json.dump(self.users, file)

    def show_error_message(self, message):
        messagebox.showerror("Error", message)

    def show_success_message(self, message):
        messagebox.showinfo("Success", message)

    def start(self):
        self.myprofile_window.mainloop()


# If myprofile_gui.py is run directly, start the MyProfile GUI
if __name__ == "__main__":
    session = Session()
    myprofile = MyProfileGUI(session)
    myprofile.start()
