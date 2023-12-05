import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import sys

# Define a function that helps us in choosing options for the match case
def get_user_input():
  while True:
    Img_Options = int(input("Enter Option:- "))
    if Img_Options in [1, 2, 3]:
      return Img_Options
    else:
      print("Invalid input. Please enter a number between 1 and 3.")

def get_user_choice_1():
  while True:
    choice = int(input("Enter Choice:- "))
    if choice in [1,2]:
      return choice
    else:
      print("Invalid input. Please enter a number between 1 and 2.")

def get_user_choice_2():
  while True:
    choice = int(input("Enter Choice:- "))
    if choice in [1, 2, 3, 4]:
      return choice
    else:
      print("Invalid input. Please enter a number between 1 and 4.")


def prewitt_edge_detection(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply the Prewitt filter
    kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

    gradient_x = cv2.filter2D(gray_image, cv2.CV_64F, kernel_x)
    gradient_y = cv2.filter2D(gray_image, cv2.CV_64F, kernel_y)

    # Combine the x and y gradients
    gradient_magnitude = np.sqrt(np.square(gradient_x) + np.square(gradient_y))

    # Normalize the gradient values to the range [0, 255]
    gradient_normalized = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)

    # Convert the gradient to uint8 type
    gradient_uint8 = np.uint8(gradient_normalized)

    return gradient_uint8

def sobel_edge_detection(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply the Sobel filter
    gradient_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

    # Combine the x and y gradients
    gradient_magnitude = np.sqrt(np.square(gradient_x) + np.square(gradient_y))

    # Normalize the gradient values to the range [0, 255]
    gradient_normalized = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)

    # Convert the gradient to uint8 type
    gradient_uint8 = np.uint8(gradient_normalized)

    return gradient_uint8

def canny_edge_detection(image, low_threshold, high_threshold):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply the Canny filter
    edges = cv2.Canny(gray_image, low_threshold, high_threshold)

    return edges

def robert_cross_edge_detection(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Define the Robert Cross kernels
    kernel_x = np.array([[1, 0], [0, -1]])
    kernel_y = np.array([[0, 1], [-1, 0]])

    # Apply the kernels to compute the x and y gradients
    gradient_x = cv2.filter2D(gray_image, cv2.CV_64F, kernel_x)
    gradient_y = cv2.filter2D(gray_image, cv2.CV_64F, kernel_y)

    # Combine the x and y gradients
    gradient_magnitude = np.sqrt(np.square(gradient_x) + np.square(gradient_y))

    # Normalize the gradient values to the range [0, 255]
    gradient_normalized = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)

    # Convert the gradient to uint8 type
    gradient_uint8 = np.uint8(gradient_normalized)

    return gradient_uint8

home_directory = os.path.expanduser("~") # Expand the user's home directory.
file_path = input("Enter the file's path:- \n") # Prompt the user for a file path.
full_file_path = os.path.join(home_directory, file_path) # Join the user's home directory with the file path.
print(f"The provided file path is:- {full_file_path} \n") # Print the full file path
image = cv2.imread(full_file_path)
print("Showing original Image:- \n")
cv2.imshow('Original Image', image)

