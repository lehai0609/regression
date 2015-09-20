
__author__ = 'Le Quang Hai'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
#Load the LoanStats3d.csv
loansData = pd.read_csv('LoanStats3d.csv', header=1, index_col=0)
print(loansData.head())
print(loansData.dtypes)

#Use income (annual_inc) to model interest rates (int_rate)
loansData['Intrate'] = map(lambda x: float(x.rstrip("%")), loansData['int_rate'])
#Add home ownership (home_ownership) to the model

