#Based on tutorials:
#Using Pandas and Python to explore your dataset
#https://realpython.com/pandas-python-explore-dataset/
# and for sorting:
#https://realpython.com/pandas-sort-python/#getting-started-with-pandas-sort-methods

#BEFORE RUNNING THIS MODULE: if you haven't already got a .csv file with data, run the get...Data.py to populate the dataset. HINT: you can change which module (python file) runs when the Run button is clicked by editing the .replit file

import pandas as pd  #convention is to use pd as alias for pandas 

# Read data from csv into a variable; the result is a Dataframe
#df = pd.read_csv("nba_all_elo.csv")  #NBA data

df = pd.read_csv("chicago_vac_by_zip.csv")  #Chicago vaccination data

print(type(df))  #display the type of the df variable - it is a DataFrame!
print(len(df))  #number of records in the dataset
print(df.shape)  #Dimensionality: rows and columns

#By default, only the first few and last few columns are displayed with ... in between; set max.columns to display all
pd.set_option("display.max.columns", None)  #show all columns
pd.set_option("display.precision", 2)  #decimal places

#head() and tail() functions get rows from the beginning and end of the dataset; they default
# to 5 rows but can take a parameter for number of rows wanted
print(df.head()) #the first 5 rows
#print(df.head(10)) #the first 10 rows
print(df.tail()) #the last 5 rows

print("Dataframe Describe")
print(df.describe()) #some basic statistics

print("Dataframe Describe: Include Objects")
print(df.describe(include=object)) #some basic statistics for objects

print("Dataframe Info:")
print(df.info()) #describes the columns

#sort the data: take a look at what column names are returned by the above info() function; choose 1 or 2 that would be interesting for sorting
#in this example the original dataset is sorted by Zip Code, then by Date
#Let's sort by Date first, then Zip Code
#Create a new variable, 'dfSorted' to receive the sorted data
dfSorted = df.sort_values(by=["Date", "Zip Code"])
print(dfSorted.head())

# Convert the dataframe to HTML and save to a file
# In the next step of this development we will create a Flask Web site and write to a template within the project.
html_table = df.to_html()
html_file = open("dataTable.html", "w")
html_file.write(html_table)
html_file.close()
print("Data table saved to dataTable.html")

# Take a look at the dataTable.html that is created




