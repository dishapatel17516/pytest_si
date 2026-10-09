from simple_interest import SI

def test_SI():
    assert SI(10000, 8, 12) == 9600

def test_SI_zero():
    assert SI(20000, 4, 16) ==   12800