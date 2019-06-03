'''
Created on 01-Jun-2019

@author: Sanjay Ghosh
'''
def capitalize_(str_, index):    
    return str_[0:index] + str_[index].upper() + str_[index + 1:];

def removeSmall(str_):        
    return list(set(str_) - set('abcdefghijklmnopqrstuvwxyz'));  

if __name__ == '__main__':
    print(removeSmall(input()));