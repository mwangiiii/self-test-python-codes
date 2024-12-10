# Base Class
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life

    def display_specs(self):
        return f"{self.brand} {self.model}: {self.storage}GB Storage, {self.battery_life}h Battery Life"

    def charge(self):
        return f"{self.brand} {self.model} is charging..."

# Derived Class
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, cooling_system):
        super().__init__(brand, model, storage, battery_life)
        self.cooling_system = cooling_system

    def display_specs(self):
        # Polymorphism: Overriding the display_specs method
        basic_specs = super().display_specs()
        return f"{basic_specs}, Cooling System: {self.cooling_system}"

    def enable_game_mode(self):
        return f"Game Mode enabled on {self.brand} {self.model} for an enhanced gaming experience!"

# Create instances
basic_phone = Smartphone("Samsung", "Galaxy S22", 128, 15)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 5", 256, 20, "Active Aero Cooler")

# Display details and explore methods
print(basic_phone.display_specs())  # Samsung Galaxy S22: 128GB Storage, 15h Battery Life
print(basic_phone.charge())         # Samsung Galaxy S22 is charging...

print(gaming_phone.display_specs())  # Asus ROG Phone 5: 256GB Storage, 20h Battery Life, Cooling System: Active Aero Cooler
print(gaming_phone.enable_game_mode())  # Game Mode enabled on Asus ROG Phone 5 for an enhanced gaming experience!
