import pyautogui
from PIL import ImageGrab
import time
import keyboard  # Library to detect keypress for breaking the loop

def track_color():
    print("Press 'q' to quit.")  # Exit instruction
    while True:
        # Check for exit condition (press 'q' to stop)
        if keyboard.is_pressed("q"):
            break
        
        # Get the current mouse position
        x, y = pyautogui.position()

        # Capture the screen at the current position
        pixel_image = ImageGrab.grab(bbox=(x, y, x + 1, y + 1))
        
        # Get the RGB values of the pixel
        rgb = pixel_image.getpixel((0, 0))
        
        # Convert RGB to hexadecimal color code
        color_hash = "#{:02x}{:02x}{:02x}".format(*rgb)
        
        # Output the color at the pointer's current location
        print(f"Color at ({x}, {y}): {color_hash}")

        # Wait for a brief moment to reduce CPU usage
        time.sleep(0.1)  # Adjust as needed

# Run the function to track color as the mouse pointer moves
track_color()
