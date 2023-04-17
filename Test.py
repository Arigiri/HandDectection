import cv2
import numpy as np

# Load images
y_true = cv2.imread('Objects/circle.png', cv2.IMREAD_GRAYSCALE)
y_pred = y_true#cv2.imread('Objects/circle.png', cv2.IMREAD_GRAYSCALE)

# Threshold images
y_true = cv2.threshold(y_true, 127, 1, cv2.THRESH_BINARY)[1]
y_pred = cv2.threshold(y_pred, 127, 1, cv2.THRESH_BINARY)[1]

# Calculate the Dice coefficient
intersection = np.sum(y_true * y_pred)
y_true_sum = np.sum(y_true)
y_pred_sum = np.sum(y_pred)
print(y_true_sum)
print(y_pred_sum)
print(intersection)
print(y_pred_sum/intersection)
smooth = 1
dice = (2 * intersection + smooth) / (y_true_sum + y_pred_sum + smooth)

# Print the result
print('Dice coefficient:', dice)

# Check if the result is close to 1
if np.isclose(dice, 1):
    print('The images are a perfect match.')
else:
    print('The images are not a perfect match.')