from random import *
from math import floor, sqrt
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


class block:
    def __init__(self, x, y, type, color, staticColor, colorVariant, liquid, flamable, lifetime):
        global areaCount
        self.x = x
        self.y = y
        self.type = type
        self.color = list(color)
        self.staticColor = staticColor
        self.colorVariant = list(colorVariant)
        self.liquid = liquid
        self.flamable = flamable
        self.lifetime = lifetime
        self.square = pygame.Rect(
            x*moveAmount, y*moveAmount, moveAmount, moveAmount)
        if self.lifetime != None:
            arr = list(lifetime)
            self.lifetime = floor((randint(arr[0], arr[1])/arr[2])*renderSpeed)
        if self.staticColor:
            r, g, b = 0, 0, 0
            if len(self.colorVariant) != 3:
                if self.color[0] != 0:
                    r = self.color[0]-randint(0, self.colorVariant[0])
                if self.color[1] != 0:
                    g = self.color[1]-randint(0, self.colorVariant[0])
                if self.color[2] != 0:
                    b = self.color[2]-randint(0, self.colorVariant[0])
            else:
                r = self.color[0]-randint(0, self.colorVariant[0])
                g = self.color[1]-randint(0, self.colorVariant[1])
                b = self.color[2]-randint(0, self.colorVariant[2])
            self.color = (r, g, b)

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
        if self.lifetime == 0:
            grid[self.y*blocksPW + self.x] = None
            return
        if self.lifetime != None:
            self.lifetime -= 1
        self.square.x = self.x*moveAmount
        self.square.y = self.y*moveAmount
        if self.staticColor:
            pygame.draw.rect(screen, self.color, self.square)
        else:
            if len(self.colorVariant) != 3:
                if self.color[0] != 0:
                    r = self.color[0]-randint(0, self.colorVariant[0])
                if self.color[1] != 0:
                    g = self.color[1]-randint(0, self.colorVariant[0])
                if self.color[2] != 0:
                    b = self.color[2]-randint(0, self.colorVariant[0])
            else:
                r = self.color[0]-randint(0, self.colorVariant[0])
                g = self.color[1]-randint(0, self.colorVariant[1])
                b = self.color[2]-randint(0, self.colorVariant[2])
            pygame.draw.rect(screen, (r, g, b), self.square)


class PMbutton:
    def __init__(self, pos, size, type):
        self.x, self.y = pos[0], pos[1]
        self.width, self.height = size[0], size[1]
        self.type = type
        self.rgb = (255, 255, 255)
        self.square = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.type == "sub":
            font = pygame.font.SysFont(None, 70)
            self.text = font.render('-', True, self.rgb)
        if self.type == "add":
            font = pygame.font.SysFont(None, 70)
            self.text = font.render('+', True, self.rgb)

    def test(self, event, r, can):
        bg = pygame.Rect(self.x-5, self.y-5, self.width+10, self.height+10)
        pygame.draw.rect(screen, (0, 0, 0), bg)

        if self.x <= event[0] <= self.x+self.width and self.y <= event[1] <= self.y+self.height and can:
            if r >= 1 and self.type == "sub":
                r -= 1
            elif self.type == "add":
                r += 1

        if self.x <= event[0] <= self.x+self.width and self.y <= event[1] <= self.y+self.height:
            new = pygame.Rect(self.x-2, self.y-2, self.width+4, self.height+4)
            pygame.draw.rect(screen, (100, 100, 100), new)

        if self.type == "sub":
            screen.blit(self.text, (self.x+2, self.y-16))
            return r
        screen.blit(self.text, (self.x-4, self.y-18))
        return r


class button:
    def __init__(self, pos, rgb, size, type, function):
        self.x, self.y = pos[0], pos[1]
        self.width, self.height = size[0], size[1]
        self.rgb = rgb
        self.type = type
        self.function = function
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


def create(event, type, color, staticColor, colorVariant, liquid, flamable, lifetime):
    if event[0] >= screen_width or event[0] <= 0 or event[1] >= screen_height or event[1] <= 0:
        return
    #x, y = floor(event[0]/moveAmount), floor(event[1]/moveAmount)
    x, y = event[0], event[1]
    if x <= 0 or y <= 0 or x >= blocksPW or y >= blocksPW:
        return
    if grid[y*blocksPW + x] == None:
        grid[y*blocksPW + x] = block(x, y, type, color, staticColor,
                                     colorVariant, liquid, flamable, lifetime)


