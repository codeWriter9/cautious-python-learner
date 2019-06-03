'''
Created on 21-May-2019

@author: Sanjay Ghosh
'''

def minion_game(s):    
    vowels = 'AEIOU';
    kcount = 0;
    scount = 0;
    for i in range(len(s)):        
        if s[i] in vowels:
            kcount += (len(s)-i)
        else:
            scount += (len(s)-i)

    if kcount > scount:
        print("Kevin " + str(kcount));
    elif kcount < scount:
        print("Stuart " + str(scount));
    else:
        print("Draw");

if __name__ == '__main__':
    s = input();
    minion_game(s.upper())