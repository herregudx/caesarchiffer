def caesar_cipher(text, shift):
    # Norsk alfabet
    alphabet = 'abcdefghijklmnopqrstuvwxyzæøå'
    alphabet_upper = alphabet.upper()
    encrypted_text = ''

    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            shifted_index = (index + shift) % len(alphabet)
            encrypted_text += alphabet[shifted_index]
        elif char in alphabet_upper:
            index = alphabet_upper.index(char)
            shifted_index = (index + shift) % len(alphabet_upper)
            encrypted_text += alphabet_upper[shifted_index]
        else:
            # Behold tegn som ikkje er bokstaver
            encrypted_text += char

    return encrypted_text

# Brukerinput
text = input("Skriv inn teksten du vil kryptere: ")
shift = int(input("Hvor mange plasser vil du rotere bokstavene? "))

kryptert = caesar_cipher(text, shift)
print("Kryptert tekst:", kryptert)
