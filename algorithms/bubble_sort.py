# Basic version
# Bubble Sort algorithm

"""
Bubble sort is very inefficient sorting algorithm but it is good as a learning
example. If i pass it already sorted array it will loop through maximum iteration
number even though it doesn't have to. I have defined a bubble2() function that
will break out of the loop earlier. It is still slow and not optimized but it shows
that even small modifications can shorten the completion time and lower the number
of iterations.

Try exporting the script results to file instead of showing it on screen and look
at the number of text lines or number of iterations for each

    $ python bubble_sort.py > file_name.txt

I have added the print statement in between so i can see what is happening and
how it works

"""
import random


def basic_bubble(array):

    # loop through the array, index for the adjacent element
    for i in range(len(array)):
        # outer loop for each iteration
        print(f'Main loop - Iteration - {i}')
        for j in range(0, len(array) -i -1):
            # inner loop
            # compare the elements
            print(f'Inner loop - {j}')
            if array[j] > array[j+1]:
                # swapping the elements over
                # swap their place if the first is larger then its neighbour
                print(f'swapping: {array[j]}-> <-{array[j+1]}')
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


def bubble_2(array):

    # loop through the array, index for the adjacent element
    for i in range(len(array)):
        # outer loop for each iteration

        # done flag
        done = False

        print(f'Main loop - Iteration - {i}')
        for j in range(0, len(array) -i -1):
            # inner loop
            # compare the elements
            print(f'Inner loop - {j}')
            if array[j] > array[j+1]:
                # swapping the elements over
                # swap their place if the first is larger then its neighbour
                print(f'swapping: {array[j]}-> <-{array[j+1]}')
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

                # are we done?
                done = True

        if not done:
            print('breaking out')
            break

    return array


# list of numbers between 1 and 30
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# random.shuffle() shuffles the original list, shuffling can be done in-place
# random.sample() returns a new shuffled list, based on the original list
# random.sample(array, number of items)
new_list = random.sample(numbers_list, len(numbers_list))
sorted_list1 = basic_bubble(new_list)

# shuffle again for bubble_2
new_list = random.sample(numbers_list, len(numbers_list))
sorted_list2 = bubble_2(new_list)


#modules: random,
#tags: algorithm, bubble sort
