# ngram_frequencies.py

from collections import Counter


class NgramFrequencies:
    def __init__(self):
        self.ngram_counts = Counter()
        self.total_count = 0

    def add_item(self, ngram):
        """Increments the count for an n-gram and updates the total count."""
        self.ngram_counts[ngram] += 1
        self.total_count += 1

    def top_n_counts(self, n=10):
        """Returns a list of the top n items sorted by count, with the most
        frequent first."""
        return sorted(self.ngram_counts.items(), key=lambda x: x[1], reverse=True)[:n]

    def top_n_freqs(self, n=10):
        """Returns a list of the top n items sorted by frequency, with the
        most frequent first."""
        return sorted(
            [
                (ngram, count / self.total_count)
                for ngram, count in self.ngram_counts.items()
            ],
            key=lambda x: x[1],
            reverse=True,
        )[:n]

    def frequency(self, ngram):
        """Returns the frequency of a specific n-gram."""
        return (
            self.ngram_counts[ngram] / self.total_count if self.total_count > 0 else 0
        )
