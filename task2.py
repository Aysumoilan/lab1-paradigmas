from functools import reduce
applicants = [
    {"name": "Noah", "salary": 1000, "loan": 4000},
    {"name": "Sam",  "salary": 600,  "loan": 2000},
    {"name": "Jane", "salary": 700,  "loan": 5000},
    {"name": "Aysu", "salary": 800,  "loan": 6000},
    {"name": "Aida", "salary": 900,  "loan": 10000},
    {"name": "Arzu", "salary": 750,  "loan": 8000}
]

approved = list(filter(lambda p: p["salary"] >= 700 and p["loan"] <= 10 * p["salary"], applicants)) 

messages = list(map(lambda p: f"{p['name']}: {p['loan']} AZN", approved))

total = reduce(lambda acc, p: acc + p["loan"], approved, 0)


print("Total amount of approved loans:", total)