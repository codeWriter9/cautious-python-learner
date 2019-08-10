'''
Created on 10-Aug-2019

@author: Sanjay Ghosh
'''
from os import listdir
from os.path import isfile, join
mypath = "C:/work/workspaces/first/cautious-python-learner";
cautiousPythonLearner = [f for f in listdir(mypath) if isfile(join(mypath, f))];
mypath = "C:/work/workspaces/first/LearningPython";
LearningPython = [f for f in listdir(mypath) if isfile(join(mypath, f))];
difference = [file for file in LearningPython if file not in cautiousPythonLearner];
print("\r\n".join(difference));