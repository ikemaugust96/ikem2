from collections import deque


class WordLadder:
    """A class to generate the shortest word ladder
    from start_word to end_word."""

    def __init__(self, start_word, end_word, word_set):
        """
        Initialize the WordLadder class with the start 
        and end words and a set of valid words.
        :param start_word: The starting word of the ladder.
        :param end_word: The ending word of the ladder.
        :param word_set: A set of valid words for the ladder.
        """
        self.start_word = start_word.lower()
        self.end_word = end_word.lower()
        # Ensure all words in word_set have the same length as start_word
        self.word_set = {
            word.lower() for word in word_set if len(word) == len(self.start_word)
        }

        if len(self.start_word) != len(self.end_word):
            raise ValueError("Start and end words must be of the same length.")

    def is_valid_word(self, word):
        """Check if the word exists in the word set."""
        return word in self.word_set

    def make_ladder(self):
        """
        Generate the shortest word ladder 
        from start_word to end_word using BFS.
        :return: A list representing the shortest word ladder, or None
        if no ladder exists.
        """
        # Check if start or end word is invalid
        if not self.is_valid_word(self.start_word) or not self.is_valid_word(
            self.end_word
        ):
            return None

        # Edge case: Start word is the same as end word
        if self.start_word == self.end_word:
            return [self.start_word]

        # BFS setup
        queue = deque([[self.start_word]])
        visited = set([self.start_word])

        while queue:
            path = queue.popleft()
            current_word = path[-1]

            # Generate all one-letter transformations
            for i in range(len(current_word)):
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    if letter != current_word[i]:
                        # Skip replacing the same letter
                        next_word = current_word[:i] + letter + current_word[i + 1 :]

                        if next_word in visited:
                            continue  # Skip already visited words

                        # Check if we found the end word
                        if next_word == self.end_word:
                            return path + [next_word]

                        # If valid and not visited, enqueue the path
                        if self.is_valid_word(next_word):
                            visited.add(next_word)
                            queue.append(path + [next_word])

        # If no ladder is found, return None
        return None
