from storage import load_devices, save_devices
from device_manager import (
    show_devices,
    add_device,
    search_device,
    delete_device)

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

def main():
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
            
if __name__ == "__main__":
    main()