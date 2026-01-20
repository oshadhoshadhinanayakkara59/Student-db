import csv

marks = []

with open("marks.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        marks.append(int(row[1]))

average = sum(marks) / len(marks)
print("Average Marks:", average)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))    












Add marks analyzer code
