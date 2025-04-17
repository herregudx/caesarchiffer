import tkinter as tk
from tkinter import ttk

def caesar_cipher(text, shift, mode='encrypt'):
    alphabet = 'abcdefghijklmnopqrstuvwxyzæøå'
    alphabet_upper = alphabet.upper()
    result = ''

    if mode == 'decrypt':
        shift = -shift # Roter motsatt vei

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
            result += char # Behold mellomrom og tegn

    return result

def run_cipher():
    text = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        result_label.config(text="Rotasjon må være et heltall.")
        return

    mode = mode_var.get()
    result = caesar_cipher(text, shift, mode=mode)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, result)

# GUI
root = tk.Tk()
root.title("Cæsarchiffer")

ttk.Label(root, text="Tekst:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
input_text = tk.Text(root, height=4, width=50)
input_text.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

ttk.Label(root, text="Rotasjon:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
shift_entry = ttk.Entry(root)
shift_entry.grid(row=1, column=1, padx=5, pady=5)
shift_entry.insert(0, "13")

mode_var = tk.StringVar(value='encrypt')
ttk.Radiobutton(root, text="Krypter", variable=mode_var, value='encrypt').grid(row=2, column=1, sticky="w")
ttk.Radiobutton(root, text="Dekrypter", variable=mode_var, value='decrypt').grid(row=2, column=1, sticky="e")

ttk.Button(root, text="Kjør", command=run_cipher).grid(row=3, column=1, pady=10)

ttk.Label(root, text="Resultat:").grid(row=4, column=0, sticky="nw", padx=5, pady=5)
result_text = tk.Text(root, height=4, width=50)
result_text.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

result_label = ttk.Label(root, text="")
result_label.grid(row=5, column=1, pady=5)

root.mainloop()