def createBallNew(event, r, type, color, staticColor, colorVariant, liquid, flamable, lifetime):
    x, y = floor(event[0]/moveAmount), floor(event[1]/moveAmount)
    for i in range(-r, r+1):
        for ii in range(-r, r+1):
            if sqrt(ii*ii + i*i) <= r:
                create((x+ii, y+i), type, color,
                       staticColor, colorVariant, liquid, flamable, lifetime)


def createBall(event, type, color, staticColor, colorVariant, liquid, flamable, lifetime):
    create(event, type, color, staticColor,
           colorVariant, liquid, flamable, lifetime)
    create((event[0]+moveAmount, event[1]), type, color,
           staticColor, colorVariant, liquid, flamable, lifetime)
    create((event[0]-moveAmount, event[1]), type, color,
           staticColor, colorVariant, liquid, flamable, lifetime)
    create((event[0], event[1]+moveAmount), type, color,
           staticColor, colorVariant, liquid, flamable, lifetime)
    create((event[0], event[1]-moveAmount), type, color,
           staticColor, colorVariant, liquid, flamable, lifetime)
    create((event[0]-moveAmount, event[1]-moveAmount), type, color,
           staticColor, colorVariant, liquid, flamable, lifetime)
    create((event[0]+moveAmount, event[1]-moveAmount), type, color,
           staticColor, colorVariant, liquid, flamable, lifetime)
    create((event[0]-moveAmount, event[1]+moveAmount), type, color,
           staticColor, colorVariant, liquid, flamable, lifetime)
    create((event[0]+moveAmount, event[1]+moveAmount), type, color,
           staticColor, colorVariant, liquid, flamable, lifetime)
    create((event[0]-moveAmount*2, event[1]), type, color,
           staticColor, colorVariant, liquid, flamable, lifetime)
    create((event[0]-moveAmount*2, event[1]+moveAmount), type,
           color, staticColor, colorVariant, liquid, flamable, lifetime)
    create((event[0]-moveAmount*2, event[1]-moveAmount), type,
           color, staticColor, colorVariant, liquid, flamable, lifetime)
    create((event[0]+moveAmount*2, event[1]), type, color,
           staticColor, colorVariant, liquid, flamable, lifetime)
    create((event[0]+moveAmount*2, event[1]+moveAmount), type,
           color, staticColor, colorVariant, liquid, flamable, lifetime)
    create((event[0]+moveAmount*2, event[1]-moveAmount), type,
           color, staticColor, colorVariant, liquid, flamable, lifetime)
    create((event[0], event[1]+moveAmount*2), type, color,
           staticColor, colorVariant, liquid, flamable, lifetime)
    create((event[0]-moveAmount, event[1]+moveAmount*2), type,
           color, staticColor, colorVariant, liquid, flamable, lifetime)
    create((event[0]+moveAmount, event[1]+moveAmount*2), type,
           color, staticColor, colorVariant, liquid, flamable, lifetime)
    create((event[0], event[1]-moveAmount*2), type, color,
           staticColor, colorVariant, liquid, flamable, lifetime)
    create((event[0]-moveAmount, event[1]-moveAmount*2), type,
           color, staticColor, colorVariant, liquid, flamable, lifetime)
    create((event[0]+moveAmount, event[1]-moveAmount*2), type,
           color, staticColor, colorVariant, liquid, flamable, lifetime)


def switch(pos1, pos2, val1, val2, i, sub1, sub2,):
    global grid
    grid[pos1] = val2
    grid[pos2] = val1
    i[0] += sub1
    i[1] += sub2
    return i


