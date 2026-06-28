import json

with open("schemes.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    DATA = data["national_schemes"]
print(type(DATA))
print(type(DATA[0]))

def recommend_schemes(user):
    results = []

    for i, scheme in enumerate(DATA):
        print(i, type(scheme))

        if not isinstance(scheme, dict):
            print("BAD ENTRY:", scheme)
            continue

        eligibility = scheme.get("eligibility", {})

        results.append(scheme)

    return results[:10]