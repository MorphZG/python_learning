'''
import whole module with all functions.
when calling a function you must add module name first
so python knows where to find it.

syntax for call:
module_name.function_name()
'''

import pizza 
pizza.make_pizza(16, 'pepperoni', 'paprika', 'extra cheese')
pizza.make_pizza(12, 'mushrooms')


'''
You can use alias for imported modules

syntax:
import module_name as alias_name
'''

import pizza as p
p.make_pizza(16, 'pepperoni', 'paprika', 'extra cheese')
p.make_pizza(12, 'mushrooms')


'''
dir()
Without arguments, return the list of names in the
current local scope. With an argument, attempt to
return a list of valid attributes for that object.
'''
print('\nprinting list of names in pizza module:')
print(dir(pizza))

'''
you can import all functions in a module
by using asterix so you dont have to add module
name before function call.

if you work with large modules you can get matching 
names and overwrite functions in your code.

syntax (possible conflicts with global names):
from pizza import *
'''
'''
as with functions (chapter 8), when importing classes (chapter 9) you can:

    - import a single class:
    from module import class

    - import multiple classes from module:
    from module import class1, class2, class3

    - import entire module:
    import module

    - import all classes from a module:
    from module import *

dont forget you can use aliases:
    - from [module] import [class] as [alias]
'''

#tags: module import, function, alias