def moveSand(i):
    y = floor(i[0]*blocksPW)
    y1 = floor((i[0]+1)*blocksPW)
    y2 = floor((i[0]+2)*blocksPW)
    x = floor(i[1])

    if i[0] >= blocksPW-1:
        return i

    if grid[y1 + x] == None:
        if i[0] < blocksPW-2:
            if grid[y2 + x] == None:
                return switch(y + x, y2 + x, grid[y + x], None, i, 2, 0)
        return switch(y + x, y1 + x, grid[y + x], None, i, 1, 0)
    if grid[y1 + x].liquid:
        return switch(y + x, y1 + x, grid[y + x], grid[y1 + x], i, 0, 0)
    if x != 0:
        if grid[y1 + x-1] == None:
            return switch(y + x, y1 + x-1, grid[y + x], None, i, 1, -1)
        if grid[y1 + x-1].liquid:
            return switch(y + x, y1 + x-1, grid[y + x], grid[y1 + x-1], i, 0, 0)
    if y1 + x+1 >= numOfCells or x == blocksPW-1:
        return i
    if grid[y1 + x+1] == None:
        return switch(y + x, y1 + x+1, grid[y + x], None, i, 1, 1)
    if grid[y1 + x+1].liquid:
        return switch(y + x, y1 + x+1, grid[y + x], grid[y1 + x+1], i, 0, 0)
    return i


def moveWater(i):
    y = floor(i[0]*blocksPW)
    y1 = floor((i[0]+1)*blocksPW)
    y2 = floor((i[0]+2)*blocksPW)
    x = floor(i[1])

    if i[0] >= blocksPW-1:
        if grid[y + x-1] == None and x != 0 and i[2] == 0:
            return switch(y + x, y + x-1, grid[y + x], None, i, 0, -1)
        i[2] = 1
        if y + x+1 >= numOfCells:
            i[2] = 0
            return i
        if grid[y + x+1] == None and x != blocksPW-1:
            return switch(y + x, y + x+1, grid[y + x], None, i, 0, +1)
        i[2] = 0
        return i

    if grid[y1 + x] == None:
        i[2] = randint(0, 1)
        if i[0] < blocksPW-2:
            if grid[y2 + x] == None:
                return switch(y + x, y2 + x, grid[y + x], None, i, 2, 0)
        return switch(y + x, y1 + x, grid[y + x], None, i, 1, 0)
    if grid[y1 + x-1] == None and x != 0:
        return switch(y + x, y1 + x-1, grid[y + x], None, i, 1, -1)
    if y1 + x+1 >= numOfCells:
        return i
    if grid[y1 + x+1] == None and x != blocksPW-1:
        return switch(y + x, y1 + x+1, grid[y + x], None, i, 1, 1)
    if grid[y + x-1] == None and x != 0 and i[2] == 0:
        return switch(y + x, y + x-1, grid[y + x], None, i, 0, -1)
    i[2] = 1
    if y + x+1 >= numOfCells:
        i[2] = 0
        return i
    if grid[y + x+1] == None and x != blocksPW-1:
        return switch(y + x, y + x+1, grid[y + x], None, i, 0, 1)
    i[2] = 0
    return i


