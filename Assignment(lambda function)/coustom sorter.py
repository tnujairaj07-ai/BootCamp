Students = [
    {"name": "Alice", "gpa": 8.5},
    {"name": "Bob", "gpa": 7.89},
    {"name": "Tanuj", "gpa": 9.9},
    {"name": "Eva", "gpa": 8.7}
]

top3 = sorted(Students, key=lambda x: x["gpa"], reverse=True)[:3]
print("Top 3 students:")
for Students in top3:
    print(Students)