import pyautogui

def locate_and_click(image_path):
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=0.45)
        if location:
            print(f"[+] Found at {location}. Clicking.")
            pyautogui.moveTo(location)
            pyautogui.click()
        else:
            print("[-] Image not found.")
    except pyautogui.ImageNotFoundException:
        print("[-] Image not found (exception).")
