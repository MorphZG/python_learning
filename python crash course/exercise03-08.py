## page 46
# Try it yourself 3-8
# Seeing the world

#list of five locations
#point 1, 2
locations = ['Zagreb', 'Bjelovar', 'Varazdin', 'Ogulin', 'Dubrovnik']
print(locations)

#use sorted() to print in alphabetical order
#point 3
print('\nthis is the sorted list')
print(sorted(locations))

#list still in original order
#point 4
print('\nthis is original list')
print(locations)

#use sorted() to print in reverse alphabetical order
#point 5
print('\nthis is reversed list')
print(sorted(locations,reverse=True))

#original list order:
#point 6
print('\nthis is original list')
print(locations)

#use reverse() method to change order
#point 7
print('\nthis is reversed list')
locations.reverse()
print(locations)

#reverse again, back to original order
#point 8
locations.reverse()
print('\nreverse back to original order')
print(locations)

#use sort() to store in alphabetical order
#point 9
locations.sort()
print('\nalphabetical order with sort() function')
print(locations)

#use sort() on list to store it in reversed alphabetical order
#point 10
locations.sort(reverse=True)
print('\nreversed alphabetical order')
print(locations)


#tags: list, sorted(), sort(), reverse()