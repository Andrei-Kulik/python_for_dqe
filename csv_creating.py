import re
import csv
import datetime


# COUNTING WORDS
def count_words(input, output):
    with open(input, 'r') as input_file:
        words = re.findall(r"[\w']+", input_file.read().lower())
        new_dict = dict()
        for elem in words:
            if not elem.isnumeric():
                if elem not in new_dict.keys():
                    new_dict[elem] = 1
                else:
                    new_dict[elem] += 1
        # print(new_dict)

    with open(output, 'w', newline='') as csv_words:
        writer = csv.writer(csv_words, delimiter="-")
        for key, value in new_dict.items():
            writer.writerow([key, value])


# COUNTING LETTERS
def count_letters(input, output):
    with open(input, 'r') as input_file:
        input_text = input_file.read()
        text = ''
        for char in input_text:
            if char.isalpha():
                text += char
        # print(text)

        all_dict = dict()
        upp_dict = dict()

        for char in text:
            if char.lower() not in all_dict.keys():
                all_dict[char.lower()] = 1
            else:
                all_dict[char.lower()] += 1

        for char in text:
            if char.isupper():
                if char.lower() not in upp_dict.keys():
                    upp_dict[char.lower()] = 1
                else:
                    upp_dict[char.lower()] += 1

        # print(all_dict)
        # print(upp_dict)

    with open(output, 'w', newline='') as csv_letters:
        headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
        writer = csv.DictWriter(csv_letters, fieldnames=headers)
        writer.writeheader()
        for key, value in all_dict.items():
            percentage = round(value / len(text) * 100, 2)
            if key in upp_dict.keys():
                writer.writerow({'letter': key,
                                 'count_all': value,
                                 'count_uppercase': upp_dict[key],
                                 'percentage': f'{percentage}%'})
            else:
                writer.writerow({'letter': key,
                                 'count_all': value,
                                 'count_uppercase': 0,
                                 'percentage': f'{percentage}%'})


# now = datetime.datetime.now().strftime("%m%d%H%M%S")
#
# count_words('module_6_result.txt', f'module_7_words_{now}.csv')
# count_letters('module_6_result.txt', f'module_7_letters_{now}.csv')
