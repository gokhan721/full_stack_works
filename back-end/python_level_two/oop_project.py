#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        print("Decks has been created!")
        self.all_cards = [(s, r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("Decks has been shuffled!")
        shuffle(self.all_cards)

    def cut_middle(self):
        print("Decks has been cut in half!")
        return (self.all_cards[:26], self.all_cards[26:])


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return f"Contains {len(self.cards)} cards"

    def add_cards(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class Player(Hand):
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """

    def __init__(self, name, cards):
        self.name = name
        super().__init__(cards)

    def play_card(self):
        drawn_card = super().remove_card()
        print(f"{self.name} has placed: {drawn_card}\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.cards) < 3:
            return self.cards
        else:
            for x in range(4):
                war_cards.append(super().remove_card())
            return war_cards

    def still_has_cards(self):
        return len(self.cards) != 0


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!


new_deck = Deck()
new_deck.shuffle()
half_one, half_two = new_deck.cut_middle()


comp = Player("computer", half_one)


name = input("Enter name: ")
user = Player(name, half_two)


total_rounds = 0
war_count = 0


while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Time for a new round!")
    print("here are the current standings")
    print(f"{comp.name} has the count: {len(comp.cards)}")
    print(f"{user.name} has the count: {len(user.cards)}")
    print("play a card\n")

    table_cards = []

    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1

        print("WAR!!")

        user_removed_cards = user.remove_war_cards()
        print(f"{name} cards for war: {user_removed_cards}")
        comp_removed_cards = comp.remove_war_cards()
        print(f"Comp cards for war: {comp_removed_cards}")

        i = 0
        min_len = len(user_removed_cards) if len(user_removed_cards) else len(comp_removed_cards)
        user_removed_cards = user_removed_cards[:min_len]
        comp_removed_cards = comp_removed_cards[:min_len]
        if (min_len < len(user_removed_cards)):
            user.cards.add_cards(user_removed_cards[min_len:])
        if (min_len < len(comp_removed_cards)):
            comp.cards.add_cards(comp_removed_cards[min_len:])

        table_cards.extend(comp_removed_cards)
        table_cards.extend(user_removed_cards)
        while i < min_len:
            print(RANKS.index(user_removed_cards[i][1]))
            print(RANKS.index(comp_removed_cards[i][1]))
            if RANKS.index(user_removed_cards[i][1]) > RANKS.index(comp_removed_cards[i][1]):
                user.add_cards(table_cards)
                break
            elif RANKS.index(user_removed_cards[i][1]) < RANKS.index(comp_removed_cards[i][1]):
                comp.add_cards(table_cards)
                break
            else:
                i += 1
                continue

        if i == min_len:
            print(f"All cards in table same rank! Comp win!!!")
            comp.add_cards(table_cards)
    else:

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.add_cards(table_cards)
        else:
            comp.add_cards(table_cards)

print(f"Game OVer, number of rounds: {total_rounds}")
print(f"a war happened {war_count} times")
print(f"Computer has: {comp.still_has_cards()}")
print(f"User has: {user.still_has_cards()}")
