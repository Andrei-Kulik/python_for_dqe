import datetime
import sys
import classes


def manual_processing():
    print("Select the type of new publication (news, advert, vacancy) or type 'exit' to exit form the program:")
    publication_type = input().lower().strip()
    if publication_type == "exit":
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


manual_processing()
