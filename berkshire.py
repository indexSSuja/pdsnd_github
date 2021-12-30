from typing import Union
import pandas as pd
import glob
from datetime import datetime
import numpy as np
from pandas import DataFrame, Series
from typing import Union
import pandas as pd
import calendar
import time
import pandas as pd
import numpy as np
import glob
from datetime import datetime
import re
import sys
import pandas_profiling

path = r'/home/workspace'


class berkshire():
    def load_data(self):
        all_files = glob.glob(path + "/*.csv")
        li = []

        for filename in all_files:
            df = pd.read_csv(filename, index_col=None, header=0)
            if "chicago" in filename:
                df['city'] = "chicago"
            if "washington" in filename:
                df["city"] = "washington"
            if "new_york_city" in filename:
                df["city"] = "new york"
            li.append(df)
        frame: Union[DataFrame, Series] = pd.concat(li, axis=0)
        return frame

    def calc_mostcommon_city_time_day(self, cityname, monthname, weekday, frame):
        frame["Start Time"] = pd.to_datetime(frame[
                                                 "Start Time"])  # I want to work with the dates in the column datetime as datetime objects instead of plain text
        frame['month'] = frame["Start Time"].dt.month
        frame['month'] = frame["Start Time"].dt.month_name()
        frame['Year'] = frame["Start Time"].dt.year
        frame['Day'] = frame["Start Time"].dt.day_name()
        frame['Hour'] = frame["Start Time"].dt.hour
        # change to lowercase
        frame['city'] = frame['city'].astype(str)
        frame['Day'] = frame['Day'].astype(str)
        frame['month'] = frame['month'].astype(str)
        frame['city'] = frame['city'].str.lower()
        frame['Day'] = frame['Day'].str.lower()
        frame['month'] = frame['month'].str.lower()
        frame2 = frame.query('(city== @cityname)')  # Apply filter based on input
        print('The length of dataframe is', len(frame2))
        if weekday != 'all':
            frame2 = frame2.query('(Day==@weekday)')  # skip this filter is input is all
        if monthname != 'all':
            frame2 = frame2.query('(month==@monthname)')  # skip this filter if input is all
        # print(len(frame))
        print('The length of dataframe is', len(frame2))
        most_common_month = frame2['month'].mode()
        most_common_day = frame2['Day'].mode()
        most_common_hour = frame2['Hour'].mode()
        print("The most common month is:\n", most_common_month, "\n", "The most common day is\n", most_common_day, "\n",
              "The most common hour is \n", most_common_hour, "\n")
        report = ProfileReport(frame2)
        report.to_file('test')
        return frame2

    def most_common_stations_trip(self, frame2):
        most_common_start_station = frame2['Start Station'].mode()
        most_common_end_station = frame2['End Station'].mode()
        print(most_common_start_station, "\n", most_common_end_station, "\n")
        count_series = frame2.groupby(['Start Station', 'End Station']).size()
        new_df = count_series.to_frame(name='size').reset_index()
        print(new_df.loc[new_df['size'].idxmax()])
        print(new_df.query('(size ==8)'))

    def display_data(self, frame2):
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        start_loc = 0
        while (view_data == 'yes'):
            print(frame2.iloc[start_loc:start_loc + 5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()

    def total_avg_travel_time(self, frame2):
        total = frame2['Trip Duration'].sum()
        avg = frame2['Trip Duration'].mean()

        print("Total Trip Duration is", "\n", total)
        print("Average Trip Duration is", "\n", avg),

    def user_gender_birthyear(self, frame2):
        print("Count of each user type is : ", frame2.groupby('User Type').size())
        print(frame2.groupby('Gender'))
        print("Count of each gender type is :", frame2.groupby('Gender').size())
        minbirthyear = frame2['Birth Year'].min()
        maxbirthyear = frame2['Birth Year'].max()
        mostcommonyear = frame2['Birth Year'].mode()
        print("Minimum Birth Year is", "\n", minbirthyear)
        print("Maximum Birth Year is", "\n", maxbirthyear)
        print("Most Common Birth Year", "\n", mostcommonyear)


def test_berkshire2():
    validcityname = ['chicago', 'washington', 'new york']
    while True:
        cityname = input("Please enter the name of the city :")
        cityname = cityname.lower()
        if cityname in validcityname:
            break
        else:
            print("Please enter the name of the city in strings")

    while True:
        monthname = input("Please enter the name of the month")
        if monthname.isalpha():
            monthname = monthname.lower()
            break
        else:
            print("Please enter the name of the month in strings")

    while True:
        weekday = input("Please enter the name of the weekday")
        if weekday.isalpha():
            weekday = weekday.lower()
            break
        else:
            print("Please enter the name of the weekday in strings")
    print(cityname, monthname, weekday)

    run = berkshire()
    frame = run.load_data()
    frame2 = run.calc_mostcommon_city_time_day(cityname, monthname, weekday, frame)
    if len(frame2) == 0:
        sys.exit('data set length is not long enough')
    run.display_data(frame2)
    run.most_common_stations_trip(frame2)
    run.total_avg_travel_time(frame2)
    if cityname in ('chicago', 'new york'):
        run.user_gender_birthyear(frame2)


if __name__ == "__main__":
    test_berkshire2()