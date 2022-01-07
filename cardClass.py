#Scott Robbins & CJ Duncan
#4/22/20
# This program creates a card object by printing an image of a card and
#giving it attributes that a card would have
from random import randrange
from random import random
from graphics import*

class Card:
    def __init__(self, rank, suit,win,center):
        self.rank= rank
        self.suit= suit
        #self.suit is a letter that coorelates with suit
        self.win= win
        self.suitName= self.getSuit()
        #self.suitName is the word representaion of that suit
        self.center= center
        self.image= Image(self.center, (str(self.suit)+str(self.rank)+".gif"))
        #card default shows its value but this variable changes when you hide
    def move(self,x,y):
        self.image.move(x,y)
        
    def play(self):
        self.image.draw(self.win)
    def undraw(self):
        self.image.undraw()
    def hide(self):
        #hide assumes that the card has already been drawn and redraws with-
        #image of card back
        self.image= Image(self.center, ("b1fv.gif"))
        self.image.undraw()
        self.image.draw(self.win)
    def reveal(self):
        #reveal assumes it has been hidden
        self.image.undraw()
        self.image= Image(self.center, (str(self.suit)+str(self.rank)+".gif"))
        self.image.draw(self.win)
    def getRank(self):
        # Returns word output of the card's rank
        if self.rank== 1:
            return "Ace"
        elif self.rank== 2:
            return "Two"
        elif self.rank== 3:
            return "Three"
        elif self.rank== 4:
            return "Four"
        elif self.rank== 5:
            return "Five"
        elif self.rank== 6:
            return "Six"
        elif self.rank== 7:
            return "Seven"
        elif self.rank== 8:
            return "Eight"
        elif self.rank== 9:
            return "Nine"
        elif self.rank== 10:
            return "Ten"
        elif self.rank== 11:
            return "Jack"
        elif self.rank== 12:
            return "Queen"
        elif self.rank== 13:
            return "King"
        
    def getSuit(self):
        if self.suit== "d":
            return "Diamonds"
        if self.suit== "c":
            return "Clubs"
        if self.suit== "h":
            return "Hearts"
        if self.suit== "s":
            return "Spades"

        
        
    def getSuit(self):
        # Returns word output of the card's suit
        if self.suit== "d":
            return "Diamonds"
        elif self.suit== "c":
            return "Clubs"
        elif self.suit== "h":
            return "Hearts"
        elif self.suit== "s":
            return "Spades"
        
    def value(self):
        #for most cards their value is straightforward
        if self.rank>1 and self.rank<=10:
            return int(self.rank)
        elif self.rank>= 11:
            #face cards are worth 10 points
            return 10
        elif self.rank== 1:
            #aces are worth 11 until detirmined otherwise
            return 11
            
    def __str__(self):
        # if the card is called for as a string it would tell you in words not numbers
        return (self.getRank()+ " of "+str(self.getSuit()))
    
