def ma_hoa(plaintext, k):
    k = k % 26
    result = []
    for ch in plaintext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            c = (ord(ch) - base + k) % 26 + base
            result.append(chr(c))
        else:
            result.append(ch)
    return ''.join(result)

P = "NguyenThiPhuongThao"
C = ma_hoa(P, 24)
print("Plaintext:", P)
print("Ciphertext:", C)