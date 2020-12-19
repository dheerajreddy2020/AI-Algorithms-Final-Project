import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import requests
import datetime
import pandas as pd


app = Flask(__name__)
model = pickle.load(open('randomforest.pkl', 'rb'))
def predict_output(input_dict,model):
    cat_dict = {'a':1,'b':2,'c':3,'d':4}
    predict_dict = {}
    date = datetime.datetime.strptime(input_dict['Date'], '%Y-%m-%d')
    if input_dict['State_holiday'] != 0 or date.weekday()==6:
        return 0
    else:
        predict_dict['Assortment']=[cat_dict[input_dict['Assortment']]]
        predict_dict['StoreType']=[cat_dict[input_dict['StoreType']]]
        predict_dict['DayofMonth'] = [date.day]
        predict_dict['Month'] = [date.month]
        predict_dict['DayOfWeek'] = [date.weekday()+1]
        predict_dict['SchoolHoliday'] = [input_dict['School_holiday']]
        predict_dict['Promo'] = [input_dict['Promo1']]
        predict_dict['hasPromo2'] = [input_dict['Promo2']]
        predict_dict['IsCompetitionOpen'] = input_dict['Competition_exists']
        predict_dict['CompetitionDistance']=[input_dict['CompetitionDistance']]*1000
        predict_dict['DayofYear'] = [(date - datetime.datetime(date.year, 1, 1)).days + 1]
        df = pd.DataFrame.from_dict(predict_dict)
        return model.predict(df).astype(int)[0]



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
	'''
	For rendering results on HTML GUI
	'''
	features = list(request.form.values())
	Input_dict = {'Date' : str(features[0]),
	'Assortment' : str(features[1]),
	'StoreType' : str(features[2]),
	'Promo1' : int(features[5]),
	'Promo2' : int(features[6]),
	'State_holiday' : int(features[4]),
	'School_holiday' : int(features[3]),
	'Competition_exists' : int(features[7]),
	'CompetitionDistance' : int(features[8])}
	output =  predict_output(Input_dict,model)
	return render_template('index.html', prediction_text='Predicted amount of sales are {}'.format(output))



if __name__ == "__main__":
    app.run(debug=True)