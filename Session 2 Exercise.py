# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:38:12 2020

@author: student
"""

import pandas as pd
import os
import matplotlib.pyplot as plt

data_import = os.path.join('C:/Users/student/Desktop/Secret Squirrel/examples','Session_2_pandas_data.csv')
data_set = pd.read_csv(data_import)

votes=list(data_set['Putin Vladimir Vladimirovich'])

i1=0
i2=0
i3=0
i4=0
i5=0
i6=0
i7=0
i8=0
i9=0

for num in votes:
    num_str=str(num)
    if num_str[0]=='1':
        i1+=1
    if num_str[0]=='2':
        i2+=1
    if num_str[0]=='3':
        i3+=1
    if num_str[0]=='4':
        i4+=1
    if num_str[0]=='5':
        i5+=1
    if num_str[0]=='6':
        i6+=1
    if num_str[0]=='7':
        i7+=1
    if num_str[0]=='8':
        i8+=1
    if num_str[0]=='9':
        i9+=1
        
Putin_ivotes = [i1,i2,i3,i4,i5,i6,i7,i8,i9]

ivote_fractions=[]
for i in Putin_ivotes:
    ivote_fractions.append(i / sum(Putin_ivotes))

x_votes = [1,2,3,4,5,6,7,8,9]

fig, ax = plt.subplots()
ax.plot(x_votes,ivote_fractions,label="Putin First Digit")

Benford_Lead = [.301,.176,.125,.097,.079,.067,.058,.051,.046]
ax.plot(x_votes,Benford_Lead,label="Benford First Digit")

f0=0
f1=0
f2=0
f3=0
f4=0
f5=0
f6=0
f7=0
f8=0
f9=0

for num in votes:
    num_str=str(num)
    if num_str[1]=='0':
        f0+=1
    if num_str[1]=='1':
        f1+=1
    if num_str[1]=='2':
        f2+=1
    if num_str[1]=='3':
        f3+=1
    if num_str[1]=='4':
        f4+=1
    if num_str[1]=='5':
        f5+=1
    if num_str[1]=='6':
        f6+=1
    if num_str[1]=='7':
        f7+=1
    if num_str[1]=='8':
        f8+=1
    if num_str[1]=='9':
        f9+=1
        
Putin_fvotes = [f0,f1,f2,f3,f4,f5,f6,f7,f8,f9]

fvote_fractions=[]
for i in Putin_fvotes:
    fvote_fractions.append(i / sum(Putin_fvotes))


y_votes = [0,1,2,3,4,5,6,7,8,9]
ax.plot(y_votes,fvote_fractions,label="Putin Second Digit")

Benford_Second = [.12,.114,.109,.104,.10,.097,.093,.09,.088,.085]

ax.plot(y_votes,Benford_Second,label="Benford Second Digit")

ax.legend()
plt.show()