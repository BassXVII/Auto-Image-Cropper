# Import Pillow library and Image class, and any other necessary libraries
import PIL
import base64
import io
from PIL import Image     


im1 = Image.open("C:\\Users\\sw-adbass\\Pictures\\Saved Pictures\\Ifunny.jpg")
print("The dimensions of the current image are: ", im1.size)
im1.show()

#Sets width and height for manipulation later
width, height = im1.size
 
# Setting the points for cropped image
left = 0
top = height
right = width
bottom = 90


#Encode an image as base64 to be decoded later.
with open("C:\\Users\\sw-adbass\\Pictures\\Saved Pictures\\LSC_1327.JPG", "rb") as image:
    image_string = base64.b64encode(image.read())
image = io.BytesIO(base64.b64decode(image_string))
Image.open(image)