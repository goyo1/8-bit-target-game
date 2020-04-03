# target game
#
#
#
#

from graphics import *
from random import randrange


# creates intro message and returns it


def introduction():
    message = Text(Point(450, 250), 'Welcome to target practice!\n\n'
                   'Try to beat your high score!\n'
                   'Click anywhere to begin :)')
    message.setStyle('bold')
    message.setTextColor('black')
    message.setSize(20)
    return message

# Make squares big fella
# Constructs a rectangle having opposite corners at point1 and point2.


def makeSquare(a, b, c, d, color):
    rect = Rectangle(Point(a, b), Point(c, d))
    rect.setFill(color)
    return rect

# Create random starting point in bottom third of window
# Since our graphics window is 900x900, lets make our range of starting points slightly smaller so that our initial standing point isn't off screen


def pickInitialPoint():
    a = randrange(700, 850)
    b = randrange(700, 850)
    iniPoint = Point(a, b)
    return iniPoint

# Prompts user to pick their bounce point


def pickBouncePoint(i):
    message = Text(Point(450, 50), 'Turn ' +
                   str(i + 1) + ' Click your bounce point')
    message.setStyle('bold')
    message.setSize(20)
    return message

# Calculates landing point using the difference between the initial point and where the user clicks, and returns it


def findFinal(iniCenter, p):
    initial = iniCenter
    bounce_pt = p

    x1 = initial.getX()
    x2 = bounce_pt.getX()
    # calculate dx between the initial point and the point where user clicks
    dx = x1 - x2

    y1 = initial.getY()
    y2 = bounce_pt.getY()
    # calculate dx between the initial point and the point where user clicks
    dy = y1 - y2

    landPoint = Point(x2 - dx, y2 - dy)
    return landPoint


def isInside(finPoint, makeSquare):
    land_center = finPoint.getCenter()
    p1 = makeSquare.getP1()
    p2 = makeSquare.getP2()
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()

    inside = False
    land_x = land_center.getX()
    land_y = land_center.getY()
    if (land_x >= x1 and land_x <= x2) and (land_y >= y1 and land_y <= y2):
        inside = True
    return inside


def computeScore1():
    score = 0
    score += 2
    return score


def computeScore2():
    score = 0
    score += 5
    return score


def computeScore3():
    score = 0
    score += 10
    return score


def result(score):
    message = Text(Point(450, 50), 'Score of ' + str(score) + '. Good Job!')
    message.setStyle('bold')
    message.setSize(20)
    return message


def main():
    win = GraphWin("Target Game", 900, 900)
    win.setBackground('aquamarine2')
    intro = introduction()
    intro.draw(win)
    win.getMouse()
    intro.undraw()

    s1 = makeSquare(200, 200, 700, 700, 'red')
    s1.draw(win)
    s2 = makeSquare(300, 300, 600, 600, 'green')
    s2.draw(win)
    s3 = makeSquare(400, 400, 500, 500, 'blue')
    s3.draw(win)
    s4 = makeSquare(440, 440, 460, 460, 'yellow')
    s4.draw(win)

    score = 0

    for i in range(3):
        start_point = pickInitialPoint()
        # since pickInitialPoint() returns a point, i.e. a pixel, we'll extend its coordinates to make our 'ball' more visible
        extendo1 = start_point.getX() - 10
        extendo2 = start_point.getY() - 10
        extendo3 = start_point.getX() + 10
        extendo4 = start_point.getY() + 10
        # using our starting point, lets extend it so it's more visible in our graphics window
        c1 = Point(extendo1, extendo2)
        c2 = Point(extendo3, extendo4)

        iniPoint = Rectangle(c1, c2)
        iniPoint.setFill('black')
        iniPoint.draw(win)

        bounce = pickBouncePoint(i)
        bounce.draw(win)
        user_click = win.getMouse()
        # undraw initial point and bounce prompt
        iniPoint.undraw()
        bounce.undraw()

        landPoint = findFinal(start_point, user_click)
        p1 = landPoint.getX() - 10
        p2 = landPoint.getY() - 10
        c3 = Point(p1, p2)
        p3 = landPoint.getX() + 10
        p4 = landPoint.getY() + 10
        c4 = Point(p3, p4)

        finPoint = Rectangle(c3, c4)
        finPoint.setFill('black')
        finPoint.draw(win)

        score += score
        inside = isInside(finPoint, s3)
        score1 = computeScore3()
        inside = isInside(finPoint, s2)
        score2 = computeScore2()
        inside = isInside(finPoint, s1)
        score3 = computeScore1()
        score = score1 + score2 + score3

    point = result(score)
    point.draw(win)


main()
