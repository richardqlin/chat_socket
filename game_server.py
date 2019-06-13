import pygame
import socket
from pygame.locals import *
pygame.init()
WIDTH=500
HEIGHT=500
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",1234))
s.listen(10)
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sever Python Game")
class Player:
    def __init__(self):
        self.x=WIDTH//2
        self.y=HEIGHT//2
    def moveBy(self,x_distance,y_distance):
        self.x += x_distance
        self.y += y_distance
    def draw(self):
        pygame.draw.rect(window,(255,0,0),(self.x,self.y,20,20))
player1=Player()
dis_x = dis_y =0
client, client_address = s.accept()

print("Client has connected with address: {}".format(client_address))
while True:
    pygame.time.wait(10)
    #ch = client.recv(1).decode('utf-8')
    #print('message from client',ch)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_UP:
                dis_y = -1
            elif event.key==K_DOWN:
                dis_y = 1
            elif event.key==K_LEFT:
                dis_x = -1
            elif event.key==K_RIGHT:
                dis_x = 1
        if event.type==KEYUP:
            if event.key==K_UP:
                dis_y = 0
            elif event.key==K_DOWN:
                dis_y=0
            elif event.key==K_LEFT:
                dis_x = 0
            elif event.key==K_RIGHT:
                dis_x = 0
    player1.moveBy(dis_x,dis_y)
    window.fill((255, 255, 255))
    player1.draw()
    pygame.display.update()

    player1.x, player1.y = int(player1.x),int(player1.y)
    client.sendall(bytes('{}'.format(len(str(player1.x) + ' ' + str(player1.y))),'utf-8'))

    client.sendall(bytes("{} {}".format(player1.x, player1.y), "utf-8"))

client.close()
