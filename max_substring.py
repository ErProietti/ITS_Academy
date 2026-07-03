def get_substring_from_index(parola, start_index):
    
    substring=""
    for i in range(start_index, len(parola)):
        current_char= parola[i]

        if current_char in substring:
            break
        
        substring += current_char

    return substring


def get_longest_unique_substrings(parola):
    all_substring= set()

    for i in range(len(parola)):
        substring = get_substring_from_index(parola, i)
        all_substring.add(substring)


    max_len=0
    for substring in all_substring:
        if len(substring) > max_len:
            max_len = len(substring)


    longest_sub = set()
    for substring in all_substring:
        if len(substring) == max_len:
            longest_sub.add(substring)

    return longest_sub




def main():

    user_input = input("Inserisci una stringa: ")
    
    if not user_input:
        print("La stringa è vuota!")
        return

    result = get_longest_unique_substrings(user_input)
    

    print("\nLe più lunghe sottostringhe senza caratteri ripetuti sono:")
    for elemento in result:
        print(elemento)



if __name__ == "__main__":
    main()