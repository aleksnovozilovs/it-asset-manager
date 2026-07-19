from device import Device

def load_devices():
    devices = []
    with open("devices.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            name, brand, cpu, ram = [value.strip() for value in line.split(",")]
            device = Device(name, brand, cpu, ram)
            devices.append(device)
    return devices

def save_devices(devices):
    with open("devices.txt", "w") as file:
        for device in devices:
            file.write(f"{device.name},{device.brand},{device.cpu},{device.ram}\n")

def show_menu():
    print("===== IT Asset Manager =====")
    print()
    print("1. Show Devices")
    print("2. Add Device")
    print("3. Search Device")
    print("4. Delete Device")
    print("5. Exit ")
    print()
    option = input("Choose an option: ")
    return option

def show_devices(devices):
    for device in devices:
            device.display_info()

def add_device(devices):
    new_device = Device(input("Enter device name: "), input("Enter device brand: "),
                                                     input("Enter devices CPU: "),
                                                            input("Enter device RAM: "))
    devices.append(new_device)
    save_devices(devices)
    print()
    print("Device added: ")
    print()
    new_device.display_info()

def search_device(devices):
    user_input = input("Enter device name: ").casefold()
    found = False
    for device in devices:
        if device.name.casefold() == user_input or device.brand.casefold() == user_input:
            found = True
            print()
            print ("Device found")
            print()
            device.display_info()
    if not found:
        print()
        print("Device not found")
        print()

def delete_device(devices):
    if not devices:
        print()
        print("No devices availible to delete")
        print()
        return
    for index, device in enumerate(devices):
        print(f"{index + 1}.{device.name}")
    print()
    try:
        device_number = int(input("Choose device number: "))
        if 0 <= (device_number - 1) < len(devices):
            selected_device = devices[device_number - 1]
            print()
            confirm = input(f"Delete {selected_device.name}? (y/n): ").casefold()
            if confirm == "y":
                devices.remove(selected_device)
                save_devices(devices)
                print("Device deleted.")
                print()
            elif confirm == "n":
                print("Deletion cancelled.")
                print()
            else:
                print()
                print("Invalid entry")
                print("Returning to main menu...")
                print()
        else: 
            print()
            print("Invalid entry")
            print("Returning to main menu...")
            print()

    except ValueError:
        print()
        print("Invalid entry")
        print("Returning to main menu...")
        print()
        
devices = load_devices()
option = ""
while option != "5":
    option = show_menu()
    if option == "1":
         show_devices(devices)
    elif option == "2":
        add_device(devices)
    elif option == "3":
         search_device(devices)
    elif option == "4":
        delete_device(devices)
    elif option == "5":
        print()
        print("Goodbye!")
        print()
    else:
        print("Incorrect option, please restart the programm and try again")
        print()