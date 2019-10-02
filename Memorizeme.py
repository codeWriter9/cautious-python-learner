reference = [0 for x in range(10000)];
r = int(input());
actual = list(map(int, input().split()));
for x in actual:
    reference[x] = reference[x] + 1;
for x in range(int(input())):
    index = int(input());
    print(reference[index] if reference[index] !=0 else "NOT PRESENT");