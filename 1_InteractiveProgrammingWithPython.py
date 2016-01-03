[Interactive Programming with Python - Part 1]

[Arithmetic Expressions]

# numbers - two types, an integer or a decimal number
# two correspending data types int() and float()

print 3, -1, 3.14159, -2.8

# we can convert between data types using int() and float()
# note that int() take the "whole" part of a decimal number
# float() applied to integers is boring

print type(3), type(3.14159), type(3.0)
#=> <type 'int'><type 'float'><type 'float'>

print int(3.14159), int(-2.8)
#=> 3 -2
print float(3), float(-1)
#=> 3.0 -1.0

# floating point number have around 15 decimal digits of accuracy
# pi is 3.1415926535897932384626433832795028841971...
# square root of two is 1.4142135623730950488016887242096980785696...

# approximation of pi, Python displays 12 decimal digits

print 3.1415926535897932384626433832795028841971
#=> 3.14159265359

# appoximation of square root of two, Python displays 12 decimal digits

print 1.4142135623730950488016887242096980785696
#=> 1.41421356237

# arithmetic operators
# +		plus		addition
# -		minus		subtraction
# *		times		multiplication
# /		divided by 	division
# **    power		exponentiation

# If one operand is a decimal (float), the answer is decimal

print 1.0 / 3, 5.0 / 2.0, -7 / 3.0
#=> 0.333333333333 2.5 -2.33333333333

# If both operands are ints, the answer is an int (rounded down)

print 1 / 3, 5 / 2, -7 / 3
#=> 0 2 -3 

# expressions - number or a binary operator applied to two expressions
# minus is also a unary operator and can be applied to a single expression

print 1 + 2 * 3, 4.0 - 5.0 / 6.0, 7 * 8 + 9 * 10

# expressions are entered as sequence of numbers and operations
# how are the number and operators grouped to form expressions?
# operator precedence - "Please Excuse My Dear Aunt Sallie" = (), **, *, /, +,-

print 1 * 2 + 3 * 4
print 2 + 12

# always manually group using parentheses when in doubt

print 1 * (2 + 3) * 4
print 1 * 5 * 4

[Variables]

# valid variable names - consists of letters, numbers, underscore (_)
# starts with letter or underscore
# case sensitive (capitalization matters)

# legal names - ninja, Ninja, n_i_n_j_a
# illegal names - 1337, 1337ninja

# Python convention - multiple words joined by _
# legal names - elite_ninja, leet_ninja, ninja_1337
# illegal name 1337_ninja

# assign to variable name using single equal sign =
# (remember that double equals == is used to test equality)

# examples 

my_name = "Joe Warren"
print my_name

my_age = 51
print my_age

my_age = my_age + 1 == my_age += 1

# the story of the magic pill

magic_pill = 30
print my_age - magic_pill

my_grand_dad = 74

print my_grand_dad - 2 * magic_pill

# Temperature examples

# convert from Fahrenheit to Celsuis
# c = 5 / 9 * (f - 32)
# use explanatory names

temp_Fahrenheit = 212

temp_Celsius = 5.0 / 9.0 * (temp_Fahrenheit - 32)

print temp_Celsius

# test it! 32 Fahrenheit is 0 Celsius, 212 Fahrenheit is 100 Celsius


# convert from Celsius to Fahrenheit
# f = 9 / 5 * c + 32

temp_Celsius = 100

temp_Fahrenheit = 9.0 / 5.0 * temp_Celsius + 32

print temp_Fahrenheit

[Functions]

# computes the area of a triangle
def triangle_area(base, height):     # header - ends in colon
    area = (1.0 / 2) * base * height # body - all of body is indented
    return area                      # body - return outputs value

a1 = triangle_area(3, 8)
print a1
a2 = triangle_area(14, 2)
print a2

# converts fahrenheit to celsius
def fahrenheit2celsius(fahrenheit):
    celsius = (5.0 / 9) * (fahrenheit - 32)
    return celsius

# test!!!
c1 = fahrenheit2celsius(32)
c2 = fahrenheit2celsius(212)
print c1, c2

# converts fahrenheit to kelvin
def fahrenheit2kelvin(fahrenheit):
    celsius = fahrenheit2celsius(fahrenheit)
    kelvin = celsius + 273.15
    return kelvin

# test!!!
k1 = fahrenheit2kelvin(32)
k2 = fahrenheit2kelvin(212)
print k1, k2

# prints hello, world!
def hello():
    print "Hello, world!"

# test!!!
hello()      # call to hello prints "Hello, world!"
h = hello()  # call to hello prints "Hello, world!" a second time
print h      # prints None since there was no return value

Do not forget:
- :
- return
- indentation

[More Operations]

# Remainder / % / modulo - modular arithmetic works both in negative as positive direction

# systematically restrict computation to a range
# long division - divide by a number, we get a quotient plus a remainder
# quotient is integer division //, the remainder is % (Docs)

# problem - get the ones digit of a number
num = 49
tens = num // 10 # --> 4
ones = num % 10  # --> 9
print tens, ones
print 10 * tens + ones, num

