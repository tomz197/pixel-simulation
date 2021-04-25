from random import *
from math import floor
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
    def __init__(self, x_, y_, type_, color_, staticColor_, colorVariant_, liquid_, flamable_, lifetime_):
        global areaCount
        self.x = x_
        self.y = y_
        self.type = type_
        self.color = list(color_)
        self.staticColor = staticColor_
        self.colorVariant = list(colorVariant_)
        self.liqud = liquid_
        self.flamable = flamable_
        self.lifetime = lifetime_
        self.square = pygame.Rect(
            x_*moveAmount, y_*moveAmount, moveAmount, moveAmount)
        if self.lifetime != None:
            arr = list(lifetime_)
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
    global numOfElements
    if event[0] >= screen_width or event[0] <= 0 or event[1] >= screen_height or event[1] <= 0:
        return
    x, y = floor(event[0]/moveAmount), floor(event[1]/moveAmount)
    if grid[y*blocksPW + x] == None:
        grid[y*blocksPW + x] = block(x, y, type, color, staticColor,
                                     colorVariant, liquid, flamable, lifetime)
        numOfElements += 1
        print("elements: ", numOfElements)


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


def switch(pos1, pos2, val1, val2):
    grid[pos1] = val2
    grid[pos2] = val1


def moveSand(i):
    y = floor(i[0]*blocksPW)
    y1 = floor((i[0]+1)*blocksPW)
    y2 = floor((i[0]+2)*blocksPW)
    x = floor(i[1])

    if i[0] >= blocksPW-1:
        return i

    if grid[y1 + x] == None:
        switch(y + x, y1 + x, grid[y + x], None)
        i[0] += 1
        if i[0] <= blocksPW-2:
            if grid[y2 + x] == None:
                switch(y1 + x, y2 + x, grid[y1 + x], None)
                i[0] += 1
        return i
    if grid[y1 + x].type == "water" or grid[y1 + x].type == "acid":
        switch(y + x, y1 + x, grid[y + x], grid[y1 + x])
        return i
    if x != 0:
        if grid[y1 + x-1] == None:
            switch(y + x, y1 + x-1, grid[y + x], None)
            i[0] += 1
            i[1] -= 1
            return i
        if grid[y1 + x-1].type == "water" or grid[y1 + x-1].type == "acid":
            switch(y + x, y1 + x-1, grid[y + x], grid[y1 + x-1])
            return i
    if y1 + x+1 >= numOfCells or x == blocksPW-1:
        return i
    if grid[y1 + x+1] == None:
        switch(y + x, y1 + x+1, grid[y + x], None)
        i[0] += 1
        i[1] += 1
        return i
    if grid[y1 + x+1].type == "water" or grid[y1 + x+1].type == "acid":
        switch(y + x, y1 + x+1, grid[y + x], grid[y1 + x+1])
        return i
    return i


