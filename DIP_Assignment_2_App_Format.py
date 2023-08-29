import cv2
import os
import sys

home_directory = os.path.expanduser("~") # Expand the user's home directory.
file_path_1 = input("Enter the 1st file's path:- ") # Prompt the user for a file path.
file_path_2 = input("Enter the 2nd file's path:- ") # Prompt the user for a file path.
full_file_path_1 = os.path.join(home_directory, file_path_1) # Join the user's home directory with the file path.
full_file_path_2 = os.path.join(home_directory, file_path_2) # Join the user's home directory with the file path.
print("")
print("The provided file paths are:-")
print("")
print(full_file_path_1) # Print the full file path 1.
print(full_file_path_2) # Print the full file path 2.
print("")

#Reading the images from the provided file paths

img1 = cv2.imread(full_file_path_1)
img2 = cv2.imread(full_file_path_2)
print("Showing original images:- ")
cv2.imshow('Original Image 1', img1)
cv2.imshow('Original Image 2', img2)

#creating a switchcase statement(structural pattern matching) for image operations
print("To perform operations on your images, choose options:- ")
print("1:- Add your images")
print("2:- Subtract your images")
print("3:- Multiply your images")
print("4:- Divide your images")
print("5:- AND Operation")
print("6:- OR Operation")
print("7:- NOT Operation")
print("8:- XOR Operation")
print("9:- Exit programme")
print("")

Img_Options = int(input("Enter Option:- "))
match Img_Options:
    case 1:
        #Adding images
        added_img = cv2.add(img1,img2)
        cv2.imshow('Added Image',added_img)
        cv2.waitKey(0)


    case 2:
        #Subtracting images
        subtracted_img = cv2.subtract(img1,img2)
        cv2.imshow('Subtracted Image',subtracted_img)
        cv2.waitKey(0)


    case 3:
        #Multiplying images
        multiplied_img = cv2.multiply(img1,img2)
        cv2.imshow('Multiplied Image',multiplied_img)
        cv2.waitKey(0)


    case 4:
        #Dividing images 
        divided_img = cv2.divide(img1,img2)
        cv2.imshow('Divided Image',divided_img)
        cv2.waitKey(0)


    case 5:
        #Bitwise AND
        bitwise_and_img = cv2.bitwise_and(img1,img2)
        cv2.imshow('Bitwise AND',bitwise_and_img)
        cv2.waitKey(0)


    case 6:
        #Bitwise OR
        bitwise_or_img = cv2.bitwise_or(img1,img2)
        cv2.imshow('Bitwise OR',bitwise_or_img)
        cv2.waitKey(0)


    case 7:
        #Bitwise NOT
        bitwise_not_img = cv2.bitwise_not(img1)
        cv2.imshow('Bitwise NOT',bitwise_not_img)
        cv2.waitKey(0)


    case 8:
        #Bitwise XOR
        bitwise_xor_img = cv2.bitwise_xor(img1,img2)
        cv2.imshow('BitwiseXOR',bitwise_xor_img)
        cv2.waitKey(0)


    case 9:
        #Exit Programme
        print("Exiting the Programme...")
        sys.exit()

#C:\Users\kiran\Downloads\WH4 (copy DIP A-2).jpg
#C:\Users\kiran\Downloads\WP TW(copy DIP A-2).jpg
