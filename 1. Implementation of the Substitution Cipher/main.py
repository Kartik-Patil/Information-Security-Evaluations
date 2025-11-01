import tkinter as tk
from tkinter import messagebox
import string, random

# ---------------- Cipher Logic ----------------
def generate_maps(key):
    alphabet = list(string.ascii_lowercase)
    key = ''.join([ch.lower() for ch in key if ch.isalpha()])  # remove non-letters

    missing = [ch for ch in alphabet if ch not in key]
    duplicates = [ch for ch in key if key.count(ch) > 1]
    if len(key) != 26 or sorted(key) != sorted(alphabet):
        msg = "Invalid key! "
        if duplicates:
            msg += f"Duplicates found: {', '.join(sorted(set(duplicates)))}. "
        if missing:
            msg += f"Missing letters: {', '.join(missing)}."
        raise ValueError(msg.strip())

    encrypt_map = dict(zip(alphabet, key))
    decrypt_map = dict(zip(key, alphabet))
    return encrypt_map, decrypt_map

def encrypt(text, encrypt_map):
    result = []
    for ch in text:
        if ch.isalpha():
            mapped = encrypt_map.get(ch.lower(), ch)
            result.append(mapped.upper() if ch.isupper() else mapped)
        else:
            result.append(ch)
    return ''.join(result)

def decrypt(text, decrypt_map):
    result = []
    for ch in text:
        if ch.isalpha():
            mapped = decrypt_map.get(ch.lower(), ch)
            result.append(mapped.upper() if ch.isupper() else mapped)
        else:
            result.append(ch)
    return ''.join(result)

# ---------------- GUI Functions ----------------
def show_mapping():
    key = key_entry.get().strip()
    try:
        encrypt_map, _ = generate_maps(key)
        mapping_text.config(state="normal")
        mapping_text.delete("1.0", tk.END)
        items = list(encrypt_map.items())
        line1 = " | ".join([f"{a.upper()}→{b.upper()}" for a, b in items[:13]])
        line2 = " | ".join([f"{a.upper()}→{b.upper()}" for a, b in items[13:]])
        mapping_text.insert(tk.END, line1 + "\n" + line2)
        mapping_text.config(state="disabled")
    except ValueError as e:
        mapping_text.config(state="normal")
        mapping_text.delete("1.0", tk.END)
        mapping_text.insert(tk.END, str(e))
        mapping_text.config(state="disabled")

def perform_encrypt():
    key = key_entry.get()
    text = input_text.get("1.0", tk.END).strip()
    try:
        encrypt_map, _ = generate_maps(key)
        cipher = encrypt(text, encrypt_map)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, cipher)
        show_mapping()
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def perform_decrypt():
    key = key_entry.get()
    text = input_text.get("1.0", tk.END).strip()
    try:
        _, decrypt_map = generate_maps(key)
        plain = decrypt(text, decrypt_map)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, plain)
        show_mapping()
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def clear_fields():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    key_entry.delete(0, tk.END)
    mapping_text.config(state="normal")
    mapping_text.delete("1.0", tk.END)
    mapping_text.config(state="disabled")

def generate_random_key():
    key = ''.join(random.sample(string.ascii_lowercase, 26))
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key)
    show_mapping()

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("Substitution Cipher")
root.geometry("1300x700")
root.config(bg="#e6f0ff")

title_label = tk.Label(root, text="Substitution Cipher Implementation",
                       font=("Arial", 16, "bold"), bg="#e6f0ff", fg="#003366")
title_label.pack(pady=10)

frame = tk.Frame(root, bg="#e6f0ff")
frame.pack()
tk.Label(frame, text="Enter 26-letter Key:", bg="#e6f0ff").grid(row=0, column=0, padx=5, pady=5)
key_entry = tk.Entry(frame, width=40)
key_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame, text="Generate Key", command=generate_random_key,
          bg="#ff9800", fg="white", width=12).grid(row=0, column=2, padx=5)

center_frame = tk.Frame(root, bg="#e6f0ff")
center_frame.pack(expand=True)

input_frame = tk.Frame(center_frame, bg="#e6f0ff")
tk.Label(input_frame, text="Enter Text:", bg="#e6f0ff").pack()
input_text = tk.Text(input_frame, height=10, width=45)
input_text.pack(pady=5)

btn_frame = tk.Frame(input_frame, bg="#e6f0ff")
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Encrypt", command=perform_encrypt,
          bg="#4caf50", fg="white", width=10).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Decrypt", command=perform_decrypt,
          bg="#2196f3", fg="white", width=10).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Clear", command=clear_fields,
          bg="#f44336", fg="white", width=10).grid(row=0, column=2, padx=10)

output_frame = tk.Frame(center_frame, bg="#e6f0ff")
tk.Label(output_frame, text="Output:", bg="#e6f0ff").pack()
output_text = tk.Text(output_frame, height=10, width=45)
output_text.pack(pady=5)

mapping_frame = tk.Frame(center_frame, bg="#e6f0ff")
tk.Label(mapping_frame, text="Letter Substitution Mapping:", bg="#e6f0ff").pack()
mapping_text = tk.Text(mapping_frame, font=("Arial", 9), height=5, width=75, state="disabled", wrap="word")
mapping_text.pack(pady=5)

input_frame.pack(pady=10)
output_frame.pack(pady=10)
mapping_frame.pack(pady=10)

footer = tk.Label(root, text="© 01FE20BCS325 | Kartik Patil | Substitution Cipher",
                  bg="#e6f0ff", fg="#333333", font=("Arial", 9))
footer.pack(side=tk.BOTTOM, pady=5)

root.mainloop()
