from alphabet import alphabet
from art import logo

print(logo)

status = True
while status:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26


    def caesar(main_text, main_shift, way):

        all_letters= ""
        if way == "decode":

            main_shift *= -1
        for char in main_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + main_shift
                all_letters += alphabet[new_position]
            else:
                all_letters += char
        print(f"Here's the {direction}d result: {all_letters}")



    caesar(main_text=text, main_shift=shift, way=direction)
    restart = input("Do you want to restart caeser game again ? yes/no: ").lower()
    if restart == 'no':
        print("GoodBye")
        status=False
    else:
        continue