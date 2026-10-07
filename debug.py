def encode(text, key):
    cipher = make_cipher(key)
    ciphertext_chars = []
    #print(cipher)
    for i in text:
        #print(i)
        #print (cipher.index(i))
        ciphered_char = chr(65 + cipher.index(i))
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)
    print(cipher)
    plaintext_chars = []
    for i in encrypted:
        print(23 + ord(i))
        plain_char = cipher[ord(i) - 65]#swapped ord[i] and 65, 65-ord(i) resulted in negative indicies, effectivley reverse of line 8
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 96) for i in range(1, 27)]#changed from i+98, as alphabet was starting at c. Changed range to 27 to get z 
    cipher_with_duplicates = list(key) + alphabet
    #print(alphabet)

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")

print(f"""
 Running: encode("abc", "secretkey")
Expected: HIC
  Actual: {encode('abc', 'secretkey')}
""")

print(f"""
 Running: decode("HIC", "secretkey")
Expected: abc
  Actual: {decode('HIC', 'secretkey')}
""")

