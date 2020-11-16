from itertools import product
# input no of lines and upper bound
number_of_lines, upper_bound = map(int, input().split(" "))
# load lines of input in a list of lists
all_lines = [list(map(int, input().split()))[1:] for _ in range(number_of_lines)]
# create a cartesian product of N * N
_product_ = product(*all_lines)
# reduce each tuple using the f(x) 
results = map(lambda x: sum(i**2 for i in x) % upper_bound, _product_)
# find the max
print(max(results))  