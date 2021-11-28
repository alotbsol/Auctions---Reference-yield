import pandas as pd


class Storage:
    def __init__(self, name="Project"):
        self.name = name
        self.df_results = pd.DataFrame()

    def data_in(self, data_in):
        print("data in")
        self.df_results = self.df_results.append(data_in)

    def data_export(self):
        writer = pd.ExcelWriter("{0}.xlsx".format(str(self.name)), engine="xlsxwriter")
        self.df_results.to_excel(writer, sheet_name="Results")
        writer.save()