# application - 24 hour clock
# http://en.wikipedia.org/wiki/24-hour_clock

hour = 20
shift = 8
print (hour + shift) % 24

# application - screen wraparound
# Spaceship from week seven

width = 800
position = 797
move = 5
position = (position + move) % width
print position # --> 2

width = 800
position = 797
move = -5
position = (position + move) % width
print position # --> 797

# Data conversion operations

# convert an integer into string - str
# convert an hour into 24-hour format "03:00", always print leading zero

hour = 3
ones = hour % 10 					# --> 3
tens = hour // 10 					# --> 0
print tens, ones, ":00" 			# --> 0 3 :00
print str(tens), str(ones), ":00" 	# --> 0 3 :00
print str(tens) + str(ones) + ":00" # --> 03:00

# convert a string into numbers using int and float

# Python modules - extra functions implemented outside basic Python

import simplegui	# access to drawing operations for interactive applications

import math	 		# access to standard math functions, e.g; trig

import random   	# functions to generate random numbers

# look in Docs for useful functions

print math.pi

[Logic and Comparisons]

Evaluation hierarchy: NOT - AND -  OR


-- Comparison Operators

# >
# <
# >=
# <=
# ==
# !=

[Conditionals]

def greet(friend, money):
    if friend and (money > 20):
        print "Hi!"
        money = money - 20
    elif friend:
        print "Hello"
    else:
        print "Ha ha"
        money = money + 10
    return money


money = 15

money = greet(True, money)
print "Money:", money
print ""

money = greet(False, money)
print "Money:", money
print ""

money = greet(True, money)
print "Money:", money
print ""

[Programming Tips]

import random

def random_dice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return die1 + die2

def volume_sphere(radius):
    return 4.0/3.0 * math.pi * (radius ** 3)

# => attribute error is a syntax error after the '.'

def area_triangle(base, height):
    return 0.5 * base * height

# Poor readability
def area(a,b,c):
    s = (a+b+c)/2.0
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

# Improved readability
def area_triangle_sss(side1, side2, side3):
    
    """
    Returns the area of a triangle, given the lengths of [Documentation String]
    its three sides.
    """
    
    # Use Heron's formula
    semiperim = (side1 + side2 + side3) / 2.0
    return math.sqrt(semiperim *
                     (semiperim - side1) *
                     (semiperim - side2) * 
                     (semiperim - side3))

[Rock-paper-scissors-lizard-Spock]

n = 123

print n % 100 #=> 23
print n % 10  #=> 3
print n // 10 #=> 12

[Event-driven Programming]

Start --> Initialize --> Wait <---> (Event +) Handler

Events
- Input (e.g. button, text box)
- Keyboard (e.g key down, key up)
- Mouse (e.g. click, drag)
- Timer

# Example of a simple event-driven program

# CodeSkulptor GUI module
import simplegui

# Event handler
def tick():
    print "tick!"

# Register handler
timer = simplegui.create_timer(1000, tick)

# Start timer
timer.start()

Event Queue
- System puts events in this (invisible) queue

[Local vs. Global Variables]

# global vs local examples

# num1 is a global variable

num1 = 1
print num1

# num2 is a local variable

def fun():
    num1 = 2
    num2 = num1 + 1
    print num2
    
fun()

# the scope of global num1 is the whole program, num 1 remains defined
print num1

# the scope of the variable num2 is fun(), num2 is now undefined
# print num2 #=> error 'num2' not defined

# why use local variables?
# give a descriptive name to a quantity
# avoid computing something multiple times

def fahren_to_kelvin(fahren):
    celsius = 5.0 / 9 * (fahren - 32)
    zero_celsius_in_kelvin = 273.15
    return celsius + zero_celsius_in_kelvin

print fahren_to_kelvin(212)

# the risk/reward of using global variables

# risk - consider the software system for an airliner
#       critical piece - flight control system
#       non-critical piece - in-flight entertainment system

# both systems might use a variable called "dial"
# we don't want possibility that change the volume on your audio
# causes the plane's flaps to change!

# example
num = 4

def fun1():
    global num # to access global variable
    num = 5
    
def fun2():
    global num
    num = 6

# note that num changes after each call with no obvious explanation    
print num
fun1()
print num
fun2()
print num

# global variables are an easy way for event handlers
# to communicate game information.

# safer method - but they required more sophisticated
# object-programming techniques

[SimpleGUI]

import simplegui

message = "Welcome!"

# Handler for mouse click
def click():
    global message
    message = "Good job!"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 36, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

-- Program Structure
1 - Define globals (state)
2 - Define Helper functions
3 - Define Classes
4 - Define event handlers
5 - Create a frame
6 - Register event handlers
7 - Start the frame & timers

# SimpleGUI program template

# Import the module
import simplegui

# Define global variables (program state)
counter = 0

# Define "helper" functions
def increment():
    global counter 
    counter = counter + 1

# Define event handler functions
def tick():
    increment()
    print counter

