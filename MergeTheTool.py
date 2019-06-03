'''
Created on 26-May-2019

@author: Sanjay Ghosh
'''
def remove_duplicate(s):
    dict = {};
    for x in s:
        if x in dict:
            dict[x] = dict[x] + 1;
        else:
            dict[x] = 1;
    rStr = '';
    for x in s:
        if dict[x] > 1 and rStr.find(x) != -1:
            continue;
        else :
            rStr = rStr + x;           
    return rStr;

def merge_the_tools(string, k):
    arr = [];
    for x in range(0, len(string), k):
        arr.append(string[x:x+k]);
    for s in arr:
        print(remove_duplicate(s));        
    return;
    
if __name__ == '__main__':
    string, k = input(), int(input());
    merge_the_tools(string, k);