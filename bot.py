import pyautogui
import keyboard
import time
from utils import locate_and_click

print("=== Game Bot ===")
print("Press 's' to start, 'q' to stop.")

image_path = 'screenshots/coin.png'  # Make sure the image name matches

running = False

while True:
    if keyboard.is_pressed('s'):
        print("Bot started! Looking for image...")
        running = True
        time.sleep(1)  # Debounce
    elif keyboard.is_pressed('q'):
        print("Bot stopped by user.")
        break

    if running:
        locate_and_click(image_path)
        time.sleep(0.5)  # Delay between clicks
