N = int(input());
b_array_str = input().split();
K = int(input());
b_int_list = map(lambda _str_ : int(_str_) if int(_str_) == K else 0, b_array_str);
index = 0;
for _ in b_int_list:    
    if _ == K:
        print(index);
    index = index + 1;