import random
numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suits = ['Heart','Diamond','Spade','Club']

class Deck:
    def __init__(self, numbers, suits):
        self.numbers = [number for number in numbers]
        self.suits = [suit for suit in suits]
        self.deck = []

    def __repr__(self):
        deck_size = len(self.deck)
        return "Cards Remaining: " + str(deck_size)
    def AssembleDeck(self):
        for suit in self.suits:
             for number in numbers:
                self.deck.append(Card(suit, number))
    def Show_Deck(self):
        for card in self.deck:
            print(str(card))
    
    def Shuffle(self):
        random.shuffle(self.deck)
        random.shuffle(self.deck)
        random.shuffle(self.deck)
    
    def Draw_Card(self):
        card = self.deck[-1]
        self.deck.remove(card)
        return card

class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
    
    def Show_Card(self):
        return self.suit, self.number

class Player:
    def __init__(self, name, player_number):
        self.name = name
        self.player_number = player_number
        self.hand = []
        self.win_pile = []

    def __repr__(self):
        return str(self.player_number) + ": " + str(self.name)
    
    def Add_Card(self, card):
        self.hand.append(card)

    def Show_Hand(self):
        for card in self.hand:
            print("   " + str(card.number) + " " + str(card.suit))
    
    def Show_Win_Pile(self):
        print(str(self.name) + " Win Pile:")
        for pair in self.win_pile:
            for card in pair:
                print(str(card.number) + " " + str(card.suit))

    def Complete_Pair(self, card_1, card_2):
        index_card_1 = self.hand.index(card_1)
        card_1 = (self.hand).pop(index_card_1)
        index_card_2 = self.hand.index(card_2)
        card_2 = (self.hand).pop(index_card_2)
        #print(str(card_1.number) + " " + str(card_1.suit))
        #print(str(card_2.number) + " " + str(card_1.suit))
        pair = [card_1, card_2]
        self.win_pile.append(pair)

    def Self_Verify_Card(self):
        complete_loop = False
        for card in self.hand:
            for card_in_hand in self.hand:
                if str(card.number) == str(card_in_hand.number):
                    #print(str(card.number) + " " + str(card_in_hand.number))
                    if str(card.suit) != str(card_in_hand.suit):
                        print(str(card.number) + " " + str(card_in_hand.suit)+  " and " + str(card_in_hand.suit) + "Found as match")
                        self.Complete_Pair(card, card_in_hand)
                        complete_loop = True
                        break
                    #else:
                        #print("Suit Match")
                        #print(str(card.number) + " " + str(card_in_hand.number))
                #else:
                    #print("No Match")
                    #print(str(card.number) + " " + str(card_in_hand.number))
        if complete_loop == True:
            self.Self_Verify_Card()

    def Enemy_Verify_Card(self, number):
        for card in self.hand:
            if str(number) == str(card.number):
                #print(str(card.number) + " " + str(card_in_hand.number))
                index_of_card = self.hand.index(card)
                won_card = self.hand.pop(index_of_card)
                print("Found Card: " + str(won_card.number) + " " + str(won_card.suit))
                return won_card
                break
        return False


class Table:
    def __init__(self):
        self.players = []
    
    def __repr__(self):
        return "Players at table: " + str(self.players)
    
    def Add_Player(self, player):
        self.players.append(player)

    def Add_Deck(self, deck):
        self.deck = deck

    def Prep_Game(self):
        self.deck.Shuffle()
        for i in range(0, 7):
            for player in self.players:
                player.Add_Card(self.deck.Draw_Card())
        for player in self.players:
            print(player.name + ":")
            player.Show_Hand()
            player.Self_Verify_Card()
            player.Show_Win_Pile()
            print(player.name + ":")
            player.Show_Hand()
    
    def Player_Turn(self, player):
        print(str(player.name) + ": ")
        player.Add_Card(self.deck.Draw_Card())
        player.Self_Verify_Card()
        player.Show_Hand()
        choice_success = False            
        while choice_success == False:
            choice = input("What card would you like to see if the other player has (A, J, Q, K)? ")
            if choice not in deck.numbers:
                choice
            elif choice in deck.numbers:
                choice_success = True
            else:
                continue
        print(str(player.name) + " chose: " + str(choice))
        index_of_self = self.players.index(player)
        if index_of_self == 0:
            enemy_player = self.players[1]
        elif index_of_self == 1:
            enemy_player = self.players[0]
        look_for_card = enemy_player.Enemy_Verify_Card(choice)
        if look_for_card == False:
            print("No card was found.")
        else:
            player.Add_Card(look_for_card)
        player.Self_Verify_Card()



    def Start_Game(self):
        while len(self.deck.deck) != 0:
            self.Player_Turn(self.players[0])
            print(str(deck))
            self.Player_Turn(self.players[1])
            print(str(deck))

        print(str(self.players[0].name) + " Score: " + str(len(self.players[0].win_pile)))  
        print(str(self.players[1].name) + " Score: " + str(len(self.players[1].win_pile)))           

                
    #
    # def Player_Turn_Start(self, player):






table = Table()
deck = Deck(numbers, suits)
deck.AssembleDeck()
print(str(table))
print(str(deck))


player1 = Player("Taylor", "1")
player2 = Player("Lincoln", "2")
table.Add_Player(player1)
table.Add_Player(player2)
table.Add_Deck(deck)
print(str(deck))
table.Prep_Game()
table.Start_Game()







