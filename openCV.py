import cv2
import numpy as np

# Function to calculate distance between two points
def calculate_distance(point1, point2):
    return np.sqrt((point2[0] - point1[0])*2 + (point2[1] - point1[1])*2)

# Load the image
image = cv2.imread(r"img.jpeg")
# image = cv2.imread(r"img.jpg")


# Define the conversion factor from pixels to centimeters
conversion_factor = 1.0  # Placeholder value, needs to be calibrated

# Measure the distance in pixels between the two points on the calibration object
pixel_distance_calibration = 50  # Measure this manually

# Corresponding real-world distance in centimeters
real_distance_calibration = 170   # Measure this manually

# Calculate the conversion factor
conversion_factor = real_distance_calibration / pixel_distance_calibration

# Parameters for object tracking
object1_center = None
object2_center = None
distance_threshold = 50  # Set your own threshold for considering the two points as the same object

while True:
    # Show the image
    frame = image.copy()

    if object1_center is None or object2_center is None:
        # Select the objects to track (manually)
        object1_center = cv2.selectROI('Image', frame)
        object2_center = cv2.selectROI('Image', frame)

        # Convert from (x, y, w, h) format to (x, y) center format
        object1_center = (int(object1_center[0] + object1_center[2] / 2), int(object1_center[1] + object1_center[3] / 2))
        object2_center = (int(object2_center[0] + object2_center[2] / 2), int(object2_center[1] + object2_center[3] / 2))

    # Calculate the distance between the two points
    distance = calculate_distance(object1_center, object2_center)

    # Convert distance from pixels to centimeters
    distance_in_cm = distance * conversion_factor

    # Display the distance on the frame
    cv2.putText(frame, f"Distance: {distance_in_cm:.2f} cm", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Image', frame)

    key = cv2.waitKey(0)
    if key == ord('q'):
        break

cv2.destroyAllWindows()