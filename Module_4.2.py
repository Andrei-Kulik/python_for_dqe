# importing 'randint' method for creating new list with random numbers
from random import randint


# generation list function with 3 start params
def list_gen(keys, values):
    n_list = []
    # loop for generating list with dicts
    for j in range(randint(2, 10)):
        # declaration new empty dict
        d = dict()
        # loop for generating dict with random keys and values
        for i in range(randint(0, 100)):
            # generating keys (should be letter)
            key = letters[randint(0, len(keys) - 1)]
            # generating values (should be number form 0 to 100)
            value = randint(0, values)
            # adding pair key-value to our dict
            d[key] = value
        # appending dict to our main_list
        n_list.append(d)
    # return generated list
    return n_list


# generation intermediate dict function
def inter_dict_gen(list_name):
    dict_name = dict()
    # loop for creating intermediate dict
    # keys in this new dict will be keys from dict in our main_list
    # values in this list will be list of values and also list of numbers (dict position in main_list)
    for i in range(len(list_name)):
        # loop for adding key-value to intermediate list
        for key, value in list_name[i].items():
            # for new keys we add pair key-value (value is list)
            if key not in dict_name.keys():
                dict_name[key] = [[value], [i + 1]]
            # if key also in new_dict we also append new value for this key and number (dict position in main_list)
            else:
                # appending new values
                dict_name[key][0].append(value)
                # appending dict positions in main_list
                dict_name[key][1].append(i + 1)
    return dict_name


# generation final common dict function
def cmn_dict_gen(intermediate_dict):
    cmn_dict = dict()
    # loop for adding key-value in common dict
    for key, value in intermediate_dict.items():
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
    return cmn_dict


# declaration parameters (list, keys, values)
letters, n = 'abcdefghijklmnopqrstuvwxyz', 100
# call function 'list_gen' with all start parameters and print new generated list
main_list = list_gen(letters, n)
print(main_list)
# call function 'inter_dict_gen' with new list
inter_dict = inter_dict_gen(main_list)
# print(inter_dict)
# call function 'cmn_dict_gen' with inter_dict as a parameter
common_dict = cmn_dict_gen(inter_dict)
print(common_dict)
