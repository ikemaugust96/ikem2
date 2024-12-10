# text_cleaner.py

import re


class TextCleaner:
    def __init__(self):
        self.abbreviations = {"mr.", "dr.", "ms."}

    def preprocess_text(self, text):
        """Performs basic preprocessing: lowercasing, replacing commas, and removing punctuation."""
        text = text.lower()

        # Replace common abbreviations to avoid breaking sentences
        for abbr in self.abbreviations:
            text = text.replace(abbr, abbr.replace(".", ""))

        # Replace commas with the token "COMMA" without adding extra spaces
        text = re.sub(r"\s*,\s*", " COMMA ", text)

        # Remove all punctuation except apostrophes
        text = re.sub(r"[^\w\s']", "", text)

        return text

    def split_into_sentences(self, text):
        """Splits text into sentences based on periods."""
        text = text.lower()
        for abbr in self.abbreviations:
            text = text.replace(abbr, abbr.replace(".", ""))

        sentences = re.split(r"(?<=\w)\.\s+", text)
        return [sentence.strip().rstrip(".") for sentence in sentences if sentence]
