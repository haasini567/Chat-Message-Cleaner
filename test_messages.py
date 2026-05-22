from cleaner import clean_message

def test_cleaner():
    assert clean_message("Hello!!!") == "hello"
    assert clean_message("123abc") == "abc"
    assert clean_message("   hi   there   ") == "hi there"
    assert clean_message(None) is None

    print("All tests passed!")

test_cleaner()
