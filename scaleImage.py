import cv2
print(cv2.__version__)

import argparse
import os
import time

# parse values
ap = argparse.ArgumentParser()
ap.add_argument('--scale',required=True, help='scale value 0.5 = 50% 1 = 100% , 2 = 200%', type=float)
ap.add_argument("-i", "--image", required = True, help= "path to the image we want to increase resolution")
ap.add_argument("--dest", help= "save directory ")
args = vars(ap.parse_args())

scaleValue = args["scale"]
targetImage = args["image"]
targetSaveDirectory = args["dest"]


print ("INFO : scaleValue {}".format(scaleValue))
print ("INFO : targetImage {}".format(targetImage))
print ("INFO : targetSaveDirectory {}".format(targetSaveDirectory))

# Read image
image = cv2.imread(args["image"])

height = image.shape[0]
width = image.shape[1]

print("[INFO] w: {}, h: {}".format(image.shape[1], image.shape[0]))

#use the super resolution model to upscale the image , timing how long it takes
start= time.time()

scale_factor = scaleValue


new_height = int(height * scale_factor)
new_width = int(width * scale_factor)
dimensions = (new_width, new_height)

# scale the image based on dimensions
new_image = cv2.resize(image, dimensions, interpolation=cv2.INTER_LINEAR)

end = time.time()
print("INFO: resizing resolution took {:.6f} seconds".format(end-start))

# generate timestamp for image file name
timeStamp = round(time.time() * 1000)

if targetSaveDirectory != "" and targetSaveDirectory is not None:
    fileName = f"{targetSaveDirectory}/scaledImage-{scale_factor}-{timeStamp}.png"    
else:
    fileName = f"./scaledImage-{scale_factor}-{timeStamp}.png"

# Save the image    
cv2.imwrite(fileName, new_image)
print(f"Image scaled successfully and save to {fileName}");

cv2.imshow('scaledImage', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


