import flask 
from flask import jsonify , request
import pandas as pd 
import numpy as np 

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False # avoid Chinese characters to show in ASCII

# test data
tpe = {
    "id": 0,
    "city_name": "Taipei",
    "country_name": "Taiwan",
    "is_capital": True,
    "location": {
        "longitude": 121.569649,
        "latitude": 25.036786
    }
}
nyc = {
    "id": 1,
    "city_name": "New York",
    "country_name": "United States",
    "is_capital": False,
    "location": {
        "longitude": -74.004364,
        "latitude": 40.710405
    }
}
ldn = {
    "id": 2,
    "city_name": "London",
    "country_name": "United Kingdom",
    "is_capital": True,
    "location": {
        "longitude": -0.114089,
        "latitude": 51.507497
    }
}

cities = [tpe, nyc, ldn]



# Trying to read the CSV Data 
gapminder = pd.read_csv("gapminder.csv")
gapminder_list = []
nrows = gapminder.shape[0] # getting the data rows

for i in range(nrows):
    ser = gapminder.loc[i,:] #List of labels. Note using [[]] returns a DataFrame.
    row_dict = {}
    for idx, val in zip(ser.index, ser.values):
        # the data type extract from csv is inconsisten with python int and float
        #整數資料型態並不是 Python 的 int 而是 NumPy 中的 numpy.int64；同理浮點數資料型態也不是 float 而是 numpy.float64      
        if type(val) is str:
            row_dict[idx] = val
        elif type(val) is np.int64:
            row_dict[idx] = int(val)
        elif type(val) is np.float64:
            row_dict[idx] = float(val)
    gapminder_list.append(row_dict)
    






@app.route('/' , methods = ['GET'])
def home():
    return "<h1>Hello Flask!</h1>"

@app.route('/cities/all', methods=['GET'])
def cities_all():
    return jsonify(cities)

@app.route('/gapminder/all', methods=['GET'])
def gapminder_all():
    return jsonify(gapminder_list)

# add request module to ensure User can request the data in specific country 
@app.route('/gapminder/', methods=['GET'])
def country():
    if 'country' in request.args:
        country = request.args['country']
    else:
        return "Error: No country provided . Please specify a country."
    results = []
    
    for elem in gapminder_list:
        if elem['country'] == country:
            results.append(elem)
    
    return jsonify(results)
      

app.run()