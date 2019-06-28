def flip(word):
    flipped = []
    for i in range(len(word)):
        letter = word[len(word) - i]
        flipped.append(letter)
    return ''.join(flipped)

def test_flip():
    # assert <statement>, 'Info message in case of failure of statement'
    assert flip('John') == 'nhoJ'