# rozhs massage
import socket


class Client:  
    def init(self) -> None:  
        self.server_game = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

    def client(self, ip, port):
        while True:  
            ip = input("Enter server IP address: ")  
            port_str = input("Enter server port: ")              
            port = int(port_str)
        try:
            self.server_game.connect((ip, port))
            print(f"Connected to server at {ip}:{port}")  
            break  
        except (socket.error, ConnectionRefusedError) as e:  
                print(f"Failed to connect to the server at {ip}:{port}. Error: {e}. Please try again.")  


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
