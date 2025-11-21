"""Test DB worker"""
from luminadb import integer
from luminadb_worker import DatabaseWorker

def test_worker():
    """Test worker"""

    db = DatabaseWorker(":memory:")
    t = db.create_table("t", [integer("a")])
    t.insert({"a": 1})
    t.commit()
    assert t.select_one({"a": 1}) is not None
    db.close()
