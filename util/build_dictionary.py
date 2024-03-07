import os, time, re

PLECO_NEWLINE = u'\ueab1'
PLECO_BOLD_START = u'\ueab2'
PLECO_BOLD_END = u'\ueab3'

def read_word_file(word):
    with open(f"../words/{word}", encoding="utf-8") as input_file:
        return input_file.read()

def load_pinyin():
    pinyin_map = {}
    with open(f"./pinyin.csv", encoding="utf-8") as input_file:
        for line in input_file:
            word, pinyin = line.strip().split("\t")
            pinyin_map[word] = pinyin
    return pinyin_map


    
    
def process_word(word, pinyin, output_file):
    word_file_txt = read_word_file(word)

    # Add a space between newlines to stop pleco collapsing them
    word_file_txt = word_file_txt.replace("\n\n", "\n \n")

    word_file_txt = word_file_txt.replace("\n", PLECO_NEWLINE)
    word_file_txt = word_file_txt.replace(word, f"{PLECO_BOLD_START}{word}{PLECO_BOLD_END}")
    word_file_txt = re.sub("EN:? *", "", word_file_txt)
    word_file_txt = re.sub("ZH:? *", "", word_file_txt)
    dict_line = f"{word}\t{pinyin}\t{word_file_txt}"
    print(dict_line, file=output_file)


def create_dictionary():
    words = get_words()
    pinyin_map = load_pinyin()
    with open(f"dict_output", "w", encoding="utf-8") as output_file:
        for word in words:
            pinyin = pinyin_map.get(word, "")
            process_word(word, pinyin, output_file)


def get_words():
    return os.listdir("../words/")


if __name__ == "__main__":
    create_dictionary()
