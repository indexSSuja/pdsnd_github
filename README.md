# Programming for Data Science Using Python-Course Project
## Beginner Data Exploration Data Science Data Visualization Libraries


I recently finished Programming for Data Science using Python. This blog is about the project I worked as part of the course. I am going to present my approach and some hints and tips that I used to complete this project. This is just an introductory course for aspiring individuals to make their journey towards Data Scientist, Machine Learning Engineer, Data Analyst, Artificial Intelligence, etc easier.

Note: This course is 100% project based.. Please do check out the complete course details  at Udacity.



### Data Science Process
## Overview
In this project, you will make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. You will write code to import the data and answer interesting questions about it by computing descriptive statistics. You will also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.
Project coursework provided three files
	• chicago.csv
	• new_york_city.csv
	• washington.csv


## What Software Do I Need?
To complete this project, the following software requirements apply:
• You should have Python 3, NumPy, and pandas
• Pycharm


# 1 Popular times of travel (i.e., occurs most often in the start time)
	• most common month
	• most common day of week
	• most common hour of day
# 2 Popular stations and trip
	• most common start station
	• most common end station
	• most common trip from start to end (i.e., most frequent combination of start station and end station)
# 3 Trip duration
	• total travel time
	• average travel time
# 4 User info
	• counts of each user type
	• counts of each gender (only available for NYC and Chicago)
	• earliest, most recent, most common year of birth (only available for NYC and Chicago)



Project mainly consist of the following functions

	1. Test_berkshir3 - This is the main function of our code that invokes the related function
	2. Load_data-We have to filter data based on user input and that is accomplished as part of this function
	3. Calculate most common month, day,- hour of the week
	4. Display data based on user input
	5. Calculate Trip Duration
	6. Calculate User Info 


For any data related task, the biggest challenge is the data source. For this project we were provided with a valid data source so the job was half done . The course also provided a templated code that we could follow to complete the course work but I felt strongly to not to look at the template and wanted to approach it independently. 

I was also urged to report the output differently and there were some hints to make the project even more interesting by creating html report, matlib. I wanted to present the output in an html format. Not to say that report is self-intuitive making it easier for anyone reading to understand.


There are lot of prebuild packages within pandas for exploratory data analysis like pandas data profiling which would give lot more data points than what was requested in the course work. One might argue that if there is pre built package exists then why to code for individual questions.

If you need to build visualization to showcase the output of your data analysis then you can use many of the libraries like pandas data profiling -Pandas data profiling will help us to understand the data structure even more better when you need to understand the data quickly.


### Conclusion:
In this article, you got an overview of the course work that I took for python programming and data science. We explored different reporting packages like pandas profiling, pandas, numpy for in depth data analysis. If you are a beginner like me then this is a great course work.

Thanks for reading, hope to see you in my next post. 
