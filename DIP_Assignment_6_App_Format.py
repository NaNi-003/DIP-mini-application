import numpy as np
import matplotlib.pyplot as plt
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
print("1:- Histogram of an Image (Color or Gray) and represent in line plot/bar graph")
print("2:- Histogram calculation of an Image (Color or Gray) with mask and without mask")
print("3:- Low and High contrast of an Image and representing the pixel spreading graph")
print("4:- Dark and Bright contrast of an Image and representing the pixel spreading graph")
print("5:- Exit programme \n")
Img_Options = get_user_input()
print(f"You entered {Img_Options}.")
match Img_Options:
  case 1:
    print("Which Image do you wish to find an Histogram for (Color or Gray)?")
    print("Color(type '1') or Gray(type '2')...")
    choice = get_user_choice()
    if(choice == 1 ):
     # Find histogram of a color image and represent in line plot/bar graph
     # Split the image into its color channels (BGR)
     if image is not None:
        blue_channel, green_channel, red_channel = cv2.split(image)
     else:
        print("Error: Failed to load image.")

     # Calculate histograms for each channel
     hist_blue = cv2.calcHist([blue_channel], [0], None, [256], [0, 256])
     hist_green = cv2.calcHist([green_channel], [0], None, [256], [0, 256])
     hist_red = cv2.calcHist([red_channel], [0], None, [256], [0, 256])

     # Plot histograms as line plots
     plt.figure(figsize=(12, 6))

     plt.subplot(3, 2, 1)
     plt.plot(hist_blue, color='b')
     plt.title('Blue Channel Histogram')
     plt.xlim([0, 256])

     plt.subplot(3, 2, 2)
     plt.imshow(cv2.cvtColor(blue_channel, cv2.COLOR_BGR2RGB))
     plt.title('Blue Channel Image')
     plt.subplot(3, 2, 3)

     plt.plot(hist_green, color='g')
     plt.title('Green Channel Histogram')
     plt.xlim([0, 256])

     plt.subplot(3, 2, 4)
     plt.imshow(cv2.cvtColor(green_channel, cv2.COLOR_BGR2RGB))
     plt.title('Green Channel Image')
 
     plt.subplot(3, 2, 5)
     plt.plot(hist_red, color='r')
     plt.title('Red Channel Histogram')
     plt.xlim([0, 256])

     plt.subplot(3, 2, 6)
     plt.imshow(cv2.cvtColor(red_channel, cv2.COLOR_BGR2RGB))
     plt.title('Red Channel Image')

     plt.tight_layout()
     plt.show()

    elif(choice == 2):
      # Read the grayscale image
      gray_img = cv2.imread(full_file_path, cv2.IMREAD_GRAYSCALE)

      # Calculate the histogram with 100 bins
      hist = cv2.calcHist([gray_img], [0], None, [100], [0, 256])

      # Flatten the histogram to a 1D array for plotting
      hist = hist.flatten()

      # Plot the histogram as a bar graph
      plt.figure(figsize=(12, 6))
      plt.subplot(1, 2, 1)
      plt.bar(range(100), hist, width=1.0, color='gray')
      plt.title('Grayscale Image Histogram')
      plt.xlabel('Pixel Value')
      plt.ylabel('Frequency')
      plt.xlim([0, 100])
      plt.subplot(1, 2, 2)
      plt.imshow(gray_img, cmap='gray')
      plt.title('Grayscale Image')

      plt.tight_layout()
      plt.show()

    else:
      pass

  case 2:
   # Split the image into its color channels (BGR)
   blue_channel, green_channel, red_channel = cv2.split(image)

   # Create a mask (for example, a rectangular region of interest)
   mask = np.zeros_like(blue_channel)
   mask[100:300, 200:400] = 255  # Example: Apply the mask to a specific region

   # Calculate histograms for each channel with the mask
   hist_blue_with_mask = cv2.calcHist([blue_channel], [0], mask, [256], [0, 256])
   hist_green_with_mask = cv2.calcHist([green_channel], [0], mask, [256], [0, 256])
   hist_red_with_mask = cv2.calcHist([red_channel], [0], mask, [256], [0, 256])

   # Calculate histograms for each channel without the mask
   hist_blue_without_mask = cv2.calcHist([blue_channel], [0], None, [256], [0, 256])
   hist_green_without_mask = cv2.calcHist([green_channel], [0], None, [256], [0, 256])
   hist_red_without_mask = cv2.calcHist([red_channel], [0], None, [256], [0, 256])

   # Plot histograms as line plots
   plt.figure(figsize=(12, 12))

   # Histograms with mask
   plt.subplot(3, 2, 1)
   plt.plot(hist_blue_with_mask, color='b')
   plt.title('Blue Channel Histogram with Mask')
   plt.xlim([0, 25])
 
   plt.subplot(3, 2, 2)
   plt.imshow(cv2.cvtColor(blue_channel, cv2.COLOR_BGR2RGB))
   plt.title('Blue Channel Image')

   plt.subplot(3, 2, 3)
   plt.plot(hist_green_with_mask, color='g')
   plt.title('Green Channel Histogram with Mask')
   plt.xlim([0, 256])

   plt.subplot(3, 2, 4)
   plt.imshow(cv2.cvtColor(green_channel, cv2.COLOR_BGR2RGB))
   plt.title('Green Channel Image')

   plt.subplot(3, 2, 5)
   plt.plot(hist_red_with_mask, color='r')
   plt.title('Red Channel Histogram with Mask')
   plt.xlim([0, 256])

   plt.subplot(3, 2, 6)
   plt.imshow(cv2.cvtColor(red_channel, cv2.COLOR_BGR2RGB))
   plt.title('Red Channel Image')

   # Display images without the mask
   plt.figure(figsize=(12, 6))

   plt.subplot(3, 2, 1)
   plt.plot(hist_blue_without_mask, color='b')
   plt.title('Blue Channel Histogram without Mask')
   plt.xlim([0, 256])

   plt.subplot(3, 2, 3)
   plt.plot(hist_green_without_mask, color='g')
   plt.title('Green Channel Histogram without Mask')
   plt.xlim([0, 256])
 
   plt.subplot(3, 2, 5)
   plt.plot(hist_red_without_mask, color='r')
   plt.title('Red Channel Histogram without Mask')
   plt.xlim([0, 256]) 

   plt.subplot(3, 2, 2)
   plt.imshow(cv2.cvtColor(blue_channel, cv2.COLOR_BGR2RGB))
   plt.title('Blue Channel Image (Without Mask)') 

   plt.subplot(3, 2, 4)
   plt.imshow(cv2.cvtColor(green_channel, cv2.COLOR_BGR2RGB))
   plt.title('Green Channel Image (Without Mask)')

   plt.subplot(3, 2, 6)
   plt.imshow(cv2.cvtColor(red_channel, cv2.COLOR_BGR2RGB))
   plt.title('Red Channel Image (Without Mask)')

   plt.tight_layout()
   plt.show()

  case 3:
    print("Low Contrast(type '1') or High Contrast(type '2')...")
    choice = get_user_choice()
    if(choice == 1 ):
     # Low contrast image and represent the pixel spreading graph
     # Read the grayscale image
     gray_img = cv2.imread(full_file_path, cv2.IMREAD_GRAYSCALE)

     # Apply histogram equalization
     equ = cv2.equalizeHist(gray_img)

     # Calculate histograms for the original and equalized images
     hist_original = cv2.calcHist([gray_img], [0], None, [256], [0, 256])
     hist_equalized = cv2.calcHist([equ], [0], None, [256], [0, 256])

     # Calculate pixel spreading graph
     cdf_original = hist_original.cumsum()
     cdf_equalized = hist_equalized.cumsum()

     # Plot histograms and pixel spreading graphs
     plt.figure(figsize=(12, 8))

     # Original Image and Histogram
     plt.subplot(2, 3, 1)
     plt.imshow(gray_img, cmap='gray')
     plt.title('Original Image') 

     plt.subplot(2, 3, 4)
     plt.plot(hist_original, color='b')
     plt.title('Original Histogram') 

     # Equalized Image and Histogram
     plt.subplot(2, 3, 2)
     plt.imshow(equ, cmap='gray')
     plt.title('Equalized Image')
 
     plt.subplot(2, 3, 5)
     plt.plot(hist_equalized, color='b')
     plt.title('Equalized Histogram')
   
     # Pixel Spreading Graph
     plt.subplot(2, 3, 3)
     plt.plot(cdf_original, color='b', label='Original')
     plt.plot(cdf_equalized, color='r', label='Equalized')
     plt.title('Pixel Spreading Graph')
     plt.legend()
 
     plt.tight_layout()
     plt.show()

    elif(choice == 2):
     # High contrast image and represent the pixel spreading graph
     # Read the grayscale image
     gray_img = cv2.imread(full_file_path, cv2.IMREAD_GRAYSCALE)

     # Apply contrast stretching for higher contrast
     min_val = 50  # Adjust these values to control the contrast
     max_val = 200
     high_contrast_img = cv2.convertScaleAbs(gray_img, alpha=(255.0 / (max_val - min_val)), beta=(-min_val * 255.0 / (max_val - min_val)))

     # Calculate histograms for the original and high-contrast images
     hist_original = cv2.calcHist([gray_img], [0], None, [256], [0, 256])
     hist_high_contrast = cv2.calcHist([high_contrast_img], [0], None, [256], [0, 256]) 
 
     # Calculate pixel spreading graph 
     cdf_original = hist_original.cumsum()
     cdf_high_contrast = hist_high_contrast.cumsum()
 
     # Plot histograms and pixel spreading graphs
     plt.figure(figsize=(12, 8))
 
     # Original Image and Histogram
     plt.subplot(2, 3, 1)
     plt.imshow(gray_img, cmap='gray')
     plt.title('Original Image')

     plt.subplot(2, 3, 4)
     plt.plot(hist_original, color='b')
     plt.title('Original Histogram')

     # High-Contrast Image and Histogram
     plt.subplot(2, 3, 2)
     plt.imshow(high_contrast_img, cmap='gray')
     plt.title('High-Contrast Image')

     plt.subplot(2, 3, 5)
     plt.plot(hist_high_contrast, color='b')
     plt.title('High-Contrast Histogram')
 
     # Pixel Spreading Graph
     plt.subplot(2, 3, 3)
     plt.plot(cdf_original, color='b', label='Original')
     plt.plot(cdf_high_contrast, color='r', label='High-Contrast')
     plt.title('Pixel Spreading Graph')
     plt.legend()
 
     plt.tight_layout()
     plt.show()

    else:
      pass

  case 4:
    print("Dark Contrast(type '1') or Bright Contrast(type '2')...")
    choice = get_user_choice()
    if(choice == 1 ):
      # Dark image and represent the pixel spreading graph
      # Read the image
      # Convert the image to grayscale
      gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

      # Darken the image
      dark_factor = 0.5  # Adjust this value to control the darkness (0.0 to 1.0)
      dark_img = (gray_img * dark_factor).astype(np.uint8)

      # Calculate histograms for the original and darkened images
      hist_original = cv2.calcHist([gray_img], [0], None, [256], [0, 256])
      hist_dark = cv2.calcHist([dark_img], [0], None, [256], [0, 256])

      # Calculate pixel spreading graph
      cdf_original = hist_original.cumsum()
      cdf_dark = hist_dark.cumsum()

      # Plot histograms and pixel spreading graphs
      plt.figure(figsize=(12, 8))

      # Original Image and Histogram
      plt.subplot(2, 3, 1)
      plt.imshow(gray_img, cmap='gray')
      plt.title('Original Image')

      plt.subplot(2, 3, 4)
      plt.plot(hist_original, color='b')
      plt.title('Original Histogram')

      # Darkened Image and Histogram
      plt.subplot(2, 3, 2)
      plt.imshow(dark_img, cmap='gray')
      plt.title('Darkened Image')

      plt.subplot(2, 3, 5)
      plt.plot(hist_dark, color='b')
      plt.title('Darkened Histogram')

      # Pixel Spreading Graph
      plt.subplot(2, 3, 3)
      plt.plot(cdf_original, color='b', label='Original')
      plt.plot(cdf_dark, color='r', label='Darkened')
      plt.title('Pixel Spreading Graph')
      plt.legend()

      plt.tight_layout()
      plt.show()

    elif( choice == 2):
      # Bright image and represent the pixel spreading graph
      # Convert the image to grayscale
      gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

      # Brighten the image
      bright_factor = 2.0  # Adjust this value to control the brightness (1.0 and higher)
      bright_img = (gray_img * bright_factor).astype(np.uint8)

      # Clip pixel values to ensure they are within the valid range
      bright_img = np.clip(bright_img, 0, 255)

      # Calculate histograms for the original and brightened images
      hist_original = cv2.calcHist([gray_img], [0], None, [256], [0, 256])
      hist_bright = cv2.calcHist([bright_img], [0], None, [256], [0, 256])

      # Calculate pixel spreading graph
      cdf_original = hist_original.cumsum()
      cdf_bright = hist_bright.cumsum()

      # Plot histograms and pixel spreading graphs
      plt.figure(figsize=(12, 8))

      # Original Image and Histogram
      plt.subplot(2, 3, 1)
      plt.imshow(gray_img, cmap='gray')
      plt.title('Original Image')

      plt.subplot(2, 3, 4)
      plt.plot(hist_original, color='b')
      plt.title('Original Histogram')

      # Brightened Image and Histogram
      plt.subplot(2, 3, 2)
      plt.imshow(bright_img, cmap='gray')
      plt.title('Brightened Image')

      plt.subplot(2, 3, 5)
      plt.plot(hist_bright, color='b')
      plt.title('Brightened Histogram')

      # Pixel Spreading Graph
      plt.subplot(2, 3, 3)
      plt.plot(cdf_original, color='b', label='Original')
      plt.plot(cdf_bright, color='r', label='Brightened')
      plt.title('Pixel Spreading Graph')
      plt.legend()

      plt.tight_layout()
      plt.show()

    else:
      pass

  case 5:
    print("Exiting the Programme...")
    cv2.waitKey(0)
    sys.exit()

  case _:
    pass    

# C:\Users\kiran\Downloads\WP TW(copy DIP A-2).jpg