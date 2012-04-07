# Functions for 3D Snake V100

# Function receives the array containing the piece of the snake and
# returns the coordinates of the piece ELSE returns [-1,-1,-1]. 
def PiecePosition(array, piece):
    # Loop trough the array until 'piece' is found
    for i in range(8):
        for j in range(8):
            for k in range(8):
                if array[i][j][k] == piece:
                    # Write Coordinates of Head for Return
                    position = [i, j, k]
                    return position
    return None


# Receives the position of the head of the snake and the direction
# of movement and returns the new position of the head.
def ChangePositionHead(position, direction):
    # Separate update of position is made based on direction of movement.
    # Does not allows snake to emded on self
    # Head crosses cube if colliding on wall
    # If Moving to +X
    if direction == 1:
        if direction != 2: position[0] = position[0] + 1
        if position[0] > 7: position[0] = 0
        elif position[0] < 0: position[0] = 7

    # If Moving to -X
    if direction == 2:
        if direction != 1: position[0] = position[0] - 1
        if position[0] > 7: position[0] = 0
        elif position[0] < 0: position[0] = 7

    # If Moving to +Y
    if direction == 3:
        if direction != 4: position[1] = position[1] + 1
        if position[1] > 7: position[1] = 0
        elif position[1] < 0: position[1] = 7

    # If Moving to -Y
    if direction == 4:
        if direction != 3: position[1] = position[1] - 1
        if position[1] > 7: position[1] = 0
        elif position[1] < 0: position[1] = 7

    # If Moving to +Z
    if direction == 5:
        if direction != 6: position[2] = position[2] + 1
        if position[2] > 7: position[2] = 0
        elif position[2] < 0: position[2] = 7

    # If Moving to -Z
    if direction == 6:
        if direction != 5: position[2] = position[2] - 1
        if position[2] > 7: position[2] = 0
        elif position[2] < 0: position[2] = 7

    return position

# Checks if Head will Collide and returns TRUE or FALSE
# Takes game array and intended head position
def HeadCollide(array, position):
    if array[position[0],position[1],position[2]]:
        return TRUE
    else:
        return FALSE

# Moves the Head and Body (By Joao)
# Receives size of snake, direction and game array, returns a new game array
def MovePiece(array, size, direction):
    # First calculates position for head, in case there is only one piece
    head_old = PiecePosition(array, 1) # returns a list
    head_new = ChangePositionHead(head_old, direction) #returns a list
    # Updates body
    for piece in range(size, 0, -1):
        pos = PiecePosition(array, piece)
        '''print "In position"
        print pos
        print "Piece was"
        print piece'''
        if pos:
            # Piece is deleted when equal to size
            if piece == size:
                array[pos[0]][pos[1]][pos[2]] = 0
                '''print "Now it was discarded"'''
            # Piece is Kept when less than size
            elif piece < size:
                array[pos[0]][pos[1]][pos[2]] = piece + 1
                '''print "Now piece is"
                print array[pos[0]][pos[1]][pos[2]]'''
    # Updates head
    '''print "Now head is at"
    print head_new'''
    array[head_new[0]] [head_new[1]] [head_new[2]] = 1
#    return array   # UNNECESSARY

# Create 3D Nester Array (By Joao)
def CreateArray3D():
    array = []
    for i in range(8):
        array.append([])
        for j in range(8):
            array[i].append([])
            for k in range(8):
                array[i][j].append(0)
    return array

# Function to print a specific layer of the game
# Takes the game array and the layer xframe to be displayed
# Prints the game in a neat grid
def PrintFrame(array, xframe):
    for y in range(len(array[xframe])):
        print ' '.join(map(str, array[xframe][y])) # maps each int in list to a str function and then joins with space as a separator

cube = CreateArray3D()
print cube
cube[4][4][4] = 1
print "-----"
direction = 6
size = 2
MovePiece(cube, size, direction)
print "Now frame 4 is"
PrintFrame(cube, 4)
print "-----"
direction = 6
size = 3
MovePiece(cube, size, direction)
print "Now frame 4 is"
PrintFrame(cube, 4)
print "-----"
direction = 4
size = 4
MovePiece(cube, size, direction)
print "Now frame 4 is"
PrintFrame(cube, 4)
print "-----"
direction = 4
size = 4
MovePiece(cube, size, direction)
print "Now frame 4 is"
PrintFrame(cube, 4)
print "-----"
direction = 4
size = 4
MovePiece(cube, size, direction)
print "Now frame 4 is"
PrintFrame(cube, 4)
print "-----"
direction = 4
size = 4
MovePiece(cube, size, direction)
print "Now frame 4 is"
PrintFrame(cube, 4)
print "-----"
direction = 4
size = 4
MovePiece(cube, size, direction)
print "Now frame 4 is"
PrintFrame(cube, 4)
