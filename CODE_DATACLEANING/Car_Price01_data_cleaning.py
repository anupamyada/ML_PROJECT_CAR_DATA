import pandas as pd
car = pd.read_csv("quikr_car.csv")
backup = car.copy()
car = car[car["year"].str.isnumeric()]
print(car)
car["year"] = car["year"].astype(int)
car.info()
print(car["Price"])
car = [car["Price"] != "Ask For Price"]
print(car)
car["Price"]=car["Price"].astype(int)
#car["Price"]=car["Price"].str.replace[',',''].astype(int)
## error
##car["kms_driven"]=car["kms_driven"].str.split(' ').str.get(0).str.replace(',','')
##car = car[car["kms_driven"].str.isnumeric()]
##car["kms_driven"]=car["kms_driven"].astype(int)
##car.info()
##car=car[~car["fuel_type"].isna()]
##car["name"]=car["name"].str.split(' ').str.slice(0,3).str.join(' ')
##car = car.reset_index(drop=True)
#### it correct the index position
##car.info()
##car.describe()
####Note: it returns mean , median, mode etc.
##car[car["Price"]>6e6]
####Note: one data which is outlier bcoz buying price less than reselling
##
##car=car[car["Price"]<6e6].reset_index(drop=True)
######****************storing Cleaned data to csv file***************
##car.to_csv("Cleaned Car.csv")
