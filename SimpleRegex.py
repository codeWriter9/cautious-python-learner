'''
Created on 09-Jun-2019

@author: Sanjay Ghosh
'''
import re;
for x in range(0, int(input())):
    try :
        p = re.compile(input());
        print(True);
    except Exception:
        print(False);
