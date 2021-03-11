# importing 're' module for using regexp below
import re


# creating variable with our text
s = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix “iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


# divide text on paragraphs and add it to new list function
def paragraphs(new_string):
    new_lst = []
    # loop for adding separate paragraphs (splitlines() method)
    for elem in new_string.splitlines():
        # don't need to add whitespaces to our list
        if elem not in ('', ' '):
            # delete all spaces before and after line (strip() method)
            # and make all lines to lower case
            new_elem = elem.strip().lower()
            # split elements in line through '.' to separate by sentences
            split_elem = new_elem.split('.')
            # appending our elements in list 'a'
            new_lst.append(split_elem)
    return new_lst


# finding last words from the list of paragraphs(sentences) function
def last_words(list_of_paragraph):
    # new string for adding last words from all sentences
    last_words_string = ''
    # loop for searching last words
    for i in range(1, len(list_of_paragraph)):
        # looking for in all sentences
        for j in range(len(list_of_paragraph[i])):
            # don't need elements like ''
            if list_of_paragraph[i][j] != '':
                # split sentences by separate words
                elem = list_of_paragraph[i][j].split(' ')
                # finding last word
                last_words_string += str(elem[-1]) + ' '
    return last_words_string


# function of inserting new sentence in the list on needed position
def insert_new_sentence(sentence, list, position):
    #     # creating new sentence with these words
    #     # also delete all spaces before and after (strip() method)
    #     # and make the first character to upper case (capitalize() method)
    add_sentence = sentence.strip().capitalize()
    list[position].insert(-1, add_sentence)
    return list


# creating string from list of paragraphs function
def creating_string(list):
    # variable for a new string with needed changes
    new_string = ''
    # loop for adding text to the new string
    for i in range(len(list)):
        # if we have more than one sentence in the paragraph we need to "capitalize()" it and divide with '.'
        if len(list[i]) > 1:
            # take a look all elements (paragraphs)
            for j in range(len(list[i])):
                # if element not a whitespace we need to 'capitalize()' it and divide with '.'
                if list[i][j] != '':
                    new_string += list[i][j].strip().capitalize() + '. '
                # if it's only whitespace just add a line break
                else:
                    new_string += '\n'
        # for one sentence we just add this sentence and line break after
        else:
            new_string += list[i][0].capitalize() + '\n'
    return new_string


# syntax correct function (iz = is)
def syntax_correct(text):
    # use regexp for finding all 'iz'-mistakes
    mistake = re.search(r' iz ', new_str)
    # replacing incorrect 'iz' on 'is'
    result_string = new_str.replace(mistake.group(), ' is ')
    return result_string


n_list = paragraphs(s)
# print(n_list)

last_wrds = last_words(n_list)
# print(last_word)

new_list = insert_new_sentence(last_wrds, n_list, 2)
# print(new_list)

new_str = creating_string(new_list)
# print(new_str)

result_str = syntax_correct(new_str)
print(result_str)


# space count function
def space_count(text):
    # new variable for counter
    space_cnt = 0
    # loop for count all spaces and whitespaces
    for elem in text:
        # used isspace() method to find all needed spaces
        if elem.isspace():
            # increase counter on one
            space_cnt += 1
    return space_cnt


count_of_spaces = space_count(s)
print('There are ' + str(count_of_spaces) + ' whitespaces!')
