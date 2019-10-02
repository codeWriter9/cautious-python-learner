def operation(op, l, A):
    if op == 'intersection_update':
	    A.intersection_update(l);
    elif op == 'update':
        A.update(l);
    elif op == 'symmetric_difference_update':
        A.symmetric_difference_update(l);
    elif op == 'difference_update':
        A.difference_update(l);
    else :
        print("Invalid  op code");


N = int(input());
A = set(map(int, input().split()));
M = int(input());
for i in range(M):
    arr = input().split();    
    op = arr[0];
    len_ = int(arr[1]);
    l = set(map(int, input().split()));
    operation(op, l, A);    
print(sum(A));