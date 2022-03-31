import colorsys

from PIL import Image
from PIL import ImageDraw

from noiseGenerator import noiseFactory

def showImg(file):
	img = Image.open(file)
	img.show()

def getVal(x, y, file):
	image = Image.open(file)

	#Get the RGB value of the pixel
	r, g, b = image.getpixel((x, y))
	#Translate the RGB to HSV in order to get opacity
	h, s, v = colorsys.rgb_to_hsv(r, g, b)

	return v / 10

def prodImg(xScale, yScale, file, seed, octaves, bias, smooth, xchunk = 0, ychunk = 0):
	noiseScale = max([xScale, yScale])

	noiseGenerator = noiseFactory()

	img = Image.new("HSV", (noiseScale,noiseScale), "white")
	draw = ImageDraw.Draw(img)

	noiseGenerator.makeOctaveList(noiseScale, noiseScale, seed, smooth, octaves, bias, xchunk, ychunk) 

	values = noiseGenerator.list

	minVal = min(values)
	tempList = [x - minVal for x in values]

	maxVal = max(tempList)
	values = [x / maxVal * 100 for x in tempList]

	for x in range (noiseScale):
		for y in range(noiseScale):
			draw.rectangle([x,y,x+1,y+1], fill = (0,0, int(values[y * noiseScale + x])))

	img = img.crop((0,0, xScale, yScale))

	rgbImg = img.convert(mode="RGB")
	rgbImg.save(file)

if __name__=="__main__":
	prodImg(160, 200, "Final/error.png", 12345, 8, 0.35, 25)