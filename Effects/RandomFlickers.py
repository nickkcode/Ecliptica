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

def random_flicker_effect():
    while True:
        color = RGBColor(random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        for _ in range(random.randint(5, 15)):  # Random number of flickers
            if random.choice([True, False]):
                keyboard.set_color(color)  # Set full brightness
            else:
                keyboard.set_color(RGBColor(0, 0, 0))  # Turn off
            time.sleep(random.uniform(0.05, 0.2))  # Random flicker speed

        time.sleep(random.uniform(0.5, 1.5))

try:
    random_flicker_effect()
except KeyboardInterrupt:
    print("Effect stopped.")
