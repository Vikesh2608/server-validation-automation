import psutil

def test_disk_usage():
    disk = psutil.disk_usage('/')
    assert disk.percent < 90