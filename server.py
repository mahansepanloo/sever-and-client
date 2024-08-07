import socket
import random

class Game:
 
    def __init__(self) -> None:  
        self.secret_num = random.randint(1, 1000)  

    def check_guess(self, guess):  
        if guess < self.secret_num:  
            return 'bigger'  
        elif guess > self.secret_num:  
            return 'smaller'  
        else:  
            return 'correct'



class Server:  
    def init(self):  
        self.server_game = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

    def start_server(self,ip,port):  
        self.server_game.bind((ip, port))  
        self.server_game.listen(1)  
        print(f"Server is listening on '127.0.0.1' : 12345")  
        client, addr = self.server_game.accept()  
        print(f"Connection from {addr} has been established!")  

        game = Game()  
        print(f"add : {game.secret_number}")
        while True:  
            guess = client.recv(1024).decode()  
            if not guess:  
                break  

            guess = int(guess)  
            print(f"Received guess: {guess}")  

            result = game.check_guess(guess)  
            client.sendall(result.encode())  

            if result == 'correct':  
                print('new game') 
                break

        client.close()  
        self.server_game.close()  


if __name__ == "__main__":  
    server = Server()  
    server.start_server('127.0.0.1', 12345)
