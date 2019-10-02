import re;

def translate(match):
    if "&&" == match.group(0):
        return " and ";
    else:
        return " or ";


N = int(input());
for _line in range(N):
    print(re.sub("(?<= )(&&|\|\|)(?= )", translate, input()));