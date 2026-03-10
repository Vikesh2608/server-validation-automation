import psutil

def test_memory_usage():
    memory = psutil.virtual_memory()
    assert memory.percent < 85