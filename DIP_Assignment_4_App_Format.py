import numpy as np
import cv2
import os
import sys

# Define a function that helps us in choosing options for the match case
def get_user_input():
  while True:
    Img_Options = int(input("Enter Option:- "))
    if Img_Options in [1, 2 , 3, 4, 5, 6]:
      return Img_Options
    else:
      print("Invalid input. Please enter a number between 1 and 6.")

home_directory = os.path.expanduser("~") # Expand the user's home directory.
file_path = input("Enter the file's path:- \n") # Prompt the user for a file path.
full_file_path = os.path.join(home_directory, file_path) # Join the user's home directory with the file path.
print(f"The provided file path is:- {full_file_path} \n") # Print the full file path

image = cv2.imread(full_file_path)
print("Showing original images:- \n")
cv2.imshow('Original Image', image)

#creating a switchcase statement(structural pattern matching) for image operations
print("To perform operations on your Image, choose options:- ")
print("1:- Translation Operation")
print("2:- Scaling Operation")
print("3:- Rotation Operation")
print("4:- Shrinking Operation")
print("5:- Zooming Operation")
print("6:- Exit programme \n")
Img_Options = get_user_input()
print(f"You entered {Img_Options}. \n")
match Img_Options:
  case 1:
    # Define the height and width
    height, width= input("Enter the dimensions of Height and Width:- \n").split()
    # Define the translation matrix
    M = np.float32([[1, 0, width], [0, 1, height]])
    # Apply the translation matrix to the image
    translated_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    # Display the translated image
    print("The generated Translated Image:- \n")
    cv2.imshow('Translated Image', translated_image)
    cv2.waitKey(0)

  case 2:
    # Define the scale factor. For example, 0.5 means the image size will be halved.
    scale_factor = int(input("Specify the Scale Factor to apply on the Image:- \n"))
    # Scale the image by a factor of 2 using cubic interpolation
    scaled_image = cv2.resize(image, (0, 0), fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)
    # Display the scaled image
    print(f"The genrated Image with Scale Factor {scale_factor} is:- \n")
    cv2.imshow('Scaled Image', scaled_image)
    cv2.waitKey(0)
    

  case 3:
    # Define the angle
    angle = int(input("Specify the Angle of Rotation of the Image:- \n"))
    M = cv2.getRotationMatrix2D((image.shape[1]/2, image.shape[0]/2), angle, 1)
    # Apply the rotation matrix to the image
    rotated_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    # Display the rotated image
    print(f"The genrated Image with Angle {angle} is:- \n")
    cv2.imshow('Rotated Image', rotated_image)
    cv2.waitKey(0)

  case 4:
    # Define the resize factor. For example, 0.5 means the image size will be halved.
    resize_factor = float(input("Specify the Resize Factor for the Image:- \n"))
    # Resize the image
    resized_image = cv2.resize(image, (0, 0), fx=resize_factor, fy=resize_factor, interpolation=cv2.INTER_AREA)
    # Display the resized image
    print(f"The generated Image with Resize Factor {resize_factor} is:- ")
    cv2.imshow('Resized Image', resized_image)
    cv2.waitKey(0)

  case 5:
    # Define the zoom factor. For example, 2.0 means the image size will be doubled.
    zoom_factor = float(input("Specify the Zoom Factor for the Image:- \n"))
    # Get the image size
    height, width = image.shape[:2]
    # Calculate the target size
    target_size = (int(width * zoom_factor), int(height * zoom_factor))
    # Resize the image
    zoomed_image = cv2.resize(image, target_size, interpolation = cv2.INTER_LINEAR)
    # Display the zoomed image
    print(f"The generated Image with Zoom Factor {zoom_factor}:- \n")
    cv2.imshow('Zoomed Image', zoomed_image)
    cv2.waitKey(0)

  case 6:
    #Exit Programme
    print("Exiting the Programme...")
    cv2.waitKey(0)
    sys.exit()
        
  case _ :
      pass



# C:\Users\kiran\Downloads\DIP A-3 pic 1.png
# C:\Users\kiran\Downloads\DIP A-3 pic 2.png