# SaveR
SaveR is a personal savings app that helps users track expenses, analyze grocery bills, and manage their savings and investments.

main.py: This script is the entry point of the SaveR app. It creates the main menu GUI where users can choose to login, register, or exit the app.

session.py: This script defines the Session class, which manages the user session in the app. It keeps track of the current user and provides methods to set and get the current user.

register_gui.py: This script implements the RegisterGUI class, which provides a GUI for user registration. It allows users to enter their username, password, and other details to create an account.

login_gui.py: This script implements the LoginGUI class, which provides a GUI for user login. It prompts users to enter their username and password and verifies the credentials against the user database.

myprofile_gui.py: This script implements the MyProfileGUI class, which displays the user's profile information and allows them to manage their profile settings, such as their post code, monthly budget, risk appetite, dietary requirements. It provides options to view and edit the user's personal details.

upload_grocery_bill.py: This script implements the UploadGroceryBillGUI class, which allows users to upload their grocery bills for analysis. It provides a file upload feature and displays the analyzed bill with price details and potential savings.

users.json: This JSON file stores user account information. It contains a dictionary where the keys are usernames and the values are user details, including the password.

supermarkets.json: This JSON file stores information about supermarkets. It contains a list of supermarkets, each represented by a dictionary with details of grocery products and their price.
