from device import Device

def load_devices():
    devices = []
    with open("devices.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            name, brand, cpu, ram = [value.strip() for value in line.split(",")]
            device = Device(name, brand, cpu, int(ram))
            devices.append(device)
    return devices

def save_devices(devices):
    with open("devices.txt", "w") as file:
        for device in devices:
            file.write(f"{device.name},{device.brand},{device.cpu},{device.ram}\n")