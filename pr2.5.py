# Python program to explain cv2.imwrite() method

# importing cv2
import cv2
image_path = r'C:\Users\ayush\PycharmProjects\IP_Practicals\Lotus.jpg'
directory = r'C:\Users\ayush\OneDrive\Desktop'

# importing os module
import os
image_path = r'Lotus.jpg'
directory = r'C:\Users\ayush\OneDrive\Desktop'
img = cv2.imread(image_path)
os.chdir(directory)
print("Before saving image:")
print(os.listdir(directory))
filename = 'savedImage.jpg'
cv2.imwrite(filename, img)
print("After saving image:")
print(os.listdir(directory))
print('Successfully saved')
