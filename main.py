import pygame
from Cell import Cell

def main():
    WIDTH, HEIGHT = 1280, 720
    NO_HORIZONTAL_SQUARES = 20
    NO_VERTICAL_SQUARES = 15
    SQUARE_SIZE = 40
    Cell.startingPoint = Cell.calculateStartingPoint(WIDTH, HEIGHT, NO_HORIZONTAL_SQUARES, NO_VERTICAL_SQUARES, SQUARE_SIZE)
    grid = list()
    for i in range(NO_VERTICAL_SQUARES):
        grid.append(list())
        for j in range(NO_HORIZONTAL_SQUARES):
            grid[i].append(Cell(i, j))
    
    grid[4][4].nextAlive = True
    grid[4][5].nextAlive = True
    grid[4][6].nextAlive = True
    grid[5][4].nextAlive = False
    
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    elapsed = pygame.time.get_ticks()
    counter = 0

    # First iteration
    for i in range(NO_VERTICAL_SQUARES):
        for j in range(NO_HORIZONTAL_SQUARES):
            if grid[i][j].nextAlive:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(grid[i][j].x, grid[i][j].y, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(grid[i][j].x, grid[i][j].y, SQUARE_SIZE, SQUARE_SIZE))
            grid[i][j].alive = grid[i][j].nextAlive
    
    running = True
    while running:
        pElapsed = elapsed
        elapsed = pygame.time.get_ticks()
        counter += elapsed - pElapsed
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
        if counter > 400: # Runs every 0.4 seconds
            for i in range(NO_VERTICAL_SQUARES):
                for j in range(NO_HORIZONTAL_SQUARES):
                    if grid[i][j].nextAlive:
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(grid[i][j].x, grid[i][j].y, SQUARE_SIZE, SQUARE_SIZE))
                    else:
                        pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(grid[i][j].x, grid[i][j].y, SQUARE_SIZE, SQUARE_SIZE))
                    grid[i][j].alive = grid[i][j].nextAlive
                    
            for i in range(NO_VERTICAL_SQUARES):
                for j in range(NO_HORIZONTAL_SQUARES):
                    grid[i][j].die(grid)
            counter = 0
        
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()