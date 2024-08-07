# rozhs massage
import socket


class Client:  
    def init(self) -> None:  
        self.server_game = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

    def client(self, ip, port):  
        self.server_game.connect((ip, port))  

        while True:  
            guess = input("Enter your guess (1-100): ")  
            self.server_game.sendall(guess.encode())  

            response = self.server_game.recv(1024).decode()  
            print(response)  

            if response == 'correct':  
                print("You've guessed it right! Game over.")  
                break  

        self.server_game.close()  


if name == "main":  
    # server = Server()  
    # server.start_server('127.0.0.1', 12345)  
    client = Client()  
    client.client('127.0.0.1', 12345)