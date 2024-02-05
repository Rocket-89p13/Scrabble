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

    def is_valid_word(self, word, characters):
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
            if(self.is_valid_word(word[0], player_tiles)):
                valid_words.append(word[0])
        return valid_words
    
    def valid(self, player_tiles, played_word):
        return played_word in self.get_valid_words(player_tiles)

    def close(self):
        self.cursor.close()
        self.connection.close()