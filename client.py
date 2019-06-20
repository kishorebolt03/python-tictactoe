import socket
import pickle

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port = 8080
s.connect((host,port))

choices =[]
for x in range (0, 9) :
    choices.append(str(x + 1))

    
print("connected to the server")
message =s.recv(1024)
message = message.decode()
print("Server : ",message)

def printBoard() :
    print( '\n')
    print( '-' + choices[0] + '-' + choices[1] + '-' + choices[2] + '-')
    print( ' ')
    print( '-' + choices[3] + '-' + choices[4] + '-' + choices[5] + '-')
    print( ' ')
    print( '-' + choices[6] + '-' + choices[7] + '-' + choices[8] + '-')
    print( ' \n')

print("\t Let's Start the Game \n")
printBoard()

while 1 :
        
        choice = input(">> ")
        s.send(choice.encode())
        choices = s.recv(1024)
        choices = pickle.loads(choices)
	printBoard() 
