# text_cleaner_test.py

from TextCleaner import TextCleaner


def test_preprocess_text():
    cleaner = TextCleaner()
    text = "Mr. Burton's film, Corpse Bride, is great!"
    cleaned_text = cleaner.preprocess_text(text)
    assert cleaned_text == "mr burton's film COMMA corpse bride COMMA is great"


def test_split_into_sentences():
    cleaner = TextCleaner()
    text = "This is the first sentence. And here is Mr. Burton's second sentence."
    sentences = cleaner.split_into_sentences(text)
    assert sentences == [
        "this is the first sentence",
        "and here is mr burton's second sentence",
    ]
