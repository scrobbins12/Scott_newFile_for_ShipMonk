# buttonClass.py
from graphics import *

class Button:
    
    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, words):
        ## as you read through this, ask yourself:  what are the instance variables here?
        ## it would be useful to add comments describing what some of these variables are for...
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        ## you should comment these variables...
        self.xmax, self.xmin = x+w, x-w 
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray') #make the button gray
        self.rect.draw(win)
        self.label = Text(center, words)
        self.label.draw(win)
        self.activate() ##this line was not there in class, what does it do?

    def getLabel(self):
        """Returns the label string of this button."""
        return self.label.getText()
    
    def setLabel(self, words):
        self.label.setText(words)

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black') #color the text "black"
        self.rect.setWidth(2)       #set the outline to look bolder
        self.active = True          #set the boolean variable that tracks "active"-ness to True

    ##check 3.  complete the deactivate() method
    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill("white")
        self.rect.setWidth(1)
        self.active=False
        ##color the text "darkgray"
        ##set the outline to look finer/thinner
        ##set the boolean variable that tracks "active"-ness to False

    ##check 4.  complete the clicked() method
    def isClicked(self, p):
        """Returns true if button active and Point p is inside"""
        print(p.getX(), p.getY())
        if(self.xmin < p.getX() < self.xmax and self.ymin < p.getY() < self.ymax and self.active):
            return True
        else:
            return False
        ##your code here
    def remove(self):
        """Remvoves object"""
        self.rect.undraw()
        self.label.undraw()
        

    
def main():
    win=GraphWin("Window", 800, 800)
    ##check 2. create a graphical window in which to test the Button class
    rollButton=Button(win, Point(400,400), 100, 100, "rolldice")
    
    ##check 3. test the Button constructor method...
    
    ##create two Button objects, one for "Roll Dice" and the other for "Quit"
    
    ##activate the Roll button
    
    pt=win.getMouse()
    ##check 4. now test the deactivate() method...
    ##deactivate the "Quit" button

    rollButton.setLabel("Hi")
    ##check 5. test the .clicked() method with an if statement
    ##(remove this test code before moving onto the next check)
    ##check 6: 
    ##loop until the "Quit" button is clicked...
        ##if the roll button is clicked
            ##activate the quit button
        ##take the next mouse click
            
        
    #we reach this line of code when quit button is clicked b/c loop condition breaks
     #so close the window, ending the program
    pt=win.getMouse()
    while not rollButton.isClicked(pt):
        pt=win.getMouse
    print("hi")
if __name__ == "__main__": 
    main()
##
