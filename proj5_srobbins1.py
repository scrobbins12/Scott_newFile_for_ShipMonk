#Scott Robbins & CJ Duncan
#4/22/20
# This program is a digital recreation of the 'Blackjack' card game
#It starts with a window explaining the rules of the game and
#then proceeds to a gameplay screen
from roundClass import*
#uses the object of a game round
#that object imports decks and cards

def intro():
    intro = GraphWin("Directions!", 800,400)
    intro.setBackground("Pink")
    #Intro screen is in it's own window
    welcome = Text(Point(200,100),"Welcome!")
    welcome.setFill("Blue")
    state = Text(Point(200,130),"This is a digital Black Jack Game")
    state.setFill("Blue")
    question = Text(Point(200,150),"How to play?")
    question.setFill("Green")
    #Rules of game printed for player
    rule1 = Text(Point(200,170),"1. You and the dealer will be dealt two cards at the start")
    rule2 = Text(Point(280,195),"2. Number cards are worth their value, Face cards worth 10, and Aces 1 or 11")
    rule3 = Text(Point(220,220),"3.You will be given the opportunity to draw more cars by 'hitting'")
    rule4 = Text(Point(235,245),"4.If either player draws higher than 21, they 'bust' and lose the game")
    rule5 = Text(Point(215,270),"5. Start the game by wagering based off of you starting cards")
    rule6 = Text(Point(240,295),"6. Press 'stand' when you think your cards values are closest to 21")
    welcome.draw(intro)
    state.draw(intro)
    question.draw(intro)
    rule1.draw(intro)
    rule2.draw(intro)
    rule3.draw(intro)
    rule4.draw(intro)
    rule5.draw(intro)
    rule6.draw(intro)
    playButton= Button(intro,Point(600,200), 100,100,"Play Game")
    pt= intro.getMouse()
    while not playButton.isClicked(pt):
        pt= intro.getMouse()
    intro.close()
    #user must press play game to start the game
    return True
    #returns true to make the play boolean true

def main():
    #Game relies on a while loop
    #stuff here only renders once
    play = intro()
    #Make playing board and all the buttons and labels 
    board = GraphWin("BlackJack!", 800,400)
    board.setBackground("Green")
    dealerLabel=Text(Point(100,16), "Dealer’s Hand")
    userLabel=Text(Point(80, 300), "Your Hand")
    deckLabel=Text(Point(240, 247), "Deck")
    dealerLabel.setSize(15)
    userLabel.setSize(15)
    deckLabel.setSize(15)
    dealerLabel.draw(board)
    userLabel.draw(board)
    deckLabel.draw(board)
    leave=Button(board,Point(752,25),90,50,"Exit")
    hitButton= Button(board,Point(752,125),90,50,"Hit")
    stayButton= Button(board,Point(752,225),90,50,"Stay")
    ruleButton= Button(board,Point(754,372),90,50,"See\nRules")
    newGame=Button(board,Point(400,190),90,50,"Play Again")
    newGame.deactivate()
    #New game button stays deactivated until you end previous one
    wagerButton= Button(board,Point(600,125),90,50,"Set Wager")
    wagerbox = Entry(Point(600,170),12)
    wagerbox.draw(board)
    #shorthand for win and lose conditions
    win= "You Win!!!"
    lose= "You Lose!!!"
    #Starting amount of money is preset
    money=1000
    
    

    #things at top of while loop happen once every game
    #just to be clear, the last section was once BEFORE all games
    #This is once at the start of each round
    while play==True:
        #set play to false so that the game function loops once
        #will be set back to true later only if player presses play new game
        round1=Round(board)
        for i in range(len(round1.playerHand)):
            if i ==0:
                round1.dealerHand[i].undraw()
                round1.dealerHand[i].hide()
            round1.playerHand[i].move(0,150)
            round1.dealerHand[i].move(0,-110)
        round1.playerHand[0].move(-75,0)
        round1.dealerHand[0].move(-75,0)
        #Many of the following update constantly so you will-
        #see them again in the next section:
        #This part here is so your readout is not dependent-
        #on a mouse click
        wallet= Text(Point(600,70),"You have $"+str(money))
        wallet.draw(board)
        #program would have issue if word was typed into wager so-
        #this suggestion staops accidental disruption
        wagerPrompt=("(Please type in integer value)")
        prompt= Text(Point(600,190),wagerPrompt)
        prompt.draw(board)
        #status is the text that talks to player
        #updates throughout program for whatever needs to be conveyed
        status= "Set Wager"
        result= Text(Point(400,235),status)
        result.draw(board)
        pt= board.getMouse()
        while not wagerButton.isClicked(pt):
            pt= board.getMouse()
            #If they don't hit wager it updates untill they do
            #lets them still hit exit while game waits for wager
            if leave.isClicked(pt):
                board.close()
                return True
                #The return True is just to stop the program
        result.undraw()
        wager= int(wagerbox.getText())
        money-=wager
        #Your money changes to whatever after bet placed
        #redraw money output to match
        wallet.undraw()
        wallet= Text(Point(600,70),"You have $"+str(money))
        wallet.draw(board)
        #after wager button is hit the game tells you your hand worth
        status=str(round1.evaluateHand("user"))
        result= Text(Point(400,235),status)
        result.draw(board)
        #undraw at end so that these don't stay from game to game
        result.undraw()
        wallet.undraw()
        
        #Actions checked for constantly
        while not newGame.isClicked(pt):
            wallet= Text(Point(600,70),"You have $"+str(money))
            #switch from static money output to update each frame so-
            #money jumps or falls the second you win or lose
            if hitButton.isClicked(pt):
                round1.hit("user")
                status= round1.evaluateHand("user")
                if status> 21:
                    status= "Bust!\n"+lose
                    newGame.activate()
            #everytime you hit it recounts hand and checks for a bust
                    
            if status== int:
                if status== 21:
                    status= "21\n"+win
                    money+= 2*wager
                    wallet.undraw()
                    wallet= Text(Point(600,70),"You have $"+str(money))
                    wallet.draw(board)
                    newGame.activate()
                
            elif ruleButton.isClicked(pt):
                intro()
            elif stayButton.isClicked(pt):
                yourScore=round1.evaluateHand("user")
                dealScore=round1.evaluateHand("dealer")
                round1.dealerHand[0].reveal()
                round1.dealerHand[0].move(-75,-110)
                if yourScore== 21:
                    status= win
                    money+= 2*wager
                    wallet= Text(Point(600,70),"You have $"+str(money))
                elif dealScore>21 and yourScore<21:
                    status= "Dealer Bust!\n"+win
                    money+= 2*wager
                    wallet= Text(Point(600,70),"You have $"+str(money))
                elif yourScore>=dealScore and yourScore<=21:
                   status= win
                   money+= 2*wager
                   wallet= Text(Point(600,70),"You have $"+str(money))
                elif yourScore<dealScore and dealScore<=21:
                   status= lose
                newGame.activate()
                if yourScore==dealScore and yourScore<=21:
                    status= "It's a Tie!\nReturn Bets!!!"
                    money+= wager
                    wallet= Text(Point(600,70),"You have $"+str(money))
            elif leave.isClicked(pt):
                board.close()
                return True
                #The return True is just to stop the program
            result= Text(Point(400,235),status)
            result.draw(board)
            wallet.draw(board)
            pt= board.getMouse()
            wallet.undraw()
            result.undraw()
        for card in round1.playerHand:
            card.undraw()
        for card in round1.dealerHand:
            card.undraw()
        for card in round1.Deck.order:
            card.undraw()
        round1.topCard.undraw()
        newGame.deactivate()

main()
