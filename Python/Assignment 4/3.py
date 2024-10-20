'''3
Create classes Device, Smartphone, and FeaturePhone.
• Classes:
• Device (base class)
• Smartphone (inherits from Device)
• FeaturePhone (inherits from Device)
• Create appropriate methods to get and display details for all classes.
• Implement constructors and destructors for each class.
• Modify the Smartphone class to include a method that calculates and displays the available
storage space based on the total storage and used storage.
• Modify the FeaturePhone class to include a method that calculates and displays the battery
life based on the battery capacity and usage rate.
• Add a new class called GamingSmartphone that also inherits from Smartphone.
• The GamingSmartphone class should have an additional attribute for gaming-specific
features (e.g., "High Refresh Rate", "Enhanced Cooling").
• Implement methods to display gaming features and determine if the smartphone is suitable
for gaming based on these features.
'''


class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"Device {self.brand} {self.model} created.")

    def display_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

    def __del__(self):
        print(f"Device {self.brand} {self.model} destroyed.")


class Smartphone(Device):
    def __init__(self, brand, model, total_storage, used_storage):
        super().__init__(brand, model)
        self.total_storage = total_storage
        self.used_storage = used_storage
        print(f"Smartphone {self.brand} {self.model} created.")

    def display_details(self):
        super().display_details()
        self.calculate_available_storage()

    def calculate_available_storage(self):
        available_storage = self.total_storage - self.used_storage
        print(f"Total Storage: {self.total_storage}GB, Used Storage: {self.used_storage}GB, Available Storage: {available_storage}GB")

    def __del__(self):
        print(f"Smartphone {self.brand} {self.model} destroyed.")


class FeaturePhone(Device):
    def __init__(self, brand, model, battery_capacity, usage_rate):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
        self.usage_rate = usage_rate
        print(f"FeaturePhone {self.brand} {self.model} created.")

    def display_details(self):
        super().display_details()
        self.calculate_battery_life()

    def calculate_battery_life(self):
        battery_life = self.battery_capacity / self.usage_rate
        print(f"Battery Capacity: {self.battery_capacity}mAh, Usage Rate: {self.usage_rate}mAh/hour, Estimated Battery Life: {battery_life} hours")

    def __del__(self):
        print(f"FeaturePhone {self.brand} {self.model} destroyed.")


class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, total_storage, used_storage, gaming_features):
        super().__init__(brand, model, total_storage, used_storage)
        self.gaming_features = gaming_features
        print(f"GamingSmartphone {self.brand} {self.model} created.")

    def display_details(self):
        super().display_details()
        self.display_gaming_features()
        self.is_suitable_for_gaming()

    def display_gaming_features(self):
        print(f"Gaming Features: {', '.join(self.gaming_features)}")

    def is_suitable_for_gaming(self):
        if "High Refresh Rate" in self.gaming_features and "Enhanced Cooling" in self.gaming_features:
            print(f"{self.brand} {self.model} is suitable for gaming.")
        else:
            print(f"{self.brand} {self.model} is not ideal for gaming.")

    def __del__(self):
        print(f"GamingSmartphone {self.brand} {self.model} destroyed.")


# Example usage
if __name__ == "__main__":

    gaming_phone = GamingSmartphone("SuperTech", "GamerX", 256, 120, ["High Refresh Rate", "Enhanced Cooling", "RGB Lighting"])
    

    gaming_phone.display_details()

    print("\n")


    feature_phone = FeaturePhone("OldSchool", "Classic200", 1500, 50)


    feature_phone.display_details()

    del gaming_phone
    del feature_phone
