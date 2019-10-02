import re;
for i in range(int(input())):
    if bool(re.match(r'^[789]([0-9]{9})$', input())):
        print("YES");
    else:
        print("NO");