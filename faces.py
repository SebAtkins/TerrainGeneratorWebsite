from normals import produceFaceNormal

def vertexAbove(vertices, vertex, xScale):
    position = vertices.index(vertex)

    return vertices[position + 1]

def vertexRight(vertices, vertex, xScale):
    position = vertices.index(vertex)

    return vertices[position + xScale]

def generateFaces(vertices, xScale, yScale, genNormals):
    faces = []
    faceNormals = []

    for i in vertices:
        if i[0] != (xScale - 1) and i[2] != (yScale - 1):
            #Find vertices in face
            above = vertexAbove(vertices, i, xScale)
            aboveRight = vertexRight(vertices, above, xScale)
            right = vertexRight(vertices, i, xScale)

            #Add face
            faces.append([i, above, aboveRight])
            faces.append([i, aboveRight, right])

            #Add normals
            if genNormals == True:
                faceNormals.append(produceFaceNormal(i, above, aboveRight))
                faceNormals.append(produceFaceNormal(i, right, aboveRight))
    
    return faces, faceNormals