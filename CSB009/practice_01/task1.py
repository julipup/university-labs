# Create a class that performs statistical
# processing of a text file - counting
# characters, words, sentences, etc.
# Determine the required attributes-data
# and attributes-methods in class for working with the text file.
from typing import Tuple
from os.path import isfile


# TextParser
# - Parses text
class TextParser:
    # Text Parser options
    word_end_symbols = [",", ";", ":"]
    sentence_end_symbols = [".", "!"]
    in_word_symbols = ["'"]

    # Init function
    def __init__(self, text: str):
        # Default values
        self.__characters: list[str] = []
        self.__words: list[str] = []
        self.__sentences: list[str] = []

        # Parsing text
        self.text = text

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value

        # Parsing text
        self.__parse_text()

    @text.deleter
    def text(self):
        self.text = ""

    # Characters getter
    @property
    def characters(self):
        return self.__characters

    @property
    def characters_count(self):
        return len(self.__characters)

    def get_characters(self, with_punctuation_symbols=True):
        # Filter function
        def filter_char(char):
            if not with_punctuation_symbols:
                if char in TextParser.word_end_symbols or char in TextParser.sentence_end_symbols:
                    return False

            return True

        return list(filter(filter_char, self.characters))

    # Words getter
    @property
    def words(self):
        return self.__words

    @property
    def words_count(self):
        return len(self.__words)

    def get_words(self, with_punctuation_symbols=True):
        words_string = " ".join(self.words)

        # Replacing punctuation symbols (if needed)
        if not with_punctuation_symbols:
            for symbol in TextParser.get_punctuation_symbols():
                words_string = words_string.replace(symbol, "")

        return words_string.split(" ")

    # Sentences getter
    @property
    def sentences(self):
        return self.__sentences

    @property
    def sentences_count(self):
        return len(self.__sentences)

    def get_sentences(self, with_punctuation_symbols=True):
        sentences = self.sentences.copy()

        # Replacing punctuation symbols (if needed)
        if not with_punctuation_symbols:
            processed_sentences = []

            for sentence in sentences:
                for symbol in TextParser.get_punctuation_symbols():
                    sentence = sentence.replace(symbol, "")
                processed_sentences.append(sentence)

            return processed_sentences
        else:
            return sentences

    @classmethod
    def get_punctuation_symbols(cls):
        punctuation_symbols = []

        punctuation_symbols.extend(cls.in_word_symbols)
        punctuation_symbols.extend(cls.word_end_symbols)
        punctuation_symbols.extend(cls.sentence_end_symbols)

        return punctuation_symbols

    # Counts statistics of this text
    # such as: characters, words
    # and sentences
    def __parse_text(self):
        characters: list[str] = []
        words: list[str] = []
        sentences: list[str] = []

        # Extra variables
        current_word: list[str] = []
        current_word_index: int = 0

        # explanation: int(index of starting word), int(index of ending word)
        current_sentence: Tuple[int, int] = (0, 0)

        for char in self.text:
            # Checking if this character is a letter
            if char.isalpha() or char in TextParser.in_word_symbols:
                characters.append(char)
                current_word.append(char)

            # Checking if this character is an end
            # of a word
            elif char.isspace() or char in TextParser.word_end_symbols:
                # Appending TextParser.word_end_symbols
                if not char.isspace():
                    characters.append(char)
                    current_word.append(char)

                # Checking if we can add new word to words
                # list
                if len(current_word) > 0:
                    words.append("".join(current_word))

                    current_word = []
                    current_word_index += 1

            # Checking if this character is an end of
            # a sentence
            elif char in TextParser.sentence_end_symbols:
                # Appending TextParser.sentence_end_symbols as punctuation character
                characters.append(char)
                current_word.append(char)

                # Appending current_word (if we can)
                if len(current_word) > 0:
                    words.append("".join(current_word))

                    current_word = []
                    current_word_index += 1

                # Adding this new sentence to sentences array
                current_sentence = (current_sentence[0], current_word_index)
                sentences.append(" ".join(words[current_sentence[0]:current_sentence[1]]))

                current_sentence = (current_word_index, current_word_index)
            else:
                # Just a random symbol, I guess
                characters.append(char)

        # Updating our instance
        self.__characters = characters
        self.__words = words
        self.__sentences = sentences

    def __str__(self):
        return f'TextParser object <characters_count: {self.characters_count}, words_count: {self.words_count}, ' \
               f'sentences_count: {self.sentences_count}>'


# FileParser
# - Handles file parsing
# problems
class FileParser:
    def __init__(self, file_name: str):
        # Creating TextParser instance
        self.__text_parser = TextParser("")

        self.file_name = file_name

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        # Checking if this file even exists
        if not isfile(value):
            raise FileNotFoundError()

        # Updating class instance
        self.__file_name = value

        # Parsing this file
        self.__parse_file()

    @property
    def text_parser(self) -> TextParser:
        return self.__text_parser

    # Parse file function
    # - This function will get all lines from
    # our current self.__file_name and feed them
    # to our self.__text_parser instance
    def __parse_file(self):
        # Opening this file
        with open(self.__file_name) as file:
            text = ""

            for line in file:
                text += " " + line.replace('\n', '')

            # Feeding this text into our parser
            self.text_parser.text = text


parsed = FileParser("test_file.txt")
print(parsed.text_parser)
