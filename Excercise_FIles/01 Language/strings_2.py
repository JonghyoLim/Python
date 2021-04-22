def main():
    a = "python "
    b = " is fun!"
    print(a * 100 + "\n")

    a = "Life is too short, You need Python"
    print(a[0]) #L
    print(a[-1])#n
    print(a[0:4])#Life


    ## a[ more than : less than: term size ]
    sp = "addaa"
    def in_palindrome(sp):
        return sp == sp[::-1]
    print(in_palindrome(sp))    

    num = 10;
    day = "three"
    s = "i ate %d apple. so was so sick for %s days." %(num, day)
    print(s)

    a = "21042021Sunny"
    date = a[:8]
    weather = a[8:]
    print(date)#21042021  index[0]..[7]
    print(weather)#Sunny index[8]...[a.length]
    print(a[::2])#2022Sny

    url = "http//:google.com"
    my_str = url.replace("http//:", "")#String.replace(old, new)
    print(my_str)#google

    my_str = my_str[:my_str.index(".")]#string.index[less than: more than :]
    print(my_str)


if __name__ == "__main__":
    main()