def buttonpress():
    global counter:
    counter = 0

# Create a frame
frame = simplegui.create_frame["SimpelGUI Test", 100, 100]

# Register event handlers
timer = simplegui.create_timer[1000, tick]
frame.add_button("Click me!", buttonpress)

# Start frame and timers
frame.start()
timer.start()

[Buttons & Input Fields]

# calculator with all buttons

import simplegui

# intialize globals
store = 0
operand = 0


# event handlers for calculator with a store and operand

def output():
    """prints contents of store and operand"""
    print "Store = ", store
    print "Operand = ", operand
    print ""
    
def swap():
    """ swap contents of store and operand"""
    global store, operand
    store, operand = operand, store
    output()
    
def add():
    """ add operand to store"""
    global store
    store = store + operand
    output()

def sub():
    """ subtract operand from store"""
    global store
    store = store - operand
    output()

def mult():
    """ multiply store by operand"""
    global store
    store = store * operand
    output()

def div():
    """ divide store by operand"""
    global store
    store = store / operand
    output()

def enter(t):
    """ enter a new operand"""
    global operand
    operand = float(t)
    output()
    
# create frame
f = simplegui.create_frame("Calculator",300,300)

# register event handlers and create control elements
f.add_button("Print", output, 100)
f.add_button("Swap", swap, 100)
f.add_button("Add", add, 100)
f.add_button("Sub", sub, 100)
f.add_button("Mult", mult, 100)
f.add_button("Div", div, 100)
f.add_input("Enter", enter, 100)


# get frame rolling
f.start()

[Programming Tips]

##############
# Example of missing "global"

n1 = 0

def increment():
    n1 = n1 + 1

increment()
increment()
increment()

print n1


##############
# Example of missing "global"

n2 = 0

def assign(x):
    n2 = x

assign(2)
assign(15)
assign(7)

print n2


##############
# Example of missing "return"

n3 = 0

def decrement():
    global n3
    n3 = n3 - 1

x = decrement()

print "x = ", x
print "n = ", n


##############
# Example of print debugging

import simplegui

x = 0

def f(n):
    print "f: n,x = ", n, x
    result = n ** x
    print "f: result = ",result
    return result
    
def button_handler():
    global x
    print "bh : x = ", x
    x += 1
    print "bh : x = ", x

def input_handler(text):
    print "ih : text = ", text
    print f(float(text))
    
frame = simplegui.create_frame("Example", 200, 200)
frame.add_button("Increment", button_handler)
frame.add_input("Number:", input_handler, 100)

frame.start()


##############
# Examples of simplifying conditionals

def f1(a, b):
    """Returns True exactly when a is False and b is True."""  
    if a == False and b == True:
        return True
    else:
        return False

def f2(a, b):
    """Returns True exactly when a is False and b is True."""  
    if not a and b:
        return True
    else:
        return False    

def f3(a, b):
    """Returns True exactly when a is False and b is True."""  
    return not a and b

def g1(a, b):
    """Returns False eactly when a and b are both True."""  
    if a == True and b == True:
        return False
    else:
        return True
    
def g2(a, b):
    """Returns False eactly when a and b are both True."""  
    if a and b:
        return False
    else:
        return True

def g3(a, b):
    """Returns False eactly when a and b are both True."""  
    return not (a and b)

[PEP 8 - Styleguide]

- Use 4-space indentation, and no tabs.

- 4 spaces are a good compromise between small indentation (allows greater nesting depth) and large indentation (easier to read). Tabs introduce confusion, and are best left out.

- Wrap lines so that they don’t exceed 79 characters.

- This helps users with small displays and makes it possible to have several code files side-by-side on larger displays.

- Use blank lines to separate functions and classes, and larger blocks of code inside functions.

- When possible, put comments on a line of their own.

- Use docstrings.

- Use spaces around operators and after commas, but not directly inside bracketing constructs: a = f(1, 2) + g(3, 4).

- Name your classes and functions consistently; the convention is to use CamelCase for classes and lower_case_with_underscores for functions and methods. Always use self as the name for the first method argument (see A First Look at Classes for more on classes and methods).

- Don’t use fancy encodings if your code is meant to be used in international environments. Plain ASCII works best in any case.

