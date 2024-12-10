from word_ladder import WordLadder


def test_word_ladders():
    # Test Case 1: cat -> hat
    words_set1 = {"cat", "bat", "rat", "mat", "hat"}
    wl1 = WordLadder("cat", "hat", words_set1)
    result = wl1.make_ladder()
    assert result == [
        "cat", "hat"], f"Unexpected result for 'cat -> hat': {result}"
    print("Test Case 1 Passed: cat -> hat")

    # Test Case 2: love -> hate
    words_set2 = {"love", "hove", "have", "hate"}
    wl2 = WordLadder("love", "hate", words_set2)
    result = wl2.make_ladder()
    assert result == [
        "love", "hove", "have", "hate"
        ], f"Unexpected result for 'love -> hate': {result}"
    print("Test Case 2 Passed: love -> hate")

    # Test Case 3: angel -> devil
    words_set3 = {"angel", "anger", "aeger", "leger", "lever",
                  "level", "devel", "devil"}
    wl3 = WordLadder("angel", "devil", words_set3)
    result = wl3.make_ladder()
    assert result == [
        "angel", "anger", "aeger", "leger", "lever", "level", 
        "devel", "devil"
    ], f"Unexpected result for 'angel -> devil': {result}"
    print("Test Case 3 Passed: angel -> devil")

    # Test Case 4: earth -> ocean
    words_set4 = {
        "earth", "barth", "barih", "baris", "batis", "bitis", "aitis", "antis",
        "antas", "antal", "ontal", "octal", "octan", "ocean"
    }
    wl4 = WordLadder("earth", "ocean", words_set4)
    result = wl4.make_ladder()
    assert result == [
        "earth", "barth", "barih", "baris", "batis", "bitis", "aitis", "antis",
        "antas", "antal", "ontal", "octal", "octan", "ocean"
    ], f"Unexpected result for 'earth -> ocean': {result}"
    print("Test Case 4 Passed: earth -> ocean")

    # Test Case 5: Words of different lengths
    try:
        wl5 = WordLadder("cat", "cater", words_set1)
        wl5.make_ladder()
        assert False, "Expected ValueError for words of different lengths"
    except ValueError as e:
        assert str(e) == "Start and end words must be of the same length."
        print("Test Case 5 Passed: Words of different lengths")

    print("All test cases passed!")


if __name__ == "__main__":
    try:
        test_word_ladders()
    except AssertionError as e:
        print(f"Test failed: {e}")
