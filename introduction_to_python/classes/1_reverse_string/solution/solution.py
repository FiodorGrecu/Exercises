class py_solution:
    def reverse_words(self, str):
        words = str.split()
        words.reverse()
        return ' '.join(words)
