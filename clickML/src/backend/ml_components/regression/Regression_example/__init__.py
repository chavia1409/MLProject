import pandas as pd
from sklearn.linear_model import  LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

CSV_1 = pd.read_csv(BostonData.csv)
CSV_2 = pd.read_csv(BostonTarget.csv)

X_train, X_test, y_train, y_test = train_test_split(CSV_1, CSV_2,
                                                    test_size=50, train_size= 50,
                                                    random_state= True, shuffle= True)

lg_1 = LinearRegression.fit(X_train, y_train)

pdt_1 = LinearRegression.predict(CSV_1, CSV_2)

print(pdt_1)


