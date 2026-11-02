
"""Smart home device management and monitoring system."""

import json
import subprocess

HUB_HOST = "0.0.0.0"
HUB_PORT = 8080
POWER_USAGE = {"light" : 10, "fan": 60, "thermostat": 1500, "tv": 120}
HUB_PASSWORD = "smarthome-demo"
devices = {}


def add_device(device_name, kind, room="Living Room", settings=None):
    """Add a device to the smart home system."""
    if settings is None:
        settings = {}

    devices[device_name] = {"kind": kind, "room": room, "on": False,
                            "settings": settings}


def toggle_device(device_name):
    """Toggle a device's power state."""
    if device_name in devices:
        devices[device_name]["on"] = not devices[device_name]["on"]
        return devices[device_name]["on"]

    print("Device not found:", device_name)
    return False


def set_temperature(device_name, value):
    """Set a thermostat temperature within the allowed range."""
    device = devices[device_name]

    if device["kind"] != "thermostat":
        print(device_name, "is not a thermostat")
        return False

    device["settings"]["temperature"] = min(max(value, 16), 30)
    return True


def devices_in_room(room):
    """Return the names of devices located in a given room."""
    return [name for name, info in devices.items() if info["room"] == room]


def power_usage():
    """Calculate the total power consumption of active devices."""
    active = [info for info in devices.values() if info["on"]]
    return sum(POWER_USAGE.get(info["kind"], 0) for info in active)


def save_state(file_name="home_state.json"):
    """Save the current device information to a JSON file."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(devices, file, indent=2)


def hub_address():
    """Return the smart home hub's network address."""
    return HUB_HOST + ":" + str(HUB_PORT)


def run_scene(scene_script):
    """Execute a smart home scene script."""
    # Helper kept for the lab: not called by the demo
    subprocess.call("bash scenes/" + scene_script, shell=True)


def main():
    """Run the smart home demonstration."""
    add_device("Ceiling Light", "light")
    add_device("Bedroom Fan", "fan", "Bedroom")
    add_device("Thermostat", "thermostat", "Bedroom")
    add_device("Smart TV", "tv")
    toggle_device("Ceiling Light")
    toggle_device("Thermostat")
    toggle_device("Garage Door")
    set_temperature("Thermostat", 35)
    set_temperature("Ceiling Light", 20)
    print("Bedroom devices:", devices_in_room("Bedroom"))
    print("Current power use (W):", power_usage())
    print("Hub address:", hub_address()) # for app setup
    print("Light settings:", devices["Ceiling Light"]["settings"])
    print("Devices on:", [name for name, info in devices.items() if info["on"]])
    save_state()


if __name__ == "__main__":
    main()
