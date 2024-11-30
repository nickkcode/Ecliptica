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

def heartbeat_effect(keyboard, base_color, glow_intensity=0.2):   
    strong_pulse_duration = random.uniform(0.18, 0.25)  # Random strong pulse duration
    light_pulse_duration = random.uniform(0.12, 0.18)  # Random light pulse duration
    pause_duration = random.uniform(0.7, 1.2)          # Random pause (rest phase)
    
    strong_intensity = random.uniform(0.8, 1.0)  # Strong pulse intensity (80% to 100%)
    light_intensity = random.uniform(0.6, 0.8)   # Light pulse intensity (60% to 80%)

    glow_color = RGBColor(
        int(base_color.red * glow_intensity),
        int(base_color.green * glow_intensity),
        int(base_color.blue * glow_intensity)
    )

    strong_color = RGBColor(
        int(base_color.red * strong_intensity),
        int(base_color.green * strong_intensity),
        int(base_color.blue * strong_intensity)
    )
    keyboard.set_color(strong_color)
    time.sleep(strong_pulse_duration)
    keyboard.set_color(glow_color)  # Return to soft glow
    time.sleep(0.1)  # Slight gap between pulses

    light_color = RGBColor(
        int(base_color.red * light_intensity),
        int(base_color.green * light_intensity),
        int(base_color.blue * light_intensity)
    )
    keyboard.set_color(light_color)
    time.sleep(light_pulse_duration)
    keyboard.set_color(glow_color)  # Return to soft glow

    time.sleep(pause_duration)

try:
    base_color = RGBColor(255, 0, 0)  # Red for the heartbeat
    while True:
        heartbeat_effect(keyboard, base_color)
except KeyboardInterrupt:
    print("Stopped by user.")
except Exception as e:
    print(f"An error occurred: {e}")
