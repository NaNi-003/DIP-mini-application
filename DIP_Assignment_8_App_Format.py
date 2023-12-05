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

# Defining the Weiner function beforehand, to be used later for restoring image using weiner filter
def weiner_filter(noisy_image, kernel_size, noise_var):
      # Calculate the power spectrum of the noisy image
      f = np.fft.fft2(noisy_image)
      fshift = np.fft.fftshift(f)
      magnitude_spectrum = np.abs(fshift)
      
      # Calculate the Wiener filter
      denoised_spectrum = magnitude_spectrum*2 / (magnitude_spectrum*2 + noise_var)
      restored_fshift = fshift * denoised_spectrum
      restored_image = np.abs(np.fft.ifft2(np.fft.ifftshift(restored_fshift)))
      
      return restored_image.astype(np.uint8)

home_directory = os.path.expanduser("~") # Expand the user's home directory.
file_path = input("Enter the file's path:- \n") # Prompt the user for a file path.
full_file_path = os.path.join(home_directory, file_path) # Join the user's home directory with the file path.
print(f"The provided file path is:- {full_file_path} \n") # Print the full file path
image = cv2.imread(full_file_path)
print("Showing original Image:- \n")
cv2.imshow('Original Image', image)

#creating a switchcase statement(structural pattern matching) for image operations
print("To perform operations on your Image, choose options:- ")
print("1:- Remove Salt and Pepper Noise")
print("2:- Applying Gaussian Blur")
print("3:- Medium Filter and Weiner Filter")
print("4:- Exit programme \n")
Img_Options = get_user_input()
print(f"You entered {Img_Options}. \n")
match Img_Options:
  case 1:
    # Program to understand various image noise models for Image restoration
    # Remove Salt and Pepper Noise
    
    print("Removing Salt and Pepper Noise... \n")
    noise_density = 0.02  # Adjust this value to control the noise density
    noisy_image = image.copy()
    num_salt = np.ceil(noise_density * image.size * 0.5)
    salt_coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy_image[salt_coords[0], salt_coords[1], :] = 1  # Pepper noise
    num_pepper = np.ceil(noise_density * image.size * 0.5)
    pepper_coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy_image[pepper_coords[0], pepper_coords[1], :] = 0  # Salt noise
    
    # Apply median filtering to remove the noise
    filtered_image = cv2.medianBlur(noisy_image, 3)  # 3x3 median filter
    
    # Display the original and denoised images
    plt.figure(figsize=(12, 12))
    
    print("Plotting the Noisy Image...")
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB))
    plt.title('Noisy Image')
    
    print("Plotting the Denoised Image...")
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB))
    plt.title('Denoised Image (Median Filter)')
    
    plt.tight_layout()
    plt.show()
    cv2.waitKey(0)
    
  case 2:
    # Gaussian Blur
    print("Applying Gaussian Blur on the provided Image... \n")
    filtered_image = cv2.GaussianBlur(image, (15, 15), 0)
    print("Displaying the Blurred Image:- ")
    cv2.imshow('Filtered Image', filtered_image)
    cv2.waitKey(0)

  case 3:
    # Medium Filter and Weiner Filter
    # Add noise to the image (Gaussian noise in this example)
    mean = 0
    stddev = 25  # Adjust this value to control the noise level
    noise = np.random.normal(mean, stddev, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)
    
    # Apply Median Filter to remove noise
    print("Applying Median Filter...")
    median_filtered_image = cv2.medianBlur(noisy_image, 5)  # 5x5 median filter
    
    # Apply Weiner Filter for image restoration
    print("Applying the Weiner Filter... \n")
    # Estimate the noise variance (you may need to adjust this value)
    estimated_noise_var = stddev**2
    
    # Apply Wiener filter to the noisy image
    weiner_filtered_image = weiner_filter(noisy_image, 5, estimated_noise_var)
    
    # Display the original, noisy, median filtered, and Wiener filtered images
    plt.figure(figsize=(12, 12))
    
    print("Plotting the Original Image...")
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    
    print("Plotting the Noisy Image...")
    plt.subplot(2, 2, 2)
    plt.imshow(cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB))
    plt.title('Noisy Image')
    
    print("Plotting the Median Filtered Image...")
    plt.subplot(2, 2, 3)
    plt.imshow(cv2.cvtColor(median_filtered_image, cv2.COLOR_BGR2RGB))
    plt.title('Median Filtered Image')
    
    print("Plotting the Weiner Filtered Image...")
    plt.subplot(2, 2, 4)
    plt.imshow(cv2.cvtColor(weiner_filtered_image, cv2.COLOR_BGR2RGB))
    plt.title('Weiner Filtered Image')
    
    plt.tight_layout()
    plt.show()
    cv2.waitKey(0)
    
  case 4:
    print("Exiting the Programme...")
    cv2.waitKey(0)
    sys.exit()

  case _:
    pass

# C:\Users\kiran\Downloads\NB WP.jpg