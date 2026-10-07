# variables 

counter = 0
counter = counter + 1
counter = counter * 4
print(counter)

string_variable = "Hello, World! "
string_variable = string_variable * counter
print(string_variable)
#########################################################
# functions with docstrings

def greet(name):
  """
  This function greets the person with the given name.
  """
  const = "Hello, " + name + "!"
  return const

print(greet("Alice"))

# help(greet) -> A brief English description of what the function does.

#########################################################

# functions without return values

def greet(name):
  """
  This function greets the person with the given name.
  """
  const = "Hello, " + name + "!"

print(greet("Bob"))

mystery = print()
print(mystery)

#########################################################

# functions with default arguments

print(1,2,3,44, sep=" -->") # sep is a default argument

def greet(name="World"):
  """
  This function greets the person with the given name.
  If no name is provided, it defaults to "World".
  """
  print ("Hello, " + name)

greet()
greet("Charlie")
#########################################################

# Functions Applied to Functions

# Let's take two simple functions:

# f(x) = x + 3
def f(x):
  return x + 3

# g(x) = x^2
def g(x):
  return x**2

# In Math: This is simply evaluating f(x) at x=2, which gives f(2) = 10.
def call_fn(fn, arg):
  """Call fn on arg"""
  return fn(arg)

# In Math: Self-Composition (f o f)(x) || f(f(x))  
def squre_fn(fn,arg):
  """Call fn on the result of calling fn on arg"""
  return fn(fn(arg))

# f(g(x))
def fog(fn, gn, arg):
  return fn(gn(arg))

print(
  f(2),          # 2 + 3 = 5
  call_fn(f, 2), # f(2) = 5
  squre_fn(f, 2),# f(f(2)) -> f(5) -> 5 + 3 = 8
  fog(f,g,5),    # f(g(5)) -> f(25) -> 25 + 3 = 28
  fog(g,f,5),    # g(f(5)) -> g(8) -> 8^2 = 64
  fog(f,f,5),    # f(f(5)) -> f(8) -> 8 + 3 = 11
  fog(g,g,5),    # g(g(5)) -> g(25) -> 25^2 = 625,
  sep='\n'
)

#########################################################

# Functions that operate on other functions are called "Higher-order functions." 

def mod_5 (x):
  return x % 5

print (

  mod_5(10),
  max(10, 20, 30, 40, 50),

  max(10, 20, 30, 40, 50, key=mod_5), # famous quirk in Python's max function: it returns the first maximum value if there are multiple maximum values.

  max(10, 14, 30, 40, 50, key=mod_5),
  sep='\n'
)

############################################################

print(round(338424, -3)) #output 3384000

############################################################
# Boolean conversion

print(bool(1)) # True 
print(bool(0)) # False
print(bool("asf")) # True
print(bool("")) # False

print(1 and 0) # False
print(0 or 0) # False
print( not 0) # True

############################################################

# Lists : lists can contain a mix of different types of variables:

my_favourite_things = [32, 'raindrops on roses', max]

print(my_favourite_things)

print(my_favourite_things[0])
print(my_favourite_things[1])
print(my_favourite_things[2])

print(my_favourite_things[0])
print(my_favourite_things[1])
print(my_favourite_things[2])

primes = [2, 3, 5, 7]
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Sa☻turn', 'Uranus', 'Neptune']

############################################################

# Loops
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
  print(planet, end=' ') # print all on same line
  
# range : useful for writing loops.
for i in range(5):
  print("Doing important work. i =", i)
  
#  while loops
i = 0
while i < 5:
  print("Doing important work. i =", i)
  i += 1

# enumerate
for i, planet in enumerate(planets):
  print("Planet", i, "is", planet)
  
# List comprehensions
squares = [n**2 for n in range(10)]
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets) # ['Venus', 'Earth', 'Mars']

with_vowels = [planet for planet in planets if 'a' in planet]
print(with_vowels) # ['Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus']

##############################################################

# String syntax

x = 'Pluto is a planet'
y = "Pluto is a planet"
x == y