[Guess the Number - http://www.codeskulptor.org/#user40_QwCzfXhK4H_9.py]

# template for "Guess the number" mini-project

import simplegui
import random
import math

# Global Variables

num_range = 100
num_guesses = 7
secret_number = 0

# Helper Function

def new_game():
    global secret_number, num_range, num_guesses
    secret_number = random.randint(0,num_range)
    calculation_n_1 = max(0,num_range) - min(0,num_range) + 1
    calculation_n_2 = math.ceil(math.log(calculation_n_1,2))
    num_guesses = int(calculation_n_2)
    print "New game started with range 0 - ", num_range, "!"
    print "Number of guesses left: ", num_guesses
    
# Event Handlers

def range100():
    global num_range
    num_range = 100
    new_game()
    
def range1000():
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    global secret_number, num_guesses
    value = int(guess)
    print "Guess was ", value
    
    if value > secret_number:
        num_guesses -= 1
        if num_guesses == 0:
            print "Lower & Game Over. Guesses left: ", num_guesses
            new_game()
        else:
            print "Lower, number of guesses left: ", num_guesses
    elif value < secret_number:
        num_guesses -= 1
        if num_guesses == 0:
            print "Higher & Game Over. Guesses left: ", num_guesses
            new_game()
        else:
            print "Higher, number of guesses left: ", num_guesses
    elif value == secret_number:
        num_guesses -= 1   
        print "Correct!"
        new_game()
    else:
        print "Error"
    
# Create Frame

f = simplegui.create_frame("Guess the number", 200, 200)

# Registration Event Handlers & Start Frame

f.add_button("Range is (0, 100)", range100, 200)
f.add_button("range is (0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# Starting the Game

new_game()

[Canvas and Drawing]

Event-Driven Drawing
- Computor monitor - 2D grid of pixels stored logically in a frame buffer (something which keeps track of the values of the pixels)
- Computers update the monitor based on the frame buffer at rate of around 60-72 times a second (refresh rate)
- Many applications will register a special function called a "draw handler" which will update the frame buffer.
- In CodeSkulptur we will register a simple draw handler using a simpleGUI command. CodeSkultor calls the draw handler at around 60 times per second.
- The draw handler updates the canvas using a collection of draw commands that include things like draw_text, draw_line, draw_circle. 

Canvas Coordinates
- Origin (0) is always in the left uppper corner, not lower!

# first example of drawing on the canvas

import simplegui

# define draw handler
def draw(canvas):
    canvas.draw_text("Hello!",[100, 100], 24, "White")
    canvas.draw_circle([100, 100], 2, 2, "Red")

# create frame
frame = simplegui.create_frame("Text drawing", 300, 200)

# register draw handler    
frame.set_draw_handler(draw)

# start frame
frame.start()

- You start text at the lower left of the string [X,Y.

# example of drawing operations in simplegui
# standard HMTL color such as "Red" and "Green"
# note later drawing operations overwrite earlier drawing operations

import simplegui


# Handler to draw on canvas
def draw(canvas):
    canvas.draw_circle([100, 100], 50, 2, "Red", "Pink")
    canvas.draw_circle([300, 300], 50, 2, "Red", "Pink")
    canvas.draw_line([100, 100],[300, 300], 2, "Black")
    canvas.draw_circle([100, 300], 50, 2, "Green", "Lime")
    canvas.draw_circle([300, 100], 50, 2, "Green", "Lime")
    canvas.draw_line([100, 300],[300, 100], 2, "Black")
    canvas.draw_polygon([[150, 150], [250, 150], [250, 250], [150, 250]], 2, 
          "Blue", "Aqua")
    canvas.draw_text("An example of drawing", [60, 385], 24, "Black")

    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 400, 400)
frame.set_draw_handler(draw)
frame.set_canvas_background("Yellow")


# Start the frame animation
frame.start()

[String Processing]

# String literals
s1 = "Rixner's funny"
s2 = 'Warren wears nice ties!'
s3 = " t-shirts!"
#print s1, s2
#print s3

# Combining strings
a = ' and '
s4 = "Warren" + a + "Rixner" + ' are nuts!'
print s4

# Characters and slices
print s1[3]  #=> n
print s1[-1] #=> y
print s1[-2] #=> n
print len(s1)
print s1[0:6] + s2[6:] --> up to but NOT including.
print s2[:13] + s1[9:] + s3

# Converting strings
s5 = str(375)
print s5[1:]
i1 = int(s5[1:])
print i1 + 38

# Handle single quantity
def convert_units(val, name):
    result = str(val) + " " + name
    if val > 1:
        result = result + "s"
    return result
        
# convert xx.yy to xx dollars and yy cents
def convert(val):
    # Split into dollars and cents
    dollars = int(val)
    cents = int(round(100 * (val - dollars)))

    # Convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")

    # return composite string
    if dollars == 0 and cents == 0:
        return "Broke!"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string
    
    
# Tests
print convert(11.23)
print convert(11.20) 
print convert(1.12)
print convert(12.01)
print convert(1.01)
print convert(0.01)
print convert(1.00)
print convert(0)

[Interactive Drawing]

# interactive application to convert a float in dollars and cents

import simplegui

# define global value

value = 3.12

# Handle single quantity
def convert_units(val, name):
    result = str(val) + " " + name
    if val > 1:
        result = result + "s"
    return result
        
# convert xx.yy to xx dollars and yy cents
def convert(val):
    # Split into dollars and cents
    dollars = int(val)
    cents = int(round(100 * (val - dollars)))

    # Convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")

    # return composite string
    if dollars == 0 and cents == 0:
        return "Broke!"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string  

# define draw handler
def draw(canvas):
    canvas.draw_text(convert(value), [60, 110], 24, "White")

# define an input field handler
def input_handler(text):
    global value
    value = float(text)

# create a frame
frame = simplegui.create_frame("Converter", 400, 200)
frame.add_input("Enter value", input_handler, 100)


# register event handlers
frame.set_draw_handler(draw)

# start the frame
frame.start()

---

string = '1lll1l1l1l1ll1l111ll1l1ll1l1ll1ll111ll1ll1ll1l1ll1ll1ll1ll1lll1l1l1l1l1l1l1l1l1l1l1l1ll1lll1l111ll1l1l1l1l1'
print len(string)

ones = 0
els = 0
other = 0
    
for i in range(0,len(string)):
        if string[i] == '1':
            ones += 1
        elif string[i] == 'l':
            els += 1
        else:
            other += 1

print "Ones: ", ones
print "L's: ", els
print "Other: ", other

[Timers]

# Simple "screensaver" program.

# Import modules
import simplegui
import random

# Global state
message = "Python is Fun!"
position = [50, 50]
width = 500
height = 500
interval = 2000

# Handler for text box
def update(text):
    global message
    message = text
    
# Handler for timer
def tick():
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    position[0] = x #=> When you are changing elements of a global variable, the global declaration is optional!
    position[1] = y #=> When you are changing elements of a global variable, the global declaration is optional!

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, position, 36, "Red")

# Create a frame 
frame = simplegui.create_frame("Home", width, height)

# Register event handlers
text = frame.add_input("Message:", update, 150)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# Start the frame animation
frame.start()
timer.start()

[Programming Tips - Week 3]

#####################
# Example of event-driven code, buggy version

import simplegui

size = 10
radius = 10

# Define event handlers.

def incr_button_handler():
    """Increment the size."""
    global size
    size += 1
    label.set_text("Value: " + str(size))
    
def decr_button_handler():
    """Decrement the size."""
    global size
    # Insert check that size > 1, to make sure it stays positive
    # NOTE that this restriction has changed from the video
    # since draw_circle now throws an error if radius is zero
    size -= 1
    label.set_text("Value: " + str(size))

def change_circle_handler():
    """Change the circle radius."""
    global radius
    radius = size
    # Insert code to make radius label change.
    
def draw_handler(canvas):
    """Draw the circle."""
    canvas.draw_circle((100, 100), radius, 5, "Red")

# Create a frame and assign callbacks to event handlers.

frame = simplegui.create_frame("Home", 200, 200)
label = frame.add_label("Value: " + str(size))
frame.add_button("Increase", incr_button_handler)
frame.add_button("Decrease", decr_button_handler)
frame.add_label("Radius: " + str(radius))
frame.add_button("Change circle", change_circle_handler)
frame.set_draw_handler(draw_handler)

# Start the frame animation

frame.start()

---

import simplegui

#####################
# Buggy code -- doesn't start frame

message = "Welcome!"

def click():
    """Change message on mouse click."""
    global message
    message = "Good job!"

def draw(canvas):
    """Draw message."""
    canvas.draw_text(message, [50,112], 36, "Red")

# Create a frame and assign callbacks to event handlers

frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

frame.start()

#####################
# Buggy code -- doesn't start timers

def timer1_handler():
    print "1"
    
def timer2_handler():
    print "2"

timer1 = simplegui.create_timer(100, timer1_handler)
timer2 = simplegui.create_timer(300, timer2_handler)

timer1.start()
timer2.start()

Mini-Project 3 - [Stopwatch: The Game]

http://www.codeskulptor.org/#user40_6D32nD7Dqj_6.py

# template for "Stopwatch: The Game"

import simplegui

# define global variables

time = 0
X = 0
Y = 0
XY = str(X) + '/' + str(Y)

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(time):
    A = time // 600 
    B = (time - A * 600) // 100
    C = time % 100 // 10
    D = time % 10
    return str(A) + ':' + str(B) + str(C) + ':' + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    timer.start()

def stop():
    global X, Y, XY
    if timer.is_running():
        Y += 1
        if time % 10 == 0:
            X += 1
        XY = str(X) + '/' + str(Y)
    timer.stop()

def reset():
    global time, X, Y, XY
    time = 0
    X = 0
    Y = 0 
    XY = str(X) + '/' + str(Y)
    
# define event handler for timer with 0.1 sec interval

def tick():
    global time
    time += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [110, 120], 36, 'White', 'sans-serif')
    canvas.draw_text(XY, [215, 35], 36, 'Green', 'sans-serif')
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)
timer = simplegui.create_timer(100, tick)

