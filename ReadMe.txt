// Image helper using python and opencv to resize, scale, make it hires or lowres or removing red, green or blue from image 

//Be aware that this helpers have a dependencies that you need to install first

// these are some of those dependencies but not all
// if you run it and you still lack something, you will get an error and just install what ever what is not install on your machine

// install the python on your windows machine
https://www.python.org/

// install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

// install opencv
// be aware that there's versions that migh work or not work on your machine
pip install opencv-python

python version must be
Python 3.10.6

pip version must be
pip 22.3.1 


Note: this helpers are made for windows , it might or not work on some other OS

// sample commands

//modifyResolution
python modifyResolution.py --resolution up --image [source-imagepath] --dest [output-path]
python modifyResolution.py --resolution down --image [source-imagepath] --dest [output-path]

//scaleImage
python scaleImage.py --scale 2 --image [source-imagepath] --dest [output-path]
python scaleImage.py --scale 4 --image [source-imagepath] --dest [output-path]

//crispImage
python crispImage.py --image [source-imagepath] --dest [output-path]

//resizeImage
python resizeImage.py --width 300 --image [source-imagepath] --dest [output-path]
python resizeImage.py --width 500 --image [source-imagepath] --dest [output-path]

//removeRGB
python removeRGB.py --color r --image [source-imagepath] --dest [output-path]
python removeRGB.py --color g --image [source-imagepath] --dest [output-path]
python removeRGB.py --color b --image [source-imagepath] --dest [output-path]