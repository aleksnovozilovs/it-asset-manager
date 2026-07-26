from device import Device
from storage import save_devices
from menus import show_devices_menu

def show_devices(devices):
    option = ""

    while option != "6":
        option = show_devices_menu()

        if option == "1":
            for device in devices:
                device.display_info() 
            return          
        elif option == "2":
            sorted_devices = sorted(devices, key = lambda device: device.name)
            for device in sorted_devices:
                device.display_info()
            return
        elif option == "3":
            sorted_devices = sorted(devices, key = lambda device: device.brand)
            for device in sorted_devices:
                device.display_info()
            return
        elif option == "4":
            sorted_devices = sorted(devices, key = lambda device: device.cpu)
            for device in sorted_devices:
                device.display_info()
            return
        elif option == "5":
            sorted_devices = sorted(devices, key = lambda device: device.ram)
            for device in sorted_devices:
                device.display_info()
            return
        elif option == "6": 
            break
        else:  
            print("Incorrect option, please try again")
            print()     


    
    

def add_device(devices):
    name = input("Enter device name: ")
    brand = input("Enter device brand: ")
    cpu = input("Enter devices CPU: ")
    while True:
        try:
            ram = int(input("Enter device RAM (GB): "))  
            break
        except ValueError: 
            print()
            print("Please enter a whole number.")
            print()
    new_device = Device(name, brand, cpu, ram)
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
    
    for index, device in enumerate(devices, start = 1):
        print(f"{index}. {device.name}")
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

def edit_device (devices):
    if not devices:
        print()
        print("No devices available to edit")
        print()
        return
    
    for index, device in enumerate(devices, start = 1):
        print(f"{index}. {device.name}")
    print()

    try:
        device_number = int(input("Choose device number: "))
        if 0 <= (device_number - 1) < len(devices):
            selected_device = devices[device_number - 1]

            print("Current Device:")
            print("---------------")
            print(f"1. Name: {selected_device.name}")
            print(f"2. Brand: {selected_device.brand}")
            print(f"3. CPU: {selected_device.cpu}")
            print(f"4. RAM: {selected_device.ram}")

            selected_option = int(input("Choose option to edit (1 to 4): "))
            print()
       
            if selected_option == 1:
                attribute = "name"
                label = "Name"
            elif selected_option == 2:
                attribute = "brand"
                label = "Brand"
            elif selected_option == 3:
                attribute = "cpu"
                label = "CPU"
            elif selected_option == 4:
                attribute = "ram"
                label = "RAM"
            else:
                print()
                print ("Item not found, please try again.")
                print("Returning to main menu...")
                print()
                return
        else:
            print() 
            print("Invalid device number")
            print("Returning to main menu...")
            print()
            return

        print(f"Current {label}: {getattr(selected_device, attribute)}")
        print()
        new_value = input(f"Enter new {label}: ")
        if new_value:
            print()
            setattr(selected_device, attribute, new_value)
            save_devices(devices)
            print(f"Device {label} successfully updated!")
            print()
        else:
            print()
            print("No changes made.")
            print("Returning to main menu...")
            print()

    except ValueError:
        print()
        print("Invalid entry")
        print("Returning to main menu...")
        print()  

    