# register event handlers

frame.add_button('Start', start)
frame.add_button('Stop', stop)
frame.add_button('Reset', reset)
frame.set_draw_handler(draw)

# start frame

frame.start()

# Please remember to review the grading rubric

- In Python, the time module can be used to determine the current time. This module includes the method time which returns the current system time in seconds since a date referred as the Epoch. The Epoch is fixed common date shared by all Python installations. Using the date of the Epoch and the current system time, an application such as a clock or calendar can compute the current time/date using basic arithmetic.

import simplegui

n = 23

def collatz_conjecture():
    global n
    if n == 1:
        timer.stop()
    elif n % 2 == 0:
        n = n / 2
        print n
    else:
        n = (n * 3) + 1
        print n
    
timer = simplegui.create_timer(100, collatz_conjecture)
timer.start()

[Lists]

- A list is a sequence type
- lists use square brackets 
- [] = empty list
- position = [x, y]

l = [1, 3, 4, -7, 62, 43]
l2 = ['milk', 'eggs', 'bread', 'butter']
l3 = [[3, 4], ['a', 'b', 'c'], []]

print len(l)  #=> 6
print len(l2) #=> 4
print len(l3) #=> 3

print "first element: ", l[0] #=> 1
print "last element: ", l[-1] #=> 43
print l3[1] #=> ['a', 'b', 'c'] -- start counting at 0
print l3[0][1] #=> 4
l4 = 12[1:3] # starting at element 1 but up to (not including) 3
print l4 #=> ['eggs', 'bread']

