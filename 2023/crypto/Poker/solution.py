import ntplib
import itertools
import random
import socket
import re
import ast
from telnetlib import Telnet

c = ntplib.NTPClient()
response = c.request('time.cloudflare.com', version=3)

values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

deck_of_cards = list(itertools.product(values, suites))

HOST = "localhost"
PORT = 1337

def initialise_card_decks():
    one_thousand_shuffled_card_decks = []

    timestamp_miliseconds = int(response.recv_time)*1000

    for x in range(timestamp_miliseconds, timestamp_miliseconds + 1000):
        shuffled_deck_of_cards = deck_of_cards.copy()
        random.Random(x).shuffle(shuffled_deck_of_cards)
        one_thousand_shuffled_card_decks.append(shuffled_deck_of_cards)

    return one_thousand_shuffled_card_decks

def create_socket(HOST, PORT):
    sock = socket.socket()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    return sock    

def send_data(message, sock):
    """Get requests"""
    if message:
        sock.sendall(message)

    has_request = False
    while not has_request:
        data = sock.recv(2048)
        has_request = True
    return data

if __name__ == "__main__":
    one_thousand_shuffled_card_decks = initialise_card_decks()
    server_sock = create_socket(HOST, PORT)
    server_data = send_data(b"", server_sock)
    
    cards = re.findall("\('[^']+', '[^']+'\)", server_data.decode())
    cards = [eval(card) for card in cards]

    if cards:
        first_card = cards[0]
        second_card = cards[1]
        third_card = cards[2]
        fourth_card = cards[3]
        fifth_card = cards[4]
    else:
        print("No match found.")

    found = False

    for shuffled_card_deck in one_thousand_shuffled_card_decks:
        if first_card == shuffled_card_deck[0] and second_card == shuffled_card_deck[1] and \
            third_card == shuffled_card_deck[2] and fourth_card == shuffled_card_deck[3] and fifth_card == shuffled_card_deck[4]:
            print(shuffled_card_deck)
            found = True
            print("Found")
            pass
    
    if not found:
        print("Not found")

    tn = Telnet('localhost', 1337)
    tn.sock = server_sock
    tn.interact()