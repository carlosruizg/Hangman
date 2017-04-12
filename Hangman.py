
class Hangman:
    
    def __init__(self, word):
        self.word = word
        self.chances = 7
        self.remaining = ['_'] * len(self.word)
        self.usedletters = []
        self.wordFound = False
        self._play()
    
    def _right_guess(self, letter):        
        print('Correct!')
        indexes = [ind for (ind, char) in enumerate(self.word) if char == letter]
        for c in indexes:
            self.remaining[c] = letter                     
        print(' '.join(self.remaining))        
        if ''.join(self.remaining) == self.word:
            self.wordFound = True
    
    def _wrong_guess(self, letter):
        print('Wrong!')
        self.chances-=1
        print("You have {} chances left".format(self.chances))
    
    def _guess(self, letter):
        if letter in self.usedletters:
            print('Repeated letter!')
        else:
            self.usedletters.append(letter)
            if letter in self.word:
                self._right_guess(letter)
            else:
                self._wrong_guess(letter)
                    
    def _play(self):
        print('Welcome to Hangman!')  
        word_to_guess = ' '.join(self.remaining)                          
        print("{}. you have {} guessesa".format(word_to_guess, len(self.word))) 
        while(self.chances > 0 and self.wordFound == False):
            letter = input('Enter letter: ')
            if letter:
                self._guess(letter.lower())
                    
        if self.wordFound:
            print('You Win!')
        else:
            print('You lose!')
    
if __name__ == '__main__':
    h = Hangman('captain')
    
