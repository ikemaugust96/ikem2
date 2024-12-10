# ngrams.py

import sys
from NgramFrequencies import NgramFrequencies
from TextCleaner import TextCleaner


def tokenize(sentence):
    return sentence.split()


def generate_ngrams(tokens, n):
    return zip(*[tokens[i:] for i in range(n)])


def main(filename):
    # Initialize TextCleaner and n-gram frequency collectors
    cleaner = TextCleaner()
    unigram_freqs = NgramFrequencies()
    bigram_freqs = NgramFrequencies()
    trigram_freqs = NgramFrequencies()

    with open(filename, "r") as file:
        text = file.read()

    # Preprocess and split text into sentences
    clean_text = cleaner.preprocess_text(text)
    sentences = cleaner.split_into_sentences(clean_text)

    # Process each sentence
    for sentence in sentences:
        tokens = tokenize(sentence)

        # Add unigrams, bigrams, and trigrams to respective NgramFrequencies
        # instances
        for unigram in tokens:
            unigram_freqs.add_item(unigram)
        for bigram in generate_ngrams(tokens, 2):
            bigram_freqs.add_item("_".join(bigram))
        for trigram in generate_ngrams(tokens, 3):
            trigram_freqs.add_item("_".join(trigram))

    # Print top 10 results for each n-gram type
    print("Top 10 unigrams:")
    for ngram, freq in unigram_freqs.top_n_freqs(10):
        print(f"    ('{ngram}', {freq:.3f})")

    print("Top 10 bigrams:")
    for ngram, freq in bigram_freqs.top_n_freqs(10):
        print(f"    ('{ngram}', {freq:.3f})")

    print("Top 10 trigrams:")
    for ngram, freq in trigram_freqs.top_n_freqs(10):
        print(f"    ('{ngram}', {freq:.3f})")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ngrams.py <filename>")
    else:
        main(sys.argv[1])
