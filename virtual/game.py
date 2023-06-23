import pygame
import random
import os
import time

VERBOSITY = 10


def ITYSL():
    print("Hey, it seems like you're lost. Let me help you out.")
    exit()

def eval_gamestate():
    pass

class Player:
    def __init__(self, name, card, isOut=False):
        self.name = name
        self.card = card
        self.isOut = isOut

    # TODO functions should only do one thing
    def __str__(self, admin=False):
        if admin: 
            return f"{self.name} {self.card} {self.isOut}"
        else:
            return f"{self.name}"


class Card:
    def __init__(self, color, rank):
        self.color = color
        self.rank = rank

    def __str__(self):
        return f"{self.color} {self.rank}"

    def __repr__(self):
        return f"{self.color} {self.rank}"

    def __eq__(self, other):
        return self.color == other.color and self.rank == other.rank

    def __hash__(self):
        return hash((self.color, self.rank))

    def __lt__(self, other):
        return self.rank < other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __ge__(self, other):
        return self.rank >= other.rank

    def __ne__(self, other):
        return self.rank != other.rank


def persuasion_game():
    # This file will be coded as if we are explaining the rules of "PERSUASION" to a new player.

    GREETINGS = "Hey, thanks for coming to the party! What's your name? "
    NUMBER_OF_TOTAL_PLAYERS = 5 + 1  # 5 CPUs + PC

    # Hey, thanks for coming to the party! What's your name?
    name = input(GREETINGS)

    NICE_TO_MEET_YOU = f"Nice to meet you, {name}! "

    # Welcome the new player by name
    print(NICE_TO_MEET_YOU)

    STOCK_CHARACTER_NAMES = ["Alice", "Bob", "Charlie", "Derek", "Ethan"]
    # Tell the player the names of the other existing players
    print("The other players are: ")
    for character in STOCK_CHARACTER_NAMES:
        print(character, end=", ")
    if name not in STOCK_CHARACTER_NAMES:
        STOCK_CHARACTER_NAMES.append(name)

    # Establish social ties between players
    who_made_you_come = input("Who made you come to the party? ")

    # assert that the player knows someone at the party
    assert who_made_you_come in STOCK_CHARACTER_NAMES

    COLORS = ["RED", "BLACK"]
    RANKS = ["KING", "QUEEN", "JACK"]
    cards = []

    # print the card combos
    for color in COLORS:
        for rank in RANKS:
            cards.append(Card(color, rank))
            if VERBOSITY > 5:
                print(color, rank)

    # deal a card to each player
    for player in STOCK_CHARACTER_NAMES:
        card = random.choice(cards)
        cards.remove(card)
        if VERBOSITY > 5:
            print(f"{player} got {card}")


persuasion_game()
