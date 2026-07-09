# Cipher Toolkit

A simple Python tool for encoding/decoding text using classic cipher methods.
Built as part of my cybersecurity self-study journey, to learn cryptography fundamentals hands-on.

## Currently supported

- **Caesar Cipher** — encode / decode
  - Preserves uppercase/lowercase letters
  - Non-alphabetic characters (spaces, punctuation) are left unchanged
  - Takes text and shift value as user input via terminal
  - Added Bruteforce
  - Added Window for a better looking
  - It looks like a tool than before.

## Coming soon

- [ ] ROT13
- [ ] Vigenère Cipher
- [ ] Base64 encode/decode
- [ ] XOR cipher
- [ ] Brute force mode (try all possible shifts when the shift is unknown)

## How to run

```bash
python caesar.py
```

The terminal will prompt you for a word/sentence and a shift value, then print the result.

## Example

```
Enter text: Hello World!
Enter shift: 3
Khoor Zruog!
```

## Why this project?

I started learning cryptography through OverTheWire's Bandit and Krypton series,
and built this project to turn the concepts I was learning (ASCII, modular arithmetic,
string manipulation) into a concrete tool. More cipher types will be added over time.

## Setup

No external libraries required, just Python 3.

```bash
git clone <this-repo-link>
cd cipher-toolkit
python caesar.py
```
## It helps to learn Caesar encode technic.
