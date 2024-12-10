import re
from collections import defaultdict


class DataAnalysis:
    def __init__(self, file_name):
        # TODO: set up the necessary instance variables
        self.file_path = file_name
        self.language_counts = defaultdict(int)
        self.domain_counts = defaultdict(int)
        self.total_records = 0
        self.read_data()

    def read_data(self):
        # TODO: read the data and get the counts
        with open(self.file_path, "r") as file:
            # Skip the header line
            next(file)

            for line in file:
                self.total_records += 1
                data = line.strip().split(",")

                # Extract language
                language = data[-1]
                self.language_counts[language] += 1

                # Extract the country code from email domain
                email = data[3]
                match = re.findall(r"\.([a-z]{2})$", email)
                if match:
                    country_code = match[0]
                    self.domain_counts[country_code] += 1

    # TODO:
    # Implement top_n_lang_freqs()
    # Should take a number N as an argument and return
    # an N-length list of tuples representing languages
    # and their frequencies in the data, ordered from
    # highest frequency to lowest.
    def top_n_lang_freqs(self, n=None):
        sorted_frequencies = sorted(
            [
                (lang, count / self.total_records)
                for lang, count in self.language_counts.items()
            ],
            key=lambda x: x[1],
            reverse=True,
        )

        # Return the top N frequencies if N is specified; otherwise, return all
        return sorted_frequencies[:n] if n is not None else sorted_frequencies

    # TODO:
    # Implement top_n_country_tlds_freqs()
    # Should take a number N as an argument and return
    # an N-length list of tuples representing country (2-letter)
    # top-level domain identifiers (e.g. 'jp', 'uk', 'cn', 'ca')
    # and their frequencies as email domains the data, ordered
    # from highest frequency to lowest.
    def top_n_country_tlds_freqs(self, n=None):
        """
        Calculate and return domain frequencies as a sorted list of tuples.
        """
        # Sorting using items() and lambda for descending frequency
        sorted_frequencies = sorted(
            [
                (domain, count / self.total_records)
                for domain, count in self.domain_counts.items()
            ],
            key=lambda x: x[1],
            reverse=True,
        )
        # Return the top N frequencies if N is specified; otherwise, return all
        return sorted_frequencies[:n] if n is not None else sorted_frequencies

    # TODO:
    # Implement any other necessary/helpful methods to support
    # the ones above.

    # I don't see anything left
