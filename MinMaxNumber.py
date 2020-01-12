N, _list_ = int(input()), sorted(list(map(int, input().split())));
print((str(sum(_list_[:N - 1]))) + " "  + str(sum(_list_[1:])));