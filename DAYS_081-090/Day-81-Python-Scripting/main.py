import os
import winsound
import time


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


MORSE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '/': '-..-.',
    '!': '-.-.--',
    '(': '-.--.',
    ')': '-.--.-',
    ':': '---...',
    ';': '-.-.-.',
    '+': '.-.-.',
    '-': '-....-',
    ' ': '/'
}


def text_to_morse(message):
    """This takes the text from the user as input and then converts it into respective Morse Code.
    It returns the MORSE CODE."""
    morse_code = ''

    for letter in message.upper():
        morse_code += MORSE_DICT[letter] + ' '

    return morse_code


def morse_to_text(morse_text: str):
    """This takes the Morse Code from the user as input and converts it into the respective text form.
    It returns the TEXT."""
    output_text = ''

    try:
        text_input = morse_text.split(" ")
        for letter in text_input:
            for key, value in MORSE_DICT.items():
                if value == letter:
                    output_text += key + ' '
    except Exception:
        pass
    return output_text


def morse_sound(morse):
    """ Takes the morse code and converts to short sound beeps. The duration of a dash is three times the duration of
    a dot. The letters of a word are separated by a space of duration equal to three dots, and words are separated by
    a space equal to seven dots. """
    for word in morse.split('/'):
        for char in word:
            if char == ".":
                winsound.Beep(frequency=600, duration=150)
                time.sleep(0.15)
                # print('T1')
            elif char == "-":
                winsound.Beep(frequency=600, duration=450)
                time.sleep(0.15)
                # print('T2')
            elif char == " ":
                time.sleep(0.45)
                # print('T3')
        time.sleep(1.05)
        # print('T4')


def main():
    while True:
        print('''
        
            __      _____ _    ___ ___  __  __ ___                                                        
            \ \    / / __| |  / __/ _ \|  \/  | __|                                                       
             \ \/\/ /| _|| |_| (_| (_) | |\/| | _|                                                        
              \_/\_/ |___|____\___\___/|_|  |_|___|                                                       
              |_   _/ _ \                                                                                 
                | || (_) |                                                                                
       __  __  _|_| \___/___ ___    ___ ___  ___  ___   _____ ___    _   _  _ ___ _      _ _____ ___  ___ 
      |  \/  |/ _ \| _ \/ __| __|  / __/ _ \|   \| __| |_   _| _ \  /_\ | \| / __| |    /_\_   _/ _ \| _ \ 
      | |\/| | (_) |   /\__ \ _|  | (_| (_) | |) | _|    | | |   / / _ \| .` \__ \ |__ / _ \| || (_) |   /
      |_|  |_|\___/|_|_\|___/___|  \___\___/|___/|___|   |_| |_|_\/_/ \_\_|\_|___/____/_/ \_\_| \___/|_|_\ 
                                                                                                                                                                                                                                                                                                                                                        
        ''')
        time.sleep(0.5)
        print("\nNOTE:- To give space between two words(in case of MORSE CODE) here '/' is used. ")
        time.sleep(0.5)
        choice = input('\n\nPlease Select any one Option: \n(a) TEXT --> MORSE CODE\n(b) MORSE CODE --> TEXT\n ---> ')
        if choice == 'a':
            text = input('Enter the Text you would like to be converted into Morse Code: \n')
            output = text_to_morse(text)
            print(f"\nHere is the MORSE CODE version or your message:\n"
                  f"[Turn up the volume to hear the sound]\n\n"
                  f"{output}")
            time.sleep(2.5)
            return morse_sound(output)
        elif choice == 'b':
            morse_code = input("Enter the Morse Code that you would like to be converted into Text: \n")
            morse_cd = morse_code
            output = morse_to_text(morse_code)
            print(f"\nHere is the TEXT version or your message:\n"
                  f"[Turn up the volume to hear the MORSE CODE SOUND]\n\n"
                  f"{output}")
            time.sleep(2.5)
            return morse_sound(morse_cd)
        else:
            print("\nInvalid Choice Selected."
                  "\nEnter only 'a' or 'b' ")


if __name__ == "__main__":
    main()
    while True:

        play_again = input("\nDo you like to Encrypt or Decrypt Again? (Yes/No) \n").lower()
        if play_again == "yes":
            clear()
            main()
        elif play_again == "no":
            clear()
            print("\n\n GOODBYE MAJOR......")
            time.sleep(1.8)
            exit()
        else:
            print("\n Invalid Choice. Try Again!!!")
            time.sleep(1)
            clear()
            play_again = input("\nDo you like to Encrypt or Decrypt Again? (Yes/No) \n").lower()
