l = list(map(int, input().split()));
l[1], l[0] = l[0], l[1];
l[0], l[1] = l[0] * l[2], l[1] + l[2];
print(" ".join(map(str, l[:2])));