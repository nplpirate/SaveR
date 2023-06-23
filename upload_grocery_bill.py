from tkinter import filedialog, messagebox, Tk, Label, Button, Text
import tkinter as tk
import pandas as pd
import random

class UploadGroceryBillGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("SaveR - Upload Grocery Bill")

        self.label = Label(self.root, text="Upload your grocery bill")
        self.label.pack()

        self.button = Button(self.root, text="Upload", command=self.upload_grocery_bill)
        self.button.pack()

    def upload_grocery_bill(self):
        file_path = filedialog.askopenfilename(title="Select Grocery Bill")

        if file_path:
            self.analyze_grocery_bill(file_path)
        else:
            messagebox.showerror("Error", "No file selected.")

    def analyze_grocery_bill(self, file_path):
        try:
            # Create a random dataframe with groceries and prices
            data = self.create_random_dataframe()

            # Calculate the totals for Price and Best Price columns
            price_total = data["Price"].sum()
            best_price_total = data["Best Price"].sum()

            # Calculate the difference between the totals
            savings = price_total - best_price_total
            annual_savings = savings * 52

            # Display the totals and savings
            totals_label = Label(self.root, text=f"Price Total this week: €{price_total:.2f}  |  Best Price Total this week: €{best_price_total:.2f}")
            totals_label.pack()

            savings_label = Label(self.root, text=f"Savings to be invested in portfolio this week: €{savings:.2f}")
            savings_label.pack()

            # Calculate potential savings in 52 weeks and total return
            total_return = annual_savings * 1.03  # Assuming a 3% return

            # Display potential savings and total return
            potential_savings_label = Label(self.root, text=f"Potential Savings in 52 weeks: €{annual_savings:.2f}")
            potential_savings_label.pack()

            total_return_label = Label(self.root, text=f"Total Annual Return (at a 3% return rate): €{total_return:.2f}")
            total_return_label.pack()

            # Add the "Order and Invest Savings" button
            invest_button = Button(self.root, text="Order and Invest Savings", command=self.invest_savings)
            invest_button.pack()

            # Show the dataframe in a new window
            self.show_dataframe(data)

            # Display the final message
            messagebox.showinfo("Thank You", "Thank you for choosing SaveR! Let's turn savings into future wealth!")
        except Exception as e:
            messagebox.showerror("Error", str(e))


    def create_random_dataframe(self):
        # Grocery list with expanded items and increased values
        grocery_list = [
            "Apple", "Banana", "Milk", "Bread", "Eggs", "Cheese", "Tomato", "Potato", "Carrot",
            "Chicken", "Beef", "Pork", "Salmon", "Butter", "Yogurt", "Cereal", "Orange Juice",
            "Onion", "Garlic", "Pasta", "Rice", "Coffee", "Tea"
        ]

        # Randomly select 22 items from the grocery list
        selected_items = random.sample(grocery_list, k=22)

        # Create a random dataframe with common groceries and prices
        data = {
            "Item": selected_items,
            "Price": [round(random.uniform(1, 10), 2) for _ in range(22)],
            "Supermarket": random.choices(["Lidl", "Dirk", "Coop", "Jumbo", "Bol.com"], k=22)
        }

        # Calculate the "Best Price" as a discount of 5-10% from the original price
        data["Best Price"] = [price * random.uniform(0.90, 0.95) if supermarket != "Albert Heijn" else price for price, supermarket in zip(data["Price"], data["Supermarket"])]

        df = pd.DataFrame(data)
        return df.round(2)

    def show_dataframe(self, data):
        top = Tk()
        top.title("Grocery Bill Summary")

        label = Label(top, text="Grocery Bill Summary")
        label.pack()

        # Create a text widget to display the dataframe
        text_widget = Text(top)
        text_widget.insert(tk.END, data.to_string(index=False))
        text_widget.pack()

        top.mainloop()

    def invest_savings(self):
        # Placeholder function for investing the savings
        messagebox.showinfo("Investment", "Savings will be invested in the portfolio.")

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    upload_gui = UploadGroceryBillGUI()
    upload_gui.start()
