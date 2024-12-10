# frequencies_test.py

from NgramFrequencies import NgramFrequencies


def test_add_item():
    ngram_freqs = NgramFrequencies()
    ngram_freqs.add_item("test")
    assert ngram_freqs.ngram_counts["test"] == 1
    assert ngram_freqs.total_count == 1


def test_top_n_counts():
    ngram_freqs = NgramFrequencies()
    ngram_freqs.add_item("a")
    ngram_freqs.add_item("a")
    ngram_freqs.add_item("b")
    assert ngram_freqs.top_n_counts(1) == [("a", 2)]


def test_top_n_freqs():
    ngram_freqs = NgramFrequencies()
    ngram_freqs.add_item("a")
    ngram_freqs.add_item("a")
    ngram_freqs.add_item("b")
    freqs = ngram_freqs.top_n_freqs(2)
    assert freqs[0][1] == 2 / 3
    assert freqs[1][1] == 1 / 3


def test_frequency():
    ngram_freqs = NgramFrequencies()
    ngram_freqs.add_item("a")
    ngram_freqs.add_item("a")
    ngram_freqs.add_item("b")
    assert ngram_freqs.frequency("a") == 2 / 3
    assert ngram_freqs.frequency("b") == 1 / 3
