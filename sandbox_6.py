from math import *
from random import *
from time import sleep
import threading
import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

blocksPW = 160
moveAmount = 5
renderSpeed = 30
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("simulation")

numOfCells = blocksPW*blocksPW
grid = [None]*numOfCells
area1, area2, area3, area4 = [], [], [], []
area5, area6, area7, area8 = [], [], [], []
area9, area10, area11, area12 = [], [], [], []
area13, area14, area15, area16 = [], [], [], []
areas = [[]]*16
areaCount = 0
numOfElements = 0


class block:
    def __init__(self, x_, y_, type_):
        global areaCount
        self.x = x_
        self.y = y_
        self.type = type_
        self.square = pygame.Rect(
            x_*moveAmount, y_*moveAmount, moveAmount, moveAmount)

        z = randint(0, 1)
        areaCount += 1

        if areaCount == 1:
            area1.append(list((self.y, self.x, z)))
        elif areaCount == 2:
            area2.append(list((self.y, self.x, z)))
        elif areaCount == 3:
            area3.append(list((self.y, self.x, z)))
        elif areaCount == 4:
            area4.append(list((self.y, self.x, z)))
        elif areaCount == 5:
            area5.append(list((self.y, self.x, z)))
        elif areaCount == 6:
            area6.append(list((self.y, self.x, z)))
        elif areaCount == 7:
            area7.append(list((self.y, self.x, z)))
        elif areaCount == 8:
            area8.append(list((self.y, self.x, z)))
        elif areaCount == 9:
            area9.append(list((self.y, self.x, z)))
        elif areaCount == 10:
            area10.append(list((self.y, self.x, z)))
        elif areaCount == 11:
            area11.append(list((self.y, self.x, z)))
        elif areaCount == 12:
            area12.append(list((self.y, self.x, z)))
        elif areaCount == 13:
            area13.append(list((self.y, self.x, z)))
        elif areaCount == 14:
            area14.append(list((self.y, self.x, z)))
        elif areaCount == 15:
            area15.append(list((self.y, self.x, z)))
        else:
            area16.append(list((self.y, self.x, z)))
            areaCount = 0

    def render(self):
        self.square.x = self.x*moveAmount
        self.square.y = self.y*moveAmount
        if self.type == "sand":
            pygame.draw.rect(screen, (255, 200, 0), self.square)
        elif self.type == "water":
            pygame.draw.rect(screen, (0, 0, 255), self.square)
        else:
            pygame.draw.rect(screen, (200, 200, 200), self.square)


class button:
    def __init__(self, pos_, rgb_, size_, type_, function_):
        self.x, self.y = pos_[0], pos_[1]
        self.width, self.height = size_[0], size_[1]
        self.rgb = rgb_
        self.type = type_
        self.function = function_
        self.square = pygame.Rect(self.x, self.y, self.width, self.height)

    def test(self, event, selected, can):
        bg = pygame.Rect(self.x-5, self.y-5, self.width+10, self.height+10)
        pygame.draw.rect(screen, (0, 0, 0), bg)
        if self.x <= event[0] <= self.x+self.width and self.y <= event[1] <= self.y+self.height and can and self.function != None:
            self.function()
        if selected == self.type:
            new = pygame.Rect(self.x-2, self.y-2, self.width+4, self.height+4)
            pygame.draw.rect(screen, (255, 0, 0), new)
            pygame.draw.rect(screen, self.rgb, self.square)
            return selected

        if self.x <= event[0] <= self.x+self.width and self.y <= event[1] <= self.y+self.height and can:
            pygame.draw.rect(screen, self.rgb, self.square)
            selected = self.type

        if self.x <= event[0] <= self.x+self.width and self.y <= event[1] <= self.y+self.height:
            new = pygame.Rect(self.x-2, self.y-2, self.width+4, self.height+4)
            pygame.draw.rect(screen, self.rgb, new)
            return selected

        pygame.draw.rect(screen, self.rgb, self.square)
        return selected


def deleting(event):
    global numOfElements
    if event[0] >= screen_width-moveAmount or event[0] <= moveAmount or event[1] >= screen_height-moveAmount or event[1] <= 1:
        return
    x, y = floor(event[0]/moveAmount), floor(event[1]/moveAmount)
    grid[y*blocksPW + x] = None
    grid[(y-1)*blocksPW + x-1] = None
    grid[(y-1)*blocksPW + x] = None
    grid[(y-1)*blocksPW + x+1] = None
    grid[y*blocksPW + x-1] = None
    grid[y*blocksPW + x+1] = None
    grid[(y+1)*blocksPW + x-1] = None
    grid[(y+1)*blocksPW + x] = None
    grid[(y+1)*blocksPW + x+1] = None
    numOfElements -= 1


