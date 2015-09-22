__author__ = 'Le Quang Hai'
import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
#Load the LoanStats3d.csv
df = pd.read_csv('LoanStats3d.csv', header=1, low_memory=False)

#Change format of the issue_d
df['issue_d_format'] = pd.to_datetime(df['issue_d'])
dfts = df.set_index(df['issue_d_format'])
year_month_summary = dfts.groupby(lambda x: x.year*100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']

#Plotting loan_count_summary
plt.plot(loan_count_summary)
plt.ylabel("No of Approved Loan")
plt.xlabel("Month")
plt.show()

#Plotting ACF and Partial ACF
fig = plt.figure()
fig = sm.graphics.tsa.plot_acf(loan_count_summary)
plt.show()

fig2 = plt.figure()
fig2 = sm.graphics.tsa.plot_pacf(loan_count_summary)
plt.show()