


import re

def translate_to_pig_latin1(file_path):
    # Open the file
    with open(file_path, 'r') as f:
        # Read the file
        text = f.read()

    # Split the text into sentences
    sentences = re.split(r'[.!?]', text)

    # Iterate through the sentences
    for sentence in sentences:
        # Split the sentence into words
        words = sentence.split()

        # Use list comprehension to translate the words to Pig Latin
        translated_words = [word[1:] + word[0] + 'ay' if word and word[0] not in 'aeiouAEIOU' else word + 'way' for word in words]
        # join the words and make a sentence
        translated_sentence = " ".join(translated_words)
        print(translated_sentence)


def translate_to_pig_latin(file):
    with open(file, 'r') as f:
        for line in f:
            sentences = line.strip().split(',')
            for sentence in sentences:
                words = sentence.split()
                pig_latin_sentence  = [word[1:] + word[0] + "ay" for word in words]
                return " ".join(pig_latin_sentence)

def main():
    print(translate_to_pig_latin("text.txt"))
    print(translate_to_pig_latin1("text.txt"))
main()