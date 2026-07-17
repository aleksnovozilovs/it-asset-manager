from device import Device

devices = [
    Device("Aleks laptop", "Apple", "M4", "24GB"), 
    Device("Reception PC", "Dell", "Intel i5 Ultra", "16GB")
]

for device in devices:
    device.display_info()
