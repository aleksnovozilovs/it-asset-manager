from device import Device

devices = [
    Device("Aleks laptop", "Apple", "M4", "24GB"), 
    Device("Reception PC", "Dell", "Intel i5 Ultra", "16GB")
]

print("===== IT Asset Manager =====")
print()
print("1. Show Devices")
print("2. Add Device")
print("3. Exit ")
print()
option = input("Choose an option: ")
print()

if option == "1":
    for device in devices:
        device.display_info()
elif option == "2":
    new_device = Device(input("Enter device name: "), input("Enter device brand: "),
                                                     input("Enter devices CPU: "),
                                                            input("Enter device RAM: "))
    devices.append(new_device)
    print()
    print("Device added: ")
    new_device.display_info()
    
elif option == "3":
    print("Good bye!")
    print()
    exit()
else:
    print("Incorrect option, please restart the programm and try again")
    print()