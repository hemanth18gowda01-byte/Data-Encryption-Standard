# DES Encryption Implementation in Python

## Overview

This project is a simple Python implementation of the **Data Encryption Standard (DES)** algorithm.
It demonstrates how DES encrypts plaintext by dividing it into **64-bit blocks** and processing each block through multiple permutation and substitution steps.

The program supports **plaintext messages longer than 64 bits** by splitting the message into multiple blocks, encrypting each block separately, and then combining the results to produce the final ciphertext.

This implementation is designed for **learning and educational purposes**, especially for cryptography labs and assignments.

---

## Features

* Converts plaintext into **binary format**
* Splits long messages into **64-bit blocks**
* Applies **Initial Permutation (IP)**
* Performs **16 Feistel rounds**
* Uses **Expansion, XOR, and Permutation operations**
* Applies **Final Permutation (IP⁻¹)**
* Combines encrypted blocks to produce the final ciphertext
* Displays ciphertext in **binary and hexadecimal format**

---

## How DES Works (Simplified)

Plaintext
↓
Convert to Binary
↓
Split into 64-bit Blocks
↓
Initial Permutation
↓
16 Feistel Rounds
↓
Swap Left and Right Halves
↓
Final Permutation
↓
Ciphertext

---

## Project Structure

```
DES-Encryption/
│
├── DES.py
└── README.md
```

* **DES.py** → Main Python program implementing DES encryption
* **README.md** → Documentation for the project

---

## Requirements

* Python 3.x
* No external libraries required

---

## Example

Input:

```
Enter plaintext message: iamhemanth
Enter key: 1111111111111111
```

Output:

```
Binary Plaintext:
0110100101100001...

Plaintext Blocks (64-bit)
Block 1 : ...
Block 2 : ...

Encrypted Blocks
Cipher Block 1 : ...
Cipher Block 2 : ...

Final Ciphertext (Binary):
1010101010...

Ciphertext in Hex:
a93c7f3e...
```

---

## Limitations

* This is a **simplified DES implementation**.
* Some steps such as **S-box substitution are simplified**.
* It is intended only for **educational demonstration**, not real-world security.

---

## Learning Objectives

This project helps understand:

* Block cipher encryption
* Feistel network structure
* Binary data manipulation
* Permutation and substitution techniques in cryptography

---

## DES Architecture Diagrams

### DES Key Generation Architecture 

              64-bit Key
                    │
                    ▼
            +----------------+
            |   PC-1 Table   |
            | (Parity Drop)  |
            +----------------+
                    │
                    ▼
               56-bit Key
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
     C0 (28 bits)           D0 (28 bits)

        │                       │
        │  Left Shift (Round)  │
        ▼                       ▼

     C1 (28 bits)           D1 (28 bits)
        │                       │
        └───────────┬───────────┘
                    ▼
            +----------------+
            |    PC-2 Table  |
            | (Compression)  |
            +----------------+
                    │
                    ▼
              Round Key K1
               (48 bits)

         (Repeat for 16 Rounds)

     K1, K2, K3 .............. K16

### DES Encryption Block Architecture

            64-bit Plaintext
                     │
                     ▼
             +----------------+
             | Initial        |
             | Permutation(IP)|
             +----------------+
                     │
                     ▼
        ┌────────────┴────────────┐
        ▼                         ▼
     L0 (32 bits)              R0 (32 bits)

                16 Feistel Rounds
        ┌─────────────────────────────────┐
        │                                 │
        │   Li = Ri-1                     │
        │                                 │
        │   Ri = Li-1 XOR f(Ri-1 , Ki)    │
        │                                 │
        └─────────────────────────────────┘

             After Round 16
        ┌────────────┴────────────┐
        ▼                         ▼
     L16 (32 bits)             R16 (32 bits)

                     │
                     ▼
                Swap Blocks
                     │
                     ▼
             +----------------+
             | Final          |
             | Permutation(FP)|
             +----------------+
                     │
                     ▼
              64-bit Ciphertext

### DES Round Function (f-function) Architecture

              32-bit Right Half (Ri)
                       │
                       ▼
                +--------------+
                | Expansion E  |
                | 32 → 48 bits |
                +--------------+
                       │
                       ▼
                 XOR with Ki
                  (48-bit key)
                       │
                       ▼
                +--------------+
                |   S-Boxes    |
                | 48 → 32 bits |
                +--------------+
                       │
                       ▼
                +--------------+
                | Permutation  |
                |      P       |
                +--------------+
                       │
                       ▼
                   32-bit Output

---

## Author

Hemanth Gowda A

Mathematics and Computing Student Project