l2[0] = 'cheese'
print l2 #=> ['cheese', 'eggs', 'bread', 'butter']
- Good programmers keep their lists monogamous (basically vectors) --> all data types of the same type, strings, numerics, objects, etc.

[Keyboard Input]

===

# Keyboard echo

import simplegui

# initialize state
current_key = ' '

# event handlers
def keydown(key):
    global current_key
    current_key = chr(key) # chr turns a number into a string
    
def keyup(key):
    global current_key
    current_key = ' '
    
def draw(c):
    # NOTE draw_text now throws an error on some non-printable characters
    # Since keydown event key codes do not all map directly to
    # the printable character via ord(), this example now restricts
    # keys to alphanumerics
    
    if current_key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        c.draw_text(current_key, [10, 25], 20, "Red")    
        
# create frame             
f = simplegui.create_frame("Echo", 35, 35)

# register event handlers
f.set_keydown_handler(keydown)
f.set_keyup_handler(keyup)
f.set_draw_handler(draw)

# start frame
f.start()

# <18> are the acutal key codes

===

# control the position of a ball using the arrow keys

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]

# define event handlers
def draw(canvas):
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

def keydown(key):
    vel = 4 # velocity
    if key == simplegui.KEY_MAP["left"]:
        ball_pos[0] -= vel
    elif key == simplegui.KEY_MAP["right"]:
        ball_pos[0] += vel
    elif key == simplegui.KEY_MAP["down"]:
        ball_pos[1] += vel
    elif key == simplegui.KEY_MAP["up"]:
        ball_pos[1] -= vel        
    
# create frame 
frame = simplegui.create_frame("Positional ball control", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# start frame
frame.start()

===

[Motion]

position = velocity * time [p = v * t]
# assumes velocity is constant 

===

# Ball motion with an explicit timer

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

init_pos = [WIDTH / 2, HEIGHT / 2] # middle of canvas
vel = [0, 3]  # pixels per tick
time = 0

# define event handlers
def tick():
    global time
    time = time + 1

def draw(canvas):
    # create a list to hold ball position
    ball_pos = [0, 0]

    # calculate ball position
    ball_pos[0] = init_pos[0] + time * vel[0]
    ball_pos[1] = init_pos[1] + time * vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

timer = simplegui.create_timer(100, tick)

# start frame
frame.start()
timer.start()

===

- [3,3] + vector [6,1] == [9,4]

P(0) ----> P(1) ----> P(2) ----------> P(3)
     V(0)       V(1)           V(2)

P(t+1) = P(t) + (1 * V(t))

P[0] = P[0] + V[0]
P[1] = P[1] + V[1]

===

# Ball motion with an implicit timer

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [0, 1] # pixels per update (1/60 seconds -- implicit to the draw handler)

# define event handlers
def draw(canvas):
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]

    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()

===

[Collisions and Reflections]

# Distance between two points

Point 1 == p[x,y] # end
Point 2 == q[x,y] # start

math
dist(p,q)^2 == (p[0] - q[0])^2 + (p[1] - q[1])^2 # C^2 = A^2 + B^2

Python
def dist(p, q):
    return math.sqrt((p[0] - q[0])**2 + (P[1] - q[1])**2)a=
 
# Vectors and Motion

v[0] = p[0] - q[0]
v[1] = p[1] - v[1]

Moving/translate a point using a vector: p = q + v

p[0] = q[0] + v[0]
p[1] = q[1] + v[1]

# Update for Motion

Math - point at position p with velocity v
p = p + a * v # 'a' is 'some' constant multiple of the velocity

p[0] = p[0] + a * v[0]
p[1] = p[1] + a * v[1]

[Collisions]

Left wall
p[0] <= 0

Right wall
p[0] >= width - 1

Collision of ball with center p and radius r with wall

Left wall
p[0] <= r

Right wall
p[0] >= (width - 1) - r

Bottom wall
p[1]  >= (height - 1) - r 

Reflections - update the velocity vector v

