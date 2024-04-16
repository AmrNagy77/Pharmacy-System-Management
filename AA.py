import tkinter as tk
from tkinter import messagebox

class Medicine:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class PharmacyManagementSystem:
    def __init__(self):
        self.medicines = {}
        self.medicine_prices = {}
        self.medicine_quantities = []

    def add_medicine(self, medicine):
        if medicine.name in self.medicines:
            messagebox.showinfo("Error", f"Medicine '{medicine.name}' already exists.")
        else:
            self.medicines[medicine.name] = medicine
            self.medicine_prices[medicine.name] = medicine.price
            self.medicine_quantities.append(medicine.name)
            messagebox.showinfo("Success", f"Medicine '{medicine.name}' added to inventory.")

    def remove_medicine(self, medicine_name):
        if medicine_name in self.medicines:
            del self.medicines[medicine_name]
            del self.medicine_prices[medicine_name]
            self.medicine_quantities.remove(medicine_name)
            messagebox.showinfo("Success", f"Medicine '{medicine_name}' removed from inventory.")
        else:
            messagebox.showinfo("Error", f"Medicine '{medicine_name}' not found in inventory.")

    def update_quantity(self, medicine_name, new_quantity):
        if medicine_name in self.medicines:
            self.medicines[medicine_name].quantity = new_quantity
            messagebox.showinfo("Success", f"Quantity of medicine '{medicine_name}' updated to {new_quantity}.")
        else:
            messagebox.showinfo("Error", f"Medicine '{medicine_name}' not found in inventory.")

    def search_medicine(self, medicine_name):
        if medicine_name in self.medicines:
            medicine = self.medicines[medicine_name]
            messagebox.showinfo("Medicine Details",
                                f"Medicine: '{medicine.name}'\nQuantity: {medicine.quantity}\nPrice: {medicine.price}")
        else:
            messagebox.showinfo("Error", f"Medicine '{medicine_name}' not found in inventory.")

    def get_inventory(self):
        inventory = []
        for medicine_name in self.medicine_quantities:
            medicine = self.medicines[medicine_name]
            inventory.append(f"Medicine: '{medicine.name}', Quantity: {medicine.quantity}, Price: {medicine.price}")
        return inventory

def search_medicine():
    medicine_name = search_entry.get()
    pharmacy.search_medicine(medicine_name)

def add_medicine():
    name = name_entry.get()
    quantity = int(quantity_entry.get())
    price = float(price_entry.get())
    medicine = Medicine(name, quantity, price)
    pharmacy.add_medicine(medicine)
    inventory_listbox.delete(0, tk.END) # type: ignore
    inventory_listbox.insert(tk.END, *pharmacy.get_inventory()) # type: ignore


# Creating a new pharmacy management system
pharmacy = PharmacyManagementSystem()

# Adding medicines to inventory
medicines = [
    Medicine("Paracetamol", 50, 2.5),
    Medicine("Aspirin", 100, 3.0),
    Medicine("Ibuprofen", 75, 4.0),
    # Add more medicines here
]

for medicine in medicines:
    pharmacy.add_medicine(medicine)

# Creating the GUI
window = tk.Tk()
window.title("Pharmacy Management System")

# Create search section
search_frame = tk.Frame(window)
search_frame.pack(pady=10)

search_label = tk.Label(search_frame, text="Search:")
search_label.grid(row=0, column=0, padx=5)

search_entry = tk.Entry(search_frame, width=30)
search_entry.grid(row=0, column=1, padx=5)

search_button = tk.Button(search_frame, text="Search", command=search_medicine)
search_button.grid(row=0, column=2, padx=5)

# Create add section
add_frame = tk.Frame(window)
add_frame.pack(pady=10)

name_label = tk.Label(add_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5)

name_entry = tk.Entry(add_frame, width=30)
name_entry.grid(row=0, column=1, padx=5)

quantity_label = tk.Label(add_frame, text="Quantity:")
quantity_label.grid(row=1, column=0, padx=5)

quantity_entry = tk.Entry(add_frame, width=30)
quantity_entry.grid(row=1, column=1, padx=5)

price_label = tk.Label(add_frame, text="Price:")
price_label.grid(row=2, column=0, padx=5)

price_entry = tk.Entry(add_frame, width=30)
price_entry.grid(row=2, column=1, padx=5)

add_button = tk.Button=add_frame, text="I apologize, but it seems that the code you provided is incomplete. Could you please provide the missing part of the code?"