import json

try:
    with open("schemes.json", "r", encoding="utf-8") as f:
        json.load(f)
    print("✅ JSON is valid")
except json.JSONDecodeError as e:
    print(f"Error: {e}")
    print(f"Line: {e.lineno}")
    print(f"Column: {e.colno}")

    with open("schemes.json", "r", encoding="utf-8") as f:
        lines = f.readlines()

    start = max(0, e.lineno - 5)
    end = min(len(lines), e.lineno + 5)

    print("\nContext:\n")
    for i in range(start, end):
        print(f"{i+1}: {lines[i].rstrip()}")