#exercise 05-01 www.py4e.com
#https://www.youtube.com/watch?v=kjxXZQw0uPg
#program reads numbers until the input "done"
#when "done" print total, count, average
#if user enters anything other than number
#detect mistake using try and except

total = 0
count = 0
average = 0
user_input = 0

while True:
    print('type "done" to quit')
    user_input = input("enter a number: ")
    if user_input == "done":
        break
    try:
        user_input = int(user_input)
    except:
        print('invalid input')
        continue
    total = user_input + total
    print('total: ', total)
    count += 1


average = total / count
print('total: ', total,
      'count: ', count,
      'average: ', average)

#tags: count, average, total