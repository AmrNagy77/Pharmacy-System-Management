class Medicine:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class PharmacyManagementSystem:
    def __init__(self):
        self.medicines = {}

    def add_medicine(self, medicine):
        if medicine.name in self.medicines:
            print(f"Medicine '{medicine.name}' already exists.")
        else:
            self.medicines[medicine.name] = medicine.quantity
            print(f"Medicine '{medicine.name}' added to inventory.")

    def remove_medicine(self, medicine_name):
        if medicine_name in self.medicines:
            del self.medicines[medicine_name]
            print(f"Medicine '{medicine_name}' removed from inventory.")
        else:
            print(f"Medicine '{medicine_name}' not found in inventory.")

    def update_quantity(self, medicine_name, new_quantity):
        if medicine_name in self.medicines:
            self.medicines[medicine_name] = new_quantity
            print(f"Quantity of medicine '{medicine_name}' updated to {new_quantity}.")
        else:
            print(f"Medicine '{medicine_name}' not found in inventory.")

    def check_stock(self, medicine_name):
        if medicine_name in self.medicines:
            quantity = self.medicines[medicine_name]
            print(f"Medicine: '{medicine_name}', Quantity: {quantity}")
        else:
            print(f"Medicine '{medicine_name}' not found in inventory.")

    def print_inventory(self):
        print("Inventory:")
        for medicine_name, quantity in self.medicines.items():
            print(f"Medicine: '{medicine_name}', Quantity: {quantity}")


# Creating a new pharmacy management system
pharmacy = PharmacyManagementSystem()

# Adding medicines to inventory
medicine1 = Medicine("Paracetamol", 50)
medicine2 = Medicine("Aspirin", 100)
medicine3 = Medicine("Ibuprofen", 75)

pharmacy.add_medicine(medicine1)
pharmacy.add_medicine(medicine2)
pharmacy.add_medicine(medicine3)

# Checking stock of a medicine
pharmacy.check_stock("Paracetamol")

# Updating quantity of a medicine
pharmacy.update_quantity("Aspirin", 150)

# Removing a medicine from inventory
pharmacy.remove_medicine("Ibuprofen")

# Printing the inventory
pharmacy.print_inventory()