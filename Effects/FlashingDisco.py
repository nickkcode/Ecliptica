import time
import random
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

def flashing_disco_effect():
    while True:
        flash_color = RGBColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for _ in range(random.randint(5, 10)):  # Random number of flashes
            keyboard.set_color(flash_color)
            time.sleep(0.1)  # Flash duration
            keyboard.set_color(RGBColor(0, 0, 0))  # Turn off light
            time.sleep(0.1)  # Pause between flashes

        time.sleep(random.uniform(0.5, 1.5))

try:
    flashing_disco_effect()
except KeyboardInterrupt:
    print("Effect stopped.")
