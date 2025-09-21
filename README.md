# 🏍️ Bike Showroom Management System
A Python Tkinter application to manage bike showroom inventory, sales, and billing.

## Overview
The Bike Showroom Management System is a desktop application developed in Python using Tkinter for GUI and FPDF for generating invoices. This application allows showroom owners to efficiently manage their inventory of bikes, handle sales, generate bills (with optional EMI calculation), and maintain records in a simple and intuitive interface.

## Features
Display Bikes – View all available bikes with details such as name, model, mileage, fuel capacity, and price.
Add Bike – Add new bikes to the showroom inventory.
Modify Bike – Update existing bike details like fuel capacity, mileage, and price.
Delete Bike – Remove a bike from the inventory.
Generate Bill – Create invoices for customers with total price calculation and optional EMI (12 months) breakdown.
Persistent Storage – Uses pickle to save and load bike data in a binary file.
PDF Invoice – Generate and save invoices as PDF (requires fpdf).
User-Friendly GUI – Built with Tkinter for easy navigation and interaction.
