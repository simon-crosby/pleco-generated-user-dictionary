from openai import OpenAI
import os, sys
client = OpenAI()

def generate_example_sentences(word):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Generate 20 example sentences using \"{word}\" in Chinese and English. Prefix Chinese examples with ZH:. Prefix English examples with EN:."}
        ]
    )
    return completion.choices[0].message.content

def read_file(wordlist_filename):
    word_list = []
    with open(wordlist_filename, encoding="utf-8") as input_file:
        for raw_line in input_file:
            line = raw_line.rstrip().lstrip()
            word_list.append(line)
    return word_list

def write_output(word, examples):
    with open(f"../words/{word}", "w", encoding="utf-8") as output_file:
        print(f"{examples}", file=output_file)

def already_have_files():
    return set(os.listdir("../words/"))


def generate_files(wordlist_filename):
    already_generated = already_have_files()
    word_list = read_file(wordlist_filename)
    for word in word_list:
        if word in already_generated:
            print(f"Skipping {word}")
        else:
            print(word)
            example_sentences = generate_example_sentences(word)
            write_output(word, example_sentences)

if __name__ == "__main__":
    generate_files(sys.argv[1])