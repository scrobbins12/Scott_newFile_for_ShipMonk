#Scott Robbins & CJ Duncan
#4/22/20
# This program creates an object for a signle match of blackjack
#it uses card and deck objects to set the board
from deckClass import*
from buttonclass import*

class Round:
    #this class creates all the 'materials' for the game
    #it also makes functions for the different actions that 
    #can happen in a game
    def __init__(self,win):
        self.dealerHand=[]
        self.playerHand=[]
        #the player and dealer's hands are lists containing card objects
        self.Deck= Deck(win,Point(240,190))
        self.Deck.shuffle()
        #assigns location of deck on the board and plays in random order
        self.topCard=Card(6,"h",win,Point(240,190))
        self.topCard.hide()
        #Card images show face-up so create a facedown image over deck
        for i in range(2):
            self.playerHand.append(self.Deck.deal())
            self.dealerHand.append(self.Deck.deal())
        #Player and dealer start with 2 cards
            
        
    def hit(self,player):
        #Hitting is adding a card, function is made for both player and dealer hits
        if player == "user":
            self.playerHand.append(self.Deck.deal())
            self.playerHand[-1].move(75*(len(self.playerHand)-2),150)
            #Add card to your hand and also puts card on your side of board
            #Cards 75 pixels apart
        elif player == "dealer":
            self.dealerHand.append(self.Deck.deal())
            self.dealerHand[-1].move(75*(len(self.dealerHand)-2),-110)
            #Add card to dealer hand and also puts card on your side of board
            #Cards 75 pixels apart

    def evaluateHand(self,player):
        #This function is for the routine checks to see if a player busted
        #Has a dealer function for when the dealer makes 'soft 17'
        runningValue= 0
        #regardless of player the hand value is held in this variable
        if player == "user":
            playerAceC=0
            #running count for how many aces in hand
            for card in self.playerHand:
                runningValue+=card.value()
                #adds value of each card to running integer
                if card.rank== 1:
                    playerAceC+=1
                    #adds to ace count when it applies
            while playerAceC >=1:
                if runningValue>21:
                    runningValue-=10
                playerAceC-=1
            #Allow ace to be worth 11 or 1 by subtracting 10 if the 11 would bust
            #You can do this for however many aces in hand

        elif player == "dealer":
            playerAceC=0
            #this for loop does the same thing but checks dealerHand
            for card in self.dealerHand:
                runningValue+=card.value()
                if card.rank== 1:
                    playerAceC+=1
            #makes sure the hand is atleast 17
            #Because aces are worth 11 until changed the 17 can be soft
            while runningValue< 17:
                self.hit("dealer")
                runningValue+=self.dealerHand[-1].value()
            #Ace value detirminant is the same
            while playerAceC >=1:
                if runningValue>=22:
                    runningValue-=10
                playerAceC-=1
            #After other value calculation if still above 21 the dealer busts
        return runningValue
        #Evaluate hand returns the value of the hand as an integer

