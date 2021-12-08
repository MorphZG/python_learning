'''
you can import specific function from a module
that way you just call a function like you normaly would
since we have name of the function defined on import.
you can also import multiple functions:

syntax for import:
from module_name import function_1, function_2, function_3
'''

from pizza import make_pizza
make_pizza(16, 'pepperoni', 'paprika', 'extra cheese')
make_pizza(12, 'mushrooms')


'''
You can use alias for imported functions

syntax:
from module_name import function_name as alias_name
'''

from pizza import make_pizza as mp
mp(16, 'pepperoni', 'paprika', 'extra cheese')
mp(12, 'mushrooms')


#tags: function import, module, alias