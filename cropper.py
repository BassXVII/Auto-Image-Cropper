# Import Pillow library and Image class, and any other necessary libraries
import PIL
from PIL import Image                  

im1 = Image.open("C:\\Users\\sw-adbass\\Pictures\\Saved Pictures\\Ifunny.jpg")
print("The dimensions of the current image are: ", im1.size)
