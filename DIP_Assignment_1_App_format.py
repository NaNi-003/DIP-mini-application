import cv2
import sys
import numpy as np
import os
import matplotlib.pyplot as plt

home_directory = os.path.expanduser("~") # Expand the user's home directory.
file_path = input("Enter a file path:- ") # Prompt the user for a file path. (C:\Users\kiran\Downloads\NB WP.jpg is used for the assignment)
full_file_path = os.path.join(home_directory, file_path) # Join the user's home directory with the file path.
print("")
print("The provided file path is:-")
print("")
print(full_file_path) # Print the full file path.
print("")

img = cv2.imread(file_path)
cv2.imshow('Original Image', img)
#reading and displaying the original image from local directory

#creating a switchcase statement(structural pattern matching) for image resizing
print("To resize your images, choose options:- ")
print("1:- Resize using Scale Factor")
print("2:- Resize using Pixels")
print("3:- Resize using Height and Width Ratio")
print("4:- Skip the current function and move to the next function")
print("")

resize_options = int(input("Enter your option:- "))
print("")
match resize_options:
    case 1: 
        print("Scaling Factors")
        print("Loading......")
        resized_image = cv2.resize(img, (0,0), fx=1, fy=0.5) #fx and fy are scaling factors for width & height respectively
        print("Scaling Factor resizing applied")
        cv2.imshow('image', resized_image)
        print("")
    case 2:
        print("Pixels")
        print("Loading......")
        resized_image = cv2.resize(img, (100,50)) #Reszing images using pixels
        print("Pixel resizing applied")
        cv2.imshow('image', resized_image)
        print("")

    case 3:
        print("Height and Width Ratio being applied")
        print("Loading......")
        height, width = img.shape[:2] # get the original height and width
        ratio = 1000 / width # calculate the ratio for resizing
        resized_image = cv2.resize(img, (3000, int(height * ratio))) # resize the image
        print("Ratios applied")
        cv2.imshow('image', resized_image)
        print("")
    
    case 4:
        print("Skipping.....")
        print("")

    case _:
        print('Invalid input!')
        print("")
        sys.exit()

#creating a switchcase statement(structural pattern matching) for image coloring
print("To color your images, choose options:- ")
print("1:- Grayscale")
print("2:- Grayscale and then to Black & White")
print("3:- Red color")
print("4:- Skip the current function and move to the next function")
print("")

colorize_option=int(input("Choose an option:-"))
print("")
match colorize_option:
    case 1:
        print(resize_options)
        if((resize_options == 1) or (resize_options == 2) or (resize_options == 3)):
            grayscaledimage = cv2.cvtColor(resized_image ,cv2.COLOR_BGR2GRAY)
        else:
            grayscaledimage = cv2.cvtColor(img,(cv2.COLOR_BGR2GRAY)) #Grayscaling the image
        print("Loading......")
        print("Grayscaling done!")
        cv2.imshow('image',grayscaledimage)
    
    case 2:
        if((resize_options == 1) or (resize_options == 2) or (resize_options == 3)):
            grayscaledimage = cv2.cvtColor(resized_image,(cv2.COLOR_BGR2GRAY))
            threshold = cv2.threshold(grayscaledimage, 128, 255, cv2.THRESH_BINARY)[1] #Apply a threshold to the grayscale image to make the image B&W
        else:
            grayscaledimage = cv2.cvtColor(img,(cv2.COLOR_BGR2GRAY))
            threshold = cv2.threshold(grayscaledimage, 128, 255, cv2.THRESH_BINARY)[1]
        print("Loading......")
        print("B&W done!")
        cv2.imshow('image',threshold)

    case 3:
        if((resize_options == 1) or (resize_options == 2) or (resize_options == 3)):
            hsv = cv2.cvtColor(resized_image, cv2.COLOR_BGR2HSV) # Convert the image to HSV color space
            hue = hsv[:, :, 0] # Extract the hue channel
            hue[:] = 0 # Set the hue channel to 0 (red)
            bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # Convert the HSV image back to the BGR color space
            print("Loading......")
            print("Red color done!")
            cv2.imshow('image',bgr)
        else:
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            hue = hsv[:, :, 0]
            hue[:] = 0
            bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
            print("Loading......")
            print("Red color done!")
            cv2.imshow('image',bgr)

    case 4:
        print("Skipping.....")
        print("")
    
    case _ :
        print ("Invalid Input!")
        print("")
        sys.exit()

