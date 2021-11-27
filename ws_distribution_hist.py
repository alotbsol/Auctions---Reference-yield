""" analysis of wind projects already build in Germany"""

import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import seaborn as sns


DE_wind_data = pd.read_excel("DE_wind_data.xlsx", sheet_name="AllData")


class Analysis:
    def __init__(self, power_plant_file=DE_wind_data):
        self.wind_data = power_plant_file
        self.periods = {"Period1": [1979, 1990],
                                  "Period2": [1990, 1995], "Period3": [1995, 2000],
                                  "Period4": [2000, 2005], "Period5": [2005, 2010],
                                  "Period6": [2010, 2015], "Period7": [2015, 2019]}

    def create_histogram(self, name="hist"):
        colours_list = cm.get_cmap("viridis")
        ax = plt.axes()
        sns.histplot(data=self.wind_data, ax=ax, x="average wind speed", bins=20, kde=True,
                     weights="electrical_capacity", stat="probability", color=colours_list(0))

        ax.set_title(str(self.wind_data['year'].min()) + " - " + str(self.wind_data['year'].max()))

        text_props = dict(boxstyle='square', facecolor='white', edgecolor="none", alpha=0.9, pad=0.5)
        total_added_capacity = round(self.wind_data['electrical_capacity'].sum(), 1)
        years_period = self.wind_data['year'].max() - self.wind_data['year'].min()

        y = ax.get_ylim()
        x = ax.get_xlim()

        avg = self.wind_data["average wind speed"].mean()
        med = self.wind_data["average wind speed"].median()
        stand_dev = self.wind_data["average wind speed"].std()
        plt.text(x[0]*1.05, y[1]*0.95,
                 "Total added capacity: " + str(total_added_capacity) + " MW"
                 + "\n"
                 "Added capacity per year: " + str(round(total_added_capacity/years_period)) + " MW"
                 + "\n"
                   "Mean: " + str(round(avg, 1))
                 + "\n"
                   "Median: " + str(round(med, 1))
                 + "\n"
                   "Standard deviation: " + str(round(stand_dev, 1)),

                 fontsize=10, verticalalignment='top', ha="left", bbox=text_props)

        plt.savefig(name)
        plt.clf()
        plt.close()

    def create_histogram_yearly(self, name="hist"):

        for i in self.periods:
            colours_list = cm.get_cmap("viridis")

            yearly_df = self.wind_data.loc[(self.wind_data.year >= self.periods[i][0]) &
                                           (self.wind_data.year < self.periods[i][1])]

            ax = plt.axes()
            sns.histplot(ax=ax, data=yearly_df, x="average wind speed", bins=20, kde=True,
                         weights="electrical_capacity", stat="probability", color=colours_list(0))

            ax.set_title(str(i) + ": " + str(self.periods[i][0]) + " - "
                         + str(self.periods[i][1] - 1))

            text_props = dict(boxstyle='square', facecolor='white', edgecolor="none", alpha=0.9, pad=0.5)
            total_added_capacity = round(yearly_df['electrical_capacity'].sum())
            years_period = self.periods[i][1] - self.periods[i][0]

            y = ax.get_ylim()
            x = ax.get_xlim()

            avg = yearly_df["average wind speed"].mean()
            med = yearly_df["average wind speed"].median()
            stand_dev = yearly_df["average wind speed"].std()

            plt.text(x[0] * 1.05, y[1] * 0.95,
                     "Total added capacity: " + str(total_added_capacity) + " MW"
                     + "\n"
                       "Added capacity per year: " + str(round(total_added_capacity / years_period)) + " MW"
                     + "\n"
                       "Mean: " + str(round(avg, 1))
                     + "\n"
                       "Median: " + str(round(med, 1))
                     + "\n"
                       "Standard deviation: " + str(round(stand_dev, 1)),

                     fontsize=10, verticalalignment='top', ha="left", bbox=text_props)

            plt.savefig(name + "years" + str(i))
            plt.clf()
            plt.close()


if __name__ == '__main__':
    Data = Analysis()

    # Full period
    Data.create_histogram()

    # Per periods
    Data.create_histogram_yearly()
