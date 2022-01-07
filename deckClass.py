#Scott Robbins & CJ Duncan
#4/22/20
# This program arranges card objects in a stack to simulate a deck
from cardClass import*

class Deck:
    def __init__(self,win,center):
        self.win= win
        self.center= center
        #deck takes a point to spawn on
        self.order=[]
        #this is a list of every card in deck
        self.played=0
        #keeps track of what card in the list is at at the 'top'
        for j in ["d","c","h","s"]:
            for i in range(1,14):
                card= Card(i,j,win,center)
                self.order.append(card)
        #creates cards with in all suits and ranks
    def shuffle(self):
        for i in range(len(self.order)):
            switcher = randrange(0,len(self.order))
            switch= self.order[switcher]
            self.order.remove(self.order[switcher])
            self.order.append(switch)
        #shuffles by putting a card at end at random
        #does this 52 times for extra thuroughness
        for i in range(len(self.order)):
            self.order[i].play()
        #plays all cards so they can be seen
            
    def deal(self):
        self.played+=1
        return self.order[-(self.played)]
        

