from PIL import Image
from resizeimage import resizeimage
import glob, os, sys

if len(sys.argv) != 5:
        print('Invalid Numbers of Arguments. Script will be terminated.')
        print ('resize.py /home/kl/t1/frog *.jpeg 150 150')
else:
   	for eacharg in sys.argv:
   		print eacharg
   		xpath=sys.argv[1]
   		xpattern=sys.argv[2]
   		widht=int(sys.argv[3])
   		height=int(sys.argv[4])

def res1(file):
	with open(file, 'r+b') as f:
	    with Image.open(f) as image:
	        cover = resizeimage.resize_cover(image, [widht, height])
	        cover.save(file, image.format)


zahl=0
os.chdir(xpath)
for file in glob.glob(xpattern):
	print(file)
	zahl=zahl+1
	res1(file)
print 'Number of files: ' + str(zahl)