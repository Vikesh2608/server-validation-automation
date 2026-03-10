import re

log_file = "server_logs.txt"

error_patterns = {
    "CPU Error": r"cpu.*error",
    "Memory ECC Error": r"ecc.*error",
    "Disk Failure": r"disk.*error",
}

print("\nHARDWARE LOG ANALYSIS REPORT")
print("-----------------------------")

with open(log_file, "r") as file:
    logs = file.readlines()

for error_name, pattern in error_patterns.items():
    found = any(re.search(pattern, line, re.IGNORECASE) for line in logs)

    if found:
        print(f"{error_name}: DETECTED")
    else:
        print(f"{error_name}: NOT FOUND")