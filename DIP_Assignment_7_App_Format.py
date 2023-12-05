import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import sys

# Define a function that helps us in choosing options for the match case
def get_user_input():
  while True:
    Img_Options = int(input("Enter Option:- "))
    if Img_Options in [1, 2 , 3, 4]:
      return Img_Options
    else:
      print("Invalid input. Please enter a number between 1 and 4.")

def get_user_choice():
  while True:
    choice = int(input("Enter Choice:- "))
    if choice in [1,2]:
      return choice
    else:
      print("Invalid input. Please enter a number between 1 and 2.")

home_directory = os.path.expanduser("~") # Expand the user's home directory.
file_path = input("Enter the file's path:- \n") # Prompt the user for a file path.
full_file_path = os.path.join(home_directory, file_path) # Join the user's home directory with the file path.
print(f"The provided file path is:- {full_file_path} \n") # Print the full file path
image = cv2.imread(full_file_path)
print("Showing original Image:- \n")
cv2.imshow('Original Image', image)

#creating a switchcase statement(structural pattern matching) for image operations
print("To perform operations on your Image, choose options:- ")
print("1:- Using a filter (mask) 3, 5 and 9 for low pass filter (Averaging filter (Standard Average Filter) or Order statistics nonlinear filters (Median))")
print("2:- Using a 3X3 filter (mask) high pass filter")
print("3:- Sharpening spatial filter (Laplasian + Original Image)")
print("4:- Exit programme \n")
Img_Options = get_user_input()
print(f"You entered {Img_Options}.")
match Img_Options:
  case 1:
    print("Which Filter do you wish to use (Standard Average - type 1 or Median filter - type 2 )?")
    choice = get_user_choice()
    if(choice == 1 ):
      # Removing noise using spatial filters
      
      # Averaging filter (Standard Average Filter)
      # Create the filter masks for 3x3, 5x5, and 9x9 averaging filters
      filter_3x3 = np.ones((3, 3), dtype=np.float32) / 9  # Normalized for 3x3 filter
      filter_5x5 = np.ones((5, 5), dtype=np.float32) / 25  # Normalized for 5x5 filter
      filter_9x9 = np.ones((9, 9), dtype=np.float32) / 81  # Normalized for 9x9 filter
      
      # Apply the filters to each color channel
      filtered_blue_3x3 = cv2.filter2D(image[:, :, 0], -1, filter_3x3)
      filtered_green_3x3 = cv2.filter2D(image[:, :, 1], -1, filter_3x3)
      filtered_red_3x3 = cv2.filter2D(image[:, :, 2], -1, filter_3x3)
      
      filtered_blue_5x5 = cv2.filter2D(image[:, :, 0], -1, filter_5x5)
      filtered_green_5x5 = cv2.filter2D(image[:, :, 1], -1, filter_5x5)
      filtered_red_5x5 = cv2.filter2D(image[:, :, 2], -1, filter_5x5)
      
      filtered_blue_9x9 = cv2.filter2D(image[:, :, 0], -1, filter_9x9)
      filtered_green_9x9 = cv2.filter2D(image[:, :, 1], -1, filter_9x9)
      filtered_red_9x9 = cv2.filter2D(image[:, :, 2], -1, filter_9x9)
      
      # Combine the filtered channels to get the filtered color image
      filtered_image_3x3 = cv2.merge([filtered_blue_3x3, filtered_green_3x3, filtered_red_3x3])
      filtered_image_5x5 = cv2.merge([filtered_blue_5x5, filtered_green_5x5, filtered_red_5x5])
      filtered_image_9x9 = cv2.merge([filtered_blue_9x9, filtered_green_9x9, filtered_red_9x9])
      
      # Display the original and filtered images
      plt.figure(figsize=(12, 12))

      plt.subplot(3, 2, 1)
      plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
      plt.title('Original Image')
      
      plt.subplot(3, 2, 2)
      plt.imshow(cv2.cvtColor(filtered_image_3x3, cv2.COLOR_BGR2RGB))
      plt.title('3x3 Averaging Filter')
      
      plt.subplot(3, 2, 3)
      plt.imshow(cv2.cvtColor(filtered_image_5x5, cv2.COLOR_BGR2RGB))
      plt.title('5x5 Averaging Filter')
      
      plt.subplot(3, 2, 4)
      plt.imshow(cv2.cvtColor(filtered_image_9x9, cv2.COLOR_BGR2RGB))
      plt.title('9x9 Averaging Filter')
      
      plt.tight_layout()
      print("Filter masks are applied...")
      print("Showing Images...")
      plt.show()
      cv2.waitKey(0)
      
    elif(choice == 2):
      # Make use of filter (mask) 3, 5 and 9 for low pass filter
      # Order statistics nonlinear filters (Median)
      # Apply median filters with different kernel sizes
      filtered_image_3x3 = cv2.medianBlur(image, 3)
      filtered_image_5x5 = cv2.medianBlur(image, 5)
      filtered_image_9x9 = cv2.medianBlur(image, 9)
      
      # Display the original and filtered images
      plt.figure(figsize=(12, 12))
      
      plt.subplot(3, 2, 1)
      plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
      plt.title('Original Image')
      
      plt.subplot(3, 2, 2)
      plt.imshow(cv2.cvtColor(filtered_image_3x3, cv2.COLOR_BGR2RGB))
      plt.title('3x3 Median Filter')
      
      plt.subplot(3, 2, 3)
      plt.imshow(cv2.cvtColor(filtered_image_5x5, cv2.COLOR_BGR2RGB))
      plt.title('5x5 Median Filter')
      
      plt.subplot(3, 2, 4)
      plt.imshow(cv2.cvtColor(filtered_image_9x9, cv2.COLOR_BGR2RGB))
      plt.title('9x9 Median Filter')
      
      plt.tight_layout()
      print("Filter masks are applied...")
      print("Showing Images...")
      plt.show()
      cv2.waitKey(0)

    else:
      pass

  case 2:
    # Make use of 3X3 filter (mask) high pass filter
    # Create a 3x3 high-pass filter
    high_pass_filter_3x3 = np.array([[-1, -1, -1],
                                     [-1, 8, -1],
                                     [-1, -1, -1]])
    
    # Apply the high-pass filter to the image
    filtered_image = cv2.filter2D(image, -1, high_pass_filter_3x3)
    
    # Display the original and high-pass filtered images
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB))
    plt.title('3x3 High-Pass Filter')
    
    plt.tight_layout()
    print("Filter masks are applied...")
    print("Showing Images...")
    plt.show()
    cv2.waitKey(0)

  case 3:
    # Sharpening spatial filter (Laplasian + Original Image)
    # Apply Laplacian filter to the image
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    
    # Convert the Laplacian result back to the appropriate data type
    laplacian = np.uint8(np.abs(laplacian))
    
    # Perform image sharpening by adding the Laplacian result to the original image
    sharpened_image = cv2.addWeighted(image, 1.5, laplacian, -0.5, 0)
    
    # Display the original and sharpened images
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB))
    plt.title('Sharpened Image')
    
    plt.tight_layout()
    print("Filter masks are applied...")
    print("Showing the sharpened Image:- ")
    plt.show()
    cv2.waitKey(0)

  case 4:
    print("Exiting the Programme...")
    cv2.waitKey(0)
    sys.exit()

  case _:
    pass

    




# C:\Users\kiran\Downloads\NB WP.jpg