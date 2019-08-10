'''
Created on 31-Jul-2019

@author: Sanjay Ghosh
'''
class HelloWorld:
    """A simple example class"""
    def __init__(self):
        print(self.hello_world());    
        i = 12345;
    
    def hello_world(self):
        return 'hello world'

X = HelloWorld();