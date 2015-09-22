__author__ = 'Le Quang Hai'
import pandas as pd
import math
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],'B' : ['one', 'one', 'two', 'three','two', 'two', 'one', 'three']})
grouped = df.groupby('A')
print(grouped.)