def moveAcid(i):
    y = floor(i[0]*blocksPW)
    y1 = floor((i[0]+1)*blocksPW)
    y2 = floor((i[0]+2)*blocksPW)
    ym1 = floor((i[0]-1)*blocksPW)
    x = floor(i[1])

    if randint(1, 20) != 1:
        return moveWater(i)
    smoke = block(x, y, "smoke", (100, 100, 100),
                  False, (20,), True, False, None)
    if i[0] >= blocksPW-1:
        if x != 0 and i[2] == 0 and grid[y + x-1] != None:
            if grid[y + x-1].type != "acid" and grid[y + x-1].type != "smoke":
                return switch(y + x, y + x-1, smoke, None, i, 0, -1)
        i[2] = 1
        if y + x+1 >= numOfCells:
            i[2] = 0
            return i
        if x != blocksPW-1 and grid[y + x+1] != None:
            if grid[y + x+1].type != "acid" and grid[y + x+1].type != "smoke":
                return switch(y + x, y + x+1, smoke, None, i, 0, 1)
        i[2] = 0
        return i

    if grid[y1 + x] != None:
        if grid[y1 + x].type != "acid" and grid[y1 + x].type != "smoke":
            i[2] = randint(0, 1)
            return switch(y + x, y1 + x, smoke, None, i, 1, 0)
    if x != 0 and grid[y1 + x-1] != None:
        if grid[y1 + x-1].type != "acid" and grid[y1 + x-1].type != "smoke":
            return switch(y + x, y1 + x-1, smoke, None, i, 1, -1)
    if y1 + x+1 >= numOfCells:
        return i
    if x != blocksPW-1 and grid[y1 + x+1] != None:
        if grid[y1 + x+1].type != "acid" and grid[y1 + x+1].type != "smoke":
            return switch(y + x, y1 + x+1, smoke, None, i, 1, 1)
    if x != 0 and i[2] == 0 and grid[y + x-1] != None:
        if grid[y + x-1].type != "acid" and grid[y + x-1].type != "smoke":
            return switch(y + x, y + x-1, smoke, None, i, 0, -1)
    i[2] = 1
    if y + x+1 >= numOfCells:
        i[2] = 0
        return i
    if x != blocksPW-1 and grid[y + x+1] != None:
        if grid[y + x+1].type != "acid" and grid[y + x+1].type != "smoke":
            return switch(y + x, y + x+1, smoke, None, i, 0, 1)

    if x != blocksPW-1 and grid[ym1 + x] != None:
        if grid[ym1 + x].type != "acid" and grid[ym1 + x].type != "smoke":
            return switch(y + x, ym1 + x, smoke, None, i, -1, 0)
    if x != 0 and grid[ym1 + x-1] != None:
        if grid[ym1 + x-1].type != "acid" and grid[ym1 + x-1].type != "smoke":
            return switch(y + x, ym1 + x-1, smoke, None, i, -1, -1)
    if y1 + x+1 >= numOfCells:
        return i
    if x != blocksPW-1 and grid[ym1 + x+1] != None:
        if grid[ym1 + x+1].type != "acid" and grid[ym1 + x+1].type != "smoke":
            return switch(y + x, ym1 + x+1, smoke, None, i, -1, 1)

    i[2] = 0
    return i


def moveFire(i):
    y = floor(i[0]*blocksPW)
    y1 = floor((i[0]+1)*blocksPW)
    ym1 = floor((i[0]-1)*blocksPW)
    x = floor(i[1])

    smoke = block(x, y, "smoke", (100, 100, 100),
                  False, (20,), True, False, None)
    if i[0] < blocksPW-1:
        if grid[y1 + x] != None:
            if randint(1, 100) <= grid[y1 + x].flamable:
                fire = block(x, y, "fire", (255, 180, 0), False,
                             (0, 110, 0), False, False, (100, 200, 100))
                i = switch(y + x, y1 + x, fire, smoke, i, 0, 0)
        if x != 0 and grid[y1 + x-1] != None:
            if randint(1, 100) <= grid[y1 + x-1].flamable:
                fire = block(x, y, "fire", (255, 180, 0), False,
                             (0, 110, 0), False, False, (100, 200, 100))
                i = switch(y + x, y1 + x-1, fire, smoke, i, 0, 0)
        if y1 + x+1 >= numOfCells:
            return i
        if x != blocksPW-1 and grid[y1 + x+1] != None:
            if randint(1, 100) <= grid[y1 + x+1].flamable:
                fire = block(x, y, "fire", (255, 180, 0), False,
                             (0, 110, 0), False, False, (100, 200, 100))
                i = switch(y + x, y1 + x+1, fire, smoke, i, 0, 0)
    if x != 0 and grid[y + x-1] != None:
        if randint(1, 100) <= grid[y + x-1].flamable:
            fire = block(x, y, "fire", (255, 180, 0), False,
                         (0, 110, 0), False, False, (100, 200, 100))
            i = switch(y + x, y + x-1, fire, smoke, i, 0, 0)
    if y + x+1 >= numOfCells:
        return i
    if x != blocksPW-1 and grid[y + x+1] != None:
        if randint(1, 100) <= grid[y + x+1].flamable:
            fire = block(x, y, "fire", (255, 180, 0), False,
                         (0, 110, 0), False, False, (100, 200, 100))
            i = switch(y + x, y + x+1, fire, smoke, i, 0, 0)

    if x != blocksPW-1 and grid[ym1 + x] != None:
        if randint(1, 100) <= grid[ym1 + x].flamable:
            fire = block(x, y, "fire", (255, 180, 0), False,
                         (0, 110, 0), False, False, (100, 200, 100))
            i = switch(y + x, ym1 + x, fire, smoke, i, 0, 0)
    if x != 0 and grid[ym1 + x-1] != None:
        if randint(1, 100) <= grid[ym1 + x-1].flamable:
            fire = block(x, y, "fire", (255, 180, 0), False,
                         (0, 110, 0), False, False, (100, 200, 100))
            i = switch(y + x, ym1 + x-1, fire, smoke, i, 0, 0)
    if y1 + x+1 >= numOfCells:
        return i
    if x != blocksPW-1 and grid[ym1 + x+1] != None:
        if randint(1, 100) <= grid[ym1 + x+1].flamable:
            fire = block(x, y, "fire", (255, 180, 0), False,
                         (0, 110, 0), False, False, (100, 200, 100))
            i = switch(y + x, ym1 + x+1, fire, smoke, i, 0, 0)
    if randint(1, 10) == 1:
        return moveWater(i)
    return i


