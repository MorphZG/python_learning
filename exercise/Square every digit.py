"""
www.codewars.com

Details:
Welcome. In this kata, you are asked to square every digit of a number
and concatenate them. For example, if we run 9119 through the function,
811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
"""


"""
I completed the test but it seems awfuly unefficient because of
many type conversions. Cant wait to find creative solutions by others.

At the bottom of the file is one really strange solution.... scroll to see it.
"""
# <! --- My solution doesnt seems so bad after i look at the others.
def square_digits(num):
    """first convert number to string and separate every digit
       than again convert to integer so we can do math.
       after we get list of squares i must convert those numbers
       back to string so i can join them together
       and finaly convert again to integer and return the full number....
    """
    digits = [int(i) for i in str(num)]
    squares = [i*i for i in digits]
    strings = [str(i) for i in squares]
    joined = ''.join(strings)
    return int(joined)


# These are some clever solution from other community members

# <! --- clever solution 01
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))

# <! --- clever soultion 02
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

# <! --- clever soultion 03
def square_digits(num):
    return int(''.join(str(int(c)**2) for c in str(num)))

# <! --- clever soultion 04
def square_digits(num):
    result = 0
    multiplier = 1
    while num > 0:
        digit = (num % 10)
        result += (digit**2) * multiplier
        num /= 10
        multiplier *= 10
        if digit > 3:
            multiplier *= 10
    return result

# <! --- clever soultion 05
def square_digits(num):
    result = 0
    multiplier = 1
    while num:
        digit = num % 10
        result += digit ** 2 * multiplier
        multiplier *= (10, 100)[digit > 3]
        num //= 10
                                        
    return result


# <! --- CRAZY soultion
def square_digits(num):
    num = str(num)
    nw = ""
    for i in range(0,len(num)):
        if i < len(num) - 1:
            nw += num[i] + " "
        else:
            nw += num[i]
    l = nw.split(" ")
    k = []
    for i in l:
        if i == "9":
            k += "81"
        if i == "8":
            k += "64"
        if i == "7":
            k += "49"
        elif i == "6":
            k += "36"
        elif i == "5":
            k += "25"
        elif i == "4":
            k += "16"
        elif i == "3":
            k += "9"
        elif i == "2":
            k += "4"
        elif i == "1":
            k += "1"
        elif i == "0":
            k += "0"
    r = "".join(k)
    o = int(r)
    return o


#tags: