applicants = [
    {"name": "Noah", "salary": 1000, "loan": 4000},
    {"name": "Sam",  "salary": 600,  "loan": 2000},
    {"name": "Jane", "salary": 700,  "loan": 5000},
    {"name": "Aysu", "salary": 800,  "loan": 6000},
    {"name": "Aida", "salary": 900,  "loan": 10000},
    {"name": "Arzu", "salary": 750,  "loan": 8000}
]

def has_name(p):
    return p["name"] != ""


def validate(applicant, rules):
    for rule in rules:
        if not rule(applicant):
            return False
    return True


strict_rules = [
    lambda p: p["salary"] >= 700,
    lambda p: p["loan"] <= 10 * p["salary"],
    has_name
]

lenient_rules = [
    lambda p: p["loan"] <= 10 * p["salary"],
    has_name
]

for person in applicants:
    print(person["name"],
          "strict:", validate(person, strict_rules),
          "lenient:", validate(person, lenient_rules)
        )