def moveSmoke(i):
    y = floor(i[0]*blocksPW)
    y1 = floor((i[0]-1)*blocksPW)
    y2 = floor((i[0]-2)*blocksPW)
    x = floor(i[1])

    if i[0] <= 0:
        if grid[y + x].lifetime == None:
            grid[y + x].lifetime = floor(randint(50, 250)/100*renderSpeed)
            return i
        if grid[y + x-1] == None and x != 0 and i[2] == 0:
            return switch(y + x, y + x-1, grid[y + x], None, i, 0, -1)
        i[2] = 1
        if y + x+1 >= numOfCells:
            i[2] = 0
            return i
        if grid[y + x+1] == None and x != blocksPW-1:
            return switch(y + x, y + x+1, grid[y + x], None, i, 0, 1)
        i[2] = 0
        return i

    if grid[y1 + x] == None:
        i[2] = randint(0, 1)
        if i[0] > 2:
            if grid[y2 + x] == None:
                return switch(y + x, y2 + x, grid[y + x], None, i, -2, 0)
        return switch(y + x, y1 + x, grid[y + x], None, i, -1, 0)

    if grid[y1 + x].liquid and grid[y1 + x].type != "smoke":
        return switch(y + x, y1 + x, grid[y + x], grid[y1 + x], i, 0, 0)
    if grid[y1 + x-1] == None and x != 0:
        return switch(y + x, y1 + x-1, grid[y + x], None, i, -1, -1)
    if x != 0:
        if grid[y1 + x-1].liquid and grid[y1 + x-1].type != "smoke":
            return switch(y + x, y1 + x-1, grid[y + x], grid[y1 + x-1], i, 0, 0)
    if y1 + x+1 >= numOfCells:
        return i
    if grid[y1 + x+1] == None and x != blocksPW-1:
        return switch(y + x, y1 + x+1, grid[y + x], None, i, -1, 1)
    if x != blocksPW-1:
        if grid[y1 + x+1].liquid and grid[y1 + x+1].type != "smoke":
            return switch(y + x, y1 + x+1, grid[y + x], grid[y1 + x+1], i, 0, 0)
    if grid[y + x-1] == None and x != 0 and i[2] == 0:
        return switch(y + x, y + x-1, grid[y + x], None, i, 0, -1)
    i[2] = 1
    if y + x+1 >= numOfCells:
        i[2] = 0
        return i
    if grid[y + x+1] == None and x != blocksPW-1:
        return switch(y + x, y + x+1, grid[y + x], None, i, 0, 1)

    i[2] = 0
    return i


