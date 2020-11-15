import time

def unit(x):
 return [x]

def bind(t, f):  
  return [f(i) for i in t]

def decorator(func):
  def log_time():
    start = time.process_time()            
    func()    
    end = time.process_time()    
    print("Time Taken: %10.7f seconds" % (end - start))
  return log_time


@decorator
def main():
  print("Hello World!")

if __name__ == "__main__":
    # execute only if run as a script    
    main();
    add_one = lambda x: x + 1
    add_two = lambda x: x + 2
    add_three = lambda x: x + 3
    print( bind(bind(bind(unit(10), add_one), add_two), add_three))
