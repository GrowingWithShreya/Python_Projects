students = [
    ("Shreya", 2, {"DSA": 90, "Python": 70}),
    ("Abhi", 3, {"DSA": 100, "Python": 100}),
    ("Urvi", 4, {"DSA": 50, "Python": 100 })
]

average_scores = dict()

for student in students:
    name, _, scores = student
    avg_score = sum(scores.values()) / len(scores)
    average_scores[name] = avg_score

top_students = set()

for name, avg in average_scores.items():
    if avg > 85:
        top_students.add(name)

subject_analysis = {}

for student in students:
    _, _, scores = student
    for subject_name, marks in scores.items():
        if subject_name not in subject_analysis:
            subject_analysis[subject_name] = []
        subject_analysis[subject_name].append(marks)

print("\nAverage Scores of Students:")
for name, avg in average_scores.items():
    print(f"{name}: {avg:.2f}")

print("\nTop Performing Student: ")
print(", ".join(top_students))
print(top_students)

print("\nSubject-wise Analysis:")
for subject_name, marks in subject_analysis.items():
    print(f"{subject_name}: Average Score = {sum(marks)/len(marks):.2f}, Scores = {marks}")