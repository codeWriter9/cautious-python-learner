'''
Created on 27-May-2019

@author: Sanjay Ghosh
'''
from datetime import date, time, datetime, timedelta;
def time_delta(t1, t2):            
    dt1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z");
    dt2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z");    
    return str(int(abs(dt1 - dt2).total_seconds()));

if __name__ == '__main__':
    #print(time_delta("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 +0000"));
    for _ in range(int(input())) :
        print(time_delta(input(), input()));