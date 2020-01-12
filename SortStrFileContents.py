'''
Created on 10-Aug-2019

1st Edit 05-Oct-2019

@author: Sanjay Ghosh
'''
from os import listdir;
from os.path import isfile, join;
from argparse import ArgumentParser;

def sort_file(src, dest):    
    rfile = open(src, "r");
    wfile = open(dest, "w");
    contents = [];
    for line in rfile:
        contents.append(line);
    contents.sort();
    for line in contents:
        wfile.write(line);
    wfile.flush();
    wfile.close();
    rfile.close();

if __name__ == "__main__":
    parser = ArgumentParser();
    parser.add_argument('--src', help='path of unsorted file');
    parser.add_argument('--dst', help='path where to create the sorted file ');
    args = parser.parse_args();
    if args.src and args.dst:    
        sort_file(args.src, args.dst);
    else:
        parser.print_help();