nA = int(input());
A = set(sorted(list(map(int, input().split()))));
nC = int(input());
C = set(sorted(list(map(int, input().split()))));
tempB = set();
B = set();
for c in C:
    for a in A:
        if a < c:
            tempB.add(c - a);
for b in tempB:
    isCandidate = True;
    for a in A:
        if a + b not in C:
            isCandidate = False;
            continue;
    if isCandidate:
        B.add(b);
B = sorted(B);
print(" ".join(map(str, B)));