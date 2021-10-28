from results_record import Record

def add_1(x):
    return x + 1
def test_1():
    count = 0
    count = add_1(count)
    assert count == 1

def test_record():
    record = Record("jesse", 0)
    assert record.id == "jesse"
    assert record.point == 0



