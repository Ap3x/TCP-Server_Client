
import socket


tcp_ip = socket.gethostbyname(socket.gethostname())
tcp_port = 900
buffer_size = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((tcp_ip,tcp_port))
connection = True
while(connection):

	print("Send:")
	message = input()
	b =bytes(message, 'utf-8')
	client.send(b)
	data = client.recv(buffer_size)
client.close()

print ("recieved data:", data)