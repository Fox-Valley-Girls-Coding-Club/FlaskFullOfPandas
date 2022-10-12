from flask import Flask, render_template
import random
import pandas as pd 

app = Flask(__name__, static_folder='static', template_folder='templates')

# Read data from csv into a variable; the result is a Dataframe
# NOTE: To update or create the csv first run the get...Data.py file, changing the download_url and target_csv_path variables based on the type of data you are getting

df = pd.read_csv("chicago_vac_by_zip.csv")  #Chicago vaccination data
#df = pd.read_csv("nba_all_elo.csv")  
dfSample = df.head(100)

# Flask uses the Route Decorator @app.route to define what URL triggers the function that is defined just below it. Our first route is the root of our site, indicated by '/'. When the Flask app starts, it opens the root URL https://FlaskFullOfPandas.dottiefvgcc.repl.co; a user could also enter that address in their Browser. Either way, the homepage() function will be triggered
@app.route('/')
def homepage():
    """Displays the homepage."""
    return render_template('index.html', tables=[dfSample.to_html(classes='data table table-striped table-hover')], titles= dfSample.columns.values )  

#https://flaskfullofpandas.dottiefvgcc.repl.co/about
# This simple example does not use an HTML template
@app.route('/about')
def about():
    return "It's all about Flask"


#Flask assigns the name "__main__" to this script when it is executed
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=random.randint(2000, 9000))
