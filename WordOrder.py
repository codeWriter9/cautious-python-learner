'''
Created on 02-Jun-2019

@author: Sanjay Ghosh
'''
_dict = {};
for count in range(int(input())):
    str_ = input();
    if str_ in _dict:
        _dict[str_] = _dict[str_] + 1;
    else:
        _dict[str_] = 1;
print(len(_dict));
list = [];
for key in _dict.keys():
    list.append(str(_dict[key]));
print(" ".join(list));