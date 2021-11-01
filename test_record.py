from results_record import Record
from results_record import RecordManager

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

def test_add_and_get_record():
    record_manager = RecordManager()
    record = Record("jesse", 0)

    record_manager.add(record)
    record_manager.add(record)
    record_manager.add(record)
    record_manager.get_all()
    record_manager.get('jesse')