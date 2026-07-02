def main():
    user_input= input("inserisci un numero: ")
    num = int(user_input)
    result = how_many_digits(num);
    print(f"il nmero di cifre contenute nel numero {num} è {result}")


def how_many_digits(num):
    
    if num == 0:
        return 1
    else:
        i=0
        while num > 0:
            num = num//10
            i += 1
        return i
    

if __name__ == "__main__":
    main()
