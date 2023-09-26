import numpy as np
import cv2
import os
import sys

def get_user_input():
  while True:
    Img_Options = int(input("Enter Option:- "))
    if Img_Options in [1, 2 , 3, 4, 5, 6]:
      return Img_Options
    else:
      print("Invalid input. Please enter a number between 1 and 6.")

def get_user_choice():
  while True:
    choice = int(input("Enter Choice:- "))
    if choice in [1, 2]:
      return choice
    else:
      print("Invalid input. Please enter a number between 1 and 2.")


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

image1 = cv2.imread(full_file_path_1)
image2 = cv2.imread(full_file_path_2)
print("Showing original images:- ")
cv2.imshow('Original Image 1', image1)
cv2.imshow('Original Image 2', image2)

#creating a switchcase statement(structural pattern matching) for image operations
print("To perform operations on your images, choose options:- ")
print("1:- AND Operation")
print("2:- OR Operation")
print("3:- XOR Operation")
print("4:- NOT Operation")
print("5:- Intersection(AND-NOT) Operation")
print("6:- Exit programme")
print("")

Img_Options = get_user_input()
print(f"You entered {Img_Options}.")
match Img_Options:
  case 1:
    #Bitwise AND
    bitwise_and_img = cv2.bitwise_and(image1,image2)
    print("Result Image:-")
    cv2.imshow('Bitwise AND',bitwise_and_img)
    cv2.waitKey(0)

  case 2:
    #Bitwise OR
    bitwise_or_img = cv2.bitwise_or(image1,image2)
    print("Result Image:-")
    cv2.imshow('Bitwise OR',bitwise_or_img)
    cv2.waitKey(0)

  case 3:
    #Bitwise XOR
    bitwise_xor_img = cv2.bitwise_xor(image1,image2)
    print("Result Image:-")
    cv2.imshow('BitwiseXOR',bitwise_xor_img)
    cv2.waitKey(0)

  case 4:
    print("Which Image do you wish to perform the NOT operation on?")
    print("(Type '1' for Image One and type '2' for Image Two)")
    choice = get_user_choice()
    if(choice == 1 ):
       #Bitwise NOT
       bitwise_not_img = cv2.bitwise_not(image1)
       print("Result Image:-")
       cv2.imshow('Bitwise NOT',bitwise_not_img)
       cv2.waitKey(0)

    elif(choice == 2):
         #Bitwise NOT
         bitwise_not_img = cv2.bitwise_not(image2)
         print("Result Image:-")
         cv2.imshow('Bitwise NOT',bitwise_not_img)
         cv2.waitKey(0)

    else:
      pass

  case 5:
    print("Performing the Intersection of 2 images...")
    print("Choose the Image to perform NOT operation on:- ")
    print("(Type '1' for Image One and type '2' for Image Two)")
    choice = get_user_choice()
    if(choice == 1 ):
       #Bitwise NOT
       print("Choosen Image for NOT is Image One")
       bitwise_not_img_1 = cv2.bitwise_not(image1)
       print("Intersection of NOT-One and Two Images:- ")
       bitwise_and_imgs = cv2.bitwise_and(bitwise_not_img_1,image2)
       cv2.imshow('Intersection',bitwise_and_imgs)
       cv2.waitKey(0)

    elif(choice == 2):
         #Bitwise NOT
         print("Choosen Image for NOT is Image Two")
         bitwise_not_img_2 = cv2.bitwise_not(image2)
         print("Intersection of NOT-Two and One Images:- ")
         bitwise_and_imgs = cv2.bitwise_and(bitwise_not_img_2,image1)
         cv2.imshow('Intersection',bitwise_and_imgs)
         cv2.waitKey(0)

    else:
      pass

  case 6:
    #Exit Programme
        print("Exiting the Programme...")
        cv2.waitKey(0)
        sys.exit()
        
  case _ :
      pass


# C:\Users\kiran\Downloads\DIP A-3 pic 1.png
# C:\Users\kiran\Downloads\DIP A-3 pic 2.png
