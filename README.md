# 🏍️ Bike Showroom Management System

A Python Tkinter application to manage bike showroom inventory, sales, and billing.

## Overview

The Bike Showroom Management System is a desktop application developed in Python using Tkinter for GUI and FPDF for generating invoices. This application allows showroom owners to efficiently manage their inventory of bikes, handle sales, generate bills (with optional EMI calculation), and maintain records in a simple and intuitive interface.

Features

Display Bikes – View all available bikes with details such as name, model, mileage, fuel capacity, and price.

Add Bike – Add new bikes to the showroom inventory.

Modify Bike – Update existing bike details like fuel capacity, mileage, and price.

Delete Bike – Remove a bike from the inventory.

Generate Bill – Create invoices for customers with total price calculation and optional EMI (12 months) breakdown.

Persistent Storage – Uses pickle to save and load bike data in a binary file.

PDF Invoice – Generate and save invoices as PDF (requires fpdf).

User-Friendly GUI – Built with Tkinter for easy navigation and interaction.

## Requirements

To run this project, make sure your system has the following installed:

Python 3.8+ – programming language for the application.

tkinter – built-in Python library for GUI.

fpdf – Python library for generating PDF invoices (pip install fpdf).

pickle – built-in Python module for data storage.

os – built-in Python module for file handling.

Git (optional) – for version control.

IDE or Text Editor – e.g., VSCode, PyCharm, or any text editor.

Optional: A requirements.txt can be created with fpdf to install dependencies easily:

fpdf

Installation & Setup

Clone the repository

git clone https://github.com/YourUsername/bike-showroom-management.git


Navigate to the project directory

cd bike-showroom-management


Install dependencies

pip install -r requirements.txt


Run the application

python main.py


The application will launch a GUI window where you can manage bikes and generate invoices.

Usage

Display Bikes: Click “Display Bikes” to view all available bikes.

Add Bike: Enter bike details and click “Add Bike.”

Modify Bike: Enter Bike ID and update fields.

Delete Bike: Enter Bike ID to remove a bike.

Generate Bill: Enter Bike ID, customer details, quantity, and EMI option. Invoice will be displayed and can be saved as PDF.

Exit: Close the application.

File Structure
bike-showroom-management/
│
├── main.py           # Main Python application
├── bikes.dat         # Binary file for storing bike data (auto-generated)
├── LICENSE           # MIT License
├── README.md         # Project documentation
├── requirements.txt  # Required Python packages
└── .gitignore        # Files to ignore in Git

License

This project is licensed under the MIT License – see the LICENSE
 file for details.

Future Enhancements

Search Functionality – Search bikes by name, model, or price.

Sorting & Filtering – Sort bikes by price, mileage, or model.

Advanced Billing – Include discounts, taxes, and multiple payment options.

Database Integration – Move from pickle to SQLite or MySQL for better scalability.

Modern GUI – Upgrade to ttk or PyQt for a modern interface
