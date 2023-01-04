import cv2
import numpy as np
import argparse
import time

# parse values
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help= "path to the image we want to crisp")
ap.add_argument("--dest", help= "save directory ")
args = vars(ap.parse_args())

targetImage = args["image"]
targetSaveDirectory = args["dest"]

print ("INFO : targetImage {}".format(targetImage))
print ("INFO : targetSaveDirectory {}".format(targetSaveDirectory))

img = cv2.imread(targetImage)

# crisp action
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
image_sharp = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)

        
# generate timestamp for image file name
timeStamp = round(time.time() * 1000)

if targetSaveDirectory != "" and targetSaveDirectory is not None:
    fileName = f"{targetSaveDirectory}/Crisp-Image{timeStamp}.png"    
else:
    fileName =f"./Crisp-Image{timeStamp}.png"

# Save the image
cv2.imwrite(fileName,image_sharp)    
print(f"Image Crisp successfully and save to {fileName}");

cv2.imshow("NewCrispImage", image_sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()