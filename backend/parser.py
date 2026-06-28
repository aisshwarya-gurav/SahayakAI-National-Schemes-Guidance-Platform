import re


def extract_profile(message):

    profile = {
        "age": 0,
        "gender": "Unknown",
        "state": "Unknown",
        "occupation": "Unknown",
        "annual_income": 0,
        "category": "Unknown"
    }

    text = message.lower()

    # Age
    age = re.search(r'(\d{1,2})\s*(year|years)?', text)
    if age:
        profile["age"] = int(age.group(1))

    # Gender
    if "female" in text or "girl" in text or "woman" in text:
        profile["gender"] = "Female"

    elif "male" in text or "boy" in text or "man" in text:
        profile["gender"] = "Male"

    # Occupation
    if "student" in text or "college" in text or "studying" in text:
        profile["occupation"] = "Student"

    elif "farmer" in text:
        profile["occupation"] = "Farmer"

    elif "business" in text:
        profile["occupation"] = "Business"

    elif "labour" in text:
        profile["occupation"] = "Labour"

    elif "worker" in text:
        profile["occupation"] = "Worker"

    # Income
    income = re.search(r'(\d{3,10})', text)
    if income:
        profile["annual_income"] = int(income.group(1))

    # Category
    if "obc" in text:
        profile["category"] = "OBC"

    elif "sc" in text:
        profile["category"] = "SC"

    elif "st" in text:
        profile["category"] = "ST"

    elif "general" in text:
        profile["category"] = "General"

    elif "ews" in text:
        profile["category"] = "EWS"

    # States
    states = [
        "karnataka",
        "maharashtra",
        "kerala",
        "tamil nadu",
        "goa",
        "gujarat",
        "rajasthan",
        "punjab",
        "delhi",
        "uttar pradesh",
        "bihar",
        "west bengal",
        "telangana",
        "andhra pradesh",
        "odisha",
        "madhya pradesh",
        "chhattisgarh",
        "jharkhand",
        "assam"
    ]

    for state in states:
        if state in text:
            profile["state"] = state.title()
            break

    return profile