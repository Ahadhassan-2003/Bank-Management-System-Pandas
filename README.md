# Bank-Management-System-(Pandas)
# DaulatPay Bank Management System

## Overview

DaulatPay is a simple bank management system built in Python using the Tkinter library for the graphical user interface (GUI) and Pandas for data handling. The system uses CSV files to store data for clients, accountants, and the manager, each with different levels of data accessibility.

## Features

### For Clients
- **Withdrawal:** Clients can withdraw money from their accounts.
- **Check Balance:** Clients can check their current account balance.
- **Transfer Funds:** Clients can transfer funds to another account.

### For Accountants
- **Deposit:** Accountants can deposit cash into clients' accounts using their account number.
- **Change Password:** Accountants can change a client's account password, which involves an OTP sent to the client's email for security.
- **Create New Client Account:** Accountants can create a new client account.

### For Manager
- **Block/Unblock Account:** The manager can block or unblock a client account.
- **Check Account Details:** The manager can view details of a client's account.
- **Add New Accountant:** The manager can add a new accountant account.
- **Remove Account:** The manager can remove an account.

## GUI Design

The GUI is designed to be simple, minimalistic, and eye-catching, ensuring a user-friendly experience for both clients and staff members.

## Files and Data Storage

- **client_data.csv:** Stores data related to client accounts.
- **accountant_data.csv:** Stores data related to accountant accounts.
- **manager_data.csv:** Stores data related to the manager's account.

## Dependencies

- Python 3.x
- Tkinter (standard GUI library for Python)
- Pandas (data manipulation library)

## How to Run

1. Clone the repository to your local machine.
2. Ensure you have Python and the required libraries installed.
3. Run the main application file: `python main.py`.

## Important Notes

- Make sure to handle sensitive information securely.
- The application may require additional setup for sending emails and handling OTP verification.

Feel free to explore and enhance the DaulatPay Bank Management System as needed for your specific use case. If you have any questions or suggestions, please contact the project maintainers. Thank you for using DaulatPay!
