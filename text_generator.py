# Write your code here
from nltk import WhitespaceTokenizer
from collections import defaultdict
import nltk
import random


if __name__ == "__main__":
    filename = input()
    try:
        with open(filename, encoding='utf8') as f:
            # 2 - level nested defaultdict, with the 2nd defaulting as int,
            trigrams = defaultdict(lambda: defaultdict(int))
            for trigram in nltk.trigrams(WhitespaceTokenizer().tokenize(f.read())):
                # bigram[Head][Tail] += 1
                trigrams[trigram[0] + ' ' + trigram[1]][trigram[2]] += 1

            for _ in range(10):
                sentence = []

                while True:
                    head = random.choice(list(trigrams.keys()))
                    start_word, mid_word = head.split()
                    if start_word.isalpha() and start_word.istitle():
                        break

                sentence += [start_word, mid_word]

                while True:
                    next_possible_word = random.choices(list(trigrams[head].keys()),
                                                        weights=list(trigrams[head].values()), k=1)
                    sentence += next_possible_word
                    head = sentence[-2] + " " + next_possible_word.pop()
                    last_word_punct = sentence[-1][-1]
                    if last_word_punct in ("?", ".", "!") and len(sentence) >= 5:
                        break
                print(' '.join(sentence))

    except FileNotFoundError:
        print('Corpus does not exist')
