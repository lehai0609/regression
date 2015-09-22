__author__ = 'Le Quang Hai'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
#Load the LoanStats3d.csv
loansData = pd.read_csv('LoanStats3d.csv', skiprows=1, dtype={'id':int, 'desc':str}, skip_blank_lines=True, comment='T', index_col=0)
#Convert the Interest Rate
loansData['int_rate'] = map(lambda x: float(x.rstrip("%")), loansData['int_rate'])
print(loansData['int_rate'])
#Use annual_inc to model int_rate
annualIncome = loansData['annual_inc']
intrate = loansData['int_rate']

y = np.matrix(intrate).transpose()
x1 = np.matrix(annualIncome).transpose()

x = np.column_stack([x1])

X = sm.add_constant(x)
model = sm.OLS(y, X)
f = model.fit()

print(f.summary())
#Add home_ownership(mortgage, rent, own) to the model
ownershipStatus = []
for row in loansData['home_ownership']:
    if row == "MORTGAGE":
        ownershipStatus.append(1)
    elif row == "RENT":
        ownershipStatus.append(2)
    elif row == "OWN":
        ownershipStatus.append(3)
    else:
        ownershipStatus.append(4)
loansData['home_ownership'] = ownershipStatus
print(loansData['home_ownership'].head())

annualIncome = loansData['annual_inc']
intrate = loansData['int_rate']
ownership = loansData['home_ownership']

y = np.matrix(intrate).transpose()
x1 = np.matrix(annualIncome).transpose()
x2 = np.matrix(ownership).transpose()

x = np.column_stack([x1, x2])

X= sm.add_constant(x)
model = sm.OLS(y, X)
f = model.fit()

print(f.summary())

