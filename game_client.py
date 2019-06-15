import socket
import pygame
from pygame.locals import *
pygame.init()
WIDTH=500
HEIGHT=500
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.1.245",1234))

window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("client Python Game")

class Player:
    def __init__(self,color):
        self.color = color
        self.x=WIDTH//2
        self.y=HEIGHT//2
    def moveBy(self,x_distance,y_distance):
        self.x += x_distance
        self.y += y_distance
    def draw(self):
        pygame.draw.rect(window,self.color,(self.x,self.y,20,20))

    def pos(self,x,y):
        self.x = x
        self.y = y

player2=Player((0,255,0))

player1=Player((255,0,0))

dis_x = dis_y =0
while 1:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                dis_y = -1
            elif event.key == K_DOWN:
                dis_y = 1
            elif event.key == K_LEFT:
                dis_x = -1
            elif event.key == K_RIGHT:
                dis_x = 1
        if event.type == KEYUP:
            if event.key == K_UP:
                dis_y = 0
            elif event.key == K_DOWN:
                dis_y = 0
            elif event.key == K_LEFT:
                dis_x = 0
            elif event.key == K_RIGHT:
                dis_x = 0
    d = s.recv(1).decode('utf-8')
    d =int(d)
    data = s.recv(d).decode('utf-8')
    data = data.split(' ')
    x,y = int(data[0]),int(data[1])
    s.sendall(bytes("{} {}".format(player1.x, player1.y), "utf-8"))
    window.fill((255, 255, 255))
    player1.draw()

    player2.draw()
    player2.pos(x,y)
    player1.moveBy(dis_x, dis_y)
    pygame.display.update()




