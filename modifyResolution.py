import cv2
import numpy as np
import argparse
import time

# parse values
ap = argparse.ArgumentParser()
ap.add_argument("--resolution",required = True, help= "pass up or down")
ap.add_argument("-i", "--image", required = True, help= "path to the image we want to modify the resolution")
ap.add_argument("--dest", help= "save directory ")
args = vars(ap.parse_args())


targetResolution = args["resolution"]
targetImage = args["image"]
targetSaveDirectory = args["dest"]

print ("INFO : targetImage {}".format(targetImage))
print ("INFO : targetResolution {}".format(targetResolution))
print ("INFO : targetSaveDirectory {}".format(targetSaveDirectory))

img = cv2.imread(targetImage)

# We will be Increasing or decrease the resolution based on targetResolution if up or down.
match targetResolution:
    case "up":
        newImage = cv2.pyrUp(img)
    case _:
        newImage = cv2.pyrDown(img)

        
# generate timestamp for image file name
timeStamp = round(time.time() * 1000)

if targetSaveDirectory != "" and targetSaveDirectory is not None:
    fileName = f"{targetSaveDirectory}/Res-{targetResolution}-Image{timeStamp}.png"    
else:
    fileName =f"./Res-{targetResolution}-Image{timeStamp}.png"

# Save the image
cv2.imwrite(fileName,newImage)    
print(f"Image Resolution modified successfully and save to {fileName}");

cv2.imshow("NewResImage", newImage)
cv2.waitKey(0)
cv2.destroyAllWindows()