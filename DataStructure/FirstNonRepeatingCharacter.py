
def first_non_repeating_v1(string):
    # Empty Dict
    freq = {}
    # aaacccpdddd
    for x in string:
        freq[x] = freq.get(x, 0) + 1#return the value for key

    for i in string:
        if freq[i] == 1:
            return i


def first_non_repeating_v2(string):
    #netsetosnet
    dict = {}
    size = len(string)
    for i in range(size):
        key = string[i]
        if key not in dict:
            dict[key] = 1
        else:
            dict[key] += 1

    #{n:2, e:3, t:3, s:2, 0:1}
    counter=0
    for index in range(size):
        if dict[string[index]] == 1:
            return string[index], counter
        counter+=1    


class main():

    print(first_non_repeating_v1("aaacccpdddd"))
    print(first_non_repeating_v2("aaacccpdddd"))


if __name__ == "__main__":
    main()