def create(event, type):
    global numOfElements
    if event[0] >= screen_width or event[0] <= 0 or event[1] >= screen_height or event[1] <= 0:
        return
    x, y = floor(event[0]/moveAmount), floor(event[1]/moveAmount)
    if grid[y*blocksPW + x] == None:
        new = block(x, y, type)
        grid[y*blocksPW + x] = new
        numOfElements += 1
        print("elements: ", numOfElements)


def createBall(event, type):
    create(event, type)
    create((event[0]+moveAmount, event[1]), type)
    create((event[0]-moveAmount, event[1]), type)
    create((event[0], event[1]+moveAmount), type)
    create((event[0], event[1]-moveAmount), type)
    create((event[0]-moveAmount, event[1]-moveAmount), type)
    create((event[0]+moveAmount, event[1]-moveAmount), type)
    create((event[0]-moveAmount, event[1]+moveAmount), type)
    create((event[0]+moveAmount, event[1]+moveAmount), type)
    create((event[0]-moveAmount*2, event[1]), type)
    create((event[0]-moveAmount*2, event[1]+moveAmount), type)
    create((event[0]-moveAmount*2, event[1]-moveAmount), type)
    create((event[0]+moveAmount*2, event[1]), type)
    create((event[0]+moveAmount*2, event[1]+moveAmount), type)
    create((event[0]+moveAmount*2, event[1]-moveAmount), type)
    create((event[0], event[1]+moveAmount*2), type)
    create((event[0]-moveAmount, event[1]+moveAmount*2), type)
    create((event[0]+moveAmount, event[1]+moveAmount*2), type)
    create((event[0], event[1]-moveAmount*2), type)
    create((event[0]-moveAmount, event[1]-moveAmount*2), type)
    create((event[0]+moveAmount, event[1]-moveAmount*2), type)


def moveSand(i):
    y = floor(i[0]*blocksPW)
    y1 = floor((i[0]+1)*blocksPW)
    x = floor(i[1])

    if i[0] >= blocksPW-1:
        return i

    if grid[y1 + x] == None:
        grid[y1 + x] = grid[y + x]
        grid[y + x] = None
        grid[y1 + x].y += moveAmount
        i[0] += 1
        return i
    if grid[y1 + x].type == "water":
        move = grid[y1 + x]
        grid[y1 + x] = grid[y + x]
        grid[y + x] = move
        grid[y1 + x].y += moveAmount
        grid[y + x].y -= moveAmount
        return i
    if x != 0:
        if grid[y1 + x-1] == None:
            grid[y1 + x-1] = grid[y + x]
            grid[y + x] = None
            grid[y1 + x-1].y += moveAmount
            grid[y1 + x-1].x -= moveAmount
            i[0] += 1
            i[1] -= 1
            return i
        if grid[y1 + x-1].type == "water":
            move = grid[y1 + x-1]
            grid[y1 + x-1] = grid[y + x]
            grid[y + x] = move
            grid[y1 + x-1].y += moveAmount
            grid[y1 + x-1].x -= moveAmount
            grid[y + x].y -= moveAmount
            grid[y + x].x += moveAmount
            return i
    if y1 + x+1 >= numOfCells or x == blocksPW-1:
        return i
    if grid[y1 + x+1] == None:
        grid[y1 + x+1] = grid[y + x]
        grid[y + x] = None
        grid[y1 + x+1].y += moveAmount
        grid[y1 + x+1].x += moveAmount
        i[0] += 1
        i[1] += 1
        return i
    if grid[y1 + x+1].type == "water":
        move = grid[y1 + x+1]
        grid[y1 + x+1] = grid[y + x]
        grid[y + x] = move
        grid[y1 + x+1].y += moveAmount
        grid[y1 + x+1].x += moveAmount
        grid[y + x].y -= moveAmount
        grid[y + x].x -= moveAmount
        return i
    return i


