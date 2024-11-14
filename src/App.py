import sys, pygame, random, copy


def drawRect(x, y, screen):
    white = (255, 255, 255)
    pygame.draw.rect(screen, white, pygame.Rect(x * 5, y * 5, 5, 5))

def drawGrid(grid, screen):
    screen.fill(color=(0, 0, 0))
    for xi, x in enumerate(grid):
        for yi, y in enumerate(grid[xi]):
            if y == 1:
                drawRect(xi, yi, screen)

def initGrid(grid) -> list:
    starting = random.randrange(1, 100)
    i = 0
    while i < starting:
        neighbours = random.randint(0, 8)
        x = random.randrange(1, len(grid) - 1) 
        y = random.randrange(1, len(grid) - 1)
        grid[x][y] = 1
        #TODO: set neighbours of starting pixels
        posX = x
        posY = y
        while (neighbours > 0):
            direction = random.randint(1, 8)
            
            if posX == 0 or posX == 139 or posY == 0 or posY == 139:
                break

            if direction == 1:
                posX -= 1
                posY += 1
            elif direction == 2:
                posY += 1
            elif direction == 3:
                posX += 1
                posY += 1
            elif direction == 4:
                posX += 1
            elif direction == 5:
                posX += 1
                posY -= 1
            elif direction == 6:
                posY -= 1
            elif direction == 7:
                posX -= 1
                posY -= 1
            elif direction == 8:
                posX -= 1
            grid[posX][posY] = 1
            neighbours -= 1
        i+=1
    return grid

def getNeighbours(x, y, grid) -> int:
    count = 0
    up: bool = y
    down: bool = abs(y-139)
    left: bool = x
    right: bool = abs(x-139)

    if up:
        count += grid[x][y-1]
        if left:
            count += grid[x-1][y-1]
        if right:
            count += grid[x+1][y-1]
    
    if left:
        count += grid[x-1][y]

    if down:
        count += grid[x][y+1]
        if left:
            count += grid[x-1][y+1]
        if right:
            count += grid[x+1][y+1]
    
    if right:
        count += grid[x+1][y]
    
    return count


def updateGrid(grid) -> list: 
    newGrid = copy.deepcopy(grid)
    for xi, x in enumerate(grid):
        for yi, y in enumerate(grid[xi]):
            neighbours = getNeighbours(xi, yi, grid)

            if grid[xi][yi] == 1:
                if neighbours < 2 or neighbours > 3:
                    newGrid[xi][yi] = 0
            
            else:
                if neighbours == 3:
                    newGrid[xi][yi] = 1

    return newGrid

def run():
    clock = pygame.time.Clock()

    pygame.init()

    size = x,y = 700, 700
    screen = pygame.display.set_mode(size)

    pixelSize = 5
    pixels = [[0 for _ in range(x // pixelSize)] for _ in range(y // pixelSize)]
    pixels = initGrid(pixels)
    drawGrid(pixels, screen)

    running = True
    fps = 15
    count = 0

    while running:

        for e in pygame.event.get():
            if (e.type == pygame.QUIT):
                running = False
                
        clock.tick(fps)

        pixels = updateGrid(pixels)
        drawGrid(pixels, screen)
        pygame.display.flip()

run()




