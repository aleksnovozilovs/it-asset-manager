from device import Device

def show_menu():
    print("===== IT Asset Manager =====")
    print()
    print("1. Show Devices")
    print("2. Add Device")
    print("3. Exit ")
    print()

def show_devices(devices):
    for device in devices:
            device.display_info()

def add_device(devices):
    new_device = Device(input("Enter device name: "), input("Enter device brand: "),
                                                     input("Enter devices CPU: "),
                                                            input("Enter device RAM: "))
    devices.append(new_device)
    print()
    print("Device added: ")
    print()
    new_device.display_info()
  
devices = [
    Device("Aleks laptop", "Apple", "M4", "24GB"), 
    Device("Reception PC", "Dell", "Intel i5 Ultra", "16GB")
]
option = " "
while option != "3":
    show_menu()
    option = input("Choose an option: ")
    if option == "1":
         show_devices(devices)
    elif option == "2":
        add_device(devices)
    elif option == "3":
        print("Goodbye!")
        print()
    else:
        print("Incorrect option, please restart the programm and try again")
        print()