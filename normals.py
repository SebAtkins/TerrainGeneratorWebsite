from math import sqrt

def produceVertexNormal(faceNormals):
    vertexNormal = [0, 0, 0]

    for x in faceNormals:
        vertexNormal[0] = vertexNormal[0] + x[0]
        vertexNormal[1] = vertexNormal[1] + x[1]
        vertexNormal[2] = vertexNormal[2] + x[2]

    normalMagnitude = sqrt(vertexNormal[0] ** 2 + vertexNormal[1] ** 2 + vertexNormal[2] ** 2)
    
    if normalMagnitude != 0:
        for x in vertexNormal:
            x = x / normalMagnitude
    else:
        vertexNormal = [0, 1, 0]

    if vertexNormal[1] < 0:
        vertexNormal[0] = -vertexNormal[0]
        vertexNormal[1] = -vertexNormal[1]
        vertexNormal[2] = -vertexNormal[2]

    return vertexNormal


def produceFaceNormal(vertex1, vertex2, vertex3):
    edge1 = [vertex2[0] - vertex1[0],
             vertex2[1] - vertex1[1],
             vertex2[2] - vertex1[2]]
    
    edge2 = [vertex3[0] - vertex1[0],
             vertex3[1] - vertex1[1],
             vertex3[2] - vertex1[2]]
    
    normal = [edge1[1] * edge2[2] - edge1[2] * edge2[1],
              edge1[2] * edge2[0] - edge1[0] * edge2[2],
              edge1[0] * edge2[1] - edge1[1] * edge2[0]]
    
    normalMagnitude = sqrt(normal[0] ** 2 + normal[1] ** 2 + normal[2] ** 2)

    for x in normal:
        x = x / normalMagnitude

    return normal

def generateNormals(vertices, faces, faceNormals):
    vertexNormals = []

    for x in vertices:
        normalsToUse = []

        for y in faces:
            if x in y:
                normalsToUse.append(faceNormals[faces.index(y)])
        
        vertexNormals.append(produceVertexNormal(normalsToUse))
    
    return vertexNormals