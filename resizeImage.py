import cv2
print(cv2.__version__)

import argparse
import os
import time

# parse values
ap = argparse.ArgumentParser()
ap.add_argument('--width',required=True, help='target width of image', type=int)
ap.add_argument("-i", "--image", required = True, help= "path to the image we want to resize")
ap.add_argument("--dest", help= "save directory ")
args = vars(ap.parse_args())

new_width = args["width"]
targetImage = args["image"]
targetSaveDirectory = args["dest"]

print ("INFO : targetWidth {}".format(new_width))
print ("INFO : targetImage {}".format(targetImage))
print ("INFO : targetSaveDirectory {}".format(targetSaveDirectory))


# Read image
image = cv2.imread(args["image"])
print("[INFO] w: {}, h: {}".format(image.shape[1], image.shape[0]))

height = image.shape[0]
width = image.shape[1]

#use the super resolution model to upscale the image , timing how long it takes
start= time.time()

# compute new aspect ratio based on new width
ratio = new_width / width # (or new_height / height)
new_height = int(height * ratio)

dimensions = (new_width, new_height)

# resize the image using new dimensions
new_image = cv2.resize(image, dimensions, interpolation=cv2.INTER_LINEAR)

end = time.time()
print("INFO: resizing resolution took {:.6f} seconds".format(end-start))


# generate timestamp for image file name
timeStamp = round(time.time() * 1000)
if targetSaveDirectory != "" and targetSaveDirectory is not None:
    fileName = f"{targetSaveDirectory}/resizeImage-{new_width}-{timeStamp}.png"
else:
    fileName = f"./resizeImage-{new_width}-{timeStamp}.png"

# Save the image
cv2.imwrite(fileName,new_image)
print(f"Image resize successfully and save to {fileName}");

cv2.imshow('ResizeImage', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


