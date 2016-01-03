[Interactive Programming with Python - Part 2]

[Mouse Input]

===

# Examples of mouse input

import simplegui
import math

# intialize globals
WIDTH = 450
HEIGHT = 300
ball_pos = [WIDTH / 2, HEIGHT / 2]
BALL_RADIUS = 15
ball_color = "Red"

# helper function
def distance(p, q):
    return math.sqrt( (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):
    global ball_pos, ball_color
    if distance(pos, ball_pos) < BALL_RADIUS:
        ball_color = "Green"
    else:
        ball_pos = list(pos)
        ball_color = "Red"

def draw(canvas):
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Black", ball_color)

# create frame
frame = simplegui.create_frame("Mouse selection", WIDTH, HEIGHT)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()

===

[List Methods]

lst = [1,82,-6,4,3,8]
print lst[2] #=> -6
print lst[-1] #=> 8

in --> allow me to check if something is in the list # T/F
index --> tells me where it is in the list:
lst.index(8) --> 5 (index value of 8 in lst)

append --> change the list, 
pop --> removes element

lst.append(632)
lst = [1,82,-6,4,3,8,632]

lst.pop() # removes the last element
lst = [1,82,-6,4,3,8]
lst.pop(4) # removes the element at index 4

===

# Simple task list

import simplegui

tasks = []

# Handler for button
def clear():
    global tasks
    tasks = []
    
# Handler for new task
def new(task):
    tasks.append(task)
    
# Handler for remove number
def remove_num(tasknum):
    n = int(tasknum)
    if n > 0 and n <= len(tasks):
        tasks.pop(n-1)

# Handler for remove name
def remove_name(taskname):
    if taskname in tasks:
        tasks.remove(taskname) # !!!!
        tasks.pop(tasks.index(taskname)) # same as line above!
    
# Handler to draw on canvas
def draw(canvas):
    n = 1
    for task in tasks:
        pos = 30 * n
        canvas.draw_text(str(n) + ": " + task, [5, pos], 24, "White")
        n += 1
        
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Task List", 600, 400)
frame.add_input("New task:", new, 200)
frame.add_input("Remove task number:", remove_num, 200)
frame.add_input("Remove task:", remove_name, 200)
frame.add_button("Clear All", clear)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

===

[List Examples]

===

# Examples of mouse input

import simplegui
import math

# intialize globals
width = 450
height = 300
ball_list = []
ball_radius = 15
ball_color = "Red"

# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):
    ball_list.append(pos)
#    if distance(ball_pos, pos) < ball_radius:
#        if ball_color == "Red":
#            ball_color = "Green"
#    else:
#        ball_pos = [pos[0], pos[1]]
#        ball_color = "Red"

def draw(canvas):
    for ball_pos in ball_list: 
        canvas.draw_circle(ball_pos, ball_radius, 1, "Black", ball_color)
    
# create frame
frame = simplegui.create_frame("Mouse selection", width, height)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()

===

# Examples of mouse input

import simplegui
import math

# intialize globals
width = 450
height = 300
ball_list = []
ball_radius = 15

# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):
    changed = False
    for ball in ball_list:
        if distance([ball[0], ball[1]], pos) < ball_radius:
            ball[2] = "Green"
            changed = True

    if not changed:
        ball_list.append([pos[0], pos[1], "Red"])

def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle([ball[0], ball[1]], ball_radius, 1, "Black", ball[2])
    
# create frame
frame = simplegui.create_frame("Mouse selection", width, height)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()

===

# Examples of mouse input

import simplegui
import math

# intialize globals
width = 450
height = 300
ball_list = []
ball_radius = 15
ball_color = "Red"

# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):
    remove = []
    for ball in ball_list:
        if distance(ball, pos) < ball_radius:
            remove.append(ball) # never remove something from a list while iterating over it, keep track of it and remove them later

    if remove == []:
        ball_list.append(pos)
    else:
        for ball in remove:
            ball_list.pop(ball_list.index(ball))

def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle([ball[0], ball[1]], ball_radius, 1, "Black", ball_color)
    
# create frame
frame = simplegui.create_frame("Mouse selection", width, height)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()

===

[Iteration]

# Iterating over lists

def count_odd(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 1:
            count += 1
    return count

def check_odd(numbers):
    for num in numbers:
        if num % 2 == 1:
            return True -- as soon as a function hits a return, it stops functioning! no need to use break :-)
    return False

def remove_odd(numbers):
    for num in numbers:
        if num % 2 == 1:
            numbers.remove(num)

def remove_odd2(numbers):
    remove = []
    for num in numbers:
        if num % 2 == 1:
            remove.append(numbers.index(num))
            
    for idx in remove:
        numbers.pop(idx)
        
def remove_odd3(numbers):
    remove = []
    for num in numbers:
        if num % 2 == 1:
            remove.append(num)
            
    for num in remove:
        numbers.remove(num)
        
def remove_odd4(numbers):
    newnums = []
    for num in numbers:
        if num % 2 == 0:
            newnums.append(num)
    return newnums
   
def remove_last_odd(numbers):
    has_odd = False
    last_odd = 0
    for num in numbers:
        if num % 2 == 1:
            has_odd = True
            last_odd = num
            
    if has_odd:
        numbers.remove(last_odd)
        

def run():
    numbers = [1, 7, 2, 34, 8, 7, 2, 5, 14, 22, 93, 48, 76, 15, 7]
    print numbers
    remove_last_odd(numbers)
    print numbers
    
run()

===

[Dictionaries]

- Mapping
+ Map keys to Values
d = {1:2,3:4,6:727,83:422}
d[1] = 37 #=> value of key 1 will become 37

list --> indices are fixed (0,1,2,3,4, etc.)
dictionary --> indices are keys
- when you iterate over a dictionary you iterate through the keys
- CONSTANTS should be CAPITALIZED

# Cipher

import simplegui
import random 

CIPHER = {'a': 'x', 'b': 'c', 'c': 'r', 'd': 'm', 'e': 'l'}

message = ""

LETTERS = "abcdefghijklmnopqrstuvwxyz"

def init():
    letter_list = list(LETTERS)
    random.shuffle(letter_list)
    for ch in LETTERS:
        CIPHER[ch] = letter_list.pop()

# Encode button
def encode():
    emsg = ""
    for ch in message:
        emsg += CIPHER[ch]
    print message, "encodes to", emsg

# Decode button
def decode():
    dmsg = ""
    for ch in message:
        for key, value in CIPHER.items():
            if ch == value:
                dmsg += key
    print message, "decodes to", dmsg

# Update message input
def newmsg(msg):
    global message
    message = msg
    label.set_text(msg)
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Cipher", 2, 200, 200)
frame.add_input("Message:", newmsg, 200)
label = frame.add_label("", 200)
frame.add_button("Encode", encode)
frame.add_button("Decode", decode)

# Start the frame animation
frame.start()

===

[Images]

Load an image for use in SimpleGUI:

im = simplegui.load_image(URL)
# URL example for map magnifier: "http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg"

Tips

1 - We will provide all images you need for the class in Google Storage
2 - If you wish to create and use your own images, make sure that image is accessible via the web. Cut and paste the image into a web browser to test it. Make sure it is downloadable.
3 - We will show you how to download images from you dropbox account in week six.
4 - Remember that loading images across the web takes time. The image may nog appear immediately the first time you try to load it into CodeSkulptor

- Drawing Images

canvas.draw_image(im,src_center,src_size,dst_center,dst_size)

Tips 

1 - Attempting to draw before load finishes causes draw to fail. Execution continues.
2 - Source rectangle not lying entirely on canvas causes draw to fail. Execution continues.

Gutenberg project map - 1521 pixels wide, 1821 pixels high

- Too large to draw completely on canvas at full resolution
- Strategy: scale resolution down by a factor of three and draw reduced resolution image
- Click on canvas: display small portion of image as orginial resolution around click location
- Two calls to draw_image:
+ First draws entire map at reduced resolution
+ Second draws magnfifier pane around mouse click

===

# Demonstration of a magnifier on a map

import simplegui

# 1521x1818 pixel map of native American language
# source - Gutenberg project

image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")

# Image dimensions
MAP_WIDTH = 1521
MAP_HEIGHT = 1818

# Scaling factor
SCALE = 3

# Canvas size
CAN_WIDTH = MAP_WIDTH // SCALE
CAN_HEIGHT = MAP_HEIGHT // SCALE

# Size of magnifier pane and initial center
MAG_SIZE = 120
mag_pos = [CAN_WIDTH // 2, CAN_HEIGHT // 2]


# Event handlers
# Move magnifier to clicked position
def click(pos):
    global mag_pos
    mag_pos = list(pos)

# Draw map and magnified region
def draw(canvas):
    # Draw map
    canvas.draw_image(image, 
            [MAP_WIDTH // 2, MAP_HEIGHT // 2], [MAP_WIDTH, MAP_HEIGHT], 
            [CAN_WIDTH // 2, CAN_HEIGHT // 2], [CAN_WIDTH, CAN_HEIGHT])

    # Draw magnifier    
    map_center = [SCALE * mag_pos[0], SCALE * mag_pos[1]]
    map_rectangle = [MAG_SIZE, MAG_SIZE]
    mag_center = mag_pos
    mag_rectangle = [MAG_SIZE, MAG_SIZE]
    canvas.draw_image(image, map_center, map_rectangle, mag_center, mag_rectangle)
    
# Create frame for scaled map
frame = simplegui.create_frame("Map magnifier", CAN_WIDTH, CAN_HEIGHT)

# register even handlers
frame.set_mouseclick_handler(click)    
frame.set_draw_handler(draw)

# Start frame
frame.start()

===

-- Go through examples...

[Visualizing Iteration]

def square_list1(numbers):
    """Returns a list of the squares of the numbers in the input."""
    result = []
    for n in numbers:
        result.append(n ** 2)
    return result

def square_list2(numbers):
    """Returns a list of the squares of the numbers in the input."""
    return [n ** 2 for n in numbers] # list comprehension

print square_list1([4, 5, -2])
print square_list2([4, 5, -2])

print [2 * x for x in range(5)]
#=> [0,2,4,6,8]

def is_in_range(ball):
    """Returns whether the ball is in the desired range.  """
    return ball[0] >= 0 and ball[0] <= 100 and ball[1] >= 0 and ball[1] <= 100


def balls_in_range1(balls):
    """Returns a list of those input balls that are within the desired range."""
    result = []
    for ball in balls:
        if is_in_range(ball):
            result.append(ball)
    return result

def balls_in_range2(balls):
    return [ball for ball in balls if is_in_range(ball)]

print balls_in_range1([[-5,40], [30,20], [70,140], [60,50]])
print balls_in_range2([[-5,40], [30,20], [70,140], [60,50]])

===

[Programming Tips]

l = range(5)
print len(l)
print l[5] # out of range error

d[500] = 'wow' --> if 500 is not already in dictionary, it will create key 500 and assign it 'wow'

d[(1,2)] = 10 # works
d[[1,2]] = 10 # does not work --> unhashable type (mutable)
d[{}] = 10 # does not work --> unhashable type (mutable)

-- keys have to be immutable!

[Memory]

# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric

http://www.codeskulptor.org/#user40_PgOdSvCHkI_0.py

===

# simple state example for Memory

import simplegui
     
# define event handlers
def new_game():
    global state
    state = 0
    
def buttonclick():
    global state
    if state == 0:
        state = 1
    elif state == 1:
        state = 2
    else:
        state = 1
                         
def draw(canvas):
    canvas.draw_text(str(state) + " card exposed", [30, 62], 24, "White")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory states", 200, 100)
frame.add_button("Restart", new_game, 200)
frame.add_button("Simulate mouse click", buttonclick, 200)


# register event handlers
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

http://www.codeskulptor.org/#user40_PgOdSvCHkI_24.py

# implementation of card game - Memory

import simplegui
import random

list_a = range(0,8)
list_b = range(0,8)
list_c = list_a + list_b

exposed = [False,False,False,False,False,False,False,False,
           False,False,False,False,False,False,False,False]

num_turns = 0
state = 0
pair = list()
pair_index = list()
set_text = "Turns = " + str(num_turns)

# helper function to initialize globals

def new_game():
    global state, exposed, pair, pair_index, num_turns, set_text
    state = 0
    random.shuffle(list_c)
    for i in range(0,16):
        exposed[i] = False
    pair = list()
    pair_index = list()
    num_turns = 0
    set_text = "Turns = " + str(num_turns)
    label.set_text(set_text)
    
# define event handlers

def mouseclick(pos):
    global state, pair, pair_index, exposed, completed, num_turns, set_text
    lst = list(pos)
    index = lst[0] // 50
    
    if state == 0:
        if exposed[index] == False:
            exposed[index] = True
            pair_index.append(index)
            pair.append(list_c[index])
            state = 1
        else:
            pass
        
    elif state == 1:
         if exposed[index] == False:
            exposed[index] = True
            pair_index.append(index)
            pair.append(list_c[index])
            state = 2
         elif exposed[index] == True:
             pass
             
    else: # state 2
         if exposed[index] == True:
                pass
         elif pair[0] != pair[1]:       
              exposed[index] = True
              exposed[pair_index[0]] = False
              exposed[pair_index[1]] = False
              pair = list()
              pair_index = list()
              pair_index.append(index)
              pair.append(list_c[index])
              state = 1
              num_turns += 1
              set_text = "Turns = " + str(num_turns)
              label.set_text(set_text)
         else:
             exposed[index] = True
             pair = list()
             pair_index = list()
             pair_index.append(index)
             pair.append(list_c[index])
             state = 1
             num_turns += 1
             set_text = "Turns = " + str(num_turns)
             label.set_text(set_text)
                    
# cards are logically 50x100 pixels in size  

def draw(canvas):
    num_pos = 10
    card_pos = 25
    index = 0
    for i in list_c:
        if exposed[index] == False:
            canvas.draw_line([card_pos,0],[card_pos,100],48,"Green")
            card_pos += 50
            num_pos += 50
            index += 1
        else:    
            canvas.draw_text(str(i), [num_pos,70], 72, "White")
            num_pos += 50
            card_pos += 50
            index += 1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric

[Classes]

- Objected-Oriented Programming

===

class Character: # class names are capitalised 
    
    def __init__(self, name, initial_health):
        self.name = name
        self.health = initial_health
        self.inventory = []
        
    def __str__(self):
        s  = "Name: " + self.name
        s += " Health: " + str(self.health)
        s += " Inventory: " + str(self.inventory)
        return s
    
    def grab(self, item):
        self.inventory.append(item)
        
    def get_health(self):
        return self.health
    
def example():
    me = Character("Bob", 20)
    print str(me)
    me.grab("pencil")
    me.grab("paper")
    print str(me)
    print "Health:", me.get_health()
    
example()

===

# ball physics code for generic 2D domain
# the functions inside() and normal() encode the shape of the ennvironment

import simplegui
import random
import math

# Canvas size
width = 600
height = 400

# Ball traits
radius = 20
color = "White"

# math helper function
def dot(v, w):
    return v[0] * w[0] + v[1] * w[1]

class RectangularDomain:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.border = 2

    # return if bounding circle is inside the domain    
    def inside(self, center, radius):
        in_width = ((radius + self.border) < center[0] < 
                    (self.width - self.border - radius))
        in_height = ((radius + self.border) < center[1] < 
                     (self.height - self.border - radius))
        return in_width and in_height

    # return a unit normal to the domain boundary point nearest center
    def normal(self, center):
        left_dist = center[0]
        right_dist = self.width - center[0]
        top_dist = center[1]
        bottom_dist = self.height - center[1]
        if left_dist < min(right_dist, top_dist, bottom_dist):
            return (1, 0)
        elif right_dist < min(left_dist, top_dist, bottom_dist):
            return (-1, 0)
        elif top_dist < min(bottom_dist, left_dist, right_dist):
            return (0, 1)
        else:
            return (0, -1)

    # return random location
    def random_pos(self, radius):
        x = random.randrange(radius, self.width - radius - self.border)
        y = random.randrange(radius, self.height - radius - self.border)
        return [x, y]

    # Draw boundary of domain
    def draw(self, canvas):
        canvas.draw_polygon([[0, 0], [self.width, 0], 
                             [self.width, self.height], [0, self.height]],
                             self.border*2, "Red")
        
class CircularDomain:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        self.border = 2
        
    # return if bounding circle is inside the domain    
    def inside(self, center, radius):
        dx = center[0] - self.center[0]
        dy = center[1] - self.center[1]
        dr = math.sqrt(dx ** 2 + dy ** 2)
        return dr < (self.radius - radius - self.border)

    # return a unit normal to the domain boundary point nearest center
    def normal(self, center):
        dx = center[0] - self.center[0]
        dy = center[1] - self.center[1]
        dr = math.sqrt(dx ** 2 + dy ** 2)
        return [dx / dr, dy / dr]
    
    # return random location
    def random_pos(self, radius):
        r = random.random() * (self.radius - radius - self.border)
        theta = random.random() * 2 * math.pi
        x = r * math.cos(theta) + self.center[0]
        y = r * math.sin(theta) + self.center[1]
        return [x, y]
        
    # Draw boundary of domain
    def draw(self, canvas):
        canvas.draw_circle(self.center, self.radius, self.border*2, "Red")
    
class Ball:
    def __init__(self, radius, color, domain):
        self.radius = radius
        self.color = color
        self.domain = domain
        
        self.pos = self.domain.random_pos(self.radius)
        self.vel = [random.random() + .1, random.random() + .1]
        
    # bounce
    def reflect(self):
        norm = self.domain.normal(self.pos)
        norm_length = dot(self.vel, norm)
        self.vel[0] = self.vel[0] - 2 * norm_length * norm[0]
        self.vel[1] = self.vel[1] - 2 * norm_length * norm[1]
    

    # update ball position
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        if not self.domain.inside(self.pos, self.radius):
            self.reflect()

    # draw
    def draw(self, canvas):
        canvas.draw_circle(self.pos, self.radius, 1, 
                           self.color, self.color)
        

# generic update code for ball physics
def draw(canvas):
    ball.update()
    field.draw(canvas)
    ball.draw(canvas)

field = RectangularDomain(width, height)
# field = CircularDomain([width/2, height/2], 180)
ball = Ball(radius, color, field)
        
frame = simplegui.create_frame("Ball physics", width, height)

frame.set_draw_handler(draw)

frame.start()

===

- Working with objects

# Particle class example used to simulate diffusion of molecules

import simplegui
import random

# global constants
WIDTH = 600
HEIGHT = 400
PARTICLE_RADIUS = 5
COLOR_LIST = ["Red", "Green", "Blue", "White"]
DIRECTION_LIST = [[1,0], [0, 1], [-1, 0], [0, -1]]


# definition of Particle class
class Particle:
    
    # initializer for particles
    def __init__(self, position, color):
        self.position = position
        self.color = color
        
    # method that updates position of a particle    
    def move(self, offset):
        self.position[0] += offset[0]
        self.position[1] += offset[1]
        
    # draw method for particles
    def draw(self, canvas):
        canvas.draw_circle(self.position, PARTICLE_RADIUS, 1, self.color, self.color)
    
    # string method for particles
    def __str__(self):
        return "Particle with position = " + str(self.position) + " and color = " + self.color


# draw handler
def draw(canvas):
    for p in particle_list:
        p.move(random.choice(DIRECTION_LIST))
    
    for p in particle_list:
        p.draw(canvas)


# create frame and register draw handler
frame = simplegui.create_frame("Particle simulator", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# create a list of particles
particle_list = []
for i in range(100):
    p = Particle([WIDTH / 2, HEIGHT / 2], random.choice(COLOR_LIST))
    particle_list.append(p)

# start frame
frame.start()

===

# Testing template for Particle class


###################################################
# Student should add code for the Particle class here
    


###################################################
# Test code for the Particle class


p = Particle([20, 20], "Red")
print p
print type(p)
p.move([10, 20])
print p
p.move([-15, -25])
print p
print
q = Particle([15, 30], "Green")
print q
print type(q)
q.move([0, 0])
print q


###################################################
# Output from test

#Particle with position = [20, 20] and color = Red
#<class '__main__.Particle'>
#Particle with position = [30, 40] and color = Red
#Particle with position = [15, 15] and color = Red
#
#Particle with position = [15, 30] and color = Green
#<class '__main__.Particle'>
#Particle with position = [15, 30] and color = Green

===

-- Blackjack Classes

===

# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 950x392 - source: jfitz.com
CARD_SIZE = (73, 98)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize global variables
deck = []
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            print "Invalid card: ", self.suit, self.rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (card_size[0] * (0.5 + RANKS.index(self.rank)), card_size[1] * (0.5 + SUITS.index(self.suit)))
        canvas.draw_image(card_images, card_loc, card_size, [pos[0] + card_size[0] / 2, pos[1] + card_size[1] / 2], card_size)
        
# define hand class
class Hand:
    def __init__(self):
        pass    # replace with your code

    def __str__(self):
        pass    # replace with your code

    def add_card(self, card):
        pass    # replace with your code

    # count aces as 1, if the hand has an ace, then add 10 to hand value if don't bust
    def get_value(self):
        pass    # replace with your code

    def busted(self):
        pass    # replace with your code
    
    def draw(self, canvas, p):
        pass    # replace with your code
 
        
# define deck class
class Deck:
    def __init__(self):
        pass    # replace with your code

    # add cards back to deck and shuffle
    def shuffle(self):
        pass    # replace with your code

    def deal_card(self):
        pass    # replace with your code


#define callbacks for buttons
def deal():
    global outcome, in_play

    # your code goes here
    
    outcome = ""
    in_play = True

def hit():
    pass    # replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign an message to outcome, update in_play and score
       
def stand():
    pass    # replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

def draw(canvas):
    pass    # replace with your code below


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deal an initial hand

# get things rolling
frame.start()

# Grading rubric - 18 pts total (scaled to 100)

# 1 pt - The program opens a frame with the title "Blackjack" appearing on the canvas.
# 3 pts - The program displays 3 buttons ("Deal", "Hit" and "Stand") in the control area. (1 pt per button)
# 2 pts - The program graphically displays the player's hand using card sprites. 
#       (1 pt if text is displayed in the console instead) 
# 2 pts - The program graphically displays the dealer's hand using card sprites. 
#       Displaying both of the dealer's cards face up is allowable when evaluating this bullet. 
#       (1 pt if text displayed in the console instead)
# 1 pt - Hitting the "Deal" button deals out new hands to the player and dealer.
# 1 pt - Hitting the "Hit" button deals another card to the player. 
# 1 pt - Hitting the "Stand" button deals cards to the dealer as necessary.
# 1 pt - The program correctly recognizes the player busting. 
# 1 pt - The program correctly recognizes the dealer busting. 
# 1 pt - The program correctly computes hand values and declares a winner. 
#       Evalute based on player/dealer winner messages. 
# 1 pt - The dealer's hole card is hidden until the hand is over when it is then displayed.
# 2 pts - The program accurately prompts the player for an action with the messages 
#        "Hit or stand?" and "New deal?". (1 pt per message)
# 1 pt - The program keeps score correctly.

===

[Tiled Images]

CARD_SIZE = (73,98)
CARD_CENTER = (36.5,49)

card_pos = (CARD_CENTER[0] + i * CARD_SIZE[0],
            CARD_CENTER[1] + j * CARD_SIZE[1])

canvas.draw_image(tiled_image, card_pos, CARD_SIZE, ...)

===

# demo for drawing using tiled images

import simplegui

# define globals for cards
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
SUITS = ('C', 'S', 'H', 'D')

# card sprite - 950x392
CARD_CENTER = (36.5, 49)
CARD_SIZE = (73, 98)
card_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

# define card class
class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def draw(self, canvas, loc):
        i = RANKS.index(self.rank)
        j = SUITS.index(self.suit)
        card_pos = [CARD_CENTER[0] + i * CARD_SIZE[0],
                    CARD_CENTER[1] + j * CARD_SIZE[1]]
        canvas.draw_image(card_image, card_pos, CARD_SIZE, loc, CARD_SIZE)

# define draw handler        
def draw(canvas):
    one_card.draw(canvas, (155, 90))

# define frame and register draw handler
frame = simplegui.create_frame("Card draw", 300, 200)
frame.set_draw_handler(draw)

# createa card
one_card = Card('S', '6')

frame.start()

===

##################
# Object creation and use
# Mutation with Aliasing

class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def set_x(self, newx):
        self.x = newx
    
    def get_x(self):
        return self.x

p = Point1(4, 5)
q = Point1(4, 5)
r = p

p.set_x(10)

print p.get_x()
print q.get_x()
print r.get_x()


##################
# Object shared state
# Mutation of shared state

class Point2:
    def __init__(self, coordinates):
        self.coords = coordinates
    
    def set_coord(self, index, value):
        self.coords[index] = value
    
    def get_coord(self, index):
        return self.coords[index]

coordinates = [4, 5]
p = Point2(coordinates)
q = Point2(coordinates)
r = Point2([4, 5])

p.set_coord(0, 10)

print p.get_coord(0)
print q.get_coord(0)
print r.get_coord(0)


##################
# Objects not sharing state

class Point3:
    def __init__(self, coordinates):
        self.coords = list(coordinates)
    
    def set_coord(self, index, value):
        self.coords[index] = value
    
    def get_coord(self, index):
        return self.coords[index]

coordinates = [4, 5]
p = Point3(coordinates)
q = Point3(coordinates)
r = Point3([4, 5])

p.set_coord(0, 10)

print p.get_coord(0)
print q.get_coord(0)
print r.get_coord(0)

===

[Programming Tips]

###################
# Broken code

class ball:
    def ball(pos, rad):
        position = pos
        radius = rad
        return ball
    
    def get_position():
        return position

b = ball([0,0], 10)

print get_position(b)

###################
# Fixed code

class Ball:
    def __init__(self, pos, rad):
        self.position = pos
        self.radius = rad
    
    def get_position(self):
        return self.position

b = Ball([0,0], 10)

print b.get_position()

##################
# Example while

def countdown(n):
    """Print the values from n to 0."""

    i = n
    while i >= 0:
        print i
        i -= 1

countdown(5)

##################
# Collatz

def collatz(n):
    """Prints the values in the Collatz sequence for n."""

    i = n
    while i > 1:
        print i
        
        if i % 2 == 0:
            i = i / 2
        else:
            i = 3 * i + 1
           
collatz(1000)

#################
# Timeout

i = 1
while i > 0:
    i += 1
    
print "Done!"

[Blackjack]

- Determining the value of a hand

Value of a card in Blackjack
- Number card has value equal to the number
- Face card (K, Q, J) has value 10
- Ace has value 1 or 11 (players choice)

Value of a Blackjack hand
- Key observation: Never count two Aces as 11

Let hand_value be the sum of the card values with Aces as 1.
If the hand has no Aces:
return hand_value
elif: hand_value + 10 <= 21:
    return hand_value + 10
else: return hand_value

Determining when the dealer should stand

while the value_dealer_hand < 17:
    hit the dealers hand

while test:
    body

Use the get_value method for a hand inside test
Use the hit method for hand inside the body

dealer wins ties

===

# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        pass    # create Hand object

    def __str__(self):
        pass    # return a string representation of a hand

    def add_card(self, card):
        pass    # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        pass    # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        pass    # draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        pass    # create a Deck object

    def shuffle(self):
        # shuffle the deck 
        pass    # use random.shuffle()

    def deal_card(self):
        pass    # deal a card object from the deck
    
    def __str__(self):
        pass    # return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, in_play

    # your code goes here
    
    in_play = True

def hit():
    pass    # replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    pass    # replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    card = Card("S", "A")
    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric

http://www.codeskulptor.org/#user40_Cx0yBpySGN_12.py

===

class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.initial_balance = initial_balance
        self.fee_count = 0
       
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.amount = amount
        self.initial_balance += self.amount
           
    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        self.amount = amount
        fees = 0
        if self.initial_balance < 0:
            self.initial_balance -= self.amount
        elif self.initial_balance - self.amount < 0:
            self.initial_balance -= (self.amount + 5)
            self.fee_count += 1
        else:
            self.initial_balance -= self.amount
            
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.initial_balance
        
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fee_count * 5

===

# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand_cards = list()

    def __str__(self):
        ans = ""
        for i in range(len(self.hand_cards)):
            ans += str(self.hand_cards[i]) + " "
        return "Hand contains " + ans

    def add_card(self, card):
        self.hand_cards.append(card)

    def get_value(self):
        global VALUES
        ranks = list()
        for i in self.hand_cards:
            ranks.append(i.get_rank())
        
        if 'A' not in ranks:
            sum = 0
            for i in ranks:
                sum += VALUES[i]
            return sum
        
        elif 'A' in ranks:
            sum = 0
            for i in ranks:
                sum += VALUES[i]
            if sum + 10 <= 21:
                return sum + 10
            else: return sum
   
    def draw(self, canvas, pos):
        self.pos = pos
        
        for i in self.hand_cards:
            x = RANKS.index(i.rank)
            y = SUITS.index(i.suit)
            card_pos = [CARD_CENTER[0] + x * CARD_SIZE[0],
                        CARD_CENTER[1] + y * CARD_SIZE[1]]
            pos[0] += 80
            canvas.draw_image(card_images, card_pos, CARD_SIZE, pos, CARD_SIZE)
        
        if in_play == True:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [180, 200], CARD_BACK_SIZE)
            
# define deck class 
class Deck:
    def __init__(self):
        global SUITS, RANKS
        self.deck_cards = list()
        for i in SUITS:
            for j in RANKS:
                self.deck_cards.append(Card(i,j))

    def shuffle(self):
        random.shuffle(self.deck_cards)

    def deal_card(self):
        try:
            return self.deck_cards.pop()
        except:
            print "No more cards!"
            
    def __str__(self):
        ans = ""
        for i in range(len(self.deck_cards)):
            ans += str(self.deck_cards[i]) + " "
        return "Deck contains " + ans

#define event handlers for buttons
def deal():
    global score, outcome, in_play, deck, dealer_hand, player_hand
    if in_play == True:
        score -= 1
        outcome = "Player lost, new Deal! Hit or Stand?"
    else:
        outcome = "Hit or Stand?"
    deck = Deck()
    deck.shuffle()
    dealer_hand = Hand()
    player_hand = Hand()
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    in_play = True

def hit():
    global outcome, in_play, deck, player_hand, score
    if player_hand.get_value() <= 21 and in_play == True:
        player_hand.add_card(deck.deal_card())
        if player_hand.get_value() > 21:
            outcome = "You have busted: " + str(player_hand.get_value()) + ". New Deal?"
            in_play = False
            score -= 1
        else: 
            print "Player " + str(player_hand)
            print player_hand.get_value()
       
def stand():
    global outcome, in_play, deck, dealer_hand, player_hand, score
    if in_play == True:
        while dealer_hand.get_value() <= 16:
            dealer_hand.add_card(deck.deal_card())
        
        if dealer_hand.get_value() > 21:
            outcome = "Dealer busted: " + str(dealer_hand.get_value()) + ". Player wins! New Deal?"
            score += 1
            in_play = False
        elif player_hand.get_value() > dealer_hand.get_value():
            outcome = "Player wins! Dealer Hand value: " + str(dealer_hand.get_value()) + ". New Deal?"
            score += 1
            in_play = False
        elif player_hand.get_value() == dealer_hand.get_value():
            outcome = "Tie - Dealer wins! New Deal?"
            score -= 1
            in_play = False
        else:
            outcome = "Dealer wins: " + str(dealer_hand.get_value()) + " > " + str(player_hand.get_value()) + "! New Deal?"
            score -= 1
            in_play = False
        
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    player_hand.draw(canvas, [0, 500])
    dealer_hand.draw(canvas, [100, 200])
    canvas.draw_text("Blackjack", [230,50], 36, "White", "monospace")
    canvas.draw_text(outcome, [50,100], 16, "Black", "monospace")
    canvas.draw_text("Player Hand value: " + str(player_hand.get_value()), [40,420], 20, "Black", "monospace")
    canvas.draw_text("Score: " + str(score), [450,50], 20, "Red", "monospace")
    
# Globals v2

deck = Deck()
dealer_hand = Hand()
player_hand = Hand()

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric

===

[Acceleration and Friction]

Ship class - four Fields

self.pos - ships position (vector/pair of floats)
self.vel - ships velocity (vector/pair of floats)
self.angle - ships orientation (scalar/float)
self.thrust - whether ship is accelerating in forward direction (Boolean) # flag

# Position Update

self.pos[0] += self.vel[0]
self.pos[1] += self.vel[1]

# Velocity Update - acceleration in direction of forward vector

forward = [math.cos(self.angle),math.sin(self.angle)]

if self.thrust:
    self.vel[0] += forward[0] # multiply by a constant
    self.vel[1] += forward[1]

Friction - let c be a small constant friction = - c * velocity

acceleration = thrust + friction

friction = - c * velocity
velocity = velocity + acceleration
velocity = velocity + thrust + friction
velocity = velocity + thrust - c * velocity
velocity = (1 - c) * velocity + thrust

#Position Update
self.pos[0] += self.vel[0]
self.pos[1] += self.vel[1]

#Friction Update
self.vel[0] *= (1 - c)
self.vel[1] *= (1 - c)

#Thrust update - acceleration in direction of forward vector
forward = [math.cos(self.angle), math.sin(self.angle)]
if self.thrust:
    self.vel[0] += forward[0]
    self.vel[1] += forward[1]

[Spaceship Class]

===

# Partial example code for Spaceship

import simplegui

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# sound assets purchased from sounddogs.com, please do not redistribute
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        canvas.draw_circle(self.pos, self.radius, 1, "White", "White")

    def update(self):
        pass
    
===

[Sound]

# simple music player, uses buttons and sounds
# note that .ogg sounds are not supported in Safari

import simplegui
    
# define callbacks
def play():
    """play some music, starts at last paused spot"""
    music.play()

def pause():
    """pause the music"""
    music.pause()
    
def rewind():
    """rewind the music to the beginning """
    music.rewind()
    
def laugh():
    """play an evil laugh
    will overlap since it is separate sound object"""
    laugh.play()
    
def vol_down():
    """turn the current volume down"""
    global vol
    if vol > 0:
        vol = vol - 1
    music.set_volume(vol / 10.0)
    volume_button.set_text("Volume = " + str(vol))
    
def vol_up():
    """turn the current volume up"""
    global vol
    if vol < 10:
        vol = vol + 1
    music.set_volume(vol / 10.0)
    volume_button.set_text("Volume = " + str(vol))


# create frame - canvas will be blank
frame = simplegui.create_frame("Music demo", 250, 250, 100)

# set up control elements 
frame.add_button("play", play,100)
frame.add_button("pause", pause,100)
frame.add_button("rewind",rewind,100)
frame.add_button("laugh",laugh,100)
frame.add_button("Vol down", vol_down,100)
frame.add_button("Vol up", vol_up,100)

# initialize volume, create button whose label will display the volume
vol = 7
volume_button = frame.add_label("Volume = " + str(vol))


# load some sounds
music = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg")
laugh = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Evillaugh.ogg")

# make the laugh quieter so my ears don't bleed
laugh.set_volume(.1)

frame.start()

[Sprite Class]

Sprites and sprite sheets

- Two dimensional image or animation integrated into a larger scene, usually treated as a graphical overlay
- In the 1970/1980s, doing 2D graphics was computationally expensive. Sprites were 2D images provided to
special hardware accelerators that overlaid the images onto the display.
- Now, sprites are logical entities used to organize/represent imgaes that add visual complexity to a game
- Sprite sheets consisted a collection of sprties organized as a single image. Note that the individual
sprites need not be regularly spaced on the sprite sheet
- We will prefer to load sprites as individual images to provide more flexibility in modifying the art assets
for Spaceship and RiceRocks

Color and Transparency

Color - up to now, "White", "Black", "Red"
- RGB model - three red, green, blue channels
- Stored channel values as numerical intensities in the range 0-255
- HTML string - "rgb(255, 0, 0)" - equivalent to "Red" # rgb(0, 0, 255) == Blue
http://www.w3schools.com/html/html_colors.asp

Challenge - would lie to draw irregular shapes (like an asteroid or spaceship) that lie in rectangular images

Transparency - up to now, always opaque
- Add alpha channel to RGB model - channel stores transparency 
- HTML string - "rgba(255, 0, 0, 0.5)" - (1 is opaque, 0 is transparent)

Create image with transparent alpha channel in Photoshop, GIMP, paint.etn, etc.
- PNG image format is popular choice

===

# Sprite class emo
import simplegui
import math

# helper class to organize image information
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

# load ship image
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")


# Sprite class
class Sprite():
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
           
def draw(canvas):

    # draw ship and sprites
    a_rock.draw(canvas)
    
    # update ship and sprites
    a_rock.update()
                
# initialize frame
frame = simplegui.create_frame("Sprite demo", 800, 600)

# initialize ship and two sprites
a_rock = Sprite([400, 300], [0.3, 0.4], 0, 0.1, asteroid_image, asteroid_info)

# register handlers
frame.set_draw_handler(draw)

# get things rolling
frame.start()

[Programming Tips - 7]

===

########################
# Incomplete code from Pong
# Repeated code

def draw(c):
    global paddle1_pos, paddle2_pos
    
    paddle_width = 80

    if paddle_width/2 <= paddle1_pos + paddle1_vel <= width - paddle_width/2:
        paddle1_pos += paddle1_vel
    if paddle_width/2 <= paddle2_pos + paddle2_vel <= width - paddle_width/2:
        paddle2_pos += paddle2_vel
        
    c.draw_line([width/2, 0],[width/2, height], 1, "White")
    
    c.draw_line([4, paddle1_pos-paddle_width/2], [4, paddle1_pos+paddle_width/2], 4, "White")
    c.draw_line([width-4, paddle2_pos-paddle_width/2], [width-4, paddle2_pos+paddle_width/2], 4, "White")
    
    ...

===

########################
# Incomplete code from Pong
# Avoiding repetition with functions

paddle_width = 80
    
def paddle_move(paddle_num):
    if paddle_width/2 <= paddle_pos[paddle_num] + paddle_vel[paddle_num] <= width - paddle_width/2:
        paddle_pos[paddle_num] += paddle_vel[paddle_num]

def paddle_draw(c, paddle_num):
    c.draw_line([paddle_loc[paddle_num], paddle_pos[paddle_num] - paddle_width/2],
                PADDLE_THICKNESS, "White")


def draw(c):
    paddle_move(0)
    paddle_move(1)
    
    c.draw_line([width / 2, 0],[width / 2, height], 1, "White")
 
    paddle_draw(c,0)
    paddle_draw(c,1)
    
    ...

===

########################
# Incomplete code from Pong
# Avoiding repetition with classes and methods

class Paddle:
    def __init__(self, loc, pos, vel):
        self.loc = loc
        self.pos = pos
        self.vel = vel
        self.width = 80
    
    def move(self):
        if self.width/2 <= self.pos + self.vel <= width - self.width/2:
            self.pos += self.vel
            
    def draw(c, self):
        c.draw_line([self.loc, self.pos-self.width / 2], PADDLE_THICKNESS, "White")

def draw(c):
    paddle1.move()
    paddle2.move()
        
    c.draw_line([width / 2, 0],[width / 2, height], 1, "White")
    
    paddle1.draw(c)
    paddle2.draw(c)
    
    ...

===

########################
# Incomplete code from Pong
# Long if/elif chain

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 2
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 2
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 2
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 2

===

########################
# Incomplete code from Pong
# Avoiding long if/elif chain with dictionary mapping values to actions

def paddle1_faster():
    global paddle1_vel
    paddle1_vel += 2

def paddle1_slower():
    global paddle1_vel
    paddle1_vel -= 2
    
def paddle2_faster():
    global paddle2_vel
    paddle2_vel += 2    

def paddle2_slower():
    global paddle2_vel
    paddle2_vel -= 2


inputs = {"up": paddle2_slower,
          "down": paddle2_faster,
          "w": paddle1_slower,
          "s": paddle1_faster}

def keydown(key):
    for i in inputs:
        if key == simplegui.KEY_MAP[i]:
            inputs[i]()

===

########################
# Illustration of a dictionary mapping values to functions

def f():
    print "hi"

d = {0: f}

d[0]()

===

########################
# Incomplete code from Pong
# Avoiding long if/elif chain with dictionary mapping values to action arguments

inputs = {"up": [1, -2],
          "down": [1, 2],
          "w": [0, -2],
          "s": [0, 2]}

def keydown(key):
    for i in inputs:
        if key == simplegui.KEY_MAP[i]:
            paddle_vel[inputs[i][0]] += inputs[i][1]

===

########################
# Sample of using tiled image
# Has some uses of "magic" (unexplained) constants.

# demo for drawing using tiled images

import simplegui

# define globals for cards
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
SUITS = ['C', 'S', 'H', 'D']

# card sprite - 950x392
CARD_CENTER = (36.5, 49)
CARD_SIZE = (73, 98)
card_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")


# define card class
class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def draw(self, canvas, pos):
        i = RANKS.index(self.rank)
        j = SUITS.index(self.suit)
        card_pos = [CARD_CENTER[0] + i * CARD_SIZE[0],
                    CARD_CENTER[1] + j * CARD_SIZE[1]]
        canvas.draw_image(card_image, card_pos, CARD_SIZE, pos, CARD_SIZE)

# define draw handler        
def draw(canvas):
    one_card.draw(canvas, (155, 90))

# define frame and register draw handler
frame = simplegui.create_frame("Card draw", 300, 200)
frame.set_draw_handler(draw)

# createa card
one_card = Card('S', '6')

frame.start()


########################
# Sample of using tiled image
# Naming constants and calculating other constants from those

# demo for drawing using tiled images

import simplegui

# define globals for cards
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
SUITS = ['C', 'S', 'H', 'D']

# card sprite - 950x392
CARD_SIZE = (73, 98)
card_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

FRAME_SIZE = (300, 200)

# define card class
class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def draw(self, canvas, pos):
        i = RANKS.index(self.rank)
        j = SUITS.index(self.suit)
        card_loc = [(.5 + i) * CARD_SIZE[0],
                    (.5 + j) * CARD_SIZE[1]]
        canvas.draw_image(card_image, card_loc, CARD_SIZE, pos, CARD_SIZE)

# define draw handler        
def draw(canvas):
    one_card.draw(canvas, (FRAME_SIZE[0] / 2, FRAME_SIZE[1] / 2))

# define frame and register draw handler
frame = simplegui.create_frame("Card draw", FRAME_SIZE[0], FRAME_SIZE[1])
frame.set_draw_handler(draw)

# createa card
one_card = Card('S', '6')

frame.start()


########################
# Incomplete code from Pong
# Magic unnamed constants, repeated code, long expressions

width = 600
height = 400


def ball_init():
    if random.randrange(0,2) == 0:
        return [300,200], [3 + 3 * random.random(), 8 * (random.random() - 0.5)]
    else:
        return [300,200], [-(3 + 3 * random.random()), 8 * (random.random() - 0.5)]


########################
# Incomplete code from Pong
# Constants named and computed, repetition avoided, expressions broken into
# named pieces

width = 600
height = 400


def ball_init():
    pos = [width/2, height/2]
    
    vel_x = 3 + 3 * random.random()
    vel_y = 8 * (random.random() - 0.5)
    
    if random.randrange(0,2) == 1:
        vel_x = -vel_x
    
    return pos, [vel_x, vel_y]

===

# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
first_rocket = True

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center
    
    def set_center(self, XY):
        self.XY = XY
        self.center[0] = XY[0]
        self.center[1] = XY[1]

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        
        if self.thrust == True:
            ship_info.set_center([135,45])
        else:
            ship_info.set_center([45,45])
        
        # canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest, rotation)
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update_angle(self, new_ang_vel):
        self.new_ang_vel = new_ang_vel
        self.angle_vel += new_ang_vel    
     
    def set_thruster(self, boolean):
        self.boolean = boolean
        self.thrust = boolean
        
        if boolean == True:
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.rewind()
        
    def shoot(self):
        global a_missile
        forward = angle_to_vector(self.angle)
        ship_radius = ship_info.get_radius()
        rocket_pos = [(self.pos[0] + ship_radius * forward[0]), (self.pos[1] + ship_radius * forward[1])]
        forward_vel = [0,0]
        forward_vel[0] = self.vel[0] + forward[0] * 6
        forward_vel[1] = self.vel[1] + forward[1] * 6
        a_missile = Sprite(rocket_pos, forward_vel, 0, 0, missile_image, missile_info, missile_sound)
        
    def update(self):
        global WIDTH, HEIGHT
        self.angle += self.angle_vel
        forward = angle_to_vector(self.angle)
        c = 0.005
        
        if self.pos[0] not in range(0,WIDTH):
            self.pos[0] = self.pos[0] % WIDTH
            self.pos[0] += self.vel[0]
        else:
            self.pos[0] += self.vel[0]
  
        if self.pos[1] not in range(0,HEIGHT):
            self.pos[1] = self.pos[1] % HEIGHT
            self.pos[1] += self.vel[1]
        else:
            self.pos[1] += self.vel[1]
        
        # Thrust update
        if self.thrust == True:
            self.vel[0] += (forward[0] * 0.1)
            self.vel[1] += (forward[1] * 0.1)
    
        # Friction update
        self.vel[0] *= (1 - c)
        self.vel[1] *= (1 - c)
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        # canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest, rotation)   
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def set_velocity(self, new_vel):
        self.vel = new_vel
        self.vel[0] = new_vel[0]
        self.vel[1] = new_vel[1] 
    
    def set_position(self, XY):
        self.XY = XY
        self.pos[0] = XY[0]
        self.pos[1] = XY[1]
    
    def update_angle(self, new_ang_vel):
        self.new_ang_vel = new_ang_vel
        self.angle_vel = 0
        self.angle_vel += new_ang_vel
    
    def update(self):
        self.angle  += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
def draw(canvas):
    global time, score, lives, WIDTH, HEIGHT, first_rocket
     
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    if first_rocket == False:
        a_missile.draw(canvas)
    else:
        pass

    # update ship and sprites
    my_ship.update()
    a_rock.update()
    a_missile.update()
    
    # Lives & Score
    update_lives = "Lives: " + str(lives)
    update_score = "Score: " + str(score)
    canvas.draw_text(update_lives, [WIDTH - 780, HEIGHT - 550], 36, 'White', 'sans-serif')
    canvas.draw_text(update_score, [WIDTH - 150, HEIGHT - 550], 36, 'White', 'sans-serif')
    
            
# timer handler that spawns a rock  
def rock_spawner():
    global a_rock
    
    pos_x = random.randrange(0,WIDTH,1)
    pos_y = random.randrange(0,HEIGHT,1)
    
    vel_x = random.randrange(-5,5,1)
    vel_y = random.randrange(-5,5,1)
    
    lower = 0.01
    upper = 0.15
    range_width = upper - lower
    angle = random.random() * range_width + lower
    direction = [-1,1]
    random.shuffle(direction)
    new_ang_vel = angle * direction[0]
    
    a_rock.set_velocity([vel_x,vel_y])
    a_rock.set_position([pos_x,pos_y])
    a_rock.update_angle(new_ang_vel)

# timer handler that spawns a rock  
inputs = {"left": [-0.1, 0.1],
          "right": [0.1, -0.1],
          "up": [True, False]}

# keydown handler
def keydown(key):
    global first_rocket
    if key == simplegui.KEY_MAP["up"]:
        my_ship.set_thruster(inputs["up"][0])
    elif key == simplegui.KEY_MAP["left"]:
        my_ship.update_angle(inputs["left"][0])
    elif key == simplegui.KEY_MAP["right"]:
        my_ship.update_angle(inputs["right"][0])
    elif key == simplegui.KEY_MAP["space"]:
        my_ship.shoot()
        first_rocket = False
    else:
        pass

# keyup handler
def keyup(key):
    if key == simplegui.KEY_MAP["up"]:
        my_ship.set_thruster(inputs["up"][1])
    elif key == simplegui.KEY_MAP["left"]:
        my_ship.update_angle(inputs["left"][1])
    elif key == simplegui.KEY_MAP["right"]:
        my_ship.update_angle(inputs["right"][1])
    else:
        pass
           
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0.1, asteroid_image, asteroid_info)
a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()


http://www.codeskulptor.org/#user40_tXtdaoGZG3_32.py

===

[Sets]

- List: ordered sequence
- Dictionary: key/value mapping
- Set: unordered collection of data with no duplicates (faster)

list [1,2,3,1,2]
set([1,2,3])

===

# Examples of Sets 

instructors = set(['Rixner', 'Warren', 'Greiner', 'Wong'])
print instructors #=> returns them in a random order

inst2 = set(['Rixner', 'Rixner', 'Warren', 'Warren', 'Greiner', 'Wong'])
print inst2 #=> duplicates are removed

print instructors == inst2 #=> true (same elements)

for inst in instructors:
    print inst #=> order not guaranteed, only gaurantee is that you only see each element once

instructors.add('Colbert')
print instructors
instructors.add('Rixner') #=> won't work, already there
print instructors 

instructors.remove('Wong')
print instructors
#instructors.remove('Wong') #=> keyerror if not there --> check with in operator
#print instructors

print 'Rixner' in instructors
print 'Wong' in instructors

===

# Examples of Sets 2

instructors = set(['Rixner', 'Warren', 'Greiner', 'Wong'])
print instructors

def get_rid_of(inst_set, starting_letter):
    remove_set = set([])
    for inst in inst_set:
        if inst[0] == starting_letter:
            remove_set.add(inst)
    inst_set.difference_update(remove_set)

get_rid_of(instructors, 'W')
print instructors

===

[Collisions]

d (between centers) = r1 + r2 == no collision
d (between centers) < r1 + r2 == collision

Use: get_radius & get_center

# Sprite class

def collide(self, other_sprite):
    # sprite1.collide(sprite2)
    # self.pos, self.radius
    # other_sprite.get_position()
    # other_sprite.get_radius()
    # return True/False (collide or not)

ship
rocks (set)
missiles (set)

Collisions:
[1] - ship: rock (die, lose life)
[2] - missile: rock (missile and rock explode, get points)

rock.collide(ship)

def group_collide(rocks, ship): [1]
    # check each sprite in rocks
    # does sprite collide with ship
    # If yes --> remove sprite from group
    # return True/False (True: ship blew up, etc.)

group_collide
remove_set = set([])
for s in myset:
    remove_set.add(s)
myset.difference_update(remove_set)

for s in list(myset): #list(myset) re-creates the list --> both work
    myset.remove(s)

[2] - missiles - rocks # set & set

def group_group_collide(missiles, rocks):
    # call group_collide(...) --> will make this much simpler
    # return the number of collisions (the number of True's to update the score)

[Animation]

- Flip book: sequence of drawings on pages of book, flip through images, appear to move
- Relies on phenomenon known as persistence of vision
- Create the illusion that continuous motion is being seen rather than a series of discontinuous
images being exchanged in succession (e.g. 24 frames per sec in movies)
- Example: horizontally tiled image consisting of 64 images of tumbling asteroid
- Animate tumblin asteroid - draw each sub-image briefly in sequence

===

# demo of animation using asteroid sprite sheet

import simplegui

# load 64 frame sprite sheer for asteroid - image source is opengameart, artist is warspawn 
ROCK_CENTER = [64, 64] # center of each image
ROCK_SIZE = [128, 128] # size of each image
ROCK_DIM = 64 # images in tiled image
rock_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid1.opengameart.warspawn.png")

# global time for animation
time = 0

# draw handler    
def draw(canvas):
    global time
    current_rock_index = (time % ROCK_DIM) // 1
    current_rock_center = [ROCK_CENTER[0] +  current_rock_index * ROCK_SIZE[0], ROCK_CENTER[1]]
    canvas.draw_image(rock_image, current_rock_center, ROCK_SIZE, ROCK_CENTER, ROCK_SIZE) 
    time += 0.2
    
# create frame and size frame based on 128x128 pixel sprite
frame = simplegui.create_frame("Asteroid sprite", ROCK_SIZE[0], ROCK_SIZE[1])

# set draw handler and canvas background using custom HTML color
frame.set_draw_handler(draw)
frame.set_canvas_background("Blue")

# start animation
frame.start()

===

# animation of explosion using 2D sprite sheet

import simplegui

# load 81 frame sprite sheer for explosion - image generated by phaedy explosion generator, source is hasgraphics.com
EXPLOSION_CENTER = [50, 50]
EXPLOSION_SIZE = [100, 100]
EXPLOSION_DIM = [9, 9] # 9x9
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/explosion.hasgraphics.png")

# create timer that iterates current_sprite_center through sprite
time = 0

# define draw handler
def draw(canvas):
    global time
    explosion_index = [time % EXPLOSION_DIM[0], (time // EXPLOSION_DIM[0]) % EXPLOSION_DIM[1]]
    canvas.draw_image(explosion_image, 
                    [EXPLOSION_CENTER[0] + explosion_index[0] * EXPLOSION_SIZE[0], 
                     EXPLOSION_CENTER[1] + explosion_index[1] * EXPLOSION_SIZE[1]], 
                     EXPLOSION_SIZE, EXPLOSION_CENTER, EXPLOSION_SIZE)
    time += 1 

        
# create frame and size frame based on 100x100 pixel sprite
f = simplegui.create_frame("Asteroid sprite", EXPLOSION_SIZE[0], EXPLOSION_SIZE[1])

# set draw handler and canvas background using custom HTML color
f.set_draw_handler(draw)
f.set_canvas_background("Blue")

# start animation
f.start()

[Programming Tips - 8]

print set([1,2,3,4]) # set
print {} # dictionary

s = set([1,2,3,4])
t = set([3,4,5,6])

print s.intersection(t) #=> set([3,4])
print s #=> set([1,2,3,4])
print t #=> set([3,4,5,6])

print s.intersection_update(t) #=> None
print s #=> set([3,4])
print t #=> set([3,4,5,6])

===

s = set([1,2,3,4])
t = s

s.intersection_update([3,4,5,6]) # argument can be anything

print s #=> set([3,4])
print t #=> set([3,4])

===

# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
score_tracker = 0
time = 0
lives = 0
first_rocket = True
started = False
lifespan = 240
rock_velocity = 5

inputs = {"left": [-0.1, 0.1],
          "right": [0.1, -0.1],
          "up": [True, False]}

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center
    
    def set_center(self, XY):
        self.XY = XY
        self.center[0] = XY[0]
        self.center[1] = XY[1]

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)
    
# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        
        if self.thrust == True:
            ship_info.set_center([135,45])
        else:
            ship_info.set_center([45,45])
        
        # canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest, rotation)
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
           
    def update_angle(self, new_ang_vel):
        self.new_ang_vel = new_ang_vel
        self.angle_vel += new_ang_vel    
     
    def set_thruster(self, boolean):
        self.boolean = boolean
        self.thrust = boolean
        
        if boolean == True:
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.rewind()
        
    def shoot(self):
        global rocket_group
        forward = angle_to_vector(self.angle)
        ship_radius = ship_info.get_radius()
        rocket_pos = [(self.pos[0] + ship_radius * forward[0]), (self.pos[1] + ship_radius * forward[1])]
        forward_vel = [0,0]
        forward_vel[0] = self.vel[0] + forward[0] * 6
        forward_vel[1] = self.vel[1] + forward[1] * 6
        missile_group.add(Sprite(rocket_pos, forward_vel, 0, 0, missile_image, missile_info, missile_sound))
        
    def update(self):
        global WIDTH, HEIGHT
        self.angle += self.angle_vel
        forward = angle_to_vector(self.angle)
        c = 0.005
        
        if self.pos[0] not in range(0,WIDTH):
            self.pos[0] = self.pos[0] % WIDTH
            self.pos[0] += self.vel[0]
        else:
            self.pos[0] += self.vel[0]
  
        if self.pos[1] not in range(0,HEIGHT):
            self.pos[1] = self.pos[1] % HEIGHT
            self.pos[1] += self.vel[1]
        else:
            self.pos[1] += self.vel[1]
        
        # Thrust update
        if self.thrust == True:
            self.vel[0] += (forward[0] * 0.1)
            self.vel[1] += (forward[1] * 0.1)
    
        # Friction update
        self.vel[0] *= (1 - c)
        self.vel[1] *= (1 - c)
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
        
    def draw(self, canvas):
        if self.animated == True:
            current_index = self.age // 30
            self.image_center = [self.image_center[0] + current_index * self.image_size[0], self.image_center[1]]
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update_angle(self, new_ang_vel):
        self.new_ang_vel = new_ang_vel
        self.angle_vel = 0
        self.angle_vel += new_ang_vel
    
    def update(self):
        global lifespan
        self.angle  += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        if self.age < lifespan:
            self.age += 1
            return False
        else:
            return True
        
    def collide(self, other_object):
        self.other_object = other_object
        if dist(self.get_position(), other_object.get_position()) <= float(self.get_radius() + other_object.get_radius()):
            return True
        else: 
            return False
                   
def draw(canvas):
    global time, score, lives, WIDTH, HEIGHT, first_rocket, rock_group, my_ship, missile_group, started, score_tracker
     
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    
    # draw ship and sprites
    my_ship.draw(canvas)
    process_sprite_group(rock_group, canvas, 'rocks')
    process_sprite_group(explosion_group, canvas, 'explosions')
    
    if lives == 0:
        started = False
        rock_group = set([])
       
    if group_collide(rock_group, my_ship) == True:
        lives -= 1
    
    if group_group_collide(rock_group, missile_group) == True:
            score += 1
            score_tracker += 1
    
    group_collide(rock_group, my_ship)
    group_group_collide(rock_group, missile_group)
    
    if first_rocket == False:
        process_sprite_group(missile_group, canvas, 'missiles')
    else:
        pass

    # update ship and sprites
    my_ship.update()
    
    # Lives & Score
    update_lives = "Lives: " + str(lives)
    update_score = "Score: " + str(score)
    canvas.draw_text(update_lives, [WIDTH - 780, HEIGHT - 550], 36, 'White', 'sans-serif')
    canvas.draw_text(update_score, [WIDTH - 200, HEIGHT - 550], 36, 'White', 'sans-serif')
    
    # draw splash screen if not started
    if not started:
        play()
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
        
# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started, lives, score
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if started == False and inwidth and inheight:
        started = True
        rewind()
        play()
        lives += 3
        score = 0

def process_sprite_group(set_arg, canvas, value):
    copy_set_arg = set(set_arg)
    
    if value == 'missiles':        
        for i in copy_set_arg:
            if i.update() == True:
                set_arg.remove(i)
            else:
                i.update()
                i.draw(canvas)
    elif value == 'rocks':
        for i in set_arg:
            i.update()
            i.draw(canvas)
    elif value == 'explosions':
        for i in copy_set_arg:
            if i.update() == True:
                set_arg.remove(i)
            else:
                i.update()
                i.draw(canvas)
    else:
        print "Value not recognized"
        
def group_collide(group, other_object):
    copy_group = set(group)
    for i in copy_group:
        if i.collide(other_object) == True:
            explosion_group.add(Sprite(i.get_position(), [0,0], 0, 0, explosion_image, explosion_info, explosion_sound))
            print explosion_group
            group.remove(i)
            return True

def group_group_collide(group1, group2):
    copy_group1 = set(group1)    
    for i in copy_group1:
        if group_collide(group2, i) == True:
            group1.discard(i)
            group2.discard(i)
            return True
            print "Collision"  
    
# timer handler that spawns a rock  
def rock_spawner():
    global rock_group, started, my_ship, asteroid_info, score_tracker, rock_velocity
    if score_tracker // 5 == 1:
        rock_velocity += 1
        score_tracker = 0 
    pos_x = random.randrange(0,WIDTH,1)
    pos_y = random.randrange(0,HEIGHT,1)
    vel_x = random.randrange((-1 * rock_velocity), rock_velocity, 1)
    vel_y = random.randrange((-1 * rock_velocity), rock_velocity, 1)
    lower = 0.01
    upper = 0.15
    range_width = upper - lower
    angle = random.random() * range_width + lower
    direction = [-1,1]
    random.shuffle(direction)
    new_ang_vel = angle * direction[0]
    p = [pos_x, pos_y]
    q = my_ship.get_position()    
    
    if dist(p, q) < (my_ship.get_radius() + asteroid_info.get_radius()) and started == True:
        pass
    elif len(rock_group) < 12 and started == True:
        rock_group.add(Sprite([pos_x, pos_y], [vel_x, vel_y], 0, new_ang_vel, asteroid_image, asteroid_info))
    else:
        pass

# keydown handler
def keydown(key):
    global first_rocket, inputs
    if key == simplegui.KEY_MAP["up"]:
        my_ship.set_thruster(inputs["up"][0])
    elif key == simplegui.KEY_MAP["left"]:
        my_ship.update_angle(inputs["left"][0])
    elif key == simplegui.KEY_MAP["right"]:
        my_ship.update_angle(inputs["right"][0])
    elif key == simplegui.KEY_MAP["space"]:
        my_ship.shoot()
        first_rocket = False
    else:
        pass

# keyup handler
def keyup(key):
    if key == simplegui.KEY_MAP["up"]:
        my_ship.set_thruster(inputs["up"][1])
    elif key == simplegui.KEY_MAP["left"]:
        my_ship.update_angle(inputs["left"][1])
    elif key == simplegui.KEY_MAP["right"]:
        my_ship.update_angle(inputs["right"][1])
    else:
        pass

def play():
    """play some music, starts at last paused spot"""
    soundtrack.play()
    
def rewind():
    """rewind the music to the beginning """
    soundtrack.rewind()

# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
rock_group = set([])
missile_group = set([])
explosion_group = set([])

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()

===

http://www.codeskulptor.org/#user40_tXtdaoGZG3_99.py

Bonus:

http://www.codeskulptor.org/#user40_tXtdaoGZG3_123.py