# Import Pillow library and Image class, and any other necessary libraries
from sys import float_repr_style
import PIL
import io
from PIL import Image     
import os
from os import listdir

#Loop to loop through and crop every image in Pictures folder
#Get the path or directory
#custom_Path = input("Please specify the location for all of the images: ")

#Use below line if you want to manually enter in a set location. 
set_folder = "C:\\Users\\sw-adbass\\Pictures\\Saved Pictures\\memes\\"
new_location = "C:\\Users\\sw-adbass\\Desktop\\CroppedMemes2\\"
 
#User input for save folder locationC:\\Users\\sw-adbass\\Pictures\\Saved Pictures\\

count = 0
for images in os.listdir(set_folder):
	# check if the image ends with png or jpg or jpeg
	if (images.endswith(".png") or images.endswith(".jpg")\
		or images.endswith(".jpeg")):
                  count += 1

print(count)

for images in os.listdir(set_folder):

	# check if the image ends with png or jpg or jpeg
	if (images.endswith(".png") or images.endswith(".jpg")\
		or images.endswith(".jpeg")):
            

            #Needs to read in the entire string into the .open function
            Full_path = set_folder + images
            img1 = Image.open(Full_path)
                    
            #Sets width and height for manipulation later
            width, height = img1.size
 
            # Setting the points for cropped image
            left = 0
            upper = 0
            right = width
            # Currently, height - 25 seems to be about the size of the watermark. 
            lower = height-25

            #Crops image with dimensions set above.
            cropped_Image = img1.crop((left, upper, right, lower))
            
            #Shows for test purposes. Can comment this out
            #cropped_Image.show()

            #Saves the image in the original save path and overwrites the original. 
            
            cropped_Image.save( new_location + images)
            
            
            print("Files Left ", count)
            count -= 1
            

