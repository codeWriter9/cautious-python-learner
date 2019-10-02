import re;
for i in range(int(input())):
    line = input();
    #print(line);
    print(re.findall(r'(?<!^)(#([A-Za-z0-9]{6}))', line));