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

def flame_ember_effect():
    while True:
        transition_speed = random.uniform(0.2, 1.0)  # Transition speed
        intensity = random.uniform(0.3, 1.0)  # Random brightness

        start_color = RGBColor(int(255 * intensity), int(69 * intensity), 0)
        end_color = RGBColor(int(255 * intensity), int(140 * intensity), 0)
        
        for i in range(10):
            red = int(start_color.red + (end_color.red - start_color.red) * (i / 10))
            green = int(start_color.green + (end_color.green - start_color.green) * (i / 10))
            blue = int(start_color.blue + (end_color.blue - start_color.blue) * (i / 10))
            keyboard.set_color(RGBColor(red, green, blue))
            time.sleep(transition_speed / 10)

        if random.random() < 0.1:
            keyboard.set_color(RGBColor(int(255 * intensity * random.uniform(0.3, 0.7)), 0, 0))  # Ember flicker
            time.sleep(random.uniform(0.1, 0.3))

try:
    flame_ember_effect()
except KeyboardInterrupt:
    print("Effect stopped.")
