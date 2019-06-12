'''
Created on 03-Jun-2019

@author: Sanjay Ghosh
'''
_dict_ = {};

def check(key):
    return _dict_[key];

def func(s):    
    for ch in s:        
        if ch not in _dict_:
             _dict_[ch] = 1;
        else:
            _dict_[ch] = _dict_[ch] + 1;    
    list = [];
    count = 0;    
    for mykey in sorted(sorted(_dict_.keys()), key=check, reverse=True):
        print(mykey + " " + str(_dict_[mykey]));
        count = count + 1;
        if count == 3:
            break;     
    return;

if __name__ == '__main__':
    func(input());