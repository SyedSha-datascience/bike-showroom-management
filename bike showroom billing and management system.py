import pickle
import os
from tkinter import *
from tkinter import messagebox
from fpdf import FPDF

class BikeShowroomGUI:
    FILE_NAME = "bikes.dat"

    def __init__(self, root):
        self.root = root
        self.root.title("🏍️ Bike Showroom Management System")
        self.root.geometry("600x500")

        self.bikes = self.load_bikes()

        Label(self.root, text="🏍️ Bike Showroom Management", font=("Arial", 16, "bold")).pack(pady=10)

        Button(self.root, text="Display Bikes", command=self.display_bikes, width=20, height=2).pack(pady=5)
        Button(self.root, text="Add Bike", command=self.add_bike, width=20, height=2).pack(pady=5)
        Button(self.root, text="Modify Bike", command=self.modify_bike, width=20, height=2).pack(pady=5)  # New Button
        Button(self.root, text="Delete Bike", command=self.delete_bike, width=20, height=2).pack(pady=5)
        Button(self.root, text="Generate Bill", command=self.generate_bill, width=20, height=2).pack(pady=5)
        Button(self.root, text="Exit", command=self.root.quit, width=20, height=2, bg="red", fg="white").pack(pady=20)

    def load_bikes(self):
        """Loads bikes from the binary file, if available."""
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "rb") as file:
                return pickle.load(file)
        else:
            return {
                1: {"name": "Yamaha R15", "model": "V4", "fuel_capacity": "11L", "mileage": "45 kmpl", "price": 180000},
                2: {"name": "KTM Duke 200", "model": "BS6", "fuel_capacity": "13.5L", "mileage": "35 kmpl", "price": 210000},
                3: {"name": "Royal Enfield Classic 350", "model": "BS6", "fuel_capacity": "13L", "mileage": "40 kmpl", "price": 230000},
            }

    def save_bikes(self):
        """Saves bikes to the binary file."""
        with open(self.FILE_NAME, "wb") as file:
            pickle.dump(self.bikes, file)

    def display_bikes(self):
        """Displays available bikes in a new window."""
        bike_window = Toplevel(self.root)
        bike_window.title("Available Bikes")
        bike_window.geometry("500x300")

        Label(bike_window, text="Available Bikes", font=("Arial", 14, "bold")).pack(pady=10)
        text_area = Text(bike_window, height=10, width=60)
        text_area.pack()

        for bike_id, details in self.bikes.items():
            text_area.insert(END, f"ID: {bike_id}, {details['name']} ({details['model']}) - ₹{details['price']}\n")

    def modify_bike(self):
        """Opens a window to modify bike details."""
        modify_window = Toplevel(self.root)
        modify_window.title("Modify Bike Details")
        modify_window.geometry("300x300")

        Label(modify_window, text="Enter Bike ID to Modify:").pack()
        bike_id_entry = Entry(modify_window)
        bike_id_entry.pack()

        Label(modify_window, text="New Fuel Capacity (e.g., 12L):").pack()
        fuel_entry = Entry(modify_window)
        fuel_entry.pack()

        Label(modify_window, text="New Mileage (e.g., 40 kmpl):").pack()
        mileage_entry = Entry(modify_window)
        mileage_entry.pack()

        Label(modify_window, text="New Price (₹):").pack()
        price_entry = Entry(modify_window)
        price_entry.pack()

        def update_bike():
            try:
                bike_id = int(bike_id_entry.get())
                if bike_id not in self.bikes:
                    messagebox.showerror("Error", "Invalid Bike ID!")
                    return

                new_fuel = fuel_entry.get().strip()
                new_mileage = mileage_entry.get().strip()
                new_price = int(price_entry.get().strip())

                self.bikes[bike_id]["fuel_capacity"] = new_fuel
                self.bikes[bike_id]["mileage"] = new_mileage
                self.bikes[bike_id]["price"] = new_price

                self.save_bikes()
                messagebox.showinfo("Success", "Bike details updated successfully!")
                modify_window.destroy()

            except ValueError:
                messagebox.showerror("Error", "Invalid input! Please enter correct values.")

        Button(modify_window, text="Update Bike", command=update_bike, bg="blue", fg="white").pack(pady=10)

    def add_bike(self):
        """Opens a window to add a new bike."""
        add_window = Toplevel(self.root)
        add_window.title("Add New Bike")
        add_window.geometry("300x300")

        Label(add_window, text="Bike Name:").pack()
        name_entry = Entry(add_window)
        name_entry.pack()

        Label(add_window, text="Model:").pack()
        model_entry = Entry(add_window)
        model_entry.pack()

        Label(add_window, text="Fuel Capacity:").pack()
        fuel_entry = Entry(add_window)
        fuel_entry.pack()

        Label(add_window, text="Mileage:").pack()
        mileage_entry = Entry(add_window)
        mileage_entry.pack()

        Label(add_window, text="Price (₹):").pack()
        price_entry = Entry(add_window)
        price_entry.pack()

        def save_bike():
            try:
                bike_id = max(self.bikes.keys(), default=0) + 1
                self.bikes[bike_id] = {
                    "name": name_entry.get(),
                    "model": model_entry.get(),
                    "fuel_capacity": fuel_entry.get(),
                    "mileage": mileage_entry.get(),
                    "price": int(price_entry.get())
                }
                self.save_bikes()
                messagebox.showinfo("Success", "Bike added successfully!")
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid price input!")

        Button(add_window, text="Add Bike", command=save_bike).pack(pady=10)

    def delete_bike(self):
        """Opens a window to delete a bike."""
        delete_window = Toplevel(self.root)
        delete_window.title("Delete Bike")
        delete_window.geometry("300x150")

        Label(delete_window, text="Enter Bike ID to Delete:").pack()
        bike_id_entry = Entry(delete_window)
        bike_id_entry.pack()

        def remove_bike():
            try:
                bike_id = int(bike_id_entry.get())
                if bike_id in self.bikes:
                    del self.bikes[bike_id]
                    self.save_bikes()
                    messagebox.showinfo("Success", "Bike deleted successfully!")
                    delete_window.destroy()
                else:
                    messagebox.showerror("Error", "Invalid Bike ID!")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid numeric ID!")

        Button(delete_window, text="Delete Bike", command=remove_bike, bg="red", fg="white").pack(pady=10)

    def generate_bill(self):
        """Opens a window to generate a bill."""
        bill_window = Toplevel(self.root)
        bill_window.title("Generate Bill")
        bill_window.geometry("300x350")

        Label(bill_window, text="Bike ID:").pack()
        bike_id_entry = Entry(bill_window)
        bike_id_entry.pack()

        Label(bill_window, text="Customer Name:").pack()
        customer_name_entry = Entry(bill_window)
        customer_name_entry.pack()

        Label(bill_window, text="Customer Contact:").pack()
        customer_contact_entry = Entry(bill_window)
        customer_contact_entry.pack()

        Label(bill_window, text="Quantity:").pack()
        quantity_entry = Entry(bill_window)
        quantity_entry.pack()

        Label(bill_window, text="EMI (yes/no):").pack()
        emi_entry = Entry(bill_window)
        emi_entry.pack()

        def process_bill():
            bike_id = int(bike_id_entry.get())
            if bike_id not in self.bikes:
                messagebox.showerror("Error", "Invalid Bike ID!")
                return

            bike = self.bikes[bike_id]
            quantity = int(quantity_entry.get())
            total_price = bike["price"] * quantity
            emi_option = emi_entry.get().strip().lower()
            emi_per_month = None

            if emi_option == "yes":
                tenure = 12
                interest_rate = 0.10
                total_interest = total_price * (interest_rate / 12) * tenure
                total_payable = total_price + total_interest
                emi_per_month = total_payable / tenure

            invoice = f"Customer: {customer_name_entry.get()}\nContact: {customer_contact_entry.get()}\nBike: {bike['name']} ({bike['model']})\nTotal Price: ₹{total_price}\n"
            if emi_per_month:
                invoice += f"EMI: ₹{emi_per_month:.2f} per month (12 months)"

            messagebox.showinfo("Invoice", invoice)

        Button(bill_window, text="Generate Bill", command=process_bill, bg="green", fg="white").pack(pady=10)


# Run the application
if __name__ == "__main__":
    root = Tk()
    app = BikeShowroomGUI(root)
    root.mainloop()
