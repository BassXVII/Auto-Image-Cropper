# Import Pillow library and Image class, and any other necessary libraries

from cgi import test
from html import entities
from msilib import _directories
from sys import float_repr_style
import PIL
import io
from PIL import Image     
import os
from os import listdir
#Create a popup window for user input
import tkinter as tk
from tkinter import *


#Loop to loop through and crop every image in Pictures folder
#Get the path or directory


#ROOT = tk.Tk()

#ROOT.withdraw()
# the input dialog
#USER_INP = simpledialog.askstring(title="Source",
#                                 prompt="Enter in folder source:")
# check it out
#print("Hello", USER_INP)

root = Tk()
root.title("Source Dir")
root.geometry("200x200")

#List to store values
directories = []

#Definition for command
def submit():
      entry_list = ''
      for entries in directories:
            entry_list = entry_list + entries.ge + '\n'
            my_label.config(text= entries + '\n')



#Loop for multiple inputs
for x in range(2):
      my_entry = Entry(root)
      my_entry.grid(row=0, column=2, pady=20, padx=50)
      directories.append(my_entry)

#Get labels and commands
my_button = Button(root, text="Enter", command=submit)
my_button.grid(row=1, column=0, pady=20)


my_label = Label(root, text="hello")
my_label.grid(row=2, column=0, pady=10)
root.mainloop()
#folder_dir = USER_INP
#Folder_Dest = "C:\\Users\\bassd\\OneDrive\\Pictures\\Saved Pictures\\Cropped"

#count = 0
#for images in os.listdir(folder_dir):
	# check if the image ends with png or jpg or jpeg
#	if (images.endswith(".png") or images.endswith(".jpg")\
#		or images.endswith(".jpeg")):
 #             count += 1 
#


#for images in os.listdir(folder_dir):
#
	# check if the image ends with png or jpg or jpeg
#	if (images.endswith(".png") or images.endswith(".jpg")\
#		or images.endswith(".jpeg")):
#            
#            #Needs to read in the entire string into the .open function
##            Full_path = folder_dir + images
#           img1 = Image.open(Full_path)
#                    
#            #Sets width and height for manipulation later
#            width, height = img1.size
# 
            # Setting the points for cropped image
#            left = 0
#            upper = 0
#            right = width
#            # Currently, height - 25 seems to be about the size of the watermark. 
#            lower = height-25
#
            #Crops image with dimensions set above.
 #           cropped_Image = img1.crop((left, upper, right, lower))
            
            #Shows for test purposes. Can comment this out
            #cropped_Image.show()

            #Saves the image in the original save path and overwrites the original.
#            cropped_Image.save(Folder_Dest + images)
#
#           print("Files Left ", count)
#            count -= 1
            




