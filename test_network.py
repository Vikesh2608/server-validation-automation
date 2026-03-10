import os

def test_network_connectivity():
    response = os.system("ping -n 1 google.com")
    assert response == 0