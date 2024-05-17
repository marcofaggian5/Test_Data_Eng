import pandas as pd
import json


class DataBase_Management:

    def __init__(self, places):
        self.places = places
        self.df = pd.DataFrame()
        self.results = {}
        self.keys = ['commune']
        # deal with duplicates in 'commune', it groups them up in the same row
        self.check_places()
        return

    # As there are some communes that are duplicate such as Saint-Denis. In this case, as we cannot deduce from the
    # provided data in which Saint-Denis the people live, we join the departments of Saint-Denis into La
    # Réunion/Seine-Saint-Denis and the regions into La Réunion/Île-de-France
    def check_places(self):
        places1 = self.places.groupby(['commune'])['departement'].apply('/'.join).reset_index()
        places2 = self.places.groupby(['commune'])['region'].apply('/'.join).reset_index()
        self.places = places1.merge(places2, on=self.keys, how='inner').drop_duplicates()

    def add_to_databases(self, df):
        # add places info to people
        df = df.merge(self.places, on=self.keys, how='inner').drop_duplicates()
        # update database with new rows
        self.df = self.df.append(df).drop_duplicates()
        # save new database as excel
        self.df.to_excel("output.xlsx")

    def count_freq_column(self, column):
        return self.df.groupby([column]).count()

    def return_json_counting(self, column):
        json_out = self.count_freq_column(column)
        json_out = json_out[['prenom']]
        with open("res_" + column + ".json", "w") as outfile:
            json.dump(json_out['prenom'].to_dict(), outfile)


