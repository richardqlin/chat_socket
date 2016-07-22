import socket
import time
import threading

tlock=threading.Lock()

shutdown=False

def receiving(name,sock):
	while  not shutdown:
		try:
			tlock.acquire()
			while True:
				data ,addr=sock.recvfrom(1024)
				print(str(data))
		except:
			pass
		finally:
			tlock.release()

host='127.0.0.1'
port=0

server=('127.0.0.1',7000)

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((host,port))

s.setblocking(0)

rT=threading.Thread(target=receiving,args=('RecvThread',s))

rT.start()

alias=input("Name: ")
message=input(alias+'-> ')
while message!='q':
	if message!='':
		s.sendto((alias+': '+message).encode(),server)

	tlock.acquire()
	message=input(alias+'->')
	tlock.release()
	time.sleep(0.2)
shutdown=True
rT.join()
s.close()


