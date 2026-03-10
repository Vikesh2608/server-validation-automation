import subprocess

tests = [
    "test_cpu.py",
    "test_memory.py",
    "test_disk.py",
    "test_network.py",
    "test_services.py"
]

print("\nSERVER VALIDATION REPORT")
print("------------------------")

for test in tests:
    result = subprocess.run(["pytest", test, "-q"], capture_output=True, text=True)

    if "1 passed" in result.stdout:
        status = "PASS"
    else:
        status = "FAIL"

    print(f"{test.replace('test_', '').replace('.py','').upper()} Test: {status}")