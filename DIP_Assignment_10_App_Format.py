import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import sys

# Define a function that helps us in choosing options for the match case
def get_user_input():
  while True:
    Img_Options = int(input("Enter Option:- "))
    if Img_Options in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
      return Img_Options
    else:
      print("Invalid input. Please enter a number between 1 and 9.")

home_directory = os.path.expanduser("~") # Expand the user's home directory.
file_path = input("Enter the file's path:- \n") # Prompt the user for a file path.
full_file_path = os.path.join(home_directory, file_path) # Join the user's home directory with the file path.
print(f"The provided file path is:- {full_file_path} \n") # Print the full file path
image = cv2.imread(full_file_path)
print("Showing original Image:- \n")
cv2.imshow('Original Image', image)

#creating a switchcase statement(structural pattern matching) for image operations
print("To perform Morphological Operations on your Image, choose options:- ")
print("1:- Erosion")
print("2:- Dilation")
print("3:- Opening")
print("4:- Closing")
print("5:- Boundary Extraction")
print("6:- Hit and Miss Transform")
print("7:- Hole Filling")
print("8:- Skeleton")
print("9:- Exit programme \n")
Img_Options = get_user_input()
print(f"You entered {Img_Options}. \n")
match Img_Options:
  case 1:
    def erosion(image):
      kernel = np.ones((5, 5), np.uint8)
      result = cv2.erode(image, kernel, iterations=1)
      cv2.imshow('Erosion Result', result)
      cv2.waitKey(0)

    erosion(image) 

  case 2:
    def dilation(image):
      kernel = np.ones((5, 5), np.uint8)
      result = cv2.dilate(image, kernel, iterations=1)
      cv2.imshow('Dilation Result', result)
      cv2.waitKey(0)

    dilation(image)

  case 3:
    def opening(image):
      kernel = np.ones((5, 5), np.uint8)
      result = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
      cv2.imshow('Opening Result', result)
      cv2.waitKey(0)
      
    opening(image)

  case 4:
    def closing(image):
      kernel = np.ones((5, 5), np.uint8)
      result = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
      cv2.imshow('Closing Result', result)
      cv2.waitKey(0)
      
    closing(image)

  case 5:
    def boundary_extraction(image):
      kernel = np.ones((5, 5), np.uint8)
      erosion_result = cv2.erode(image, kernel, iterations=1)
      result = image - erosion_result
      cv2.imshow('Boundary Extraction Result', result)
      cv2.waitKey(0)
    
    boundary_extraction(image)

  case 6:
    def hit_and_miss_transform(image):
      original_image = cv2.imread(full_file_path, cv2.IMREAD_GRAYSCALE)
      kernel_hit_miss = np.array([[0, 1, 0],
                                  [1, -1, 1],
                                  [0, 1, 0]], dtype=np.int8)
      result = cv2.morphologyEx(original_image, cv2.MORPH_HITMISS, kernel_hit_miss)
      cv2.imshow('Hit and Miss Transform Result', result)
      cv2.waitKey(0)

      
    hit_and_miss_transform(image)

  case 7:
    def hole_filling(image):
      original_image = cv2.imread(full_file_path, cv2.IMREAD_GRAYSCALE)
      im_th = cv2.threshold(original_image, 128, 255, cv2.THRESH_BINARY)[1]
      hole_filled_result = im_th.copy()
      cv2.floodFill(hole_filled_result, None, (0, 0), 255)
      hole_filled_result = cv2.bitwise_not(hole_filled_result)
      hole_filled_result = cv2.bitwise_or(im_th, hole_filled_result)
      cv2.imshow('Hole Filling Result', hole_filled_result)
      cv2.waitKey(0)
      
    hole_filling(image)

  case 8:
    def skeletonization(image):
      original_image = cv2.imread(full_file_path, cv2.IMREAD_GRAYSCALE)
      result = cv2.ximgproc.thinning(original_image)
      cv2.imshow('Skeletonization Result', result)
      cv2.waitKey(0)
      
    skeletonization(image)


# C:\Users\kiran\Downloads\WP Slideshow\Witcher GOG WP.jpg