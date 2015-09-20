__author__ = 'Le Quang Hai'
#import numpy, statsmodels, pandas
import numpy as np
import statsmodels.api as sm
import pandas as pd
#read loansData.csv
loansData = pd.read_csv('loansData.csv')
print(loansData)
#Create FICO Score column
loansData['FICO.Score'] = map(lambda x: float(x[0:3]), loansData['FICO.Range'])
print(loansData['FICO.Score'])
#Create Interest Rate column
loansData['Intrate'] = map(lambda x: float(x.rstrip("%")), loansData['Interest.Rate'])
print(loansData['Intrate'].head())
#Modelling
intrate = loansData['Intrate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1, x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print(f.summary())
