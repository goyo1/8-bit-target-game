# target game
#
#
#

from graphics import *
from button import *
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


def makeBounds(a, b, c, d):
    p1 = Point(a, b)
    p2 = Point(c, d)
    lineBounds = Line(p1, p2)
    return lineBounds

# Create random starting point in bottom third of window
# Since our graphics window is 900x900, lets make our range of starting points slightly smaller
# so that our initial starting point isn't off screen


def pickInitialPoint():
    a = randrange(50, 850)
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

# Draws the values of each target square


def score_label(a, b, n):
    message = Text(Point(a, b), str(n))
    message.setStyle('bold')
    message.setTextColor('black')
    message.setSize(15)
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


def run_game(win, s1, s2, s3, s4, draw_list):
    score = 0
    for i in range(3):
        start_point = pickInitialPoint()
        # since pickInitialPoint() returns a point, i.e. a pixel, we'll extend its coordinates to make our 'ball' more visible
        extendo1 = start_point.getX() - 10
        extendo2 = start_point.getY() - 10
        extendo3 = start_point.getX() + 10
        extendo4 = start_point.getY() + 10

        c1 = Point(extendo1, extendo2)
        c2 = Point(extendo3, extendo4)
        # using the extension points, create a rectangle with the initial point as its center
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
        draw_list.append(finPoint)

        compute = computeScore(finPoint, s1, s2, s3, s4)
        score += compute
    return score

# Takes the landing point returned by findFinal() and returns a boolean of whether or not it's inside a square
# in the target using the corners of the target square and the landing point


def isInside(finPoint, makeSquare):
    # Grabs center point of where the "ball" landed
    land_center = finPoint.getCenter()

    # Grabs corner points of makeSquare
    p1 = makeSquare.getP1()
    p2 = makeSquare.getP2()

    # Grabs individual x and y values of p1 and p2
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()

    inside = False
    land_x = land_center.getX()
    land_y = land_center.getY()

    # Determines whether or not "ball" is inside a square
    if (land_x >= x1 and land_x <= x2) and (land_y >= y1 and land_y <= y2):
        inside = True
    return inside

# Takes the inner, middle, and outer targets of game and gives appropriate score depending on where the "ball" landed


def computeScore(finPoint, s1, s2, s3, s4):
    round_score = 0

    bonus = isInside(finPoint, s4)
    inner = isInside(finPoint, s3)
    middle = isInside(finPoint, s2)
    outer = isInside(finPoint, s1)

    if bonus == True:
        round_score += 25
    elif inner == True:
        round_score += 10
    elif middle == True:
        round_score += 5
    elif outer == True:
        round_score += 2
    else:
        round_score += 0
    return round_score

# draws results message at the top of screen after final turn


def result(score):
    message = Text(Point(450, 50), 'Score of ' + str(score))
    message.setStyle('bold')
    message.setSize(20)
    return message


def remove(draw_list):
    for element in draw_list:
        element.undraw()


def play_again():
    message = Text(Point(450, 750),
                   "Click anywhere to play again, or 'Quit' below to exit")
    message.setStyle('bold')
    message.setSize(20)
    return message


def main():
    win = GraphWin("Target Game", 900, 950)
    intro = introduction()
    intro.draw(win)
    pt = win.getMouse()
    intro.undraw()

    draw_list = []

    s1 = makeSquare(200, 100, 700, 600, 'red')
    s1.draw(win)
    left_2 = score_label(250, 350, 2)
    left_2.draw(win)
    right_2 = score_label(650, 350, 2)
    right_2.draw(win)

    s2 = makeSquare(300, 200, 600, 500, 'green')
    s2.draw(win)
    left_5 = score_label(350, 350, 5)
    left_5.draw(win)
    right_5 = score_label(550, 350, 5)
    right_5.draw(win)

    s3 = makeSquare(400, 300, 500, 400, 'blue')
    s3.draw(win)
    left_10 = score_label(420, 350, 10)
    left_10.draw(win)
    right_10 = score_label(480, 350, 10)
    right_10.draw(win)

    s4 = makeSquare(440, 340, 460, 360, 'yellow')
    s4.draw(win)

    lineBounds = makeBounds(0, 875, 900, 875)
    lineBounds.draw(win)

    quit = Button(win, Point(450, 900), 100, 50, 'Quit')
    quit.deactivate()

    while not quit.clicked(pt):
        score = run_game(win, s1, s2, s3, s4, draw_list)

        point = result(score)
        point.draw(win)
        draw_list.append(point)
        play_or_exit = play_again()
        play_or_exit.draw(win)
        draw_list.append(play_or_exit)
        quit.activate()
        pt = win.getMouse()
        remove(draw_list)

    win.close()


main()
