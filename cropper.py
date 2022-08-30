# Import Pillow library and Image class, and any other necessary libraries

from cProfile import label
from cgi import test
from html import entities
from msilib import _directories
from operator import ge
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

root = tk.Tk()
root.title("Source Dir")
root.geometry("500x100")


source_Dir = tk.StringVar()
dest_Dir = tk.StringVar()

#Function that is getting and storing them as a variable
def submit():
      source = source_Dir.get()
      dest = dest_Dir.get()

      print("Source: " + source)
      print("Dest: " + dest)

      source_Dir.set("")
      dest_Dir.set("")
      
#Set an entry point and a label for source directory
source_label = tk.Label(root, text="Source Directory", font=('calibre', 10, 'bold'))
source_entry = tk.Entry(root,textvariable = source_Dir, font=('calibre',10,'normal'))

#Create an entry point and a label for destination folders
dest_label = tk.Label(root, text = 'Destination Directory', font = ('calibre',10,'bold'))
dest_entry=tk.Entry(root, textvariable = dest_Dir, font = ('calibre',10,'normal'))

#create a quit Button
exit = Button(root, text="Exit", command=root.destroy)

# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)

source_label.grid(row=0,column=0)
source_entry.grid(row=0,column=1)
dest_label.grid(row=1,column=0)
dest_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=0)
exit.grid(row=2, column=1)
  
# performing an infinite loop
# for the window to display

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
            




