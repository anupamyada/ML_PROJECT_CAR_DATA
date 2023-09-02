import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
pd.read_csv("Cleaned Car.csv")
x = car.drop(columns = "Price")
y = car["Price"]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline

ohe = OneHotEncoder()
ohe.fit(X[['name','company','fuel_type']])
column_trans =make_column_transformer((OneHotEncoder(),['name','company','fuel_type']),
                                      remainder = 'passthrough')
lr=LinearRegression()
pipe = make_pipeline(column_trans,lr)
pipe.fit(x_train)
