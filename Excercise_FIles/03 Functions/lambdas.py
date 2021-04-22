# Use lambdas as in-place functions


def CelsisusToFahrenheit(temp):
    return (temp * 9/5) + 32


def FahrenheitToCelsisus(temp):
    return (temp-32) * 5/9


def main():
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]

    # Use regular functions to convert temps
    print(list(map(FahrenheitToCelsisus, ftemps)))
    print(list(map(CelsisusToFahrenheit, ctemps)))

    # Use lambdas to accomplish the same thing
    #[0.0, 18.333333333333332, 37.77777777777778, 100.0]
    print(list(map(lambda t: (t-32) * 5/9, ftemps)))
    
    #[32.0, 53.6, 93.2, 212.0]
    print(list(map(lambda t: (t * 9/5) + 32, ctemps)))


if __name__ == "__main__":
    main()