def moveWater(i):
    y = floor(i[0]*blocksPW)
    y1 = floor((i[0]+1)*blocksPW)
    x = floor(i[1])

    if i[0] >= blocksPW-1:
        if grid[y + x-1] == None and x != 0 and i[2] == 0:
            grid[y + x-1] = grid[y + x]
            grid[y + x] = None
            grid[y + x-1].x -= moveAmount
            i[1] -= 1
            return i
        i[2] = 1
        if y + x+1 >= numOfCells:
            i[2] = 0
            return i
        if grid[y + x+1] == None and x != blocksPW-1:
            grid[y + x+1] = grid[y + x]
            grid[y + x] = None
            grid[y + x+1].x += moveAmount
            i[1] += 1
            return i
        i[2] = 0
        return i

    if grid[y1 + x] == None:
        grid[y1 + x] = grid[y + x]
        grid[y + x] = None
        grid[y1 + x].y += moveAmount
        i[0] += 1
        i[2] = randint(0, 1)
        return i
    if grid[y1 + x-1] == None and x != 0:
        grid[y1 + x-1] = grid[y + x]
        grid[y + x] = None
        grid[y1 + x-1].y += moveAmount
        grid[y1 + x-1].x -= moveAmount
        i[0] += 1
        i[1] -= 1
        return i
    if y1 + x+1 >= numOfCells:
        return i
    if grid[y1 + x+1] == None and x != blocksPW-1:
        grid[y1 + x+1] = grid[y + x]
        grid[y + x] = None
        grid[y1 + x+1].y += moveAmount
        grid[y1 + x+1].x += moveAmount
        i[0] += 1
        i[1] += 1
        return i
    if grid[y + x-1] == None and x != 0 and i[2] == 0:
        grid[y + x-1] = grid[y + x]
        grid[y + x] = None
        grid[y + x-1].x -= moveAmount
        i[1] -= 1
        return i
    i[2] = 1
    if y + x+1 >= numOfCells:
        i[2] = 0
        return i
    if grid[y + x+1] == None and x != blocksPW-1:
        grid[y + x+1] = grid[y + x]
        grid[y + x] = None
        grid[y + x+1].x += moveAmount
        i[1] += 1
        return i
    i[2] = 0
    return i


def render(arr):
    for i in arr:
        pos = i[0]*blocksPW + i[1]
        #print(blocksPW, pos, len(grid))
        if pos > len(grid):
            return
        if grid[pos] == None:
            arr.remove(i)
            continue
        if grid[pos].type == "water":
            i = moveWater(i)
            grid[i[0]*blocksPW + i[1]].x = i[1]
            grid[i[0]*blocksPW + i[1]].y = i[0]
        elif grid[pos].type == "sand":
            i = moveSand(i)
            grid[i[0]*blocksPW + i[1]].x = i[1]
            grid[i[0]*blocksPW + i[1]].y = i[0]
        grid[i[0]*blocksPW + i[1]].render()


def mainRender():
    thread1 = threading.Thread(target=render(area1))
    thread2 = threading.Thread(target=render(area2))
    thread3 = threading.Thread(target=render(area3))
    thread4 = threading.Thread(target=render(area4))
    thread5 = threading.Thread(target=render(area5))
    thread6 = threading.Thread(target=render(area6))
    thread7 = threading.Thread(target=render(area7))
    thread8 = threading.Thread(target=render(area8))
    thread9 = threading.Thread(target=render(area9))
    thread10 = threading.Thread(target=render(area10))
    thread11 = threading.Thread(target=render(area11))
    thread12 = threading.Thread(target=render(area12))
    thread13 = threading.Thread(target=render(area13))
    thread14 = threading.Thread(target=render(area14))
    thread15 = threading.Thread(target=render(area15))
    thread16 = threading.Thread(target=render(area16))
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()
    thread11.start()
    thread12.start()
    thread13.start()
    thread14.start()
    thread15.start()
    thread16.start()


def reset():
    global grid, allSand, allWater, allStone
    global numOfElements, deleting
    numOfCells = blocksPW*blocksPW
    grid = [None]*numOfCells
    area1, area2, area3, area4 = [], [], [], []
    rea5, area6, area7, area8 = [], [], [], []
    rea9, area10, area11, area12 = [], [], [], []
    rea13, area14, area15, area16 = [], [], [], []
    numOfElements = 0
    deleting = False


def main():
    sand_button = button([760, 20], (255, 200, 0), [20, 20], "sand", None)
    water_button = button([760, 50], (0, 0, 255), [20, 20], "water", None)
    stone_button = button([760, 80], (200, 200, 200), [20, 20], "stone", None)
    delete_button = button([20, 20], (200, 0, 0), [20, 20], "delete", None)
    reset_button = button([50, 20], (240, 240, 240), [20, 20], "", reset)
    selected = ""

    while True:
        # print(len(area1), len(area2), len(area3), len(area4), len(area5), len(area6), len(area7), len(area8), len(
        #    area9), len(area10), len(area11), len(area12), len(area13), len(area14), len(area15), len(area16))
        clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True

            if pygame.mouse.get_pressed()[0] == True and not clicked:
                if selected == "sand":
                    createBall(pygame.mouse.get_pos(), "sand")
                if selected == "water":
                    createBall(pygame.mouse.get_pos(), "water")
                if selected == "stone":
                    createBall(pygame.mouse.get_pos(), "stone")
                if selected == "delete":
                    deleting(pygame.mouse.get_pos())
        screen.fill((30, 30, 30))

        mainRender()

        mouse = pygame.mouse.get_pos()
        selected = sand_button.test(mouse, selected, clicked)
        selected = water_button.test(mouse, selected, clicked)
        selected = stone_button.test(mouse, selected, clicked)
        selected = delete_button.test(mouse, selected, clicked)
        reset_button.test(mouse, None, clicked)

        pygame.display.flip()
        clock.tick(renderSpeed)


main()