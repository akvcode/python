import keyboard
import pyautogui

def block_f2(event):
    if event.name == 'f2':
        print("F2 key pressed, blocking...")
        pyautogui.press('esc')  # Simulate pressing the 'esc' key to block F2
        return False  # Return False to block the key event

keyboard.hook(block_f2)

# Keep the script running
keyboard.wait('esc')  # Wait for the 'esc' key to be pressed to exit
