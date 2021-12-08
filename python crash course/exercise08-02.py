'''Favorite Book
Write a function called favorite_book(), accept 1 parameter, title.
Function should print a message: One of my favorite books is...
Call the function, making sure to include a book title as argument.
'''


def favorite_book(title):
    print(f'One of my favorite books is {title.title()}')
    return


favorite_book('needful things')