#creating a switchcase statement(structural pattern matching) for RGB image color plane seperation
print("Do you want to seperate the RGB planes of the image? ")
print("1:- Yes, please")
print("2:- Yes, and also merge the colored images back and make a recreated image")
print("3:- No, thank you")
print("")

RGB_seperation = int(input("Enter your option:- "))
print('')
match RGB_seperation:
    case  1:
       # split the Blue, Green and Red color channels
       blue,green,red = cv2.split(img)
       # define channel having all zeros
       zeros = np.zeros(blue.shape, np.uint8)
       # merge zeros to make BGR image
       blueBGR = cv2.merge([blue,zeros,zeros])
       greenBGR = cv2.merge([zeros,green,zeros])
       redBGR = cv2.merge([zeros,zeros,red])

       print("Splitting the image into RGB planes....")
       print("Done!")
       print("")
       
       # display the three Blue, Green, and Red channels as BGR image
       cv2.imshow('Blue Channel', blueBGR)
       cv2.imshow('Green Channel', greenBGR)
       cv2.imshow('Red Channel', redBGR)

    case 2:
        # Split the image into RGB channels
        b, g, r = cv2.split (img)
        # Create black images with only the specific channel
        blue_channel_img = np.zeros_like(img)
        blue_channel_img[:,:,0]=b
        # Set blue channel values
        green_channel_img = np.zeros_like (img)
        green_channel_img[:,:, 1] = g
        # Set green channel values
        red_channel_img = np.zeros_like (img)
        red_channel_img[:,:, 2] = r 
        # Set red channel values

        # Recreate the original image by merging the color channels
        recreated_img = cv2.merge( (blue_channel_img[:, :, 0], green_channel_img[:, :, 1], red_channel_img[:, :, 2]))

        print("Splitting the image into RGB planes....")
        print (" Recrearting the original image by merging the colors...")
        print("Done!")
        print("")
        
        # Display the recreated image and individual RGB channels
        cv2.imshow ('Recreated Image', recreated_img) 
        cv2.imshow ('Blue Channel', blue_channel_img) 
        cv2.imshow ('Green Channel', green_channel_img) 
        cv2.imshow ('Red Channel', red_channel_img)
    
    case 3:
         print('Skipping...')
         print('')

    case _ :
        print ("Invalid Input!")
        print("")
        sys.exit()

#creating a switchcase statement(structural pattern matching) for creating an image out of 2D data
print("Do you want the specified 2D data be converted to an image?")
print("1:- Yes, please")
print("2:- No, thank you")
print("")

fig_size = int(input("Enter your option:- "))
print('')
match fig_size:
    case   1:
        # Create a sample 2D data array
        data = np.array([[255, 0, 0], [0, 255, 0], [0, 0, 255]], dtype=np.uint8)

        # Define the scaling factor
        scale_factor = int(input("Enter the scale factor:- "))

        # Upscale the 2D data array
        scaled_data = cv2.resize(data, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
        
        # Write the upscaled data as an image file
        output_file = cv2.imwrite(r"C:\Users\kiran\Downloads\New Image.jpg",scaled_data)
        cv2.imshow('scaled_data',scaled_data)
        print("Image written successfully.")
        print("")

    case 2:
         print('Skipping...')
         print('')

    case _ :
        print ("Invalid Input!")
        print("")
        sys.exit()

#WaitKey
cv2.waitKey(0)
