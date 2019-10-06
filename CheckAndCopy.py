'''
Created on 10-Aug-2019

1st Edit 05-Oct-2019

@author: Sanjay Ghosh
'''
from os import listdir;
from os.path import isfile, join;
from argparse import ArgumentParser;

def compare(src, dest):    
    cautiousPythonLearner = [f for f in listdir(dest) if isfile(join(dest, f))];    
    LearningPython = [f for f in listdir(src) if isfile(join(src, f))];
    difference = [file for file in LearningPython if file not in cautiousPythonLearner];
    if len(difference) != 0:
        print("\r\n".join(difference));
        command = input("Copy This files ? (Y)es or (N)o");
        if "Y" == command or "y" == command: 
            for pfile in difference:
                rfile = open(src + "/" + pfile, "r");
                wfile = open(dest + "/" + pfile, "w");
                for line in rfile:
                    wfile.write(line);
            print(str(len(difference)) + " Files copied.");
        else:
            print("Not copied.");
    else :
        print("No Difference found!!");

if __name__ == "__main__":
    parser = ArgumentParser();
    parser.add_argument('--src', help='dir from where to copy files');
    parser.add_argument('--dst', help='dir to where copy files');
    args = parser.parse_args();
    if args.src and args.dst:    
        compare(args.src, args.dst);
    else:
        parser.print_help();