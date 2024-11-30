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

def ocean_waves_effect():
    while True:
        wave_speed = random.uniform(0.5, 1.5)
        smooth_transition = random.choice([True, False])

        blue_intensity = random.uniform(0.3, 1.0)
        color = RGBColor(0, int(255 * blue_intensity), int(255 * blue_intensity))
        
        if smooth_transition:
            for i in range(10):
                intensity = int(255 * blue_intensity * (i / 10))
                keyboard.set_color(RGBColor(0, intensity, intensity))
                time.sleep(wave_speed / 10)
        else:
            keyboard.set_color(color)

        time.sleep(wave_speed)

try:
    ocean_waves_effect()
except KeyboardInterrupt:
    print("Effect stopped.")
