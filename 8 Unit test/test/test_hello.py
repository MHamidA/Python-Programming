from hello import hello

def test_default():
    assert hello() == 'helo, world'


def test_argument():
     assert hello('Hamid') == 'helo, Hamid'

# run in terimnal
# run this to test whole folder (dont forget the init file):
# pytest test