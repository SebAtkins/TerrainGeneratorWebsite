from normals import generateNormals
from vertices import generateVertices
from faces import generateFaces

def createFile(fileName, vertices, faces, genNormals, vertexNormals = []):
    file = open(fileName, "w")

    #Add vertices
    for i in vertices:
        file.write("v " + str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")
    
    #Add vertex normals
    if genNormals == True:
        for i in vertexNormals:
            file.write("vn " + str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")
    
    #Add faces
    for i in faces:
        vert1 = vertices.index(i[0]) + 1 #+ 1 as obj isn't 0 indexed
        vert2 = vertices.index(i[1]) + 1
        vert3 = vertices.index(i[2]) + 1

        #Check to see if normals are required
        if genNormals != True:
            file.write("f " + str(vert1) + " " + str(vert2) + " " + str(vert3) + "\n")
        else:
            file.write("f " + str(vert1) + "//" + str(vert1) + " " + str(vert2) + "//" + str(vert2) + " " + str(vert3) + "//" + str(vert3) + "\n")
    
    file.close()

def runGen(xScale, yScale, fileName, imgName, genNormals):
    vertexNormals = []

    vertices = generateVertices(xScale, yScale, imgName)
    faces, faceNormals = generateFaces(vertices, xScale, yScale, genNormals)
    if genNormals == True:
        vertexNormals = generateNormals(vertices, faces, faceNormals)
    createFile(fileName, vertices, faces, genNormals, vertexNormals)