def moveWater(i):
    y = floor(i[0]*blocksPW)
    y1 = floor((i[0]+1)*blocksPW)
    y2 = floor((i[0]+2)*blocksPW)
    x = floor(i[1])

    if i[0] >= blocksPW-1:
        if grid[y + x-1] == None and x != 0 and i[2] == 0:
            switch(y + x, y + x-1, grid[y + x], None)
            i[1] -= 1
            return i
        i[2] = 1
        if y + x+1 >= numOfCells:
            i[2] = 0
            return i
        if grid[y + x+1] == None and x != blocksPW-1:
            switch(y + x, y + x+1, grid[y + x], None)
            i[1] += 1
            return i
        i[2] = 0
        return i

    if grid[y1 + x] == None:
        switch(y + x, y1 + x, grid[y + x], None)
        i[0] += 1
        i[2] = randint(0, 1)
        if i[0] <= blocksPW-2:
            if grid[y2 + x] == None:
                switch(y1 + x, y2 + x, grid[y1 + x], None)
                i[0] += 1
        return i
    if grid[y1 + x-1] == None and x != 0:
        switch(y + x, y1 + x-1, grid[y + x], None)
        i[0] += 1
        i[1] -= 1
        return i
    if y1 + x+1 >= numOfCells:
        return i
    if grid[y1 + x+1] == None and x != blocksPW-1:
        switch(y + x, y1 + x+1, grid[y + x], None)
        i[0] += 1
        i[1] += 1
        return i
    if grid[y + x-1] == None and x != 0 and i[2] == 0:
        switch(y + x, y + x-1, grid[y + x], None)
        i[1] -= 1
        return i
    i[2] = 1
    if y + x+1 >= numOfCells:
        i[2] = 0
        return i
    if grid[y + x+1] == None and x != blocksPW-1:
        switch(y + x, y + x+1, grid[y + x], None)
        i[1] += 1
        return i
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
                switch(y + x, y + x-1, smoke, None)
                i[1] -= 1
                return i
        i[2] = 1
        if y + x+1 >= numOfCells:
            i[2] = 0
            return i
        if x != blocksPW-1 and grid[y + x+1] != None:
            if grid[y + x+1].type != "acid" and grid[y + x+1].type != "smoke":
                switch(y + x, y + x+1, smoke, None)
                i[1] += 1
                return i
        i[2] = 0
        return i

    if grid[y1 + x] != None:
        if grid[y1 + x].type != "acid" and grid[y1 + x].type != "smoke":
            switch(y + x, y1 + x, smoke, None)
            i[0] += 1
            i[2] = randint(0, 1)
            return i
    if x != 0 and grid[y1 + x-1] != None:
        if grid[y1 + x-1].type != "acid" and grid[y1 + x-1].type != "smoke":
            switch(y + x, y1 + x-1, smoke, None)
            i[0] += 1
            i[1] -= 1
            return i
    if y1 + x+1 >= numOfCells:
        return i
    if x != blocksPW-1 and grid[y1 + x+1] != None:
        if grid[y1 + x+1].type != "acid" and grid[y1 + x+1].type != "smoke":
            switch(y + x, y1 + x+1, smoke, None)
            i[0] += 1
            i[1] += 1
            return i
    if x != 0 and i[2] == 0 and grid[y + x-1] != None:
        if grid[y + x-1].type != "acid" and grid[y + x-1].type != "smoke":
            switch(y + x, y + x-1, smoke, None)
            i[1] -= 1
            return i
    i[2] = 1
    if y + x+1 >= numOfCells:
        i[2] = 0
        return i
    if x != blocksPW-1 and grid[y + x+1] != None:
        if grid[y + x+1].type != "acid" and grid[y + x+1].type != "smoke":
            switch(y + x, y + x+1, smoke, None)
            i[1] += 1
            return i

    if x != blocksPW-1 and grid[ym1 + x] != None:
        if grid[ym1 + x].type != "acid" and grid[ym1 + x].type != "smoke":
            switch(y + x, ym1 + x, smoke, None)
            i[0] -= 1
            return i
    if x != 0 and grid[ym1 + x-1] != None:
        if grid[ym1 + x-1].type != "acid" and grid[ym1 + x-1].type != "smoke":
            switch(y + x, ym1 + x-1, smoke, None)
            i[0] -= 1
            i[1] -= 1
            return i
    if y1 + x+1 >= numOfCells:
        return i
    if x != blocksPW-1 and grid[ym1 + x+1] != None:
        if grid[ym1 + x+1].type != "acid" and grid[ym1 + x+1].type != "smoke":
            switch(y + x, ym1 + x+1, smoke, None)
            i[0] -= 1
            i[1] += 1
            return i

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
                switch(y + x, y1 + x, fire, smoke)
        if x != 0 and grid[y1 + x-1] != None:
            if randint(1, 100) <= grid[y1 + x-1].flamable:
                fire = block(x, y, "fire", (255, 180, 0), False,
                             (0, 110, 0), False, False, (100, 200, 100))
                switch(y + x, y1 + x-1, fire, smoke)
        if y1 + x+1 >= numOfCells:
            return i
        if x != blocksPW-1 and grid[y1 + x+1] != None:
            if randint(1, 100) <= grid[y1 + x+1].flamable:
                fire = block(x, y, "fire", (255, 180, 0), False,
                             (0, 110, 0), False, False, (100, 200, 100))
                switch(y + x, y1 + x+1, fire, smoke)
    if x != 0 and grid[y + x-1] != None:
        if randint(1, 100) <= grid[y + x-1].flamable:
            fire = block(x, y, "fire", (255, 180, 0), False,
                         (0, 110, 0), False, False, (100, 200, 100))
            switch(y + x, y + x-1, fire, smoke)
    if y + x+1 >= numOfCells:
        return i
    if x != blocksPW-1 and grid[y + x+1] != None:
        if randint(1, 100) <= grid[y + x+1].flamable:
            fire = block(x, y, "fire", (255, 180, 0), False,
                         (0, 110, 0), False, False, (100, 200, 100))
            switch(y + x, y + x+1, fire, smoke)

    if x != blocksPW-1 and grid[ym1 + x] != None:
        if randint(1, 100) <= grid[ym1 + x].flamable:
            fire = block(x, y, "fire", (255, 180, 0), False,
                         (0, 110, 0), False, False, (100, 200, 100))
            switch(y + x, ym1 + x, fire, smoke)
    if x != 0 and grid[ym1 + x-1] != None:
        if randint(1, 100) <= grid[ym1 + x-1].flamable:
            fire = block(x, y, "fire", (255, 180, 0), False,
                         (0, 110, 0), False, False, (100, 200, 100))
            switch(y + x, ym1 + x-1, fire, smoke)
    if y1 + x+1 >= numOfCells:
        return i
    if x != blocksPW-1 and grid[ym1 + x+1] != None:
        if randint(1, 100) <= grid[ym1 + x+1].flamable:
            fire = block(x, y, "fire", (255, 180, 0), False,
                         (0, 110, 0), False, False, (100, 200, 100))
            switch(y + x, ym1 + x+1, fire, smoke)
    if randint(1, 10) == 1:
        return moveWater(i)
    return i


