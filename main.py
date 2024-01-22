# Hello world program
# print is a "function" in python, more on functions later
print("Hello, World!")

# VARIABLES
# A variable is a place to store data/information
# For example, someone's name, a breed of dog, if someone has eaten today, etc.
# There are five main data types
# Python is dynamically typed, so there is no need to say the data type when creating a variable
# String, integer, double (decimal number), boolean (True/False), and None (null data type)
# notice how True, False, and None have the first letter capitalized. This is because they are "keywords"
name = "Aram Sodhi" # string
age = 17 # integer
test_score = 96.4 # double
eaten_today = True # boolean
occupation = None # Nonetype - represents nothing

# we can use operations to change the value of variables
# create two numbers x and y with values of 2 and 3 respectfully
x = 2
y = 3

# BASIC OPERATORS
print(x + y) # addition: 5
print(x - y) # subtraction: -1
print(x * y) # multiplication: 6
print(x / y) # division: 0.666666666...
print(y % x) # modulus - gives remainder when y is divided by x: 1
print(x ** y) # exponent - x to the power of y: 8

# COMPARISON OPERATORS
# evaluates to True or False
print(x == y) # False - two equals signs for checking equality and one for assignment
print(x > y) # False - is x greater than y ?
print(x < y) # True - is x less than y ?
print(x >= y) # False - is x greater than or equal to y ?
print(x <= y) # True - is x less than or equal to y ?
print(x != y) # True, checks if x is NOT equal to y

# BOOLEAN OPERATORS
print(x > 0 and x < 100) # evaluates to True if x is between x and 100 exclusive
print(not x > 50) # evaluates to true if x is not greater than 50
print(x < 0 or x > 10) # evaluates to true if x is less than 0 or greater than 10


# IF STATEMENTS
# the code inside the if statemnt is ONLY run if the condition in the if statement is True
# think of it as an "if (...), then..." setup
z = 10
if (z > 8):
    print("z is greater than 8")

# IF, ELIF, ELSE
# if (z > 8) is ran first
# if true, then the print statement is run
# if it is not true, then the elif statemnt is run
# if true, the print statement in the elif is run
# if false, the code in the else statement is run
if (z > 8):
    print("z is greater than 8")
elif (z == 8):
    print("z is equal to 8")
else:
    print("z is less than 8")


# FUNCTIONS/METHODS
# a function is a block of code with a name
# the name can be called from anywhere in the code after where the function is defined
# calling the name of the function will run the code the function contains
def say_hi():
    print("hello")

# it is important to know that the code inside the function is not run when it is defined, only when it is called
# now, saying "say_hi()" in our code will run the print statement inside of it
say_hi() # will output "hello"

# ARGUMENTS
# we can pass data into a function to change how it behaves
# the data we pass in is called an argument
# for example, we can create a new function to say hi to a particular person
def say_hi_to(name):
    print("hello " + name)

# this function does a few things
# based on the name of the person we "pass in" to the function, it will change what the print statement outputs
# it also "concatenates" the string "hello" with the name we pass into the function
say_hi_to("Aram") # this will output "hello Aram"

# one function can contain calls to several other functions as well
# additionally, we can have multiple arguments in a function, not just one
# similar to an if statement, the code "inside" the function is indented to signify it represents what the function does

# CLASSES
# a class represents an object in the physical world
# for example, we can create a class that reprents a character in a video game
# a class contains variables (attributes) and methods (functions)
# attibutes are information that represent a class
# methods can be thought of actions for that class - they DO THINGS
# In our Character class, we create a __init__ method, which initializes/sets up our class
# We also have methods for our class such as attacking another character and a speed powerup
class Character():
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

    def attack(self, enemy):
        enemy.health -= self.damage
        print("Attack that deals " + str(self.damage) + " damage")

    def speed_powerup(self, speed_increase):
        self.speed += speed_increase
        print("Speed has been increased by " + str(speed_increase))

# In order to use the code we write in our class, we need to create an "instance" of our class
warrior = Character(100, 20, 10) # create a warrior character that has 100 health, 20 damage, and 10 speed
zombie = Character(50, 50, 5) # create a zombie character that has 50 health, 50 damage, and 5 speed

# after creating these two instances of our class, we can start using methods
# lets say in our game, the zombie attacks the warrior
# we can use the attack method we wrote to do this
# before the zombie attacks the warrior, let's display the health of the warrior
# we also need to convert the warrior's health (an integer) to a string so that it can be printed
print("warrior health: " + str(warrior.health))

# now the zombie attacks the warrior
zombie.attack(warrior)

# and the health of the warrior should have decreased by 50 since the zombie deals 50 damage
print("warrior health: " + str(warrior.health))

# we can add more complicated functions to our methods to make them even more useful
