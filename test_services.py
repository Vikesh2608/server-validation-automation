import os

def test_windows_service():
    result = os.system("sc query EventLog")
    assert result == 0