# importing 're' module for using regexp below
import re

# creating variable with our text
s = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix “iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# creating a new list for appending separate paragraphs
a = []

# loop for adding separate paragraphs (splitlines() method)
for elem in s.splitlines():
    # don't need to add whitespaces to our list
    if elem not in ('', ' '):
        # delete all spaces before and after line (strip() method)
        # and make all lines to lower case
        new_elem = elem.strip().lower()
        # split elements in line through '.' to separate by sentences
        split_elem = new_elem.split('.')
        # appending our elements in list 'a'
        a.append(split_elem)

# print(a)

# new string for adding last words from all sentences
last_words = ''

# loop for searching last words
for i in range(1, len(a)):
    # looking for in all sentences
    for j in range(len(a[i])):
        # don't need elements like ''
        if a[i][j] != '':
            # split sentences by separate words
            elem = a[i][j].split(' ')
            # finding last word
            last_words += str(elem[-1]) + ' '

# creating new sentence with these words
# also delete all spaces before and after (strip() method)
# and make the first character to upper case (capitalize() method)
add_sentence = last_words.strip().capitalize()

# insert new sentence after second paragraph
a[2].insert(-1, add_sentence)

# print(a)

# variable for a new string with needed changes
new_s = ''

# loop for adding text to the new string
for i in range(len(a)):
    # if we have more than one sentence in the paragraph we need to "capitalize()" it and divide with '.'
    if len(a[i]) > 1:
        # take a look all elements (paragraphs)
        for j in range(len(a[i])):
            # if element not a whitespace we need to 'capitalize()' it and divide with '.'
            if a[i][j] != '':
                new_s += a[i][j].strip().capitalize() + '. '
            # if it's only whitespace just add a line break
            else:
                new_s += '\n'
    # for one sentence we just add this sentence and line break after
    else:
        new_s += a[i][0].capitalize() + '\n'

# print(new_s)

# use regexp for finding all 'iz'-mistakes
mistake = re.search(r' iz ', new_s)

# replacing incorrect 'iz' on 'is'
result_string = new_s.replace(mistake.group(), ' is ')
# printing new homework text
print(result_string)

# spaces counting
# new variable for counter
space_count = 0

# loop for count all spaces and whitespaces
for elem in s:
    # used isspace() method to find all needed spaces
    if elem.isspace():
        # increase counter on one
        space_count += 1

# printing results
result_spaces = 'There are ' + str(space_count) + ' whitespaces!'
print(result_spaces)
