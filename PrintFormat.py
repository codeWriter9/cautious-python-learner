'''
Created on 13-May-2019

@author: Sanjay Ghosh
'''
def print_formatted(number):
    width = len(str('{0:b}'.format(number)));
    for x in range(1, number + 1):        
        for base in 'doXb':
             print('{0:{width}{base}}'.format(x, base=base, width=width), end=' ');
        print();


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)