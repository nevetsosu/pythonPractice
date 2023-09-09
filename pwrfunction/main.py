def main():
    print(pwr(123456789,123))

def pwr(base: int = 1, exp: int = 1):
    if (exp == 0): return 1

    # exp is even
    if (exp % 2 == 0): 
        return pwr(base * base, exp / 2)
    else: 
        return base * pwr(base, exp - 1)

## this one reaches max recursion depth really fast, like orders of magnitude lower exponents cause recusion depth errors compared to the other one
# def pwr(base: int, exp: int):
#     if (exp == 1): return base
#     else: return base * pwr(base, exp - 1)

if __name__ == "__main__": main()