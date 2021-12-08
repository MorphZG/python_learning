'''
Exercise 9: Check Palindrome Number
https://pynative.com/python-basic-exercise-for-beginners/

Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is same after reverse.
For example 545, is the palindrome numbers

Expected Output:
    original number 121
    Yes. given number is palindrome number
    
    original number 125
    No. given number is not palindrome number
'''


def palindrome(number):
    ''' returns True if param1 is palindrome '''
    original_num = number
    reverse_num = 0
    
    # reversing the given number
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    if original_num == reverse_num:
        return True
    else:
        return False


print('Original number', 121)
print(palindrome(121))
