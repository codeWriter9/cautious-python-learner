import email.utils;
n = int(input());
l = [input() for x in range(n)];
for _str_ in l:
    try:
        print(email.utils.formataddr(email.utils.parseaddr(_str_)));
    except:        
        continue;