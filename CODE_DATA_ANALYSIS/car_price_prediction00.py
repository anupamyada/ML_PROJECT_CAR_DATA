import numpy as np
import pandas as pd
car=pd.read_csv("quikr_car.csv")
print(car.head())
print(car.shape)
print(car.info())

print(car["year"].unique())


##Note: 1. year has many non year value
##2. year Is in object , i need to convert it into integer

print(car["Price"].unique())


##Note: 1. one mistake ask for price ,need to remove that
##2. object data need to convert into integer,& remove comma

print(car["kms_driven"].unique())

## note: 1. need to convert object into integer
## 2. need to remove int from kms
## 3. need to remove nan and comma

print(car["fuel_type"].unique())

## 1. need to remove nan

## 1. keep 1st 3 words of name

