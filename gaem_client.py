import socket
import pygame
from pygame.locals import *
pygame.init()
WIDTH=500
HEIGHT=500
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.1.78",1234))

window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Cool Python Game")

class Player:
    def __init__(self):
        self.x=WIDTH//2
        self.y=HEIGHT//2
    def moveBy(self,x_distance,y_distance):
        self.x += x_distance
        self.y += y_distance
    def draw(self):
        pygame.draw.rect(window,(0,255,0),(self.x,self.y,20,20))

player2=Player()
player1=Player()
while 1:
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_UP:
                player1.moveBy(0,-5)
            elif event.key==K_DOWN:
                player1.moveBy(0,5)
            elif event.key==K_LEFT:
                player1.moveBy(-5,0)
            elif event.key==K_RIGHT:
                player1.moveBy(5,0)
    window.fill((255,255,255))
    player1.draw()
    pygame.display.update()
    data = s.recv(2048)
    print(data)
    
