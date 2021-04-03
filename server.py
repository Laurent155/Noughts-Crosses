import socket
from _thread import *
import pickle
from player import Player
from game import Game, Turn


server = "192.168.0.35"  
port = 5555  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port)) 
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

players = [Player("circle", True), Player("cross", False)]
game = Game("circle")



def threaded_client(conn, player):
    if player % 2 == 0:
        symb = 'circle'
    else:
        symb = 'cross'
    conn.send(str.encode(symb))
   

    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))

            if not data:
                print("Disconnected")
                break
            else:
                if game.valid_move(data):
                    game.add_move(data)
                    game.change_turn()
                    game.check_victory()
                    game.check_draw()
                reply = game
            conn.sendall(pickle.dumps(reply))
        except:
            break
            
    print("Lost connection")
    conn.close()


currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
   
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
