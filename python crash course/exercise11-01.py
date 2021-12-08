# Chapter 11, Testing your code
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

'''City, country
Write a function that accepts two parameters: a city name and a country name.
The function should return a single string of the form City, Country, such as
Santiago, Chile. Store the function in a module called city_functions.py

Create a file called test_cities.py that tests the function you just wrote
(remember that you need to import unittest and the function you want to test).
Write a method called test_city_country() to verify that calling your function
with values such as 'santiago' and 'chile' results in the correct string.
Run test_cities.py, and make sure test_city_country() passes.
'''

import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    '''tests for city_functions.py'''
    
    def test_city_country(self):  # auto run, no need to call test methods
        '''test'''
        wanted_output = city_country('zagreb', 'croatia')
        self.assertEqual(wanted_output, 'Zagreb, Croatia')


'''
special variable __name__ is set when program is executed. If this file is
being run as the main program, the value of __name__ is set to '__main__'.
In this case, we call unittest.main() which runs the test case. When a testing
framework imports this file, the value of __name__ won't be '__main__' and
this block will not be executed.
'''

# __name__ is special variable
# __main__ is value set if file is run as main program(not imported to another)
if __name__ == '__main__':
    unittest.main()

'''         <! --- OFFICIAL DOCUMENTATION
https://docs.python.org/3/library/unittest.html


     Method === === === === ===  Assertion Check

assertEqual(a,b) --- --- --- --    a == b
assertNotEqual(a,b) --- --- ---    a != b
assertTrue(x) --- --- --- --- -  bool(x) is True
assertFalse(x) --- --- --- ---   bool(x) is False
assertIs(a,b) --- --- --- ---      a is b
assertIsNot(a, b) --- --- ---     a is not b
assertIsNone(x) --- --- --- ---   x is None
assertIsNotNone(x) --- --- ---   x is not None
assertIn(a, b) --- --- --- ---     a in b
assertNotIn(a, b) --- --- --- --  a not in b
assertIsInstance(a, b) --- ---   isinstance(a, b)
assertNotIsInstance(a, b) -- -- not isinstance(a, b)
'''

#modules: unittest
#tags: test, __main__(),