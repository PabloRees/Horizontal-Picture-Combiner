from PIL import Image
import os
import concurrent.futures
from random import randint

directory = r'C:\Users\Game330\Desktop\Design\Surfboard'
imageList=[]

# selects random image names and adds them to the imageList
class randoImage:
    def __init__(self, numImages, directory, imageList):
        self.numImages = numImages
        self.directory = directory
        self.imageList = imageList

        randomNumber = []
        for x in range(numImages):
                                           #avoids duplicate numbers in the image list
            newNum = randint(0,65)
            while randomNumber.__contains__(newNum):
                newNum +=1
                y=64
                while newNum >y:
                    newNum = randint(0,y)
                    y -=1
            randomNumber.append(newNum)

        for x in range(numImages):

            image = directory + '\\' + os.listdir(directory)[randomNumber[x]]
            imageList.append(image)

# concatenates the images in image list
class concatImages:
    def __init__(self, imageList):
        self.imageList = imageList
        images = [Image.open(x) for x in imageList]
        widths, heights = zip(*(i.size for i in images))
        total_width = 0
        total_height = max(heights)


        for j in images:
            jWidth, jHeight = j.size
            jRatio = total_height / jHeight
            jNewWidth = jWidth * jRatio  #adds up the resized widths to decide the total image width
            total_width = int(total_width + jNewWidth)

        new_im = Image.new('RGB', (total_width, total_height))

        x_offset = 0
        for j in images:
            jWidth, jHeight = j.size
            jRatio = total_height / jHeight
            jNewWidth = jWidth * jRatio
            size = (int(jNewWidth),total_height)


            new_im.paste(j.resize(size), (x_offset, 0))
            x_offset += size[0]

        saveLocation = r'C:\Users\Game330\Desktop\Design\Collages\Collage' + str(x) + '.jpg'
        new_im.save(saveLocation)


for x in range(100):
    numImages = randint(3,15)
    height = 0
    imageList = []
    randoImage(numImages, directory, imageList)


    concatImages(imageList)


