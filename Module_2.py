# importing 'randint' method for creating new list with random numbers
from random import randint

# declaration size of list
list_size = randint(2, 10)
# declaration string with all letters
letters = 'abcdefghijklmnopqrstuvwxyz'
# declaration top border for values in dicts
n = 100
# declaration new empty list
main_list = []

# loop for generating list with dicts
for j in range(list_size):
    # declaration new empty dict
    d = dict()
    # loop for generating dict with random keys and values
    for i in range(randint(0, 100)):
        # generating keys (should be letter)
        key = letters[randint(0, len(letters) - 1)]
        # generating values (should be number form 0 to 100)
        value = randint(0, n)
        # adding pair key-value to our dict
        d[key] = value
    # appending dict to our main_list
    main_list.append(d)

# printing main_list with dicts
print(main_list)

# declaration new empty dict
new_dict = dict()

# loop for creating intermediate dict
# keys in this new dict will be keys from dict in our main_list
# values in this list will be list of values and also list of numbers (dict position in main_list)
for i in range(len(main_list)):
    # loop for adding key-value to intermediate list
    for key, value in main_list[i].items():
        # for new keys we add pair key-value (value is list)
        if key not in new_dict.keys():
            new_dict[key] = [[value], [i + 1]]
        # if key also in new_dict we also append new value for this key and number (dict position in main_list)
        else:
            # appending new values
            new_dict[key][0].append(value)
            # appending dict positions in main_list
            new_dict[key][1].append(i + 1)

# printing new_dict
# print(new_dict)

# creating common dict
cmn_dict = dict()

# loop for adding key-value in common dict
for key, value in new_dict.items():
    # if we have more than one value for one key, we will add max value and change key name
    if len(value[0]) > 1:
        # changing key name
        key = key + '_' + str(value[1][value[0].index(max(value[0]))])
        # choosing maximum value
        value = max(value[0])
        # adding pair key-value to our common dict
        cmn_dict[key] = value
    # if we have only one value for key we create just key-value pair
    else:
        # adding pair key-value to our common dict
        cmn_dict[key] = value[0][0]

# printing our common dict
print(cmn_dict)
