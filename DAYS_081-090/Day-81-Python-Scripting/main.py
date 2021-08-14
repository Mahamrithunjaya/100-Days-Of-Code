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
    morse_code = ''

    for letter in message.upper():
        morse_code += MORSE_DICT[letter] + ' '

    return print(morse_code)


def morse_to_text(morse_text: str):
    output_text = ''

    try:
        text_input = morse_text.split(" ")
        for letter in text_input:
            for key, value in MORSE_DICT.items():
                if value == letter:
                    output_text += key + ' '
    except Exception:
        pass
    return print(output_text)


def main():
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
    print("\nNOTE:- To give space between two words here '/' is used. ")
    choice = input('\n\nPlease Select any one Option: \n(a) TEXT --> MORSE CODE\n(b) MORSE CODE --> TEXT\n ---> ')
    if choice == 'a':
        text = input('Enter the text to convert: \n')
        text_to_morse(text)
    elif choice == 'b':
        morse_code = input("Enter the Morse Code: \n")
        morse_to_text(morse_code)
    else:
        print("Enter only 'a' or 'b' ")


main()
