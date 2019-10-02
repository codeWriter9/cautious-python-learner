'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
def fprintf(characters):
    output = '';
    for character in characters:        
        if character == 'G':
            output = output + 'C';
        elif character == 'C':
            output = output + 'G';
        elif character == 'T':
            output = output + 'A';
        elif character == 'A':
            output = output + 'U';
        else :        
            return 'Invalid Input';
    return output;
print(fprintf(input()));