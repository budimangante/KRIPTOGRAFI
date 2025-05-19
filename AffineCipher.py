def char_to_number(ch):
    if ch.isalpha():
        return ord(ch.upper()) - ord('A')  
    elif ch.isdigit():
        return 26 + int(ch)                
    else:
        raise ValueError("Only letters and digits allowed")

def number_to_char(num):
    if 0 <= num <= 25:
        return chr(num + ord('A'))
    elif 26 <= num <= 35:
        return str(num - 26)
    else:
        raise ValueError("Invalid number for mod 36")

def affine_encrypt(text, a, b):
    mod = 36
    encrypted = ""

    for ch in text:
        if ch.isalnum():
            P = char_to_number(ch)
            C = (a * P + b) % mod
            encrypted += number_to_char(C)
        else:
            continue 

    return encrypted

plain_text = "RAIHANGAMING2025"
a = 11
b = 15

cipher_text = affine_encrypt(plain_text, a, b)
print("Plaintext :", plain_text)
print("Ciphertext:", cipher_text)