def moveSmoke(i):
    y = floor(i[0]*blocksPW)
    y1 = floor((i[0]-1)*blocksPW)
    y2 = floor((i[0]-2)*blocksPW)
    x = floor(i[1])

    if i[0] <= 0:
        if randint(1, 30) == 1:
            grid[y + x] = None
            return i
        if grid[y + x-1] == None and x != 0 and i[2] == 0:
            switch(y + x, y + x-1, grid[y + x], None)
            i[1] -= 1
            return i
        i[2] = 1
        if y + x+1 >= numOfCells:
            i[2] = 0
            return i
        if grid[y + x+1] == None and x != blocksPW-1:
            switch(y + x, y + x+1, grid[y + x], None)
            i[1] += 1
            return i
        i[2] = 0
        return i

    if grid[y1 + x] == None:
        switch(y + x, y1 + x, grid[y + x], None)
        i[0] -= 1
        i[2] = randint(0, 1)
        if i[0] >= 2:
            if grid[y2 + x] == None:
                switch(y1 + x, y2 + x, grid[y1 + x], None)
                i[0] -= 1
        return i
    if grid[y1 + x].type == "sand" or grid[y1 + x].type == "water" or grid[y1 + x].type == "acid":
        switch(y + x, y1 + x, grid[y + x], grid[y1 + x])
        i[2] = randint(0, 1)
        return i
    if grid[y1 + x-1] == None and x != 0:
        switch(y + x, y1 + x-1, grid[y + x], None)
        i[0] -= 1
        i[1] -= 1
        return i
    if x != 0:
        if grid[y1 + x-1].type == "sand" or grid[y1 + x-1].type == "water" or grid[y1 + x-1].type == "acid":
            switch(y + x, y1 + x-1, grid[y + x], grid[y1 + x-1])
            i[2] = randint(0, 1)
            return i
    if y1 + x+1 >= numOfCells:
        return i
    if grid[y1 + x+1] == None and x != blocksPW-1:
        switch(y + x, y1 + x+1, grid[y + x], None)
        i[0] -= 1
        i[1] += 1
        return i
    if x != blocksPW-1:
        if grid[y1 + x+1].type == "sand" or grid[y1 + x+1].type == "water" or grid[y1 + x+1].type == "acid":
            switch(y + x, y1 + x+1, grid[y + x], grid[y1 + x+1])
            i[2] = randint(0, 1)
            return i
    if grid[y + x-1] == None and x != 0 and i[2] == 0:
        switch(y + x, y + x-1, grid[y + x], None)
        i[1] -= 1
        return i
    i[2] = 1
    if y + x+1 >= numOfCells:
        i[2] = 0
        return i
    if grid[y + x+1] == None and x != blocksPW-1:
        switch(y + x, y + x+1, grid[y + x], None)
        i[1] += 1
        return i
    i[2] = 0
    return i


