def main():
    user_input= input("inserisci un numero: ")
    num = int(user_input)
    result= reverse_digits(num)
    print(result)

def reverse_digits(num):
    if num == 0:
        return 0
    else:
        reversed_num=0
        while num > 0:
            reversed_num= reversed_num * 10 + num % 10
            num = num // 10
        return reversed_num
    

if __name__ == "__main__":
    main()
