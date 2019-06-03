'''
Created on 25-May-2019

@author: Sanjay Ghosh
'''
def transcribe(ch):
    if ch == 'G':
        return 'C';
    elif ch == 'C':
        return 'G';
    elif ch == 'T':
        return 'A';
    elif ch == 'A':
        return 'U';
    else :
        return '='; 
    

def translate(myStr):
    rString = "";
    for ch in myStr:
        if ch not in ['G', 'C', 'T', 'A']:
            return "Invalid Input";
        else :
            xc = transcribe(ch);            
            rString = rString + xc;   
    return rString;
    
print(translate(input()));