'''
Una stringa si dice "palindroma" se resta uguale sia se letta da 
sinistra verso destra che da destra verso sinistra (ignorando spazi e 
punteggiatura).

Ad esempio, la stringa seguente è palindroma:

Ed Irene se ne ride.

Scrivere un programma che, letta una stringa 'string' da tastiera, 
verifichi se la stringa è palindroma, ignorando eventuali spazi e 
caratteri di punteggiatura.

Organizzare il programma in opportune funzioni che effettuino il calcolo.
'''

def main():
    string = input("Inserisci una stringa: ")
    if is_palindrome(string.lower()):
        print(f"La stringa '{string}' è palindroma.")
    else:
        print(f"La stringa '{string}' non è palindroma.")


def is_palindrome(string):
    # Rimuove spazi e punteggiatura e converte in minuscolo
    cleaned_string = clear_string(string)
    # Confronta la stringa pulita con la sua versione invertita
    return cleaned_string == cleaned_string[::-1]


def clear_string(s):
    cleaned = ""
    for char in s: 
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            cleaned += char
    return cleaned



if __name__ == "__main__":
    main()