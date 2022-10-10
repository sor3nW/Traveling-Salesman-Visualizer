import random
from collections import deque
import pygame
from queue import PriorityQueue
import time

pygame.init()
screenWidth = 500
screen = pygame.display.set_mode((screenWidth, 750))
num = 25
diff = screenWidth // num
font = pygame.font.SysFont("comicsans", 20)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
GREY = (200,200,200)


class Box:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.color = WHITE
        self.maxRows = num
        self.neighbors = []
        self.neighborCount = 0
    def get_pos(self):
        return self.row, self.col

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.row * diff, self.col * diff, diff + 1, diff + 1))

    def update_neighbors(self, grid):
        self.neighbors = []
        directions = [[0,1],[1,1], [1,0],[0,-1], [-1,-1],[0,-1],[1,-1]]
        for i, j in directions:
            r, c = self.row + i, self.col + j
            if (
                    0 <= r < self.maxRows
                    and 0 <= c < self.maxRows
                    and grid[r][c].color != WHITE
            ):
                self.neighbors.append(grid[r][c])
                self.neighborCount +=1








def fillrandom(grid):
    num1 = random.randint(0, num-1)
    num2 = random.randint(0, num-1)
    if grid[num1][num2].color == PURPLE:
        return None
    else:
        grid[num1][num2].color = PURPLE
        return grid[num1][num2]

def drawBoxes(grid):
    for row in grid:
        for box in row:
            box.draw()


def draw(grid, nodes, minimum, percent):
    screen.fill(WHITE)
    drawBoxes(grid)
    drawLines(nodes)
    pygame.draw.line(screen, BLACK, (0, screenWidth), (screenWidth, screenWidth))
    text1 = font.render("percent finished: ", False, BLACK)
    text2 = font.render("minimum distance: ", False, BLACK)
    screen.blit(text1, (100, screenWidth+100))
    screen.blit(text2, (100, screenWidth+50))
    text3 = font.render(f"{minimum}", False, BLACK)
    format_float = "{:.2f}".format(percent)
    text4 = font.render(f"{format_float}", False, BLACK)
    screen.blit(text3, (300, screenWidth+50))
    screen.blit(text4, (300, screenWidth+100))
    pygame.display.flip()


def get_pos(x, y):
    newx = x // diff
    newy = y // diff
    return newx, newy


def gridAndNeighbors():
    grid = [[] for j in range(num)]
    for i in range(num):
        for j in range(num):
            box = Box(i, j)
            grid[i].append(box)

    return grid

def heuristic(p1, p2):
    x1, y1 = p1.get_pos()
    x2, y2 = p2.get_pos()
    return abs(x1 - x2) + abs(y1 - y2)

def drawLines(nodes):
    for i in range(len(nodes)-1):
        pygame.draw.line(screen, PURPLE, (nodes[i].row * diff + (diff/2), nodes[i].col * diff + diff/2), (nodes[i+1].row * diff + diff/2, nodes[i+1].col * diff + diff/2), 10)
def calcTotalDistance(nodes):
    total = 0
    for i in range(len(nodes)-1):
        distance = heuristic(nodes[i],  nodes[i+1])
        total += distance
    return total
def factorial(num):
    if num in [0,1]:
        return 1
    else:
        return num * factorial(num-1)

def TSP(nodes, count, minimum):
    percentage = (count / factorial(len(nodes))) * 100
    total = factorial(len(nodes))
    dist = calcTotalDistance(nodes)
    newNodes = [0 for i in range(len(nodes))]
    for i in range(len(nodes)):
        newNodes[i+1] = nodes[i]
        newNodes[:i] = nodes[:i]
        newNodes[i:] = nodes[i:]








grid = gridAndNeighbors()
percentage = 0
minimumDistance = float("inf")
nodes = []
ready = True
flag2 = False
flag1 = False
let = None
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_r:
                grid = gridAndNeighbors()
                ready = True
                nodes = []
                minimumDistance = float("inf")
                percentage = 0

            if event.key == pygame.K_1 and ready:
                count =  0
                while count < 5:
                    node = fillrandom(grid)
                    if node:
                        count += 1
                        nodes.append(node)
                ready = False



            if event.key == pygame.K_RETURN:
                flag1 = True






        if event.type == pygame.MOUSEBUTTONDOWN:
            pass



    draw(grid, nodes, minimumDistance, percentage)
    if flag1:
        count = 1
        percentage, dist = TSP(nodes, count)
        count += 1
        minimumDistance = min(dist, minimumDistance)


        flag1 = False

pygame.quit()