#creating a switchcase statement(structural pattern matching) for image operations
print("To perform operations on your Image, choose options:- ")
print("1:- Edge Detection using Filters")
print("2:- Detect Lines and Circles")
print("3:- Exit programme \n")
Img_Options = get_user_input()
print(f"You entered {Img_Options}. \n")
match Img_Options:
  case 1:
    print("Which Filter do you wish to use (Prewitt - type 1 or Sobel - type 2 or Canny - type 3 or Robert - type 4)?")
    choice = get_user_choice_2()
    if(choice == 1):
      # Perform Prewitt edge detection
      edge_detected_image = prewitt_edge_detection(image)
 
      # Display the original and edge-detected images
      cv2.imshow('Original Image', image)
      cv2.imshow('Edge Detected Image (Prewitt)', edge_detected_image)

      # Wait for a key press and then close the windows
      cv2.waitKey(0)

    elif(choice == 2):
      # Perform Sobel edge detection
      edge_detected_image = sobel_edge_detection(image)

      # Display the original and edge-detected images
      cv2.imshow('Original Image', image)
      cv2.imshow('Edge Detected Image (Sobel)', edge_detected_image)

      # Wait for a key press and then close the windows
      cv2.waitKey(0)
     
    elif(choice == 3):
      # Set the Canny edge detection thresholds (you can adjust these values)
      low_threshold = 50
      high_threshold = 150

      # Perform Canny edge detection
      edges_image = canny_edge_detection(image, low_threshold, high_threshold)

      # Display the original and edge-detected images
      cv2.imshow('Original Image', image)
      cv2.imshow('Edge Detected Image (Canny)', edges_image)

      # Wait for a key press and then close the windows
      cv2.waitKey(0)
    
    elif(choice == 4):
      # Perform Robert Cross edge detection
      edges_image = robert_cross_edge_detection(image)
      
      # Display the original and edge-detected images
      cv2.imshow('Original Image', image)
      cv2.imshow('Edge Detected Image (Robert Cross)', edges_image)
      
      # Wait for a key press and then close the windows
      cv2.waitKey(0)

    else:
      pass

  case 2:
    print("Detect Lines - type 1, Detect Circles - type 2")
    choice = get_user_choice_1()
    if(choice == 1):
      def detect_lines(image_path, output_path, rho, theta, threshold, min_line_length, max_line_gap):
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
        # Apply GaussianBlur to reduce noise and help in edge detection
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
     
        # Use Canny edge detector to find edges in the image
        edges = cv2.Canny(blurred, 50, 150)
    
        # Apply Hough Transform to detect lines
        lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                                minLineLength=min_line_length, maxLineGap=max_line_gap)
    
        # Draw the detected lines on the original image
        line_image = np.copy(image)
        draw_lines(line_image, lines)
    
        # Display the result
        cv2.imshow('Detected Lines', line_image)
        cv2.waitKey(0)

      def draw_lines(image, lines):
        # Draw lines on the given image
        for line in lines:
          x1, y1, x2, y2 = line[0]
          cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

      # Set the parameters for Hough Transform
      rho = 1              # distance resolution of the accumulator in pixels
      theta = np.pi/180    # angle resolution of the accumulator in radians
      threshold = 50       # minimum number of votes (intersections in Hough grid cell)
      min_line_length = 100 # minimum number of pixels making up a line
      max_line_gap = 10     # maximum gap in pixels between connectable line segments

      # Specify the paths for input and output images
      input_image_path = 'path_to_input_image.jpg'
      output_image_path = 'path_to_output_image_with_lines.jpg'

      # Detect and draw lines
      detect_lines(input_image_path, output_image_path, rho, theta, threshold, min_line_length, max_line_gap)

    elif(choice == 2):
      def detect_circles(image_path, output_path, dp, min_dist, param1, param2, min_radius, max_radius):
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
        # Apply GaussianBlur to reduce noise and help in circle detection
        blurred = cv2.GaussianBlur(gray, (9, 9), 2)
    
        # Use Hough Circle Transform to detect circles
        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp, minDist=min_dist,
                                   param1=param1, param2=param2,
                                   minRadius=min_radius, maxRadius=max_radius)
    
        # Ensure that some circles were found
        if circles is not None:
          circles = np.uint16(np.around(circles))
        
          # Draw the detected circles on the original image
          circle_image = np.copy(image)
          draw_circles(circle_image, circles)
        
          # Display the result
          cv2.imshow('Detected Circles', circle_image)
          cv2.waitKey(0)
          # Save the result
          cv2.imwrite(output_path, circle_image)
        else:
          print("No circles detected.")

      def draw_circles(image, circles):
        # Draw circles on the given image
        for circle in circles[0, :]:
          center = (circle[0], circle[1])
          radius = circle[2]
          cv2.circle(image, center, radius, (0, 255, 0), 2)

      # Set the parameters for Hough Circle Transform
      dp = 1       # inverse ratio of accumulator resolution to image resolution
      min_dist = 50 # minimum distance between the centers of detected circles
      param1 = 50   # higher threshold of the two passed to the Canny edge detector
      param2 = 30   # accumulator threshold for circle detection (lower means more false positives)
      min_radius = 10 # minimum radius of the detected circle
      max_radius = 100 # maximum radius of the detected circle

      # Specify the paths for input and output images
      input_image_path = 'path_to_input_image.jpg'
      output_image_path = 'path_to_output_image_with_circles.jpg'

      # Detect and draw circles
      detect_circles(input_image_path, output_image_path, dp, min_dist, param1, param2, min_radius, max_radius)

    else:
      pass

  case 3:
    print("Exiting the Programme...")
    cv2.waitKey(0)
    sys.exit()

  case _:
    pass

# C:\Users\kiran\Downloads\NB WP.jpg