from menus import show_main_menu
from storage import load_devices
from device_manager import (
    show_devices,
    add_device,
    search_device,
    delete_device,
    edit_device)

def main():
    devices = load_devices()
    option = ""

    while option != "6":
        option = show_main_menu()

        if option == "1":
            show_devices(devices)
        elif option == "2":
            add_device(devices)
        elif option == "3":
            search_device(devices)
        elif option == "4":
            delete_device(devices)
        elif option == "5":
            edit_device(devices)
        elif option == "6":
            print()
            print("Goodbye!")
            print()
        else:
            print("Incorrect option, please restart the programm and try again")
            print()
            
if __name__ == "__main__":
    main()