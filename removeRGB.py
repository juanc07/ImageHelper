import cv2
import time
import argparse

from PIL import Image

# parse values
ap = argparse.ArgumentParser()
ap.add_argument('--color',required=True, help='color to remove')
ap.add_argument("-i", "--image", required = True, help= "path to the image we want to remove RGB")
ap.add_argument("--dest", help= "save directory ")
args = vars(ap.parse_args())

colorToRemove = args["color"]
targetImage = args["image"]
targetSaveDirectory = args["dest"]

print ("INFO : colorToRemove {}".format(colorToRemove))
print ("INFO : targetImage {}".format(targetImage))
print ("INFO : targetSaveDirectory {}".format(targetSaveDirectory))


pict = Image.open(targetImage)

#We will have to use the .bmp extension.
#This allows for other functions to be performed in the image
#Storing the image using save() function
pict.save('removeBlue.bmp')

#We create a loop that allows for iteration between the X and Y pixels
for x in range(pict.size[0]):
    for y in range(pict.size[1]):
        r, g, b = pict.getpixel((x, y))
        match colorToRemove:
            case "r":
                pict.putpixel((x, y), (0, g, b))
            case "g":
                pict.putpixel((x, y), (r, 0, b))
            case "b":
                pict.putpixel((x, y), (r, g, 0))
            case _:
                pict.putpixel((x, y), (r, g, 0))
        
# generate timestamp for image file name
timeStamp = round(time.time() * 1000)

if targetSaveDirectory != "" and targetSaveDirectory is not None:
    fileName = f"{targetSaveDirectory}/removeRGB-{colorToRemove}-{timeStamp}.png"    
else:
    fileName = f"./removeRGB-{colorToRemove}-{timeStamp}.png"

# Save the image    
pict.save(fileName)

print(f"Image removeColor: {colorToRemove} successfully and save to {fileName}");

pict.show()
cv2.waitKey(0)
cv2.destroyAllWindows()