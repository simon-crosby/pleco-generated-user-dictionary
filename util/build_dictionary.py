import os, time, re

PLECO_NEWLINE = u'\ueab1'
PLECO_BOLD_START = u'\ueab2'
PLECO_BOLD_END = u'\ueab3'

def read_word_file(word):
    with open(f"results/{word}", encoding="utf-8") as input_file:
        return input_file.read()

def process_word(word, output_file):
    word_file_txt = read_word_file(word)

    # Add a space between newlines to stop pleco collapsing them
    word_file_txt = word_file_txt.replace("\n\n", "\n \n")

    word_file_txt = word_file_txt.replace("\n", PLECO_NEWLINE)
    word_file_txt = word_file_txt.replace(word, f"{PLECO_BOLD_START}{word}{PLECO_BOLD_END}")
    word_file_txt = re.sub("EN:? *", "", word_file_txt)
    word_file_txt = re.sub("ZH:? *", "", word_file_txt)
    dict_line = f"{word}\t\t{word_file_txt}"
    print(dict_line, file=output_file)


def create_dictionary():
    words = get_words()
    with open(f"dict_output", "w", encoding="utf-8") as output_file:
        for word in words:
            process_word(word, output_file)


def get_words():
    return os.listdir("results/")


if __name__ == "__main__":
    create_dictionary()