# Leap Motion Dataset Collector
Collect data from a leap motion device and a camera for multi-modality dataset creation 

Outputs a CSV file

# Requirements
Python: Leap API, NumPy. vg. cv2

Leap: Software for your device and OS 

# Set up
Just drop this script alongside the Leap python example in the Developer API when unzipped

Lines 32 and 33:

label = "CAR"
subject = "JORDAN"

Would form:
CAR-JORDAN-epochtime.csv

So, you can record it as many times as you want since the epoch time results in a unique filename each time

# Output
A CSV file containing each recorded vector every 0.25 seconds 
Change line 72 - time.sleep(0.25) - to change this

The final column in the dataset is the label variable (in this case CAR) as a string, for gesture classification


# For complex gestures
It would likely be useful to introduce lag windows for more complex problems

# To Do
Clean up code, it is a bit of a mess at the moment. It works fine though. 

Option to turn camera off (can be easily done by deleting the block of code for it)

Edit this readme when I have some time in order to give more details and more user-friendly help

3D angles are calculated using a separate script, which I will upload soon

A Python 3.x version of this script if Leap ever decide to release a stable API. I had no luck with the Python 3 APIs out there from third parties unfortunately. 

# Usage
Feel free to use this for anything. I will merge pulls for new features and engineered features from those which have been collected. 

# Publication
This script was used in part for data collection in:

Bird, Jordan J., Aniko Ekart, and Diego R. Faria. "British Sign Language Recognition via Late Fusion of Computer Vision and Leap Motion with Transfer Learning to American Sign Language." (2020).

In this work, we use a multi-modality approach to improve sign language recognition via inputting camera images and Leap Motion data to a branched neural network and performing late fusion.


