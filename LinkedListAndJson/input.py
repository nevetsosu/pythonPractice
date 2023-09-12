def main():
    print("\'{input:}\'".format(input = input("testing with just input()\n").strip()))

    print("\'{input:}\'".format(input = input("now the same thing on input() without the strip\n").strip())) # input automatically takes away extra spaces

    # print(raw_input("testing with raw_input()\n")) # <- probably deprecated

if __name__ == "__main__" : main()