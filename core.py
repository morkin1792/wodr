import sys

if __name__ == '__main__':
    words = sys.argv[1]
    numbers = sys.argv[2]
    symbols = sys.argv[3]
    for word in open(words):
        word = word.strip()
        for number in open(numbers):
            number = number.strip()
            for symbol in open(symbols):
                symbol = symbol.strip()
                word_variations = []
                if len(word) > 0:
                    word_variations.append(word.lower())
                    word_variations.append(word.upper())
                    word_variations.append(word[0].upper() + word[1:].lower())        
                for word_var in word_variations:
                    # high common
                    print(word_var + symbol + number)
                    print(word_var + number + symbol)
                    # medium
                    print(number + symbol + word_var)
                    print(number + word_var + symbol)
                    # less common
                    print(number + symbol + word_var + symbol)
                    print(word_var + symbol + number + symbol)
                    print(symbol + word_var + number)
                    print(symbol + word_var + number + symbol)
                    # print(symbol + word_var + symbol + number)
                    # print(symbol + word_var + symbol + number + symbol)
            if len(word) == 0 and len(number) > 0:
                print(number)
        
