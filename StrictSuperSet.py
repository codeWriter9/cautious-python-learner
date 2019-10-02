S, superSetbool = set(map(int, input().split())), True;
for _ in range(int(input())):    
    X = set(map(int, input().split()));
    XdiffS = (len(X - S) == 0);
    SdiffX = (len(S - X) != 0);    
    superSetbool = superSetbool and XdiffS and SdiffX;
print(superSetbool);