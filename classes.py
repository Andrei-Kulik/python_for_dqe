import datetime
import pyodbc


class Publication:
    def __init__(self, publication_type):
        self.publication_type = publication_type


class News(Publication):
    def __init__(self, publication_type, content, city):
        Publication.__init__(self, publication_type=publication_type)
        self.content = content
        self.city = city

    def create(self):
        article = f"--- {self.publication_type.capitalize()} ---\n{self.content}\n{self.city.capitalize()}, {datetime.datetime.now().strftime('%d-%m-%Y %H:%M')}\n\n"
        return article

    def publish(self):
        news = open("result_file.txt", "a")
        news.write(self.create())

    def add_database(self):
        with pyodbc.connect("Driver=SQLite3 ODBC Driver;Database=publications.db", autocommit=True) as connection:
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS news (content text, city text, publish_date text);')
            insert_query = "INSERT INTO news VALUES (?, ?, ?);"
            values_tuple = (self.content, self.city.capitalize(), datetime.datetime.now().strftime('%d-%m-%Y %H:%M'))
            cursor.execute(insert_query, values_tuple)


class Advert(Publication):
    def __init__(self, publication_type, content, ex_date):
        Publication.__init__(self, publication_type=publication_type)
        self.content = content
        self.ex_date = ex_date

    def actual_period_calc(self):
        actual_period = (self.ex_date - datetime.datetime.now().date()).days
        return actual_period

    def create(self):
        body = f"--- {self.publication_type.capitalize()} ---\n{self.content}\nActual until: {self.ex_date}, {self.actual_period_calc()} days left\n\n"
        return body

    def publish(self):
        advert = open("result_file.txt", "a")
        advert.write(self.create())

    def add_database(self):
        with pyodbc.connect("Driver=SQLite3 ODBC Driver;Database=publications.db", autocommit=True) as connection:
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS adverts (content text, ex_date);')
            insert_query = "INSERT INTO adverts VALUES (?, ?);"
            values_tuple = (self.content, self.ex_date)
            cursor.execute(insert_query, values_tuple)


class Vacancy(Publication):
    def __init__(self, publication_type, vacancy, requirements, actual):
        Publication.__init__(self, publication_type=publication_type)
        self.vacancy = vacancy
        self.requirements = requirements
        self.actual = actual

    def calc_expire_date(self):
        ex_date = datetime.datetime.now() + datetime.timedelta(days=self.actual)
        return ex_date

    def create(self):
        body = f"--- {self.publication_type.capitalize()} ---\nPosition: {self.vacancy}\nRequirements: {self.requirements}\nValid until: {self.calc_expire_date().strftime('%d-%m-%Y')}\n\n"
        return body

    def publish(self):
        vacancy = open("result_file.txt", "a")
        vacancy.write(self.create())

    def add_database(self):
        with pyodbc.connect("Driver=SQLite3 ODBC Driver;Database=publications.db", autocommit=True) as connection:
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS vacancies (vacancy text, requirements text);')
            insert_query = "INSERT INTO vacancies VALUES (?, ?);"
            values_tuple = (self.vacancy, self.requirements)
            cursor.execute(insert_query, values_tuple)

