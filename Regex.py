import re;
def regex(__in):
    TESTER = re.compile(r'(?<=-)'r'\d+');
    print("Valid" if TESTER.search(__in.strip()) else "Invalid");
    print(__in);

if __name__ == "__main__":
    regex(input());