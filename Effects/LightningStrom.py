import random
import time
from openrgb import OpenRGBClient
from openrgb.utils import RGBColor

client = OpenRGBClient()

keyboard = None
for device in client.devices:
    if 'keyboard' in device.name.lower():
        keyboard = device
        break

if not keyboard:
    print("Keyboard not found.")
    exit()

print(f"Found keyboard: {keyboard.name}")

def lightning_storm_effect():
    while True:
        flash_duration = random.uniform(0.1, 0.3)
        keyboard.set_color(RGBColor(255, 255, 255))  # Lightning flash
        time.sleep(flash_duration)

        for i in range(10):
            intensity = int(30 + (225 * (i / 10)))
            keyboard.set_color(RGBColor(intensity, intensity, intensity))  # Stormy clouds
            time.sleep(0.05)

        keyboard.set_color(RGBColor(30, 30, 30))  # Dark storm color
        time.sleep(random.uniform(0.5, 2.0))

try:
    lightning_storm_effect()
except KeyboardInterrupt:
    print("Effect stopped.")