Left wall - compute reflected velocity vector (negate it)
v[0] = -v[0] # negate
v[1] = v[1]  # stays the same

===

0 == x == horizontal
1 == y == vertical

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-40.0 / 60.0,  5.0 / 60.0]

# define event handlers
def draw(canvas):
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS:
        vel[0] = - vel[0]
    
    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
frame = simplegui.create_frame("Ball physics", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()

===

[Velocity Control]

===

# control the position of a ball using the arrow keys

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]

# define event handlers
def draw(canvas):
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

def keydown(key):
    vel = 4
    if key == simplegui.KEY_MAP["left"]:
        ball_pos[0] -= vel
    elif key == simplegui.KEY_MAP["right"]:
        ball_pos[0] += vel
    elif key == simplegui.KEY_MAP["down"]:
        ball_pos[1] += vel
    elif key == simplegui.KEY_MAP["up"]:
        ball_pos[1] -= vel        
    
    print ball_pos

# create frame 
frame = simplegui.create_frame("Positional ball control", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# start frame
frame.start()

===

# control the velocity of a ball using the arrow keys

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [0, 0]

# define event handlers
def draw(canvas):
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]

    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

def keydown(key):
    acc = 1
    if key==simplegui.KEY_MAP["left"]:
        vel[0] -= acc
    elif key==simplegui.KEY_MAP["right"]:
        vel[0] += acc
    elif key==simplegui.KEY_MAP["down"]:
        vel[1] += acc
    elif key==simplegui.KEY_MAP["up"]:
        vel[1] -= acc
        
    print ball_pos
    
