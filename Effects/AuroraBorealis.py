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

def aurora_borealis_effect():
    while True:
        smooth_transition = random.choice([True, False])
        color = RGBColor(
            int(random.uniform(0, 100)),  # Random green
            int(random.uniform(0, 255)),  # Random blue
            int(random.uniform(0, 100))   # Random purple
        )
        
        if smooth_transition:
            for i in range(10):
                red = int(color.red * (i / 10))
                green = int(color.green * (i / 10))
                blue = int(color.blue * (i / 10))
                keyboard.set_color(RGBColor(red, green, blue))
                time.sleep(random.uniform(0.1, 0.5))
        else:
            keyboard.set_color(color)

        time.sleep(random.uniform(0.3, 1.5))

try:
    aurora_borealis_effect()
except KeyboardInterrupt:
    print("Effect stopped.")
