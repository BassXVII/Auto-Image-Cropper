# Import Pillow library and Image class, and any other necessary libraries
import PIL
import base64
import io
from PIL import Image     

# import the modules
import os
from os import listdir

#Loop to loop through and crop every image in Pictures folder
#Get the path or directory
folder_dir = "C:\\Users\\sw-adbass\\Pictures\\Saved Pictures\\"
for images in os.listdir(folder_dir):

	# check if the image ends with png or jpg or jpeg
	if (images.endswith(".png") or images.endswith(".jpg")\
		or images.endswith(".jpeg")):
            

            #Needs to read in the entire string into the .open function
            Full_path = folder_dir + images
            img1 = Image.open(Full_path)
                    
            #Sets width and height for manipulation later
            width, height = img1.size
 
            # Setting the points for cropped image
            left = 0
            upper = 0
            right = width
            # Currently, height - 25 seems to be about the size of the watermark. 
            lower = height-25

            cropped_Image = img1.crop((left, upper, right, lower))
            cropped_Image.show()

            cropped_Image.save(folder_dir + images)

