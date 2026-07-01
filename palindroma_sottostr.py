
def main():
    string = input("Inserisci una stringa: ")
    result = is_the_longest_palindrome(string)
    print(f"La sottostringa palindroma più lunga è: '{result}'.")


def is_the_longest_palindrome(string):

    cleaned_string = clear_string(string)
    longest_palindrome = ""
    for i in range(len(cleaned_string)):
        for j in range(i, len(cleaned_string)):
            substring = cleaned_string[i:j+1]
            if substring == substring[::-1]:
                if len(substring) > len(longest_palindrome):
                    longest_palindrome = substring
    return longest_palindrome


def is_palindrome(string):

    cleaned_string = clear_string(string)
    return cleaned_string == cleaned_string[::-1]


def clear_string(s):
    cleaned = ""
    for char in s: 
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            cleaned += char
    return cleaned



if __name__ == "__main__":
    main()