import datetime
import json
# import os
import re
import sys

import capitalize
import classes
import csv_creating


def main():
    print("Select the format of adding data (manual, txt, json) or type 'exit' to exit form the program:")
    format = input().lower().strip()
    if format == "exit":
        sys.exit()
    elif format in ("manual", "txt", "json", "xml"):
        processing(format)
        add_csv()
    else:
        print("Incorrect format!")
        main()


def processing(format):
    if format == "manual":
        manual_processing()
    elif format == "txt":
        txt_processing()
        print(".txt file processed successfully!")
    elif format == "json":
        json_processing()
        print(".json file processed successfully!")


def manual_processing():
    print("Select the type of new publication (news, advert, vacancy) or type 'exit' to exit form the program:")
    publication_type = input().lower().strip()
    if publication_type == "exit":
        add_csv()
        sys.exit()
    elif publication_type in ("news", "advert", "vacancy"):
        manual_publication(publication_type)
        manual_processing()
    else:
        print("Incorrect publication type!")
        manual_processing()


def manual_publication(publication_type):
    if publication_type == "news":
        print("Type the news:")
        content = input()
        print("Enter the city:")
        city = input()
        news = classes.News(publication_type, content, city)
        news.publish()
        print("News added successfully!")
    elif publication_type == "advert":
        print("Type the text of your advert:")
        content = input()
        print("Enter the expiration date (yyyy-mm-dd):")
        ex_date = datetime.datetime.strptime(input(), '%Y-%m-%d').date()
        ad = classes.Advert(publication_type, content, ex_date)
        ad.publish()
        print("Advertise added successfully!")
    elif publication_type == "vacancy":
        print("Type the name of vacancy:")
        vacancy = input()
        print("Type the requirements:")
        requirements = input()
        print("Type vacancy period (days):")
        actual = int(input())
        vacancy = classes.Vacancy(publication_type, vacancy, requirements, actual)
        vacancy.publish()
        print("Vacancy added successfully!")


def txt_processing():
    print("Input filename (press 'Enter' to use '\\txt_input.txt'):")
    filename = input()
    if filename == "":
        filename = 'txt_input.txt'
    print(f"File name is {filename}")

    with open(filename, 'r') as input_file:
        initial_list = re.split("/", input_file.read().replace("\n", ""))
        # print(initial_list)

    list_of_publications = []
    for elem in initial_list:
        list_elem = elem.split(";")
        d = dict()
        for element in list_elem:
            key, value = element.split(": ")
            d[key.strip()] = value.strip()
        list_of_publications.append(d)
    # print(list_of_publications)

    file_parsing(list_of_publications)

    # os.remove(filename)


def json_processing():
    print("Input filename (press 'Enter' to use '\\json_input.json'):")
    filename = input().strip()
    if filename == "":
        filename = 'json_input.json'
    print(f"File name is {filename}")

    list_of_publications = json.load((open(filename)))
    # print(list_of_publications)

    file_parsing(list_of_publications)

    # os.remove(filename)


def file_parsing(list_of_publications):
    for elem in list_of_publications:
        publication_type = elem["type"]
        if publication_type == "news":
            content = capitalize.capitalizing(elem["content"])
            city = elem["city"]
            news = classes.News(publication_type, content, city)
            news.publish()
        elif publication_type == "advert":
            content = capitalize.capitalizing(elem["content"])
            ex_date = datetime.datetime.strptime(elem["ex-date"], '%Y-%m-%d').date()
            ad = classes.Advert(publication_type, content, ex_date)
            ad.publish()
        elif publication_type == "vacancy":
            position = elem["position"]
            requirements = elem["requirements"]
            actual = int(elem["actual-days"])
            vacancy = classes.Vacancy(publication_type, position, requirements, actual)
            vacancy.publish()


def add_csv():
    now = datetime.datetime.now().strftime("%m%d%H%M%S")
    csv_creating.count_words('result_file.txt', f'words_count_{now}.csv')
    csv_creating.count_letters('result_file.txt', f'letters_count_{now}.csv')


main()
