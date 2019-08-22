'''
Created on 16-Aug-2019

@author: Sanjay Ghosh
'''
from _collections import OrderedDict;
mydict = OrderedDict();
T = int(input());
for loop in range(T):
    myarr = input().split();
    key = " ".join(myarr[0:len(myarr)-1]);
    value = int(" ".join(myarr[len(myarr)-1:]));
    if key not in mydict:
        mydict[key] = value;
    else :
        mydict[key] = mydict[key] + value;
for key in mydict.keys():
    print(key + " " + str(mydict[key]));