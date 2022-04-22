import pandas as pd
from database_functions import DataBase_Management

if __name__ == '__main__':
    places = pd.read_csv(r'data/lieux.csv').drop_duplicates()
    people = pd.read_csv(r'data/people.csv').drop_duplicates()

    # create an object that associates the department and the region to data with a 'commune'
    DB_Func = DataBase_Management(places)
    # create a database with information about people, and associate to each person region and department
    DB_Func.add_to_databases(people)
    # output counting of people for each department
    DB_Func.return_json_counting('departement')
    # output counting of people for each region
    DB_Func.return_json_counting('region')