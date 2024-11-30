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

def police_light_effect():
    while True:
        flash_speed = random.uniform(0.01, 0.3)  # Adjust for faster or slower flashing

        for _ in range(random.randint(3, 5)):  # Number of flashes per cycle
            keyboard.set_color(RGBColor(255, 0, 0))  # Red light
            time.sleep(flash_speed)  # Flash duration
            keyboard.set_color(RGBColor(0, 0, 255))  # Blue light
            time.sleep(flash_speed)  # Flash duration

        time.sleep(random.uniform(1.0, 3.0))

try:
    police_light_effect()
except KeyboardInterrupt:
    print("Effect stopped.")