# create frame 
frame = simplegui.create_frame("Velocity ball control", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# start frame
frame.start()

[Visualizing Lists and Mutation]

###################################
# Mutation vs. assignment

is == ==

################
# Look alike, but different

a = [4, 5, 6]
b = [4, 5, 6]
print "Original a and b:", a, b
print "Are they same thing?", a is b #=> False

a[1] = 20
print "New a and b:", a, b
print

################
# Aliased

c = [4, 5, 6]
d = c
print "Original c and d:", c, d
print "Are they same thing?", c is d #=> True

c[1] = 20
print "New c and d:", c, d
print

################
# Copied

e = [4, 5, 6]
f = list(e)
print "Original e and f:", e, f
print "Are they same thing?", e is f

e[1] = 20
print "New e and f:", e, f
print


###################################
# Interaction with globals


a = [4, 5, 6]

def mutate_part(x):
    a[1] = x #=> for item assignment (mutation) you don't need to specify global, it assumes it

def assign_whole(x):
    a = x  #=> here it assumes a is a local variable

def assign_whole_global(x):
    global a
    a = x

mutate_part(100)
print a

assign_whole(200)
print a

assign_whole_global(300)
print a

[Programming Tips]

print 1 is 1 # True
print 1.0 is 1.0 # True
print True is True # True
print "abc" is "abc" # True
print [4, 5, 6] is [4, 5, 6] # False - only type that is mutable // two different lists that happen to look-a-like
print 1 is 1.0 # False - integers are not floating type
print (4, 5, 6) is (4, 5, 6) # False - Tuple

Tuples
- Look like lists but are NOT mutable.
- Tuples and lists support the same non-mutation operations. Like lists, you can loop on tuples.
- The benefit is that sometimes you want to make sure your data is not changed, to protect you data.

# Lists (mutable) vs. tuples (immutable)

print [4, 5, 6] #=> [4, 5, 6]
print (4, 5, 6) #=> (4, 5, 6)

print type([4, 5, 6]) #=> <class 'list'>
print type((4, 5, 6)) #=> <class 'tuple'>

a = [4, 5, 6]
a[1] = 100
print a #=> [4, 100, 6]

b = (4, 5, 6)
b[1] = 100
print b #=> Error - 'tuple' does not support item assignment

[Pong]

===

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals 

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

paddle1_vel = [0] # only one item since we do not move horizontally
paddle1_pos = [(WIDTH - 4.0),(HEIGHT / 2.0)]
paddle2_vel = [0] # only one item since we do not move horizontally
paddle2_pos = [(WIDTH - (PAD_WIDTH / 2.0)),(HEIGHT / 2.0)]

ball_pos = [(WIDTH/2), (HEIGHT/2)]
ball_vel = [0.0, 0.0]
acc = 4
vel_increase = 0.1

score_left = 0
score_right = 1

def spawn_ball(direction):
    global ball_pos 
    ball_pos = [(WIDTH/2), (HEIGHT/2)]
    
    if direction == 'LEFT':
            # draw handler draws 60x per second: 120/60 = 2 & 240/60 = 4
            ball_vel[0] = (random.randrange(2.0, 4.0, 1) * -1) 
            ball_vel[1] = (random.randrange(1.0, 3.0, 1) * -1)
    elif direction == 'RIGHT':
            # draw handler draws 60x per second: 60/60 = 1 & 180/60 = 3
            ball_vel[0] = random.randrange(2.0, 4.0, 1)
            ball_vel[1] = (random.randrange(1.0, 3.0, 1) * -1)
    else: 
        print "Direction parameter of spawn_ball() not recognized.."

# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score_left, score_right
    score_left = 0
    score_right = 0
    random_side = random.randint(1, 2)
    
    if random_side == 1:
        spawn_ball('LEFT')
    elif random_side == 2:
        spawn_ball('RIGHT')
    else:
        print "Error new_game() direction not recognized"
    
def draw(canvas):
    global vel_increase, score_left, score_right
    
    # draw mid line and gutters
    
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
            
    # draw ball

    canvas.draw_circle([(ball_pos[0] + ball_vel[0]),(ball_pos[1] + ball_vel[1])], BALL_RADIUS, 5, "White", "White")
        
    # Paddle 1 position + keep on screen
    
    if paddle1_pos[1] - HALF_PAD_HEIGHT < 0:
         paddle1_pos[1] = HALF_PAD_HEIGHT
    elif paddle1_pos[1] + HALF_PAD_HEIGHT > HEIGHT:
         paddle1_pos[1] = (HEIGHT - HALF_PAD_HEIGHT)
    else:
         paddle1_pos[1] += paddle1_vel[0]
    
    # Paddle 2 position + keep on screen
    
    if paddle2_pos[1] - HALF_PAD_HEIGHT < 0:
         paddle2_pos[1] = HALF_PAD_HEIGHT
    elif paddle2_pos[1] + HALF_PAD_HEIGHT > HEIGHT:
         paddle2_pos[1] = (HEIGHT - HALF_PAD_HEIGHT)
    else:
        paddle2_pos[1] += paddle2_vel[0]
    
    # Ball position + collision
    
    if ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
         ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] < BALL_RADIUS + 1:
         ball_vel[1] = -ball_vel[1]
    elif ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH:
        
            if ball_pos[1] > (paddle2_pos[1] - HALF_PAD_HEIGHT) and ball_pos[1] < (paddle2_pos[1] + HALF_PAD_HEIGHT):
                ball_vel[0] = -ball_vel[0]
                ball_vel[0] = ball_vel[0] * (1 + vel_increase)
                ball_vel[1] = ball_vel[1] * (1 + vel_increase)
            else:
                 spawn_ball('LEFT')
                 score_right += 1
                    
    elif ball_pos[0] - BALL_RADIUS <= PAD_WIDTH:
           
            if ball_pos[1] > (paddle1_pos[1] - HALF_PAD_HEIGHT) and ball_pos[1] < (paddle1_pos[1] + HALF_PAD_HEIGHT):
                ball_vel[0] = -ball_vel[0]
                ball_vel[0] = ball_vel[0] * (1 + vel_increase)
                ball_vel[1] = ball_vel[1] * (1 + vel_increase)
            else:
                spawn_ball('RIGHT')
                score_left += 1
                
    ball_pos[0] += ball_vel[0] 
    ball_pos[1] += ball_vel[1]
    
    # Draw Paddle 1

    canvas.draw_line([(PAD_WIDTH / 2),(paddle1_pos[1] + HALF_PAD_HEIGHT)], [(PAD_WIDTH / 2),(paddle1_pos[1] - HALF_PAD_HEIGHT)], PAD_WIDTH, "White")
    
    # Draw Paddle 2

    canvas.draw_line([(WIDTH - (PAD_WIDTH / 2)),(paddle2_pos[1] + HALF_PAD_HEIGHT)], [(WIDTH - (PAD_WIDTH / 2)),(paddle2_pos[1] - HALF_PAD_HEIGHT)], PAD_WIDTH, "White")    
    
    # draw scores

    canvas.draw_text(str(score_left), (450, 30), 24, "White", "monospace")
    canvas.draw_text(str(score_right), (150, 30), 24, "White", "monospace")

def keydown(key):
    global acc
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel[0] -= acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[0] += acc
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[0] -= acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[0] += acc

def keyup(key):
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel[0] = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[0] = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[0] = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[0] = 0
    
# create frame

frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', new_game)

# start frame

new_game()
frame.start()

http://www.codeskulptor.org/#user40_zOy9sLlDqc_31.py

===

Dividing lists:

my_list[: len(my_list) // 2] and my_list[len(my_list) // 2 :]
my_list[0 : len(my_list) // 2] and my_list[len(my_list) // 2 : len(my_list)]

import math

def dist(p, q):
    radius = 2
    distance = math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)
    result = distance - radius
    return result
    
p = [4, 7]
q = [2, 9]

print dist(p,q)

===

import simplegui

global_var = 5

def draw(canvas):
    global global_var
    canvas.draw_text(str(global_var), (10, 50), 24, "White", "monospace")

def keydown(key):
    global global_var
    if key == simplegui.KEY_MAP["w"]:
        global_var *= 2
  
def keyup(key):
    global global_var
    if key == simplegui.KEY_MAP["w"]:
        global_var -= 3

frame = simplegui.create_frame("Quiz", 100, 100)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

frame.start()