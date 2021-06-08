class Dictionary:
    FILE = "./dictionary/words.txt"

    def __init__(self):
        self.__words = dict()
        self.load()

    def load(self):
        file = open(Dictionary.FILE)

        for line in file.readlines():
            word = line.replace("\n", "")
            letter = word[0]

            if letter in self.__words:
                self.__words[letter].append(word)
            else:
                self.__words[letter] = list()

    def words(self):
        return self.__words
