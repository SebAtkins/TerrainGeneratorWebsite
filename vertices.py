from random import randint
from image import getVal

def generateVertices(xScale, yScale, file="output.png"):
    vertices = [] 

    for y in range(yScale):
        for x in range(xScale):
            vertices.append([x, getVal(x,y, file), y])
    
    return vertices