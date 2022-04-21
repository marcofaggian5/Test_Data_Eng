
class DataBase_Management:

    def __init__(self, df1, df2):
        self.df1 = df1
        self.df2 = df2
        self.df = {}
        return

    def join_databases(self, keys):
        df = self.df2.merge(self.df1, on='commune', how=keys)
        return df