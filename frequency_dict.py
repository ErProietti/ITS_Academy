def main():
    user_input = input("inserire una parola: ")
    result = frequency_dict(user_input.lower())
    result2= get_chars_with_max_freq(user_input.lower())
    print(result)
    print(result2)


def frequency_dict(parola):
    frequency = {}
    for char in parola:
        if char in frequency:
            frequency[char] = frequency[char] + 1
        else:
            frequency[char] = 1
    return frequency




def get_chars_with_max_freq(parola):
    frequency = frequency_dict(parola)
    
    with_max_freq = {}  
    freq = 0               

    for key, times in frequency.items():
        

        if times > freq:
            freq = times
            with_max_freq = {key : freq}
        elif  times == freq:
            with_max_freq[key] = freq
            
    return with_max_freq


if __name__ == "__main__":
    main()
