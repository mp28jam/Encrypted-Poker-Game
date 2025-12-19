# This project implements a poker-test game on the Internet. It will 
# accept two players. The house has each player’s public key.

# 1. Each player generates a session key and distributes the session key 
# to the house securely. The session key is used to encrypt messages 
# sent between the house and the players.

# 2. The house randomly generates three numbers between 1 and 15 and 
# sends the numbers to the first player. 

# 3. The house randomly generates 
# three numbers between 1 and 15 and sends them to the second player.

# 4. There are three rounds. In each round, each player chooses a 
# number out of the three numbers and sends the number to the server.
# The server compares the numbers. The player who chooses the larger 
# numbers for at least two rounds wins. At the end of the 3rd round, 
# the house announces the winner.

# 5. The session key will be destroyed after a player leaves a current session.


# Generate cryptographically strong pseudo-random numbers suitable for
# managing secrets such as account authentication, tokens, and similar.
import secrets
import os # for cryptographic RNGs
import asyncio
import websockets

# from cryptography


class PokerTest:
    def __init__(self): 
        self.session_key = secrets.token_bytes
        self.random_A = ""
        self.random_B = ""


    def hello():
        pass
        # with connect
    def enter_session(self): pass
    def generate_public_key(self): pass
    def generate_session_key(self): pass
    def destroy_session_key(self): pass
    def send_numbers(self, player): pass
    def compare_prngs(self, player1, player2): pass


    def game(self):
        self.prng = secrets.randbelow(15)
        os.urandom(16)


if __name__ == "__main__":
    app = PokerTest()
    app.game()
    

