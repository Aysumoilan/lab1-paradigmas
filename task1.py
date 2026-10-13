applicants = [
    {"name": "Noah", "salary": 1000, "loan": 4000},
    {"name": "Sam",  "salary": 600,  "loan": 2000},
    {"name": "Jane", "salary": 700,  "loan": 5000},
    {"name": "Aysu", "salary": 800,  "loan": 6000},
    {"name": "Aida", "salary": 900,  "loan": 10000},
    {"name": "Arzu", "salary": 750,  "loan": 8000}
]

approved = []
rejected = []

for person in applicants:
    salary = person["salary"]
    loan = person["loan"]

    if salary >= 700 and loan <= 10 * salary:
        approved.append(person["name"])
    else:
        rejected.append(person["name"])


print("Approved count:", len(approved))
print("Rejected count:", len(rejected))