import random;

def deckGenerator():
    faces = list(["Jack", "Queen", "King", "Ace"]);
    suits = list(["Clubs", "Spades", "Diamonds", "Hearts"]);
    deck = list([]);
    for i in suits:
        deck += [str(n) + "-" + i for n in range(2, 11)];
        deck += [faces[f] + "-" + i for f in range(len(faces))];
    return deck;

print(deckGenerator());