def caesar_encode(text, shift):
    result = ""                        # Result
    for letter in text:                
        if letter.isalpha():           # is it a letter
            if letter.isupper():       # upper case letter
                base = 65               # From "A" 
            else:
                base = 97               # From "a"

            index = ord(letter) - base          # find index (0-25)
            new_index = (index + shift) % 26    
            new_letter = chr(new_index + base)  #  converting to letter (same base)
            result += new_letter
        else:
            result += letter            # if not letter (space, "!")
    return result


kelime = input("Enter Text: ")
shift = int(input("How many shift to your text?: "))
print(caesar_encode(kelime, shift))