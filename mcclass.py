from graphics import*
from buttonclass import*
from random import randrange

class mchoice:
    def __init__(self):
        textfile=open("mcquestions.txt", "r")
        self.ac1=[]
        self.ac2=[]
        self.ac3=[]
        self.ac4=[]
        self.question=[]
        self.rans=[]
        for line in textfile:
            datalist=line.split(",,")
            self.question.append(datalist[0])
            self.ac1.append(datalist[1])
            self.ac2.append(datalist[2])
            self.ac3.append(datalist[3])
            self.ac4.append(datalist[4])
            self.rans.append(datalist[5])
    def at(self, n, studywin):
        numwr=0
        numcor=0
        chs=Text(Point(200, 50), "Please click the button for\
    which choice you think is the correct answer.")
        chs.draw(studywin)
        nqb=Button(studywin, Point(400, 600), 100, 100, "Next \n Question")
        for i in range(n):
            rannum=randrange(0,len(self.question))
            qest=question[rannum]
            choice1=self.ac1[rannum]
            choice2=self.ac2[rannum]
            choice3=self.ac3[rannum]
            choice4=self.ac4[rannum]
            button1=Button(studywin, Point(235, 200), 400, 50, choice1)
            button2=Button(studywin, Point(235, 300), 400, 50, choice2)
            button3=Button(studywin, Point(235, 400), 400, 50, choice3)
            button4=Button(studywin, Point(235, 500), 400, 50, choice4)
            qbox=Text(Point(400,100), qest)
            qbox.draw(studywin)
            pt=studywin.getMouse()
            while not button1.isClicked and not button2.isClicked and not button3.isClicked and not button4.isClicked(pt):
                pt=studywin.getMouse()
            #if one of the buttons is clicked
            if button1.isClicked(pt) or button2.isClicked(pt) or button3.isClicked(pt) or button4.isClicked(pt):
                if self.rans[rannum]==1:
                    ransb=button1
                elif self.rans[rannum]==2:
                    ransb=button2
                elif self.rans[rannum]==3:
                    ransb=button3
                else:
                    self.ransb=button4
                if ransb.isClicked(pt):
                    ran=randrange(0, len(question))
                    result="correct"
    ##                ac1.pop(i)
    ##                ac1.append(ac1[ran])
    ##                ac2.pop(i)
    ##                ac2.append(ac1[ran])
    ##                ac3.pop(i)
    ##                ac3.append(ac3[ran])
    ##                ac4.pop(i)
    ##                ac4.append(ac4[ran])
    ##                rans.pop(i)
    ##                ac4.append(ac4[ran])
    ##                question.pop(i)
    ##                question.append(question[ran])
                else:
                    result="incorrect"
            tbox=Text(Point(620, 400), "Your answer is " + result + " .")
            tbox.draw(studywin)
            if result=="incorrect":
                ransbox=Text(Point(400,700), "The right answer was answer choice " + str(rans[i]) +" .")
                ransbox.draw(studywin)
                numwr=numwr+1
            elif result=="correct":
                numcor=numcor+1
            pt=studywin.getMouse()
            while not nqb.isClicked(pt):
                pt=studywin.getMouse()
            tbox.undraw()
            qbox.undraw()
            if numwr>0:
                ransbox.undraw()
        chs.undraw()
        nqb.remove()
        button1.remove()
        button2.remove()
        button3.remove()
        button4.remove()
        corbox=Text(Point(200, 400), "You answered"+ str(numcor) +" out of "+str(numcor+numwr)+" questions.")
        corbox.draw(studywin)
        bb=Button(studywin, Point(400, 400), 100, 100, "Back to \n home screen")
        pag=Button(studywin, Point(400, 200), 100, 100, "Play \n again")
        pt=studywin.getMouse()
        while not bb.isClicked(pt):
            if pag.isClicked(pt):
                at(self, n, studywin)
        #back to home screen
