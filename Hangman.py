
MAX_TRIES = 6
def open_screen():

    HANGMAN_ASCII_ART = ("""
Welcome to the Hangman game!
  _    _
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
 |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |
                      |___/

The amount of your maximum mistakes is""")

    print(HANGMAN_ASCII_ART, MAX_TRIES)

NOT_UPDATED_STR = "You wrong!\n{0}"

HANGMAN_PHOTOS = {
1: "x-------x",
2: """x-------x
|
|
|
|
|
""",
3: """x-------x
|       |
|       0
|
|
|
""",
4: """x-------x
|       |
|       0
|       |
|
|
 """,
5: """x-------x
|       |
|       0
|      /|\\
|
|
 """,
6: """x-------x
|       |
|       0
|      /|\\
|      /
|
 """,
7: """x-------x
|       |
|       0
|      /|\\
|      / \\
|
""",
}

def print_hangman(num_of_tries):
    """Prints hangman state, according to input nunmer.
    :param: num_of_tries: define the state to be displayed
    :type: int """
    return HANGMAN_PHOTOS[num_of_tries]
def choose_word(file_path, index):
    """ returns the length of your string, without counting the same words.
     :Param file_path: your url file.
     :Param index: the position of your word by chosing an index number.
     :rtype: string.
    """
    with open(file_path, 'r') as read_file:
        lines = read_file.read()
        read_file.close()
        words = lines.split(' ')
        words_list = []
        count_list = []
        for word in words:
            count_list.append(word)
            if word not in words_list:
                words_list.append(word)
        answer = len(words_list)
        counter = (index - 1) % len(count_list)
        chosen_word = count_list[counter]
    return chosen_word
def show_hidden_word(secret_word, old_letters_guessed):
    """show the status of the hidden word.
    :param secret_word: user's chosen word
    :param old_letters_guessed: List of guessed letters
    :type secret_word: string
    :type old_letters_guessed: list
    :return: variable "result" which contain the satus
    :rtype: string
    """
    secret_word_progress = ['']
    for letter in secret_word:
        if letter in old_letters_guessed:
            secret_word_progress.append(letter + " ")
        else:
            secret_word_progress.append("_ ")
    result = ''.join(secret_word_progress)
    return result
def check_valid_input(letter_guessed, old_letters_guessed):
    """ this function get a letter from the player and check if the letter is fine:
    - its not more than a 1 word.
    - its a letter in English.
    - its not in the old list. """
    letter_guessed = letter_guessed.lower()
    if (letter_guessed.isalpha() == True) and (len(letter_guessed) == 1) and (letter_guessed not in old_letters_guessed):
        return True
    else:
        return False
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """ function that checks if the letter is in the list.
 if its in - the function return False.
 if its not in, the function adds the letter.
 :Param letter_guessed: user's inputs
 :param old_letters_guessed: user's wrong inputs"""
    if letter_guessed not in old_letters_guessed and (letter_guessed.isalpha() == True):
         old_letters_guessed.append(letter_guessed.lower())
         print(NOT_UPDATED_STR.format(" -> ".join(sorted(old_letters_guessed))))
         return True
    else:

        print(NOT_UPDATED_STR.format(" -> ".join(sorted(old_letters_guessed))))
        return False
def check_win(secret_word, old_letters_guessed):
    """checks if the user win.
    :Param1: secret_word: user's secret word.
    :Param2: old_letters_guessed: user's letter guessed.
    :rtype: bool"""
    empty_list = []
    for letter in secret_word:
        if (letter not in empty_list):
            empty_list.append(letter)

    check = all(item in old_letters_guessed for item in secret_word)
    if check == True:
        return True
    else:
        return False

def main():
    open_screen()
    num_of_tries = 0
    file_path = r"C:\Users\yasha\OneDrive\שולחן העבודה\Works\working with files\meaningless.txt"
    index = int(input("Enter your word position:"))
    secret_word = choose_word(file_path, index)
    old_letters_guessed = []
    print(print_hangman(1))
    while num_of_tries < MAX_TRIES:
        print(show_hidden_word(secret_word, old_letters_guessed))
        letter_guessed = str(input("Enter word/letter: ")).lower()
        game_status = check_win(secret_word, old_letters_guessed)
        valied_text = check_valid_input(letter_guessed, old_letters_guessed)
        if game_status:
            print("GGWP!")
            break
        elif not(game_status):
                if letter_guessed in secret_word:
                    # if the user right.
                    if valied_text:
                        print("Good choice \n")
                        old_letters_guessed.append(letter_guessed)
                    if not(valied_text):
                    # if the user right but the letter guessed already.
                        print("its already gussed! \n")
                elif letter_guessed not in secret_word:
                    # if the user not right
                    if valied_text:
                        num_of_tries += 1
                        print(print_hangman(num_of_tries + 1))
                        print(try_update_letter_guessed(letter_guessed, old_letters_guessed))
                        print("You have", (6 - num_of_tries) ,"more tries")
                    elif not(valied_text):
                        print("Look at your input again :( \n")

                    elif num_of_tries == 5:
                        num_of_tries += 1
                        old_letters_guessed.append(letter_guessed)
                        print(print_hangman(7),"""no more tries,
                        GAME OVER!""")

if __name__ == "__main__":
    main()
