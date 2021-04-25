from socket import *

def initMailBox():
	"This function creates mailbox and opens socket"
	mbx = socket(AF_INET, SOCK_DGRAM)
	mbx.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	mbx.bind(('',12345))
	return mbx

def sendMessage(message):
	s=socket(AF_INET, SOCK_DGRAM)
	s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
	s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	s.sendto(message.encode('utf-8'),('255.255.255.255',12345))

def getMessage(mailbox):
	return mailbox.recv(1024).decode('utf-8')
