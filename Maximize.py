from itertools import product;
num_lines, modulo = map(int, input().split());
list_of_lists = [ (list(map(int, input().split())))[1:] for line in range(num_lines)];
f = lambda x : sum ( element ** 2 for element in list ) % modulo;
for _ in product(*list_of_lists):
    print(map(lambda _ : (i ** 2 for i in _) % modulo, _));