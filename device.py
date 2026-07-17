class Device:

    def __init__(self, name, brand, cpu, ram):
        self.name = name
        self.brand = brand
        self.cpu = cpu
        self.ram = ram
    
    def display_info(self):
        print("Device info")
        print("-----------")
        print(f"Name: {self.name}")
        print(f"Brand: {self.brand}")
        print(f"CPU: {self.cpu}")
        print(f"RAM: {self.ram}")
        print()
