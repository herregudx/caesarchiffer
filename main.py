def caesar_cipher(text, shift, mode='encrypt'):
    # Norsk alfabet med æ, ø og å
    alphabet = 'abcdefghijklmnopqrstuvwxyzæøå'
    alphabet_upper = alphabet.upper()
    result = ''

    if mode == 'decrypt':
        shift = -shift  # Roter motsatt vei

    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            shifted_index = (index + shift) % len(alphabet)
            result += alphabet[shifted_index]
        elif char in alphabet_upper:
            index = alphabet_upper.index(char)
            shifted_index = (index + shift) % len(alphabet_upper)
            result += alphabet_upper[shifted_index]
        else:
            # Behold mellomrom og tegn
            result += char

    return result

# Brukerinput
mode = input("Vil du kryptere eller dekryptere? (skriv 'k' eller 'd'): ").strip().lower()
text = input("Skriv inn teksten: ")
shift = int(input("Hvor mange plasser skal det roteres med? "))

if mode == 'k':
    output = caesar_cipher(text, shift, mode='encrypt')
elif mode == 'd':
    output = caesar_cipher(text, shift, mode='decrypt')
else:
    print("Ugyldig valg.")
    exit()

print("Resultat:", output)
