# FlaskFullOfPandas - a Python Experience
## Examples using:
- [Python Requests Library] (https://docs.python-requests.org/en/latest/) to handle HTTP requests and responses
- [Pandas] (https://pandas.pydata.org/), a Python Data Analysis Library, to perform data operations including sorting and cleaning
- [Flask] (https://palletsprojects.com/p/flask/), a Web Framework for using Python as a backend Server 

This project has separate code files to demonstrate use of each library:

1.  **getChicagoVacByZipData.py** and other **get*DataName*data.py** files. Using Requests, get a dataset from an external source such as [Data.gov](data.gov) and write it to a CSV file. 

2. **main.py**: Use Pandas to read your CSV file into a DataFrame which is the main object used by Pandas to store and manipulate data; it is a set of rows and columns. There are some basic examples of how to display or manipulate the data

3. **server.py** : Creates an instance of a Flask Web server, populates a DataFrame from an existing csv file, and attaches a function to the Web site's root that will use the DataFrame variable to supply data to the **index.html** template.

4. **index.html**: Inside the *views* folder because our Flask instance in server.py is configured to look there. The Flask render_template method fills in data where there is code between the {%  %} symbols 

### How to configure the RUN button to run different Python files###
 The .replit file is referenced when the Run button is clicked. You can edit .replit to swap out which .py file will run.  



