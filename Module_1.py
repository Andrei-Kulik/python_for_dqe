# importing 'randint' method for creating new list with random numbers
from random import randint

# declaring size of list 'n'
n = 100
# declaring new empty list 'a'
a = []

# loop for creating our new list
for i in range(n):
    # 'append' method for adding new elements to list
    # 'randint' method for creating a random number from 0 to 1000
    a.append(randint(1, 1000))

# sorting algorithm (I used bubble sorting)
# index 'i' we will use for further reducing our scope of unsorted numbers
for i in range(len(a) - 1):
    # index 'j' we will use for list elements iterations
    # we need to find maximum form the list and put it at the end
    # after we decrease our range() on 'i', because we no longer need to compare sorted items at the end
    for j in range(len(a) - 1 - i):
        # comparing element with next element
        if a[j] > a[j + 1]:
            # replacing elements with each other
            a[j], a[j + 1] = a[j + 1], a[j]

# declaration variables for counting average values (sum / count = average)
even_sum, even_count = 0, 0
odd_sum, odd_count = 0, 0

# loop for counting sum and count for even and odd elements
for elem in a:
    # sum and count for even elements (even % 2 == 0)
    if elem % 2 == 0:
        # increasing the sum on element value
        even_sum += elem
        # increasing the count on one element
        even_count += 1
    # sum and count for odd elements
    else:
        # increasing the sum on element value
        odd_sum += elem
        # increasing the count on one element
        odd_count += 1

# printing final results
# added converting to the 'int' type to round float values (* optional)
# also added converting average values to the 'str' type for concatenating with the string
print('Even average: ', str(int(even_sum / even_count)))
print(' Odd average: ', str(int(odd_sum / odd_count)))
