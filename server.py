import socket
import pickle


s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port = 8080
s.bind((host,port))
s.listen(1)
print("waiting for connections ")
conn,addr =s.accept()
print("client one has connnected")
conn.send("welcome to the game ".encode())
conn1, addr1 = s.accept()
conn1.send("welcome to the game ".encode())

choices = []
for x in range (0, 9) :
    choices.append(str(x + 1))

playerOneTurn = True
winner = False

def printBoard() :
    print( '\n')
    print( '-' + choices[0] + '-' + choices[1] + '-' + choices[2] + '-')
    print( ' ')
    print( '-' + choices[3] + '-' + choices[4] + '-' + choices[5] + '-')
    print( ' ')
    print( '-' + choices[6] + '-' + choices[7] + '-' + choices[8] + '-')
    print( ' \n')

f=0

while (not winner and f<9 ):

     printBoard()

     if playerOneTurn :
             print( "Player 1:")
             try:
                choice = conn.recv(1024)
                choice = int(choice.decode())
                print(choice)
             except:
                print("please enter a valid field")
                break
             f=f+1

	
     else :
             print( "Player 2:")
             try:
                choice = conn1.recv(1024)
                choice=int(choice.decode())
                print(choice)
             except:
                print("please enter a valid field")
                break
             f=f+1


        
    
     if choices[choice - 1] == 'X' or choices [choice-1] == 'O':
            print("illegal move, plase try again")
            continue

     if playerOneTurn :
        choices[choice - 1] = 'X'
     else :
        choices[choice - 1] = 'O'

     
    

     playerOneTurn = not playerOneTurn
     message = pickle.dumps(choices)
        
     conn.send(message)
     conn1.send(message)

     for x in range (0, 3) :
        y = x * 3
        if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) :
                winner = True
                printBoard()
        if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)] ) :
                winner = True
                printBoard()

     if((choices[0] == choices[4] and choices[0] == choices[8]) or 
       (choices[2] == choices[4] and choices[4] == choices[6])) :
             winner = True
             printBoard()
       
if winner == True:
	print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")
else:
	print (" its a tie")


'''while 1:
	message = input(str(">>"))
	message= message.encode()
	conn.send(message)
	conn1.send(message)
	print("message sent ..")
	recv_message = conn.recv(1024)
	print("client : ", recv_message.decode())
	conn1.send(recv_message)
	recv_message =conn1.recv(1024)
	print("Client 1 : ", recv_message.decode())
	conn.send(recv_message)
'''
