from hello import hello

def test_default():
    assert hello() == 'helo, world'


def test_argument():
     assert hello('Hamid') == 'helo, Hamid'