def render(arr):
    for i in arr:
        pos = i[0]*blocksPW + i[1]
        if pos >= len(grid):
            arr.remove(i)
            continue
        if grid[pos] == None:
            arr.remove(i)
            # print("elements: ", len(area1)+len(area2)+len(area3)+len(area4)+len(area5)+len(area6)+len(area7) +
            #      len(area8)+len(area9)+len(area10)+len(area11)+len(area12)+len(area13)+len(area14)+len(area15)+len(area16))
            continue
        if grid[pos].type == "water" or grid[pos].type == "oil":
            i = moveWater(i)
        elif grid[pos].type == "sand":
            i = moveSand(i)
        elif grid[pos].type == "smoke":
            i = moveSmoke(i)
        elif grid[pos].type == "acid":
            i = moveAcid(i)
        elif grid[pos].type == "fire":
            i = moveFire(i)
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
    global deleting
    numOfCells = blocksPW*blocksPW
    grid = [None]*numOfCells
    area1, area2, area3, area4 = [], [], [], []
    rea5, area6, area7, area8 = [], [], [], []
    rea9, area10, area11, area12 = [], [], [], []
    rea13, area14, area15, area16 = [], [], [], []


def main():
    elementButtons = [
        button([760, 20], (255, 200, 0), [20, 20], "sand", None),
        button([760, 50], (0, 0, 255), [20, 20], "water", None),
        button([760, 140], (0, 255, 0), [20, 20], "acid", None),
        button([760, 80], (200, 200, 200), [20, 20], "stone", None),
        button([760, 110], (50, 50, 50), [20, 20], "oil", None),
        button([760, 170], (70, 40, 0), [20, 20], "wood", None),
        button([760, 200], (255, 70, 0), [20, 20], "fire", None),
        button([20, 20], (200, 0, 0), [20, 20], "delete", None),
    ]
    reset_button = button([50, 20], (240, 240, 240), [20, 20], "", reset)
    sub_button = PMbutton([20, 60], [20, 20], "sub")
    add_button = PMbutton([50, 60], [20, 20], "add")
    r = 3
    selected = ""

    while True:
        # print(len(area1), len(area2), len(area3), len(area4), len(area5), len(area6), len(area7), len(area8), len(
        #    area9), len(area10), len(area11), len(area12), len(area13), len(area14), len(area15), len(area16))
        clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True

            if pygame.mouse.get_pressed()[0] == True and not clicked:
                if selected == "sand":
                    createBallNew(pygame.mouse.get_pos(), r, "sand",
                                  (255, 200, 0), True, (20, 0), False, 0, None)
                if selected == "water":
                    createBallNew(pygame.mouse.get_pos(), r, "water",
                                  (0, 0, 255), False, (0, 0, 35), True, 0, None)
                if selected == "acid":
                    createBallNew(pygame.mouse.get_pos(), r, "acid",
                                  (0, 255, 0), False, (0, 25, 0), True, 0, None)
                if selected == "stone":
                    createBallNew(pygame.mouse.get_pos(), r, "stone",
                                  (200, 200, 200), True, (25,), False, 0, None)
                if selected == "oil":
                    createBallNew(pygame.mouse.get_pos(), r, "oil",
                                  (15, 15, 15), False, (15,), True, 80, None)
                if selected == "wood":
                    createBallNew(pygame.mouse.get_pos(), r, "wood",
                                  (75, 45, 0), True, (10, 5, 0), False, 12, None)
                if selected == "fire":
                    createBallNew(pygame.mouse.get_pos(), r, "fire",
                                  (255, 180, 0), False, (0, 110, 0), False, False, (10, 75, 100))
                if selected == "delete":
                    deleting(pygame.mouse.get_pos())
        screen.fill((30, 30, 30))

        mainRender()
        mouse = pygame.mouse.get_pos()
        for i in elementButtons:
            selected = i.test(mouse, selected, clicked)
        reset_button.test(mouse, None, clicked)
        r = sub_button.test(mouse, r, clicked)
        r = add_button.test(mouse, r, clicked)
        font = pygame.font.SysFont(None, 50)
        text = font.render(str(r), True, (255, 255, 255))
        screen.blit(text, (80, 55))

        pygame.display.flip()
        clock.tick(renderSpeed)


numOfCells = blocksPW*blocksPW
grid = [None]*numOfCells
area1, area2, area3, area4 = [], [], [], []
area5, area6, area7, area8 = [], [], [], []
area9, area10, area11, area12 = [], [], [], []
area13, area14, area15, area16 = [], [], [], []
areas = [[]]*16
areaCount = 0


main()
sys.exit()
