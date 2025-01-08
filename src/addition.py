# app.py
# app.py test_1
# app.py test_2
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
