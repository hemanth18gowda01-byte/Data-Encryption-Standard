
# -----------------------------------------
# Simple DES-like Implementation
# Supports plaintext longer than 64 bits
# -----------------------------------------

# Initial Permutation Table
IP = [
[58,50,42,34,26,18,10,2],
[60,52,44,36,28,20,12,4],
[62,54,46,38,30,22,14,6],
[64,56,48,40,32,24,16,8],
[57,49,41,33,25,17,9,1],
[59,51,43,35,27,19,11,3],
[61,53,45,37,29,21,13,5],
[63,55,47,39,31,23,15,7]
]

# Expansion Table
E = [
[32,1,2,3,4,5],
[4,5,6,7,8,9],
[8,9,10,11,12,13],
[12,13,14,15,16,17],
[16,17,18,19,20,21],
[20,21,22,23,24,25],
[24,25,26,27,28,29],
[28,29,30,31,32,1]
]

# Permutation Table
P = [
[16,7,20,21,29,12,28,17],
[1,15,23,26,5,18,31,10],
[2,8,24,14,32,27,3,9],
[19,13,30,6,22,11,4,25]
]

# Final Permutation Table
IP_INV = [
[40,8,48,16,56,24,64,32],
[39,7,47,15,55,23,63,31],
[38,6,46,14,54,22,62,30],
[37,5,45,13,53,21,61,29],
[36,4,44,12,52,20,60,28],
[35,3,43,11,51,19,59,27],
[34,2,42,10,50,18,58,26],
[33,1,41,9,49,17,57,25]
]

# -----------------------------------------
# Convert string to binary
# -----------------------------------------
def string_to_binary(text):

    binary = ""

    for ch in text:
        binary += format(ord(ch),'08b')

    return binary


# -----------------------------------------
# Split plaintext into 64-bit blocks
# -----------------------------------------
def split_blocks(binary_text):

    blocks = []

    for i in range(0,len(binary_text),64):

        block = binary_text[i:i+64]

        # padding if block < 64 bits
        if len(block) < 64:
            block = block.ljust(64,'0')

        blocks.append(block)

    return blocks


# -----------------------------------------
# Permutation Function
# -----------------------------------------
def permute(block,table):

    result = ""

    for row in table:
        for element in row:
            result += block[element-1]

    return result


# -----------------------------------------
# XOR Function
# -----------------------------------------
def xor(a,b):

    result = ""

    for i in range(len(a)):

        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"

    return result


# -----------------------------------------
# Feistel Round Function
# -----------------------------------------
def feistel(left,right,key):

    # Expansion
    expanded = permute(right,E)

    # XOR with key
    xored = xor(expanded,key)

    # Simplified substitution (taking first 32 bits)
    substituted = xored[:32]

    # Permutation
    permuted = permute(substituted,P)

    # XOR with left
    new_right = xor(left,permuted)

    return right,new_right


# -----------------------------------------
# Encrypt One 64-bit Block
# -----------------------------------------
def encrypt_block(block,key):

    # Initial Permutation
    permuted_block = permute(block,IP)

    left = permuted_block[:32]
    right = permuted_block[32:]

    # 16 DES rounds
    for i in range(16):

        left,right = feistel(left,right,key[:48])

    # Swap halves
    combined = right + left

    # Final Permutation
    cipher = permute(combined,IP_INV)

    return cipher


# -----------------------------------------
# MAIN PROGRAM
# -----------------------------------------

message = input("Enter plaintext message: ")
key = input("Enter key: ")

# simple key length validation
if len(key) < 48:
    print("Key is too short. Please enter a valid key.")
    exit()

# convert plaintext to binary
binary_text = string_to_binary(message)

print("\nBinary Plaintext:")
print(binary_text)

# split plaintext into blocks
blocks = split_blocks(binary_text)

print("\nPlaintext Blocks (64-bit):")

for i,block in enumerate(blocks):
    print("Block",i+1,":",block)

cipher_text = ""

print("\nEncrypted Blocks:")

# encrypt each block
for i,block in enumerate(blocks):

    cipher_block = encrypt_block(block,key)

    print("Cipher Block",i+1,":",cipher_block)

    cipher_text += cipher_block


print("\nFinal Ciphertext (Binary):")
print(cipher_text)

print("\nCiphertext Length:",len(cipher_text))

# convert ciphertext to hex
cipher_hex = hex(int(cipher_text,2))[2:]

print("\nCiphertext in Hex:")
print(cipher_hex)

