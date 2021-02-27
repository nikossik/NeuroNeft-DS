import eel
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

@eel.expose
def print_graphX_py(user_date_in, user_date_out):
    forecast = pd.read_csv(r'Your Path \main_forecast.csv')
    forecast['id'] = [i for i in range(len(forecast))]
    user_date_id_in = int(forecast.loc[forecast['Date'] == user_date_in]['id'])
    user_date_id_out = int(forecast.loc[forecast['Date'] == user_date_out]['id'])
    X = [str(i) for i in forecast['Date'][user_date_id_in:user_date_id_out]]
    print('X!')
    return X

@eel.expose
def print_graphy_py(user_date_in, user_date_out):
    forecast = pd.read_csv(r'Your Path \main_forecast.csv')
    forecast['id'] = [i for i in range(len(forecast))]
    user_date_id_in = int(forecast.loc[forecast['Date'] == user_date_in]['id'])
    user_date_id_out = int(forecast.loc[forecast['Date'] == user_date_out]['id'])
    y = list(forecast['Price'][user_date_id_in:user_date_id_out])
    print('y!')
    return y

@eel.expose
def price_x_py(user_date_in):
    forecast = pd.read_csv(r'Your Path \main_forecast.csv')
    forecast['id'] = [i for i in range(len(forecast))]
    price = float(forecast.loc[forecast['Date'] == user_date_in]['Price'])
    print('price!')
    return round(price, 2)

@eel.expose
def date_py(date):
    return str(date)

eel.init(r' Your Path \web')
eel.start('main.html', size=(1400, 800))