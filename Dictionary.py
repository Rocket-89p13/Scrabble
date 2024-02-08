import sqlite3
import re

class Dictionary:
    def __init__(self):
        self.connection = sqlite3.connect('dictionary.db')
        self.connection.create_function("REGEXP", 2, self.regexp)
        self.cursor = self.connection.cursor()

    def regexp(self, pattern, item):
        reg = re.compile(pattern)
        return reg.match(item) is not None 

    # this function determines if a word is valid
    # the regexp function gives you all the words that only contain those characters but words can have more
    # characters then there are in the set e.x. set = 'oveents' some words like 'ententes' will appear
    # but since there are only 2 es in the set ententes is an invalid word
    def character_count_matches(self, word, characters):
        dictionary = {}
        for char in word:
            dictionary[char] = dictionary.get(char, 0) + 1
        for char, count in dictionary.items():
            if (count > characters.count(char)):
                return False
        return True

    def get_valid_words(self, player_tiles):
        valid_words = []
        pattern = '^[' + player_tiles + ']+$'
        self.cursor.execute("SELECT * FROM dictionary WHERE word REGEXP ?", (pattern,))
        matching_words = self.cursor.fetchall()
        for word in matching_words:
            if(self.character_count_matches(word[0], player_tiles)):
                valid_words.append(word[0])
        return valid_words

    def word_in_dictionary(self, word):
        self.cursor.execute("SELECT * FROM dictionary WHERE word=?",(word,))
        word = self.cursor.fetchone()
        if(word):
            return True
        else:
            return False

    def close(self):
        self.cursor.close()
        self.connection.close()