import numpy as np
import cv2
import os
import sys

# Define a function that helps us in choosing options for the match case
def get_user_input():
  while True:
    Img_Options = int(input("Enter Option:- "))
    if Img_Options in [1, 2 , 3, 4, 5]:
      return Img_Options
    else:
      print("Invalid input. Please enter a number between 1 and 5.")

def get_user_choice():
  while True:
    choice = int(input("Enter Choice:- "))
    if choice in [0,1]:
      return choice
    else:
      print("Invalid input. Please enter a number between 0 and 1.")

home_directory = os.path.expanduser("~") # Expand the user's home directory.
file_path = input("Enter the file's path:- \n") # Prompt the user for a file path.
full_file_path = os.path.join(home_directory, file_path) # Join the user's home directory with the file path.
print(f"The provided file path is:- {full_file_path} \n") # Print the full file path
image = cv2.imread(full_file_path)
print("Showing original Image:- \n")
cv2.imshow('Original Image', image)

#creating a switchcase statement(structural pattern matching) for image operations
print("To perform operations on your Image, choose options:- ")
print("1:- Negative Image")
print("2:- Flip Image(Horizontal and Vertical)")
print("3:- Thresholding")
print("4:- Contrast Stretching")
print("5:- Exit programme \n")
Img_Options = get_user_input()
print(f"You entered {Img_Options}.")
match Img_Options:
  case 1:
    print("Creating the negative Image...\n")
    # Create a negative image
    negative_image = cv2.merge([255 - channel for channel in cv2.split(image)])
    # Display the negative image
    print("The Negative Image is:-")
    cv2.imshow('Negative Image', negative_image)
    # Wait for a key press and close the windows
    cv2.waitKey(0)

  case 2:
    print("Which direction do you wish to flip the Image at (Horizontal or Vertical)?")
    print("Vertical(type '0') or Horizontal(type '1')...")
    choice = get_user_choice()
    if(choice == 0 ):
      print("Flipping the Image vertically...\n")
      # Flip the image vertically
      flipped_image_ver = cv2.flip(image, 0)
      # Display the flipped image
      print("Showing the Flipped Image:-")
      cv2.imshow('Vertically Flipped Image', flipped_image_ver)
      # Wait for a key press and close the windows
      cv2.waitKey(0)


    elif(choice == 1):
      print("Flipping the Image horizontally... ")
      # Flip the image horizontally 
      flipped_image_hor = cv2.flip(image, 1)
      # Display the flipped image
      print("Showing the Flipped Image:-")
      cv2.imshow('Horizontally Flipped Image', flipped_image_hor)
      # Wait for a key press and close the windows
      cv2.waitKey(0)

    else:
      pass

  case 3:
    threshold_value = int(input("Enter the Threshold value:- "))
    print("Applying Thresholding...")
    # Apply thresholding
    ret, thresh_img = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    # Display the thresholded image
    print("Showing the Thresholded Image:-")
    cv2.imshow('Thresholded Image', thresh_img)
    # Wait for a key press and close the windows
    cv2.waitKey(0)

  case 4:
    print("Performing Contrast Stretching...")
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Calculate the histogram of the grayscale image
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    # Calculate the cumulative distribution of the histogram
    cumulative_hist = np.cumsum(hist)
    # Calculate the minimum and maximum pixel values for the output image
    min_val = np.where(cumulative_hist >= 0.01 * gray.size)[0][0]
    max_val = np.where(cumulative_hist >= 0.99 * gray.size)[0][0]
    # Apply the contrast stretching to the grayscale image
    contrast_stretched = np.clip((gray - min_val) * (255.0 / (max_val - min_val)), 0, 255).astype(np.uint8)
    # Display the contrast stretched image
    print("Showing the Contrast Stretched Image:-")
    cv2.imshow('Contrast Stretched Image', contrast_stretched)
    # Wait for a key press and close the windows
    cv2.waitKey(0)

  case 5:
    print("Exiting the Programme...")
    cv2.waitKey(0)
    sys.exit()

  case _:
    pass

  




# C:\Users\kiran\Downloads\WP TW(copy DIP A-2).jpg