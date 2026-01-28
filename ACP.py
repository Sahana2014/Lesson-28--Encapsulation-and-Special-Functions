class Reverse:
    def __init__(self, s=""):
        self.s = s

    def reverse_string(self):
        words = self.s.split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words

input_string = input("Enter a sentence: ")
rev = Reverse(input_string)
print(rev.reverse_string())
