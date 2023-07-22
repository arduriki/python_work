import pizza as p  # -> import module (file name) + alias
from pizza import make_pizza as mp  # from file import function and assign an alias
from pizza import *  # import all functions from the module

# Import entire module -> 2nd best
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Import a function from a module -> 1st best
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# Import all functions from a module
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')