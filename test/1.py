from PIL import ImageGrab
import time

# Optional: Add a delay so you can switch to the desired screen/window
time.sleep(2) 

# Take the screenshot
screenshot = ImageGrab.grab(xdisplay=':1')

# Display the screenshot (optional)
# screenshot.show()

# Save the screenshot to a file
file=time.strftime("%Y-%m-%d %H:%M:%S") + ".png"
screenshot.save(file)
