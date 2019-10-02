for _ in range(int(input())):
    n, A = input(), set(map(int, input().split()));
    m, B = input(), set(map(int, input().split()));    
    print(A - B == set());