def render(arr):
    global numOfElements
    for i in arr:
        pos = i[0]*blocksPW + i[1]
        if pos >= len(grid):
            arr.remove(i)
            numOfElements -= 1
            continue
        if grid[pos] == None:
            arr.remove(i)
            numOfElements -= 1
            print("elements: ", len(area1)+len(area2)+len(area3)+len(area4)+len(area5)+len(area6)+len(area7) +
                  len(area8)+len(area9)+len(area10)+len(area11)+len(area12)+len(area13)+len(area14)+len(area15)+len(area16))
            continue
        if grid[pos].type == "water" or grid[pos].type == "oil":
            i = moveWater(i)
        elif grid[pos].type == "sand":
            i = moveSand(i)
        elif grid[pos].type == "smoke":
            i = moveSmoke(i)
            if grid[i[0]*blocksPW + i[1]] == None:
                arr.remove(i)
                numOfElements -= 1
                continue
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
    global numOfElements, deleting
    numOfCells = blocksPW*blocksPW
    grid = [None]*numOfCells
    area1, area2, area3, area4 = [], [], [], []
    rea5, area6, area7, area8 = [], [], [], []
    rea9, area10, area11, area12 = [], [], [], []
    rea13, area14, area15, area16 = [], [], [], []
    numOfElements = 0


def main():
    sand_button = button([760, 20], (255, 200, 0), [20, 20], "sand", None)
    water_button = button([760, 50], (0, 0, 255), [20, 20], "water", None)
    acid_button = button([760, 140], (0, 255, 0), [20, 20], "acid", None)
    stone_button = button([760, 80], (200, 200, 200), [20, 20], "stone", None)
    oil_button = button([760, 110], (50, 50, 50), [20, 20], "oil", None)
    wood_button = button([760, 170], (70, 40, 0), [20, 20], "wood", None)
    fire_button = button([760, 200], (255, 70, 0), [20, 20], "fire", None)
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True

            if pygame.mouse.get_pressed()[0] == True and not clicked:
                if selected == "sand":
                    createBall(pygame.mouse.get_pos(), "sand",
                               (255, 200, 0), True, (20, 0), False, 0, None)
                if selected == "water":
                    createBall(pygame.mouse.get_pos(), "water",
                               (0, 0, 255), False, (0, 0, 35), True, 0, None)
                if selected == "acid":
                    createBall(pygame.mouse.get_pos(), "acid",
                               (0, 255, 0), False, (0, 25, 0), True, 0, None)
                if selected == "stone":
                    createBall(pygame.mouse.get_pos(), "stone",
                               (200, 200, 200), True, (25,), False, 0, None)
                if selected == "oil":
                    createBall(pygame.mouse.get_pos(), "oil",
                               (15, 15, 15), False, (15,), True, 80, None)
                if selected == "wood":
                    createBall(pygame.mouse.get_pos(), "wood",
                               (75, 45, 0), True, (10, 5, 0), False, 10, None)
                if selected == "fire":
                    createBall(pygame.mouse.get_pos(), "fire",
                               (255, 180, 0), False, (0, 110, 0), False, False, (10, 75, 100))
                if selected == "delete":
                    deleting(pygame.mouse.get_pos())
        screen.fill((30, 30, 30))

        mainRender()

        mouse = pygame.mouse.get_pos()
        selected = sand_button.test(mouse, selected, clicked)
        selected = water_button.test(mouse, selected, clicked)
        selected = stone_button.test(mouse, selected, clicked)
        selected = oil_button.test(mouse, selected, clicked)
        selected = wood_button.test(mouse, selected, clicked)
        selected = delete_button.test(mouse, selected, clicked)
        selected = fire_button.test(mouse, selected, clicked)
        selected = acid_button.test(mouse, selected, clicked)
        reset_button.test(mouse, None, clicked)

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
numOfElements = 0


main()
sys.exit()
