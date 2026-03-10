import psutil

def test_cpu_usage():
    cpu = psutil.cpu_percent(interval=1)
    assert cpu < 85