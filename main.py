def main():
    inp = str(input("Input 'd' to decode or 'e' to encode or 'q' to quit\n"))
    if inp == "d":
        decode()
    elif inp == "e":
        encode()
    elif inp == 'q':
        quit()
    else:
        print("Invalid input.")
        main()


def decode():
    mes = str(input("Enter your encrypted message\n"))
    cod = str(input("Enter your code word\n"))
    i = 0
    nMes = ""
    printable_start = 32
    printable_end = 126
    printable_range = printable_end - printable_start + 1

    for char in mes:
        if i >= len(cod):
            i = 0
        val = (ord(char) - ord(cod[i]) - printable_start) % printable_range + printable_start
        nMes += chr(val)
        i += 1
    print("Your decoded message:\n" + nMes)
    main()
    

def encode():
    mes = str(input("Enter your message to encrypt\n"))
    cod = str(input("Enter your code word\n"))
    i = 0
    nMes = ""
    printable_start = 32
    printable_end = 126
    printable_range = printable_end - printable_start + 1

    for char in mes:
        if i >= len(cod):
            i = 0
        val = (ord(char) + ord(cod[i]) - printable_start) % printable_range + printable_start
        nMes += chr(val)
        i += 1
    print("Your encoded message:\n\"" + nMes + "\"")
    print("Your codeword:\n" + cod)
    main()


main()