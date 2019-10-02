K = int(input());
U = list(map(int, input().split()));
S = set(U);
s1 = sum(U); # K X ( 1 + 2 + ...) + C
s2 = sum(S); # 1 + 2 + ... + C
s = (s1 - s2); # (K - 1) X (1 + 2 + .. )
r = s / (K - 1); # (1 + 2 + .. )
print(int(s2 - r)); # (1 + 2 + ... + C) -  (1 + 2 + .. )