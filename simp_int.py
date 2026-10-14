from simpleint import simple_intrest

def test_simple_intrest():
    assert simple_intrest(2000, 20, 3) == 1200
def test_simple_intrest_2():    
    assert simple_intrest(10000, 10, 1) == 1000
def test_simple_intrest_3():    
    assert simple_intrest(1000, 10, 1) == 100