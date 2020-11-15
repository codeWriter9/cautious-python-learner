'''
Created on 31-Jul-2019
Updated on 11-Oct-2020
@author: Sanjay Ghosh
'''
class HelloWorld:
    """A simple example class"""
    def __init__(self):
        print(self.hello_world())
    
    def hello_world(self):
        return 'hello world!!'




if __name__ == '__main__':
    X = HelloWorld();
